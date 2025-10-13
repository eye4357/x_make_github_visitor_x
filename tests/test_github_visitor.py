from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pytest

from x_cls_make_github_visitor_x import x_cls_make_github_visitor_x


def _create_repo(root: Path, name: str) -> Path:
    repo = root / name
    repo.mkdir(parents=True)
    (repo / ".git").mkdir()
    return repo


class DummyVisitor(x_cls_make_github_visitor_x):
    """Test double that injects predetermined visitor results."""

    def __init__(
        self,
        root_dir: Path,
        *,
        reports_dir: Path,
        tool_reports: Dict[str, Dict[str, object]],
        failure_messages: List[str],
        failure_details: List[Dict[str, object]],
        had_failures: bool,
        run_started: str,
        run_completed: str,
    ) -> None:
        super().__init__(root_dir, enable_cache=False)
        self._preset_reports = tool_reports
        self._preset_failure_messages = failure_messages
        self._preset_failure_details = failure_details
        self._preset_had_failures = had_failures
        self._preset_run_started = run_started
        self._preset_run_completed = run_completed
        self._reports_dir = reports_dir

    def body(self) -> None:  # noqa: D401 - matches superclass contract
        self._tool_reports = self._preset_reports
        self._failure_messages = self._preset_failure_messages
        self._failure_details = self._preset_failure_details
        self._last_run_failures = self._preset_had_failures
        self._runtime_snapshot["run_started_at"] = self._preset_run_started
        self._runtime_snapshot["run_completed_at"] = self._preset_run_completed


def test_run_inspect_flow_writes_markdown_report_and_preserves_order(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    repo_a = _create_repo(workspace, "repo_a")
    repo_b = _create_repo(workspace, "repo_b")

    reports_dir = tmp_path / "reports"

    tool_reports: Dict[str, Dict[str, object]] = {
        "repo_a": {
            "repo_hash": "hash-a",
            "timestamp": "2025-10-12T12:15:00+00:00",
            "files": ["a.py"],
            "tool_reports": {
                "ruff_check": {
                    "exit": 1,
                    "cached": False,
                    "stdout": "lint error",
                    "stderr": "E999 broken",
                }
            },
        },
        "repo_b": {
            "repo_hash": "hash-b",
            "timestamp": "2025-10-12T12:16:00+00:00",
            "files": ["b.py"],
            "tool_reports": {
                "mypy": {
                    "exit": 2,
                    "cached": False,
                    "stdout": "",
                    "stderr": "error: incompatible types",
                }
            },
        },
    }
    failure_messages = [
        "ruff_check failed for repo_a (exit 1)",
        "mypy failed for repo_b (exit 2)",
    ]
    failure_details: List[Dict[str, object]] = [
        {
            "repo": "repo_a",
            "repo_path": str(repo_a),
            "tool": "ruff_check",
            "cmd_display": "python -m ruff check .",
            "exit": 1,
            "stdout": "lint error",
            "stderr": "E999 broken",
            "ended_at": "2025-10-12T12:15:00+00:00",
            "tool_version": "ruff 0.5.0",
        },
        {
            "repo": "repo_b",
            "repo_path": str(repo_b),
            "tool": "mypy",
            "cmd_display": "python -m mypy . --strict",
            "exit": 2,
            "stdout": "",
            "stderr": "error: incompatible types",
            "ended_at": "2025-10-12T12:16:00+00:00",
            "tool_version": "mypy 1.10.0",
        },
    ]

    visitor = DummyVisitor(
        workspace,
        reports_dir=reports_dir,
        tool_reports=tool_reports,
        failure_messages=failure_messages,
        failure_details=failure_details,
        had_failures=True,
        run_started="2025-10-12T12:00:00+00:00",
        run_completed="2025-10-12T12:20:00+00:00",
    )

    with pytest.raises(AssertionError) as excinfo:
        visitor.run_inspect_flow()

    err = excinfo.value  # type: ignore[attr-defined]
    assert isinstance(err, AssertionError)
    assert "visitor_failures_" in str(err)

    report_path = visitor.last_report_path
    assert report_path is not None
    report_text = report_path.read_text(encoding="utf-8")

    first_item = report_text.index("- [ ] `repo_a`")
    second_item = report_text.index("- [ ] `repo_b`")
    assert first_item < second_item
    assert "Command: `python -m ruff check .`" in report_text
    assert "Command: `python -m mypy . --strict`" in report_text
    assert "Suggested action: Investigate" in report_text
    assert "Stdout preview" in report_text
    assert "Stderr preview" in report_text


def test_run_inspect_flow_creates_empty_failure_report(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    _create_repo(workspace, "repo_clean")

    reports_dir = tmp_path / "reports"

    tool_reports: Dict[str, Dict[str, object]] = {
        "repo_clean": {
            "repo_hash": "hash-clean",
            "timestamp": "2025-10-12T10:01:00+00:00",
            "files": ["ok.py"],
            "tool_reports": {
                "ruff_check": {
                    "exit": 0,
                    "cached": False,
                    "stdout": "",
                    "stderr": "",
                }
            },
        }
    }

    visitor = DummyVisitor(
        workspace,
        reports_dir=reports_dir,
        tool_reports=tool_reports,
        failure_messages=[],
        failure_details=[],
        had_failures=False,
        run_started="2025-10-12T10:00:00+00:00",
        run_completed="2025-10-12T10:01:00+00:00",
    )

    visitor.run_inspect_flow()

    report_path = visitor.last_report_path
    assert report_path is not None
    report_text = report_path.read_text(encoding="utf-8")
    assert "- [x] No failures detected" in report_text
    assert "repo_clean" not in report_text.splitlines()[0]

