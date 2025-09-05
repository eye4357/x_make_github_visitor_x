"""add_none_return_to_main.py
Safe, programmatic annotator for top-level `def main()` functions.

This script finds top-level Python functions named `main` that:
- have no existing return type annotation, and
- do not contain any `return` statement with a value.

For each such file it finds, it writes a backup copy with the suffix
`.bak` (for example `x.py` -> `x.py.bak`) and then replaces the
function signature with one that adds `-> None` (e.g. `def main() -> None:`).

Rationale and safety notes
- We only annotate functions that appear safe (no value-returning `return`).
- The script creates backups so you can review changes before committing.
- It uses the stdlib `ast` to conservatively detect safe candidates, and
  `libcst` to perform source-safe edits preserving formatting.

Usage (PowerShell)
1. Install the library required for editing:
   pip install libcst

2. Run the script on a single file or a directory (recursively):
   python .\add_none_return_to_main.py C:\path\to\file_or_dir

Examples (your workspace):
   python .\add_none_return_to_main.py c:\x_cloned_repos_x\x_0_make_all_x

Review changes (git or by inspecting `.bak` files) before committing.

Limitations and edge cases
- If a `main` function is nested inside another function or class it will
  be skipped (we only consider top-level functions).
- If a function uses `return` without a value (i.e. `return`) it's still
  considered safe and will be annotated because it does not produce a value.
- If you want to annotate other function names or broader patterns, extend
  the `file_has_safe_main` predicate or the transformer.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path
from typing import List

try:
    import libcst as cst
except Exception:  # pragma: no cover - friendly error for missing dependency
    print("libcst is required: pip install libcst", file=sys.stderr)
    sys.exit(2)


def file_has_safe_main(path: Path) -> bool:
    """Return True if the given Python file has a top-level `def main()`
    with no return annotation and no `return` with a value.
    """
    try:
        src = path.read_text(encoding="utf-8")
    except Exception:
        return False
    try:
        tree = ast.parse(src)
    except Exception:
        return False

    for node in tree.body:  # only top-level definitions
        if isinstance(node, ast.FunctionDef) and node.name == "main":
            if node.returns is not None:
                return False
            # if any return with a value is present, skip
            for sub in ast.walk(node):
                if isinstance(sub, ast.Return) and sub.value is not None:
                    return False
            return True
    return False


class AddNoneReturnTransformer(cst.CSTTransformer):
    """A small LibCST transformer that adds `-> None` to `def main()`.

    We rely on `file_has_safe_main` to ensure safety (no value-returning
    returns) before applying this transformer to a file.
    """

    def leave_FunctionDef(self, original: cst.FunctionDef, updated: cst.FunctionDef) -> cst.FunctionDef:  # type: ignore[override]
        if isinstance(original.name, cst.Name) and original.name.value == "main" and original.returns is None:
            return updated.with_changes(returns=cst.Annotation(cst.Name("None")))
        return updated


def process_file(path: Path) -> bool:
    """Process a single file. Returns True if the file was modified."""
    if not path.exists() or path.suffix != ".py":
        return False
    if not file_has_safe_main(path):
        return False

    src = path.read_text(encoding="utf-8")
    # backup
    bak = path.with_suffix(path.suffix + ".bak")
    bak.write_text(src, encoding="utf-8")

    module = cst.parse_module(src)
    new_module = module.visit(AddNoneReturnTransformer())
    path.write_text(new_module.code, encoding="utf-8")
    return True


def walk_and_process(p: Path) -> List[str]:
    changed: List[str] = []
    if p.is_file():
        if p.suffix == ".py" and process_file(p):
            changed.append(str(p))
    else:
        for f in p.rglob("*.py"):
            try:
                if process_file(f):
                    changed.append(str(f))
            except Exception:
                # skip files we cannot parse/edit
                continue
    return changed


def main(argv: List[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print("Usage: python add_none_return_to_main.py <file-or-dir> [...])", file=sys.stderr)
        sys.exit(2)

    paths = [Path(x) for x in argv]
    all_changed: List[str] = []
    for p in paths:
        all_changed.extend(walk_and_process(p))

    if all_changed:
        print("Edited files:")
        for c in all_changed:
            print(" ", c)
    else:
        print("No safe 'main' functions found to annotate.")


if __name__ == "__main__":
    main()
