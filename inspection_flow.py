from __future__ import annotations

import importlib
import logging
import os
import typing as t
from contextlib import suppress
from os import PathLike
from pathlib import Path
from typing import Protocol, cast

_LOGGER = logging.getLogger("x_make_github_visitor")


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
    detect_clones_root: t.Callable[[], str],
    instantiate_visitor: t.Callable[[object | None, str], VisitorProtocol],
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
    runner = _load_visitor_runner(visitor_factory)
    if runner is not None:
        report_path = runner(root_path, ctx=ctx)
        if report_path is not None:
            _info("Visitor markdown report:", str(report_path))
        return report_path

    root_str = str(root_path)
    _info(
        "Running x_make_github_visitor against cloned repos",
        f"root={root_str} ...",
    )
    try:
        visitor = instantiate_visitor(ctx, root_str)
    except (RuntimeError, ValueError, TypeError) as exc:
        message = f"x_make_github_visitor instantiate failed: {exc}"
        raise AssertionError(message) from exc

    return _run_visitor_flow(visitor)


__all__ = [
    "VisitorProtocol",
    "VisitorRunner",
    "WorkspaceRootResolver",
    "run_inspection",
]
