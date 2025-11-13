"""Acceleration flag traceability tests."""

# ruff: noqa: S101,TC003

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from types import SimpleNamespace
from typing import Protocol

from x_make_github_visitor_x import x_cls_make_github_visitor_x


def _make_repo(root: Path, name: str) -> Path:
    repo = root / name
    repo.mkdir(parents=True)
    (repo / ".git").mkdir()
    # minimal python file for has_python flag
    (repo / "demo.py").write_text("print('ok')\n", encoding="utf-8")
    return repo


class _MonkeyPatch(Protocol):  # minimal protocol for the single usage
    def setattr(
        self,
        target: object,
        name: str,
        value: object,
        *,
        raising: bool = ...,
    ) -> None: ...


def test_runtime_snapshot_records_fast_paths(
    monkeypatch: _MonkeyPatch, tmp_path: Path
) -> None:
    """Fast path environment flags should appear in runtime snapshot & summary."""

    # Engage all acceleration flags
    os.environ["VISITOR_SKIP_CONTENT_HASH"] = "1"
    os.environ["VISITOR_SKIP_TOOLS"] = "1"
    os.environ["VISITOR_QUICK_MODE"] = "1"

    # Avoid real pip/network calls
    def _fake_run(*_a: object, **_kw: object) -> SimpleNamespace:
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", _fake_run, raising=False)

    workspace = tmp_path / "workspace"
    workspace.mkdir()
    (workspace / ".git").mkdir()  # permit root to be a git repo
    _make_repo(workspace, "child_repo")

    visitor = x_cls_make_github_visitor_x(workspace)
    visitor.run_inspect_flow()

    snapshot = visitor.runtime_snapshot()
    fast_paths = snapshot.get("fast_paths")
    assert isinstance(fast_paths, dict)
    assert fast_paths.get("skip_content_hash") is True
    assert fast_paths.get("skip_tools") is True
    assert fast_paths.get("quick_mode") is True
    active_raw = snapshot.get("fast_paths_active")
    assert isinstance(active_raw, list)
    active_flags = {flag for flag in active_raw if isinstance(flag, str)}
    assert active_flags == {"skip_content_hash", "skip_tools", "quick_mode"}

    summary = visitor.generate_summary_report()
    summary_fast = summary.get("fast_paths")
    assert isinstance(summary_fast, dict)
    assert summary_fast.get("quick_mode") is True
    assert summary.get("fast_paths_active")

    # Cleanup env vars so they do not leak to other tests
    for key in [
        "VISITOR_SKIP_CONTENT_HASH",
        "VISITOR_SKIP_TOOLS",
        "VISITOR_QUICK_MODE",
    ]:
        os.environ.pop(key, None)
