from __future__ import annotations

import importlib
import logging
import multiprocessing as mp
import os
import pickle
import queue
from contextlib import suppress
from os import PathLike
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING, Protocol, cast

from x_make_common_x import (
    configure_event_sink,
    emit_event,
    ensure_workspace_on_syspath,
    make_event,
    register_listener,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from x_make_common_x.telemetry import TelemetryEvent

SUBPROCESS_FLAG_ENV = "X_VISITOR_USE_SUBPROCESS"
_SUBPROCESS_DEFAULT = True

_LOGGER = logging.getLogger("x_make_github_visitor")

MessagePayload = dict[str, object]


class _MessageQueue(Protocol):
    def put(self, value: MessagePayload, *, block: bool = ...) -> None: ...

    def get(self, timeout: float | None = ...) -> MessagePayload: ...

    def close(self) -> None: ...

    def join_thread(self) -> None: ...


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
    module_name = getattr(factory, "__module__", None)
    attr_name = getattr(factory, "__name__", None)
    if not isinstance(module_name, str) or not isinstance(attr_name, str):
        message = "Visitor factory must have importable module and name"
        raise TypeError(message)
    return module_name, attr_name


def _resolve_factory(module_name: str, attr_name: str) -> object:
    module = importlib.import_module(module_name)
    try:
        return getattr(module, attr_name)
    except AttributeError as exc:  # pragma: no cover - defensive guard
        message = f"Unable to resolve visitor factory {module_name}.{attr_name}"
        raise RuntimeError(message) from exc


def _visitor_process_main(  # noqa: C901, PLR0915
    root_path: str,
    ctx_payload: bytes | None,
    factory_module: str,
    factory_name: str,
    queue_obj: _MessageQueue,
) -> None:
    os.environ[SUBPROCESS_FLAG_ENV] = "0"
    ensure_workspace_on_syspath()
    configure_event_sink(None, echo=False)

    ctx_obj: object | None
    if ctx_payload is None:
        ctx_obj = None
    else:
        try:
            ctx_obj = pickle.loads(ctx_payload)  # noqa: S301 - trusted payload
        except (pickle.UnpicklingError, AttributeError, ValueError, TypeError):
            ctx_obj = None

    factory_obj = _resolve_factory(factory_module, factory_name)
    factory_callable = cast("Callable[..., object]", factory_obj)

    def _forward(event: TelemetryEvent) -> None:
        with suppress(Exception):
            queue_obj.put({"type": "event", "payload": dict(event)}, block=True)

    remover = register_listener(_forward)
    try:
        visitor: object
        try:
            visitor = factory_callable(root_path, ctx=ctx_obj)
        except TypeError:
            visitor = factory_callable(root_path)

        run_method = getattr(visitor, "run_inspect_flow", None)
        if not callable(run_method):
            message = "Visitor instance does not provide run_inspect_flow"
            raise TypeError(message)

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
            report_path = getattr(visitor, "last_report_path", None)
            if isinstance(report_path, Path):
                report_value: str | None = str(report_path)
            elif isinstance(report_path, str):
                report_value = report_path
            else:
                report_value = None
            queue_obj.put(
                {
                    "type": "result",
                    "status": "ok",
                    "report": report_value,
                },
                block=True,
            )
    finally:
        with suppress(Exception):
            remover()
        with suppress(Exception):
            queue_obj.put({"type": "done"}, block=True)


def _run_visitor_in_subprocess(  # noqa: C901, PLR0912
    root_path: Path,
    ctx: object | None,
    visitor_factory: object,
) -> Path | None:
    factory_module, factory_name = _factory_spec(visitor_factory)
    ctx_payload = _serialize_ctx(ctx)
    mp_ctx = mp.get_context("spawn")
    queue_raw = mp_ctx.Queue()
    queue_obj = cast("_MessageQueue", queue_raw)
    process = mp_ctx.Process(
        target=_visitor_process_main,
        args=(str(root_path), ctx_payload, factory_module, factory_name, queue_raw),
        name="visitor-subprocess",
    )
    process.start()

    report_value: str | None = None
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
            if kind == "event":
                payload = message.get("payload")
                if isinstance(payload, dict):
                    emit_event(cast("TelemetryEvent", payload))
            elif kind == "result":
                status = message.get("status")
                if status == "ok":
                    raw_report = message.get("report")
                    report_value = (
                        str(raw_report) if isinstance(raw_report, str) else None
                    )
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
        message = f"Visitor subprocess exited with code {process.exitcode}"
        raise RuntimeError(message)

    return Path(report_value) if report_value else None


class VisitorProtocol(Protocol):
    def run_inspect_flow(self) -> None: ...


class VisitorRunner(Protocol):
    def __call__(
        self,
        root_path: Path,
        *,
        ctx: object | None = None,
    ) -> Path | None: ...


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


def _run_visitor_flow(visitor: VisitorProtocol) -> Path | None:
    try:
        visitor.run_inspect_flow()
    except RuntimeError as err:
        lowered_error = str(err).lower()
        if "no child git repositories found" in lowered_error:
            _info(
                "Visitor skipped: no child git repositories present at root;",
                "continuing orchestrator flow",
            )
            return None
        message = f"x_make_github_visitor run failed: {err}"
        raise AssertionError(message) from err
    except ValueError as err:
        message = f"x_make_github_visitor run failed: {err}"
        raise AssertionError(message) from err
    report_attr: object = getattr(visitor, "last_report_path", None)
    return report_attr if isinstance(report_attr, Path) else None


def run_inspection(  # noqa: PLR0913
    *,
    cloner: object,
    ctx: object | None,
    detect_clones_root: Callable[[], str],
    instantiate_visitor: Callable[[object | None, str], VisitorProtocol],
    clones_factory: object,
    visitor_factory: object,
) -> Path | None:
    fallback_str = detect_clones_root()
    fallback_root = Path(fallback_str or ".")
    resolver = _load_workspace_root_resolver(clones_factory)
    root_path = _resolve_workspace_root(
        cloner,
        fallback=fallback_root,
        resolver=resolver,
    )
    root_str = str(root_path)
    attempt = 1
    start = perf_counter()
    use_subprocess = _should_use_subprocess()
    emit_event(
        make_event(
            source="visitor",
            phase="inspection",
            status="started",
            repository=None,
            tool="x_make_github_visitor_x",
            attempt=attempt,
            duration_ms=None,
            details={
                "message": "Visitor inspection flow starting",
                "root": root_str,
            },
        )
    )
    runner = _load_visitor_runner(visitor_factory)
    try:
        if use_subprocess:
            _info(
                "Running x_make_github_visitor via subprocess",
                f"root={root_str} ...",
            )
            report_path = _run_visitor_in_subprocess(root_path, ctx, visitor_factory)
        elif runner is not None:
            report_path = runner(root_path, ctx=ctx)
        else:
            _info(
                "Running x_make_github_visitor against cloned repos",
                f"root={root_str} ...",
            )
            visitor = instantiate_visitor(ctx, root_str)
            report_path = _run_visitor_flow(visitor)
    except AssertionError as exc:
        duration_ms = int((perf_counter() - start) * 1000)
        emit_event(
            make_event(
                source="visitor",
                phase="inspection",
                status="failed",
                repository=None,
                tool="x_make_github_visitor_x",
                attempt=attempt,
                duration_ms=duration_ms,
                details={
                    "message": str(exc),
                    "error_kind": "runtime",
                },
            )
        )
        raise
    except Exception as exc:
        duration_ms = int((perf_counter() - start) * 1000)
        emit_event(
            make_event(
                source="visitor",
                phase="inspection",
                status="failed",
                repository=None,
                tool="x_make_github_visitor_x",
                attempt=attempt,
                duration_ms=duration_ms,
                details={
                    "message": f"Unexpected error: {exc}",
                    "error_kind": "unknown",
                },
            )
        )
        raise

    duration_ms = int((perf_counter() - start) * 1000)
    details: dict[str, str] = {
        "message": "Visitor inspection flow completed",
        "root": root_str,
    }
    status = "succeeded"
    if report_path is not None:
        details["artifact_path"] = str(report_path)
        _info("Visitor markdown report:", str(report_path))
    else:
        details["message"] = "Visitor inspection completed without report"
    emit_event(
        make_event(
            source="visitor",
            phase="inspection",
            status=status,
            repository=None,
            tool="x_make_github_visitor_x",
            attempt=attempt,
            duration_ms=duration_ms,
            details=details,
        )
    )
    return report_path


__all__ = [
    "VisitorProtocol",
    "VisitorRunner",
    "WorkspaceRootResolver",
    "run_inspection",
]
