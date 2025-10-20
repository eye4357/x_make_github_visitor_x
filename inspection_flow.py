from __future__ import annotations

import importlib
import multiprocessing as mp
import os
import pickle
import queue
from contextlib import suppress
from dataclasses import dataclass
from os import PathLike
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING, Protocol, TypeGuard, cast

from x_make_common_x import ensure_workspace_on_syspath, get_logger

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

SUBPROCESS_FLAG_ENV = "X_VISITOR_USE_SUBPROCESS"
_SUBPROCESS_DEFAULT = True

_LOGGER = get_logger("x_make_github_visitor")

MessagePayload = dict[str, object]


@dataclass(frozen=True)
class VisitorRunResult:
    report_path: Path | None
    had_failures: bool
    failure_messages: tuple[str, ...] = ()
    failure_details: tuple[dict[str, object], ...] = ()
    skipped: bool = False


class _MessageQueue(Protocol):
    def put(self, value: MessagePayload, *, block: bool = ...) -> None: ...

    def get(self, timeout: float | None = ...) -> MessagePayload: ...

    def close(self) -> None: ...

    def join_thread(self) -> None: ...


class _VisitorFactory(Protocol):
    def __call__(self, *args: object, **kwargs: object) -> object: ...


class _RunInspectFlow(Protocol):
    def __call__(self) -> object: ...


def _is_run_inspect_callable(value: object | None) -> TypeGuard[_RunInspectFlow]:
    return callable(value)


def _bool_env(value: str | None, *, default: bool) -> bool:
    if value is None:
        return default
    lowered = value.strip().lower()
    return lowered not in {"0", "false", "no", "off"}


def _should_use_subprocess() -> bool:
    return _bool_env(os.environ.get(SUBPROCESS_FLAG_ENV), default=_SUBPROCESS_DEFAULT)


def _serialize_ctx(ctx: object | None) -> bytes | None:
    if ctx is None:
        return None
    try:
        return pickle.dumps(ctx)
    except (pickle.PickleError, AttributeError, TypeError):
        return None


def _factory_spec(factory: object) -> tuple[str, str]:
    module_name_obj = cast("object | None", getattr(factory, "__module__", None))
    attr_name_obj = cast("object | None", getattr(factory, "__name__", None))
    module_name = module_name_obj if isinstance(module_name_obj, str) else None
    attr_name = attr_name_obj if isinstance(attr_name_obj, str) else None
    if module_name is None or attr_name is None:
        message = "Visitor factory must have importable module and name"
        raise TypeError(message)
    return module_name, attr_name


def _resolve_factory(module_name: str, attr_name: str) -> object:
    module = importlib.import_module(module_name)
    attr_candidate = cast("object | None", getattr(module, attr_name, None))
    if attr_candidate is None:
        message = f"Unable to resolve visitor factory {module_name}.{attr_name}"
        raise RuntimeError(message)
    return attr_candidate


