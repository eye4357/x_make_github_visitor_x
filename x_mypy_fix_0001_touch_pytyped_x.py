"""touch_pytyped.py

Create empty `py.typed` marker files in one or more package directories or
touch the parent directory of a given Python file.

This is useful when you have local packages that are installed (or importable)
but are not marked as typed. Creating a zero-byte `py.typed` file at the
package root tells mypy and other checkers that the package is typed and
should be analyzed.

Usage (PowerShell):
    python ./x_mypy_fix_0001_touch_pytyped_x.py C:/path/to/package_dir
    python ./x_mypy_fix_0001_touch_pytyped_x.py C:/path/to/file.py

Example for this workspace:
    python ./x_mypy_fix_0001_touch_pytyped_x.py C:/x_cloned_repos_x/x_make_github_clones_x
    python ./x_mypy_fix_0001_touch_pytyped_x.py C:/x_cloned_repos_x/x_0_make_all_x/x_cls_make_all_x.py

The script is intentionally minimal and will not overwrite an existing
`py.typed` file.
"""

from __future__ import annotations

from pathlib import Path
import sys


def touch_pytyped(pkg_dirs: list[str]) -> None:
    for d in pkg_dirs:
        p = Path(d)
        try:
            print(f"Processing: {d}")
        except Exception:
            pass
        if not p.exists():
            print(f"Path does not exist: {p}")
            continue
        # if the path is a file, touch its parent directory
        if p.is_file():
            p = p.parent
        if not p.is_dir():
            print(f"Not a directory, skipping: {p}")
            continue
        target = p / "py.typed"
        if target.exists():
            print(f"Exists: {target}")
        else:
            try:
                target.write_text("", encoding="utf-8")
                print(f"Created: {target}")
            except Exception as e:
                print(f"Failed to create {target}: {e}")


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print("Usage: python touch_pytyped.py <path-to-package> [...])", file=sys.stderr)
        sys.exit(2)
    touch_pytyped(argv)
    # Emit a machine-readable one-line JSON summary for caller automation
    try:
        import json

        summary = {"explanation_and_fix": "touched py.typed marker(s) where needed"}
        print(json.dumps(summary))
    except Exception:
        pass


if __name__ == "__main__":
    main()
