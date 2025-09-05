from __future__ import annotations

"""Helper to append lessons for ruff/black/mypy into x_lessons_x.json.

Provides a class `x_cls_make_github_visitor_lesson_x` with three methods:
- add_ruff_lesson(json_data, explanation_and_fix)
- add_black_lesson(json_data, explanation_and_fix)
- add_mypy_lesson(json_data, explanation_and_fix)

Each method accepts a breadcrumb JSON (as a dict) and a human-friendly
explanation_and_fix string. Lessons are appended to the lists under keys
`ruff`, `black`, and `mypy` in `x_lessons_x.json` located in the same
directory as this script.
"""

from pathlib import Path
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List


class x_cls_make_github_visitor_lesson_x:
    """Manage lessons for ruff/black/mypy by appending entries to x_lessons_x.json."""

    def __init__(self, root: str | Path | None = None) -> None:
        # root defaults to the directory containing this file
        self.root = Path(root) if root is not None else Path(__file__).resolve().parent
        self.lessons_path = self.root / "x_lessons_x.json"

    def _load(self) -> Dict[str, List[Dict[str, Any]]]:
        data: Dict[str, List[Dict[str, Any]]] = {"ruff": [], "black": [], "mypy": []}
        try:
            if self.lessons_path.exists():
                with self.lessons_path.open("r", encoding="utf-8") as fh:
                    raw = json.load(fh)
                    if isinstance(raw, dict):
                        # keep only the expected keys and ensure lists of dicts
                        for k in ("ruff", "black", "mypy"):
                            v = raw.get(k, [])
                            if isinstance(v, list):
                                data[k] = [x for x in v if isinstance(x, dict)]
                            else:
                                data[k] = []
        except Exception:
            data = {"ruff": [], "black": [], "mypy": []}
        return data

    def _write(self, data: Dict[str, List[Dict[str, Any]]]) -> None:
        tmp = self.lessons_path.with_name(self.lessons_path.name + ".tmp")
        with tmp.open("w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=4, sort_keys=True)
            fh.flush()
            try:
                os.fsync(fh.fileno())
            except Exception:
                pass
        os.replace(str(tmp), str(self.lessons_path))

    def _append(self, key: str, json_data: Dict[str, Any], explanation_and_fix: str) -> None:
        if key not in ("ruff", "black", "mypy"):
            raise AssertionError("invalid lesson key")
        data = self._load()
        entry = {
            "breadcrumb": json_data,
            "explanation_and_fix": explanation_and_fix,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        # Fail-fast if the same breadcrumb was already added (ignore explanation)
        for existing in data.get(key, []):
            if existing.get("breadcrumb") == json_data:
                raise AssertionError(f"duplicate breadcrumb for key={key} repo={json_data.get('repo')}")

        data[key].append(entry)
        self._write(data)

    def add_ruff_lesson(self, breadcrumb: Dict[str, Any], explanation_and_fix: str) -> None:
        """Append a lesson under the `ruff` key.

        breadcrumb: JSON-like dict describing the failure.
        explanation_and_fix: human readable instructions to fix it.
        """
        self._append("ruff", breadcrumb, explanation_and_fix)

    def add_black_lesson(self, breadcrumb: Dict[str, Any], explanation_and_fix: str) -> None:
        """Append a lesson under the `black` key."""
        self._append("black", breadcrumb, explanation_and_fix)

    def add_mypy_lesson(self, breadcrumb: Dict[str, Any], explanation_and_fix: str) -> None:
        """Append a lesson under the `mypy` key."""
        self._append("mypy", breadcrumb, explanation_and_fix)


if __name__ == "__main__":
    inst = x_cls_make_github_visitor_lesson_x()
    inst.add_mypy_lesson(
        {
            "repo": "x_0_make_all_x",
            "report": {
            "cmd": "C:\\Users\\eye43\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m mypy --strict --no-warn-unused-configs --show-error-codes .",
            "exit": 1,
            "stderr": "",
            "stdout": "x_cls_make_all_x.py:11: error: Skipping analyzing \"x_make_github_clones_x.x_cls_make_github_clones_x\": module is installed, but missing library stubs or py.typed marker  [import-untyped]\nx_cls_make_all_x.py:11: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports\nx_cls_make_all_x.py:14: error: Skipping analyzing \"x_make_pypi_x.x_cls_make_pypi_x\": module is installed, but missing library stubs or py.typed marker  [import-untyped]\nFound 2 errors in 1 file (checked 1 source file)\n"
            },
            "timestamp": "2025-09-05T02:59:14.803213+00:00",
            "tool": "mypy"
        },
        "TODO"
    )
    print(f"Wrote lesson to: {inst.lessons_path}")
