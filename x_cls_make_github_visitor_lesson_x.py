from __future__ import annotations

"""Helper to append lessons for ruff/black/mypy into x_lessons_x.json.

Provides a class `x_cls_make_github_visitor_lesson_x` with three methods:
- add_ruff_lesson(json_data, explanation)
- add_black_lesson(json_data, explanation)
- add_mypy_lesson(json_data, explanation)

Each method accepts a breadcrumb JSON (as a dict) and a human-friendly
explanation string. Lessons are appended to the lists under keys
`ruff`, `black`, and `mypy` in `x_lessons_x.json` located in the same
directory as this script.
"""

from pathlib import Path
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict


class x_cls_make_github_visitor_lesson_x:
    """Manage lessons for ruff/black/mypy by appending entries to x_lessons_x.json."""

    def __init__(self, root: str | Path | None = None) -> None:
        # root defaults to the directory containing this file
        self.root = Path(root) if root is not None else Path(__file__).resolve().parent
        self.lessons_path = self.root / "x_lessons_x.json"

    def _load(self) -> Dict[str, list]:
        data: Dict[str, list] = {"ruff": [], "black": [], "mypy": []}
        try:
            if self.lessons_path.exists():
                with self.lessons_path.open("r", encoding="utf-8") as fh:
                    raw = json.load(fh)
                    if isinstance(raw, dict):
                        # keep only the expected keys and ensure lists
                        for k in ("ruff", "black", "mypy"):
                            v = raw.get(k, [])
                            data[k] = v if isinstance(v, list) else []
        except Exception:
            # on any error, return the default structure
            data = {"ruff": [], "black": [], "mypy": []}
        return data

    def _write(self, data: Dict[str, list]) -> None:
        tmp = self.lessons_path.with_name(self.lessons_path.name + ".tmp")
        with tmp.open("w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=4, sort_keys=True)
            fh.flush()
            try:
                os.fsync(fh.fileno())
            except Exception:
                pass
        os.replace(str(tmp), str(self.lessons_path))

    def _append(self, key: str, json_data: Dict[str, Any], explanation: str) -> None:
        if key not in ("ruff", "black", "mypy"):
            raise AssertionError("invalid lesson key")
        data = self._load()
        entry = {
            "breadcrumb": json_data,
            "explanation": explanation,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        data[key].append(entry)
        self._write(data)

    def add_ruff_lesson(self, breadcrumb: Dict[str, Any], explanation: str) -> None:
        """Append a lesson under the `ruff` key.

        breadcrumb: JSON-like dict describing the failure.
        explanation: human readable instructions to fix it.
        """
        self._append("ruff", breadcrumb, explanation)

    def add_black_lesson(self, breadcrumb: Dict[str, Any], explanation: str) -> None:
        """Append a lesson under the `black` key."""
        self._append("black", breadcrumb, explanation)

    def add_mypy_lesson(self, breadcrumb: Dict[str, Any], explanation: str) -> None:
        """Append a lesson under the `mypy` key."""
        self._append("mypy", breadcrumb, explanation)


if __name__ == "__main__":
    # tiny interactive demo
    inst = x_cls_make_github_visitor_lesson_x()
    sample = {"repo": "example", "tool": "mypy", "report": {"exit": 1}}
    inst.add_mypy_lesson(sample, "Example: run mypy and fix missing annotations")
    print(f"Wrote lesson to: {inst.lessons_path}")
