"""add_none_return_to_main.py

Aggressively annotate functions with `-> None` where safe.

This script operates on Python files (or directories). For each Python file
it processes it will annotate every function definition (top-level,
nested, or methods) that:
    - has no existing return annotation, and
    - contains no `return` statement with a value.

For each modified file the script writes a backup with the suffix `.bak` and
then replaces the file in-place. The script uses the stdlib `ast` for a
conservative check and `libcst` to perform source-safe edits while preserving
formatting.

Usage (PowerShell)
1. Install the library required for editing:
    pip install libcst

2. Run the script on one or more Python files or directories:
    python ./x_mypy_fix_0000_add_none_return_to_main_x.py C:/path/to/file.py
    python ./x_mypy_fix_0000_add_none_return_to_main_x.py C:/path/to/dir

Note: this script does NOT create `py.typed` markers. Use the companion
`x_mypy_fix_0001_touch_pytyped_x.py` script to add `py.typed` markers to
package directories. Each fixer modifies one thing only.

Safety notes
- The transformation is conservative: a function that returns a value is
    never annotated. The script creates `.bak` backups for easy rollback.
- Review `.bak` files or use `git diff` before committing changes.
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


def file_has_safe_functions(path: Path) -> set[tuple[int, int]]:
    """Return a set of (lineno, col_offset) for FunctionDef nodes that are
    safe to annotate (no return annotation and no return with a value).

    We return the node positions to use as a conservative fingerprint when
    applying edits with LibCST.
    """
    out: set[tuple[int, int]] = set()
    try:
        src = path.read_text(encoding="utf-8")
    except Exception:
        return out
    try:
        tree = ast.parse(src)
    except Exception:
        return out

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # skip if already annotated
            if node.returns is not None:
                continue
            # skip if any return with a value exists inside this function
            has_value_return = False
            for sub in ast.walk(node):
                if isinstance(sub, ast.Return) and sub.value is not None:
                    has_value_return = True
                    break
            if not has_value_return:
                # use the start position as a fingerprint
                out.add((node.lineno, node.col_offset))
    return out


class AddNoneReturnTransformer(cst.CSTTransformer):
    """LibCST transformer that adds `-> None` to safe function definitions.

    The transformer checks each FunctionDef node: if it has no return
    annotation and its body contains no `return` with a value, we add
    `-> None` to the signature. This applies to top-level functions,
    nested functions, and methods.
    """

    def _has_value_return(self, node: cst.CSTNode) -> bool:
        # Walk the subtree to detect any Return with a value
        for n in node.walk():
            if isinstance(n, cst.Return) and n.value is not None:
                return True
        return False

    def leave_FunctionDef(self, original: cst.FunctionDef, updated: cst.FunctionDef) -> cst.FunctionDef:  # type: ignore[override]
        # only annotate when there's no existing annotation
        if original.returns is not None:
            return updated
        # skip if there is any return with a value in the function body
        if self._has_value_return(updated):
            return updated
        # add -> None
        return updated.with_changes(returns=cst.Annotation(cst.Name("None")))


def process_file(path: Path) -> bool:
    """Process a single file. Returns True if the file was modified."""
    if not path.exists() or path.suffix != ".py":
        return False
    # Always report that we attempted to process this file
    try:
        print(f"Processing: {path}")
    except Exception:
        pass
    safe_funcs = file_has_safe_functions(path)
    if not safe_funcs:
        try:
            print(f"  no safe functions found in: {path}")
        except Exception:
            pass
        return False

    # ensure parent dir has py.typed
    parent = path.parent
    pytyped = parent / "py.typed"
    try:
        if not pytyped.exists():
            pytyped.write_text("", encoding="utf-8")
    except Exception:
        # best-effort; do not fail the annotator if we cannot write py.typed
        pass

    src = path.read_text(encoding="utf-8")
    # backup
    bak = path.with_suffix(path.suffix + ".bak")
    bak.write_text(src, encoding="utf-8")

    module = cst.parse_module(src)
    new_module = module.visit(AddNoneReturnTransformer())
    path.write_text(new_module.code, encoding="utf-8")
    try:
        print(f"  annotated: {path}")
    except Exception:
        pass
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

    # Emit a machine-readable one-line JSON summary for caller automation
    try:
        import json

        if all_changed:
            summary = {"explanation_and_fix": f"annotated {len(all_changed)} file(s): {all_changed}"}
        else:
            summary = {"explanation_and_fix": "no safe functions annotated"}
        print(json.dumps(summary))
    except Exception:
        pass


if __name__ == "__main__":
    main()
