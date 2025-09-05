"""xmypy002fix

Apply two targeted mypy-friendly transformations to Python files:
1) Add `-> None` to top-level `def main(...)` declarations that lack a return annotation.
2) Replace static `from x_make_... import Name` imports with a small importlib-based dynamic import block
   (this mirrors the manual changes applied in x_cls_make_all_x.py) so mypy does not complain about
   installed packages missing `py.typed` or stubs.

Usage:
    python x_mypy_fix_0002_xmypy002fix_x.py <file-or-dir> [...]

This script creates a `.bak` backup for each file it modifies.
It prints a JSON one-line summary to stdout on exit: {"explanation_and_fix": "..."}
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List
import json


def _ensure_typing_any_import(src: str) -> str:
    # Add `from typing import Any` if not present and if we need it
    if "from typing import Any" in src:
        return src
    # If there's any 'Any' references already, ensure import exists
    if "Any" in src and "from typing import Any" not in src:
        # place import after module docstring if present or at top
        m = re.match(r"(\s*\"\"\".*?\"\"\"\s*)", src, flags=re.S)
        if m:
            i = m.end(1)
            return src[:i] + "from typing import Any\n" + src[i:]
        return "from typing import Any\n" + src
    return src


def transform_imports(src: str) -> tuple[str, int]:
    # Replace lines like: from x_make_github_clones_x.x_cls_make_github_clones_x import x_cls_make_github_clones_x
    # with a dynamic import block using importlib and Any typing.
    changed = 0

    # match lines like: (optional indent) from x_make_pkg.module import Name[, Other]
    pattern = re.compile(r"^[ \t]*from\s+(x_make[\w\.]+)\s+import\s+([\w,\s]+)$", flags=re.M)

    def repl(match: re.Match) -> str:
        nonlocal changed
        module = match.group(1)
        names = [n.strip() for n in match.group(2).split(",") if n.strip()]
        sb = []
        sb.append("try:")
        sb.append("    import importlib")
        sb.append("")
        for name in names:
            sb.append(f"    {name}: Any")
        sb.append("")
        for name in names:
            sb.append(f"    mod = importlib.import_module(\"{module}\")")
            sb.append(f"    {name} = getattr(mod, \"{name}\")")
        sb.append("except Exception:")
        sb.append("    import sys")
        sb.append("    sys.stderr.write(\"ERROR: Could not import required packages from site-packages.\\n\")")
        sb.append("    sys.stderr.write(\"Install the packages (e.g. pip install x_make_github_clones_x x_make_pip_updates_x x_make_pypi_x)\\n\")")
        sb.append("    raise")
        changed += 1
        return "\n".join(sb)

    new_src = pattern.sub(repl, src)
    # if we replaced anything and we used 'Any', ensure import
    if changed:
        new_src = _ensure_typing_any_import(new_src)
    return new_src, changed


def transform_main_annotation(src: str) -> tuple[str, int]:
    # Annotate any function definition lacking a return annotation and containing
    # no `return <value>` inside. This requires LibCST; fail fast with a
    # clear error if libcst is not installed to avoid flaky regex-based edits.
    try:
        import libcst as _cst
    except Exception:  # pragma: no cover - environment must install libcst
        print("libcst is required for xmypy002fix: pip install libcst", file=sys.stderr)
        sys.exit(2)

    class _AnnotateNoneTransformer(_cst.CSTTransformer):
        def _has_value_return(self, node: _cst.CSTNode) -> bool:
            for n in node.walk():
                if isinstance(n, _cst.Return) and n.value is not None:
                    return True
            return False

        def leave_FunctionDef(self, original: _cst.FunctionDef, updated: _cst.FunctionDef) -> _cst.FunctionDef:  # type: ignore[override]
            # only annotate when there's no existing annotation
            if original.returns is not None:
                return updated
            # skip if there is any return with a value in the function body
            if self._has_value_return(updated):
                return updated
            return updated.with_changes(returns=_cst.Annotation(_cst.Name("None")))

    module = _cst.parse_module(src)
    new_module = module.visit(_AnnotateNoneTransformer())
    new_src = new_module.code
    changed = 1 if new_src != src else 0
    return new_src, changed


def process_file(path: Path) -> dict:
    info = {"path": str(path), "changes": []}
    try:
        src = path.read_text(encoding="utf-8")
    except Exception:
        info["error"] = "read_failed"
        return info

    orig = src
    src, imp_changes = transform_imports(src)
    if imp_changes:
        info["changes"].append(f"rewrote {imp_changes} import(s)")
    src, main_changes = transform_main_annotation(src)
    if main_changes:
        info["changes"].append(f"annotated main {main_changes} time(s)")

    if src != orig:
        # backup
        bak = path.with_suffix(path.suffix + ".bak")
        try:
            bak.write_text(orig, encoding="utf-8")
            path.write_text(src, encoding="utf-8")
        except Exception as exc:
            info["error"] = f"write_failed: {exc}"
            return info
        info["modified"] = True
    else:
        info["modified"] = False
    return info


def walk_and_process(p: Path) -> List[dict]:
    out: List[dict] = []
    if p.is_file():
        if p.suffix == ".py":
            out.append(process_file(p))
    else:
        for f in p.rglob("*.py"):
            try:
                out.append(process_file(f))
            except Exception:
                continue
    return out


def main(argv: List[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print("Usage: python xmypy002fix <file-or-dir> [...])", file=sys.stderr)
        sys.exit(2)

    paths = [Path(x) for x in argv]
    all_changed: List[dict] = []
    for p in paths:
        all_changed.extend(walk_and_process(p))

    modified = [x for x in all_changed if x.get("modified")]
    changed_paths = [m.get("path") for m in modified]
    if modified:
        print("Modified files:")
        for m in modified:
            print(" ", m.get("path"), m.get("changes"))
    else:
        print("No changes applied by xmypy002fix")

    # Emit machine-readable summary
    try:
        summary = {
            "explanation_and_fix": (
                f"xmypy002fix: modified {len(modified)} file(s): {changed_paths}"
                if modified
                else "xmypy002fix: no changes"
            )
        }
        print(json.dumps(summary))
    except Exception:
        pass


if __name__ == "__main__":
    main()