def _visitor_process_main(  # noqa: C901, PLR0912, PLR0915
    root_path: str,
    ctx_payload: bytes | None,
    factory_module: str,
    factory_name: str,
    queue_obj: _MessageQueue,
) -> None:
    os.environ[SUBPROCESS_FLAG_ENV] = "0"
    ensure_workspace_on_syspath()

    ctx_obj: object | None
    if ctx_payload is None:
        ctx_obj = None
    else:
        try:
            ctx_obj = pickle.loads(ctx_payload)  # noqa: S301 - trusted payload
        except (pickle.UnpicklingError, AttributeError, ValueError, TypeError):
            ctx_obj = None

    factory_obj = _resolve_factory(factory_module, factory_name)
    if not callable(factory_obj):
        message = "Visitor factory must be callable"
        raise TypeError(message)
    factory_callable = cast("_VisitorFactory", factory_obj)

    try:
        visitor: object
        try:
            ctx_arg = cast("object", ctx_obj)
            visitor = factory_callable(root_path, ctx=ctx_arg)
        except TypeError:
            visitor = factory_callable(root_path)

        run_attr = cast(
            "object | None",
            getattr(visitor, "run_inspect_flow", None),
        )
        if not _is_run_inspect_callable(run_attr):
            message = "Visitor instance does not provide run_inspect_flow"
            raise TypeError(message)
        run_method = run_attr

        try:
            run_method()
        except AssertionError as exc:
            queue_obj.put(
                {
                    "type": "result",
                    "status": "assertion",
                    "message": str(exc),
                },
                block=True,
            )
            raise
        except Exception as exc:
            queue_obj.put(
                {
                    "type": "result",
                    "status": "error",
                    "message": str(exc),
                },
                block=True,
            )
            raise
        else:
            result_attr = cast(
                "object | None",
                getattr(visitor, "last_run_result", None),
            )
            if isinstance(result_attr, VisitorRunResult):
                run_result = result_attr
            else:
                report_attr = cast(
                    "object | None",
                    getattr(visitor, "last_report_path", None),
                )
                if isinstance(report_attr, Path):
                    report_value: Path | None = report_attr
                elif isinstance(report_attr, str):
                    report_value = Path(report_attr)
                else:
                    report_value = None
                run_result = VisitorRunResult(
                    report_path=report_value,
                    had_failures=False,
                )

            queue_obj.put(
                {
                    "type": "result",
                    "status": "ok",
                    "report": (
                        str(run_result.report_path)
                        if isinstance(run_result.report_path, Path)
                        else None
                    ),
                    "had_failures": run_result.had_failures,
                    "failure_messages": list(run_result.failure_messages),
                    "failure_details": [
                        dict(entry) for entry in run_result.failure_details
                    ],
                    "skipped": run_result.skipped,
                },
                block=True,
            )
    finally:
        with suppress(Exception):
            queue_obj.put({"type": "done"}, block=True)


def _run_visitor_in_subprocess(  # noqa: C901, PLR0912, PLR0915
    root_path: Path,
    ctx: object | None,
    visitor_factory: object,
) -> VisitorRunResult:
    factory_module, factory_name = _factory_spec(visitor_factory)
    ctx_payload = _serialize_ctx(ctx)
    mp_ctx = mp.get_context("spawn")
    queue_obj = cast("_MessageQueue", mp_ctx.Queue())
    process = mp_ctx.Process(
        target=_visitor_process_main,
        args=(str(root_path), ctx_payload, factory_module, factory_name, queue_obj),
        name="visitor-subprocess",
    )
    process.start()

    result_payload: dict[str, object] | None = None
    error_exc: Exception | None = None
    done = False

    try:
        while True:
            try:
                message = queue_obj.get(timeout=0.2)
            except queue.Empty:
                if done and not process.is_alive():
                    break
                continue
            kind = message.get("type")
            if kind == "result":
                status = message.get("status")
                if status == "ok":
                    raw_report = message.get("report")
                    failure_messages_raw = message.get("failure_messages")
                    failure_details_raw = message.get("failure_details")
                    had_failures_raw = message.get("had_failures")
                    skipped_raw = message.get("skipped")

                    if isinstance(raw_report, str) and raw_report:
                        report_value: str | None = raw_report
                    else:
                        report_value = None

                    if isinstance(failure_messages_raw, (list, tuple)):
                        messages_seq = cast("Sequence[object]", failure_messages_raw)
                        messages = [str(entry) for entry in messages_seq]
                    else:
                        messages = []

                    details: list[dict[str, object]] = []
                    if isinstance(failure_details_raw, (list, tuple)):
                        details_seq = cast("Sequence[object]", failure_details_raw)
                        for entry in details_seq:
                            if isinstance(entry, dict):
                                entry_mapping = cast("dict[object, object]", entry)
                                normalized_detail = {
                                    str(key_obj): value
                                    for key_obj, value in entry_mapping.items()
                                }
                                details.append(normalized_detail)

                    result_payload = {
                        "report": report_value,
                        "failure_messages": tuple(messages),
                        "failure_details": tuple(details),
                        "had_failures": bool(had_failures_raw),
                        "skipped": bool(skipped_raw),
                    }
                else:
                    msg_text = str(
                        message.get(
                            "message",
                            "Visitor subprocess reported failure",
                        )
                    )
                    if status == "assertion":
                        error_exc = AssertionError(msg_text)
                    else:
                        error_exc = RuntimeError(msg_text)
            elif kind == "done":
                done = True
                if not process.is_alive():
                    break
        process.join()
    finally:
        with suppress(Exception):
            queue_obj.close()
        with suppress(Exception):
            queue_obj.join_thread()

    if error_exc is not None:
        raise error_exc
    if process.exitcode not in (0, None):
        exit_message = f"Visitor subprocess exited with code {process.exitcode}"
        raise RuntimeError(exit_message)

    if result_payload is None:
        result_payload = {
            "report": None,
            "failure_messages": (),
            "failure_details": (),
            "had_failures": False,
            "skipped": False,
        }

    report_obj = result_payload.get("report")
    report_path = (
        Path(report_obj) if isinstance(report_obj, str) and report_obj else None
    )
    failure_messages_raw = result_payload.get("failure_messages")
    failure_details_raw = result_payload.get("failure_details")
    had_failures = bool(result_payload.get("had_failures"))
    skipped = bool(result_payload.get("skipped"))

    if isinstance(failure_messages_raw, (list, tuple)):
        failure_messages_seq = cast("Sequence[object]", failure_messages_raw)
        failure_messages = tuple(str(entry) for entry in failure_messages_seq)
    else:
        failure_messages = ()

    if isinstance(failure_details_raw, (list, tuple)):
        normalized_details: list[dict[str, object]] = []
        failure_details_seq = cast("Sequence[object]", failure_details_raw)
        for entry in failure_details_seq:
            if isinstance(entry, dict):
                entry_mapping = cast("dict[object, object]", entry)
                normalized_detail = {
                    str(key_obj): value for key_obj, value in entry_mapping.items()
                }
                normalized_details.append(normalized_detail)
        failure_details = tuple(normalized_details)
    else:
        failure_details = ()

    return VisitorRunResult(
        report_path=report_path,
        had_failures=had_failures,
        failure_messages=failure_messages,
        failure_details=failure_details,
        skipped=skipped,
    )


