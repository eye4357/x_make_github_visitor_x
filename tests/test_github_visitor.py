from __future__ import annotations

# ruff: noqa: S101
import json
import pathlib
from collections.abc import Mapping
from typing import cast

from x_make_github_visitor_x import x_cls_make_github_visitor_x


def _create_repo(root: pathlib.Path, name: str) -> pathlib.Path:
    repo = root / name
    repo.mkdir(parents=True)
    (repo / ".git").mkdir()
    return repo


class DummyVisitor(x_cls_make_github_visitor_x):
    """Test double that injects predetermined visitor results."""

    def __init__(  # noqa: PLR0913
        self,
        root_dir: pathlib.Path,
        *,
        reports_dir: pathlib.Path,
        tool_reports: dict[str, dict[str, object]],
        failure_messages: list[str],
        failure_details: list[dict[str, object]],
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

    def body(self, *, children: object | None = None) -> None:
        _ = children
        self._tool_reports = self._preset_reports
        self._failure_messages = self._preset_failure_messages
        self._failure_details = self._preset_failure_details
        self._last_run_failures = self._preset_had_failures
        self._runtime_snapshot["run_started_at"] = self._preset_run_started
        self._runtime_snapshot["run_completed_at"] = self._preset_run_completed


def test_run_inspect_flow_writes_json_report_and_preserves_order(  # noqa: PLR0915
    tmp_path: pathlib.Path,
) -> None:
    workspace = pathlib.Path(tmp_path) / "workspace"
    workspace.mkdir()
    repo_a = _create_repo(workspace, "repo_a")
    repo_b = _create_repo(workspace, "repo_b")

    reports_dir = pathlib.Path(tmp_path) / "reports"

    tool_reports: dict[str, dict[str, object]] = {
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
    failure_details: list[dict[str, object]] = [
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

    visitor.run_inspect_flow()

    result = visitor.last_run_result
    assert result is not None
    assert result.had_failures is True
    assert list(result.failure_messages) == failure_messages
    result_details = [dict(detail) for detail in result.failure_details]
    assert result_details == failure_details

    report_path = visitor.last_report_path
    assert report_path is not None
    assert report_path.suffix == ".json"
    assert result.report_path == report_path
    payload_text = report_path.read_text(encoding="utf-8")
    report_data_raw = cast("object", json.loads(payload_text))
    assert isinstance(report_data_raw, dict)
    report_data = cast("dict[str, object]", report_data_raw)

    failures_value = report_data.get("failures")
    assert isinstance(failures_value, list)
    failure_entries = cast("list[object]", failures_value)
    failures: list[dict[str, object]] = []
    for entry in failure_entries:
        assert isinstance(entry, dict)
        typed_entry = cast("dict[str, object]", entry)
        failures.append(typed_entry)

    repo_tool_pairs: list[tuple[str, str]] = []
    for entry in failures:
        repo = entry.get("repo")
        tool = entry.get("tool")
        assert isinstance(repo, str)
        assert isinstance(tool, str)
        repo_tool_pairs.append((repo, tool))
    assert repo_tool_pairs == [("repo_a", "ruff_check"), ("repo_b", "mypy")]

    command_a = failures[0].get("command")
    command_b = failures[1].get("command")
    assert isinstance(command_a, str)
    assert isinstance(command_b, str)
    assert command_a == "python -m ruff check ."
    assert command_b == "python -m mypy . --strict"

    suggested = failures[0].get("suggested_action")
    assert suggested == "Investigate"

    stdout_preview = failures[0].get("stdout_preview")
    assert stdout_preview == "lint error"

    stderr_preview = failures[1].get("stderr_preview")
    assert isinstance(stderr_preview, str)
    assert "incompatible types" in stderr_preview


def test_run_inspect_flow_creates_empty_failure_report(
    tmp_path: pathlib.Path,
) -> None:
    workspace = pathlib.Path(tmp_path) / "workspace"
    workspace.mkdir()
    _create_repo(workspace, "repo_clean")

    reports_dir = pathlib.Path(tmp_path) / "reports"

    tool_reports: dict[str, dict[str, object]] = {
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
    payload_text = report_path.read_text(encoding="utf-8")
    report_data_raw = cast("object", json.loads(payload_text))
    assert isinstance(report_data_raw, dict)
    report_data = cast("dict[str, object]", report_data_raw)
    failures_value = report_data.get("failures")
    assert isinstance(failures_value, list)
    failures = cast("list[object]", failures_value)
    assert failures == []

    summary = report_data.get("summary")
    assert isinstance(summary, Mapping)
    summary_map = cast("Mapping[str, object]", summary)
    assert summary_map.get("total_repos") == 1


def test_workspace_root_can_be_git_repo(tmp_path: pathlib.Path) -> None:
    workspace = pathlib.Path(tmp_path)
    (workspace / ".git").mkdir()
    _create_repo(workspace, "child_repo")

    visitor = x_cls_make_github_visitor_x(workspace)
    assert visitor.root == workspace
