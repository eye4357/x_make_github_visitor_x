# ruff: noqa: S101

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

import pytest
from x_make_common_x.json_contracts import validate_payload, validate_schema

from x_make_github_visitor_x import (
    VisitorRunResult,
    main_json,
    x_cls_make_github_visitor_x,
)
from x_make_github_visitor_x.json_contracts import (
    ERROR_SCHEMA,
    INPUT_SCHEMA,
    OUTPUT_SCHEMA,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from _pytest.monkeypatch import MonkeyPatch
else:
    pytest = cast("Any", pytest)

fixture = cast("Callable[..., Any]", pytest.fixture)

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" / "json_contracts"


def _load_fixture(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        data: object = json.load(handle)
    if not isinstance(data, dict):
        message = f"Fixture payload must be an object: {path}"
        raise TypeError(message)
    return cast("dict[str, object]", data)


@fixture(scope="module")
def sample_input() -> dict[str, object]:
    return _load_fixture(FIXTURE_DIR / "input.json")


@fixture(scope="module")
def sample_output() -> dict[str, object]:
    return _load_fixture(FIXTURE_DIR / "output.json")


@fixture(scope="module")
def sample_error() -> dict[str, object]:
    return _load_fixture(FIXTURE_DIR / "error.json")


def test_schemas_are_valid() -> None:
    for schema in (INPUT_SCHEMA, OUTPUT_SCHEMA, ERROR_SCHEMA):
        validate_schema(schema)


def test_sample_payloads_match_schema(
    sample_input: dict[str, object],
    sample_output: dict[str, object],
    sample_error: dict[str, object],
) -> None:
    validate_payload(sample_input, INPUT_SCHEMA)
    validate_payload(sample_output, OUTPUT_SCHEMA)
    validate_payload(sample_error, ERROR_SCHEMA)


def test_main_json_runs_successfully(
    sample_input: dict[str, object],
    tmp_path: Path,
    monkeypatch: MonkeyPatch,
) -> None:
    payload = cast("dict[str, object]", json.loads(json.dumps(sample_input)))
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    parameters = cast("dict[str, object]", payload["parameters"])
    parameters["root_dir"] = str(workspace)

    def fake_run(self: x_cls_make_github_visitor_x) -> None:
        self._tool_reports = {
            "demo": {
                "repo_hash": "hash-demo",
                "tool_reports": {
                    "ruff_check": {
                        "exit": 0,
                        "cached": False,
                        "timed_out": False,
                    }
                },
            }
        }
        self._failure_messages = []
        self._failure_details = []
        self._last_run_failures = False
        self._runtime_snapshot = {
            "workspace_root": str(self.root),
            "run_started_at": "2025-10-18T10:00:00Z",
            "run_completed_at": "2025-10-18T10:01:00Z",
            "platform": "test-platform",
            "python_executable": sys.executable,
            "python_version": sys.version.replace("\n", " "),
        }
        self._tool_versions = {"ruff": "0.6.0"}
        report_path = self.package_root / "reports" / "visitor.json"
        self._last_report_path = report_path
        self._last_run_result = VisitorRunResult(
            report_path=report_path,
            had_failures=False,
            failure_messages=(),
            failure_details=(),
            skipped=False,
        )

    monkeypatch.setattr(
        x_cls_make_github_visitor_x,
        "run_inspect_flow",
        fake_run,
        raising=False,
    )

    result = main_json(payload)

    validate_payload(result, OUTPUT_SCHEMA)
    status = result.get("status")
    assert isinstance(status, str)
    assert status == "success"
    workspace_root = result.get("workspace_root")
    assert isinstance(workspace_root, str)
    assert workspace_root == str(workspace)
    failures = result.get("failures")
    assert isinstance(failures, list)
    assert not failures
    summary = result.get("summary")
    assert isinstance(summary, dict)
    total_repos = summary.get("total_repos")
    assert isinstance(total_repos, int)
    assert total_repos == 1


def test_main_json_handles_skip(
    sample_input: dict[str, object],
    tmp_path: Path,
    monkeypatch: MonkeyPatch,
) -> None:
    payload = cast("dict[str, object]", json.loads(json.dumps(sample_input)))
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    parameters = cast("dict[str, object]", payload["parameters"])
    parameters["root_dir"] = str(workspace)

    def fake_run(_: x_cls_make_github_visitor_x) -> None:
        error_message = "no child git repositories found under workspace"
        raise AssertionError(error_message)

    monkeypatch.setattr(
        x_cls_make_github_visitor_x,
        "run_inspect_flow",
        fake_run,
        raising=False,
    )

    result = main_json(payload)

    validate_payload(result, OUTPUT_SCHEMA)
    status = result.get("status")
    assert isinstance(status, str)
    assert status == "skipped"
    skipped = result.get("skipped")
    assert isinstance(skipped, bool)
    assert skipped is True
    report_path = result.get("report_path")
    assert report_path is None
    failures = result.get("failures")
    assert isinstance(failures, list)
    assert not failures


def test_main_json_reports_validation_error() -> None:
    payload: dict[str, object] = {
        "command": "x_make_github_visitor_x",
        "parameters": {},
    }

    result = main_json(payload)

    validate_payload(result, ERROR_SCHEMA)
    status = result.get("status")
    assert isinstance(status, str)
    assert status == "failure"
    message = result.get("message")
    assert isinstance(message, str)
    assert message == "input payload failed validation"