class VisitorProtocol(Protocol):
    last_report_path: Path | None

    @property
    def last_run_result(self) -> VisitorRunResult | None: ...

    def run_inspect_flow(self) -> None: ...


class VisitorRunner(Protocol):
    def __call__(
        self,
        root_path: Path,
        *,
        ctx: object | None = None,
    ) -> VisitorRunResult: ...


class WorkspaceRootResolver(Protocol):
    def __call__(
        self,
        cloner: object,
        *,
        default_root: Path,
    ) -> Path: ...


def _info(*parts: object) -> None:
    message = " ".join(str(p) for p in parts)
    _LOGGER.info("%s", message)
    if not _LOGGER.handlers:
        print(message)


def _error(*parts: object) -> None:
    message = " ".join(str(p) for p in parts)
    _LOGGER.error("%s", message)
    if not _LOGGER.handlers:
        print(message)


def _load_workspace_root_resolver(
    clones_factory: object,
) -> WorkspaceRootResolver | None:
    module_name = cast("str | None", getattr(clones_factory, "__module__", None))
    if not isinstance(module_name, str):
        return None
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return None
    resolver_attr = cast(
        "object | None",
        getattr(module, "resolve_workspace_root", None),
    )
    if resolver_attr is None or not callable(resolver_attr):
        return None
    return cast("WorkspaceRootResolver", resolver_attr)


def _determine_visitor_root(cloner: object, *, fallback: Path) -> Path:
    root_attr = cast(
        "str | PathLike[str] | None",
        getattr(cloner, "target_dir", None),
    )
    if isinstance(root_attr, str):
        root_path = Path(root_attr)
    elif isinstance(root_attr, PathLike):
        root_path = Path(os.fspath(root_attr))
    else:
        root_path = fallback
    if (root_path / ".git").is_dir():
        parent = root_path.parent
        with suppress(OSError):
            for entry in parent.iterdir():
                if entry == root_path:
                    continue
                if (entry / ".git").is_dir():
                    root_path = parent
                    break
    return root_path


