from __future__ import annotations

"""Small helper to append lessons for ruff/black/mypy into x_lessons_x.json.

Atomic file writes. Duplicate breadcrumbs are rejected with AssertionError.
"""

from pathlib import Path
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List


class x_cls_make_github_visitor_lesson_x:
    def __init__(self, root: str | Path | None = None) -> None:
        pkg_dir = Path(__file__).resolve().parent
        self.root = pkg_dir
        self.lessons_path = pkg_dir / "x_lessons_x.json"

    def _load(self) -> Dict[str, List[Dict[str, Any]]]:
        default = {"ruff": [], "black": [], "mypy": []}
        if not self.lessons_path.exists():
            return default
        try:
            with self.lessons_path.open("r", encoding="utf-8") as fh:
                raw = json.load(fh)
        except Exception:
            return default
        if not isinstance(raw, dict):
            return default
        out: Dict[str, List[Dict[str, Any]]] = {"ruff": [], "black": [], "mypy": []}
        for k in ("ruff", "black", "mypy"):
            v = raw.get(k, [])
            if isinstance(v, list):
                out[k] = [x for x in v if isinstance(x, dict)]
        return out

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

    def _append(self, key: str, breadcrumb: Dict[str, Any], explanation: str) -> None:
        if key not in ("ruff", "black", "mypy"):
            raise AssertionError("invalid lesson key")
        data = self._load()
        entry = {
            "breadcrumb": breadcrumb,
            "explanation_and_fix": explanation,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        for existing in data.get(key, []):
            if existing.get("breadcrumb") == breadcrumb:
                # idempotent: duplicate breadcrumb already recorded, no-op
                return None
        data[key].append(entry)
        self._write(data)

    def add_ruff_lesson(self, breadcrumb: Dict[str, Any], explanation: str) -> None:
        self._append("ruff", breadcrumb, explanation)

    def add_black_lesson(self, breadcrumb: Dict[str, Any], explanation: str) -> None:
        self._append("black", breadcrumb, explanation)

    def add_mypy_lesson(self, breadcrumb: Dict[str, Any], explanation: str) -> None:
        self._append("mypy", breadcrumb, explanation)


if __name__ == "__main__":
    inst = x_cls_make_github_visitor_lesson_x()
    inst.add_mypy_lesson({"repo": "x_0_make_all_x"}, "TODO")
    print(f"Wrote lesson to: {inst.lessons_path}")
