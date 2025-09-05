"""touch_pytyped.py

Create empty `py.typed` marker files in one or more package directories.

This is useful when you have local packages that are installed (or importable)
but are not marked as typed. Creating a zero-byte `py.typed` file at the
package root tells mypy and other checkers that the package is typed and
should be analyzed.

Usage (PowerShell):
  python .\touch_pytyped.py c:\path\to\package1 c:\path\to\package2

Example for this workspace:
  python .\touch_pytyped.py c:\x_cloned_repos_x\x_make_github_clones_x c:\x_cloned_repos_x\x_make_pypi_x

The script is intentionally minimal and will not overwrite an existing
`py.typed` file.
"""

from __future__ import annotations

from pathlib import Path
import sys


def touch_pytyped(pkg_dirs: list[str]) -> None:
    for d in pkg_dirs:
        p = Path(d)
        if not p.exists():
            print(f"Path does not exist: {p}")
            continue
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


if __name__ == "__main__":
    main()