def _resolve_workspace_root(
    cloner: object,
    *,
    fallback: Path,
    resolver: WorkspaceRootResolver | None,
) -> Path:
    if resolver is not None:
        try:
            return resolver(cloner, default_root=fallback)
        except Exception as exc:  # noqa: BLE001 - log and fall back
            _error("Workspace root resolution failed via clones package:", exc)
    return _determine_visitor_root(cloner, fallback=fallback)


def _load_visitor_runner(
    visitor_factory: object,
) -> VisitorRunner | None:
    module_name = cast("str | None", getattr(visitor_factory, "__module__", None))
    if not isinstance(module_name, str):
        return None
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return None
    runner_attr = cast(
        "object | None",
        getattr(module, "run_workspace_inspection", None),
    )
    if runner_attr is None or not callable(runner_attr):
        return None
    return cast("VisitorRunner", runner_attr)


def _run_visitor_flow(visitor: VisitorProtocol) -> VisitorRunResult:
    try:
        visitor.run_inspect_flow()
    except RuntimeError as err:
        lowered_error = str(err).lower()
        if "no child git repositories found" in lowered_error:
            _info(
                "Visitor skipped: no child git repositories present at root;",
                "continuing orchestrator flow",
            )
            return VisitorRunResult(
                report_path=None,
                had_failures=False,
                skipped=True,
            )
        message = f"x_make_github_visitor run failed: {err}"
        raise AssertionError(message) from err
    except ValueError as err:
        message = f"x_make_github_visitor run failed: {err}"
        raise AssertionError(message) from err
    result_attr = visitor.last_run_result
    if isinstance(result_attr, VisitorRunResult):
        return result_attr

    report_path = visitor.last_report_path
    return VisitorRunResult(
        report_path=report_path,
        had_failures=False,
    )


def run_inspection(  # noqa: PLR0913
    *,
    cloner: object,
    ctx: object | None,
    detect_clones_root: Callable[[], str],
    instantiate_visitor: Callable[[object | None, str], VisitorProtocol],
    clones_factory: object,
    visitor_factory: object,
) -> VisitorRunResult:
    fallback_str = detect_clones_root()
    fallback_root = Path(fallback_str or ".")
    resolver = _load_workspace_root_resolver(clones_factory)
    root_path = _resolve_workspace_root(
        cloner,
        fallback=fallback_root,
        resolver=resolver,
    )
    root_str = str(root_path)
    start = perf_counter()
    use_subprocess = _should_use_subprocess()
    _info("Visitor inspection flow starting", f"root={root_str}")
    runner = _load_visitor_runner(visitor_factory)
    run_result: VisitorRunResult | None = None
    try:
        if use_subprocess:
            _info(
                "Running x_make_github_visitor via subprocess",
                f"root={root_str} ...",
            )
            run_result = _run_visitor_in_subprocess(root_path, ctx, visitor_factory)
        elif runner is not None:
            run_result = runner(root_path, ctx=ctx)
        else:
            _info(
                "Running x_make_github_visitor against cloned repos",
                f"root={root_str} ...",
            )
            visitor = instantiate_visitor(ctx, root_str)
            run_result = _run_visitor_flow(visitor)
    except AssertionError as exc:
        duration_ms = int((perf_counter() - start) * 1000)
        _error(
            "Visitor inspection flow failed",
            f"duration={duration_ms}ms",
            str(exc),
        )
        raise
    except Exception as exc:
        duration_ms = int((perf_counter() - start) * 1000)
        _error(
            "Visitor inspection flow encountered an unexpected error",
            f"duration={duration_ms}ms",
            str(exc),
        )
        raise

    duration_ms = int((perf_counter() - start) * 1000)
    summary_parts: list[str] = [f"duration={duration_ms}ms"]
    if run_result.had_failures:
        summary_parts.append(f"failures={len(run_result.failure_messages)}")
    if run_result.skipped:
        summary_parts.append("skipped")
    _info("Visitor inspection flow completed", " ".join(summary_parts))
    if run_result.report_path is not None:
        _info("Visitor JSON report:", str(run_result.report_path))
    return run_result


__all__ = [
    "VisitorProtocol",
    "VisitorRunResult",
    "VisitorRunner",
    "WorkspaceRootResolver",
    "run_inspection",
]
