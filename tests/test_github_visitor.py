from __future__ import annotations

import json
from pathlib import Path

from x_cls_make_github_visitor_x import x_cls_make_github_visitor_x


def _make_repo(parent: Path, name: str) -> Path:
    repo = parent / name
    repo.mkdir()
    (repo / ".git").mkdir()
    (repo / "sample.py").write_text("print('hello')\n", encoding="utf-8")
    return repo


def test_caching_round_trip(tmp_path: Path) -> None:
    _make_repo(tmp_path, "demo")
    visitor = x_cls_make_github_visitor_x(tmp_path, enable_cache=True)

    repo = visitor._child_dirs()[0]
    repo_hash = visitor._repo_content_hash(repo)

    result = {"exit": 0, "stdout": "ok", "stderr": "", "cached": False}
    visitor._store_cache("demo", "ruff_check", repo_hash, result)

    loaded = visitor._load_cache("demo", "ruff_check", repo_hash)
    assert loaded is not None
    assert loaded["stdout"] == "ok"


def test_summary_generation(tmp_path: Path) -> None:
    _make_repo(tmp_path, "demo")
    visitor = x_cls_make_github_visitor_x(tmp_path, enable_cache=False)

    visitor._tool_reports = {
        "demo": {
            "repo_hash": "abc",
            "tool_reports": {
                "ruff_fix": {"exit": 0, "cached": False},
                "black": {"exit": 1, "cached": False},
            },
        }
    }

    summary = visitor.generate_summary_report()
    assert summary["total_repos"] == 1
    assert summary["overall_stats"]["total_tools_run"] == 2
    assert summary["overall_stats"]["failed_tools"] == 1


def test_run_inspect_flow_indexes(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path, "demo")
    visitor = x_cls_make_github_visitor_x(tmp_path, enable_cache=False)

    (repo / "sample.py").write_text("value = 1\n", encoding="utf-8")

    visitor.inspect("test_index.json")
    output = visitor.package_root / "test_index.json"
    assert output.exists()
    data = json.loads(output.read_text(encoding="utf-8"))
    assert "demo" in data
    output.unlink()
