from __future__ import annotations

"""Utility to index local git repository clones under a root path.

This first-step implementation performs the following on construction:
- asserts the provided root path exists and is a directory
- examines each immediate child directory of the root and asserts it
  contains a `.git` directory (i.e. is a git clone)
- builds a JSON structure mapping the child repo name (path relative to
  the root) to a list of files present in that repo (excluding files
  inside any `.git` or `__pycache__` directories)
- writes the JSON file at the root directory (default filename
  `repos_index.json`) with indent=4 and sorted keys

Notes / assumptions:
- only immediate children of the root are considered repos (no
  recursive discovery)
- file lists are stored as paths relative to each repo root
"""

from pathlib import Path
import json
from typing import Optional


class x_cls_make_github_visitor_x:
   """Index immediate child git repositories under a given root.

   Example usage:
      inst = x_cls_make_github_visitor_x(r"C:/aaa/bbb/ccc")
   On construction the instance will validate and write `repos_index.json`
   into the provided root directory.
   """

   def __init__(self, root_dir: str | Path, *, output_filename: str = "repos_index.json") -> None:
      self.root = Path(root_dir)
      if not self.root.exists() or not self.root.is_dir():
         raise AssertionError(f"root path must exist and be a directory: {self.root}")

      # assert root is not itself a git repository
      if (self.root / ".git").exists():
         raise AssertionError(f"root path must not be a git repository: {self.root}")

      self.output_filename = output_filename

      # examine immediate child directories
      children = [p for p in self.root.iterdir() if p.is_dir()]

      # assert that each child directory is a git repo (contains .git)
      bad = [p for p in children if not (p / ".git").exists()]
      if bad:
         names = ", ".join(str(p) for p in bad)
         raise AssertionError(f"the following child directories are not git repos (missing .git): {names}")

      # build mapping: key = path relative to root (e.g. 'ddd'), value = list of files
      index: dict[str, list[str]] = {}
      for child in sorted(children):
         relkey = str(child.relative_to(self.root))
         files: list[str] = []
         for p in child.rglob("*"):
            # only include files
            if not p.is_file():
               continue
            # skip anything inside a .git or __pycache__ directory
            if ".git" in p.parts or "__pycache__" in p.parts:
               continue
            # store path relative to the repository root
            files.append(str(p.relative_to(child).as_posix()))

         index[relkey] = sorted(files)

      # write JSON to the provided root
      out_path = self.root / self.output_filename
      with out_path.open("w", encoding="utf-8") as fh:
         json.dump(index, fh, indent=4, sort_keys=True)


def init_name(root_dir: str | Path, *, output_filename: Optional[str] = None) -> "x_cls_make_github_visitor_x":
   """Convenience initializer that constructs and returns the visitor instance.

   This function matches the requested `init==name` behavior: it takes a
   root directory path as the first argument, constructs the class (which
   performs validation and writes the JSON), and returns the instance.
   """
   if output_filename is None:
      return x_cls_make_github_visitor_x(root_dir)
   else:
      return x_cls_make_github_visitor_x(root_dir, output_filename=output_filename)


def init_main() -> "x_cls_make_github_visitor_x":
   """Initialize the visitor with the fixed root path C:\\foboar.

   This convenience function follows your request to make the root
   path `c:\\foboar` and returns the constructed instance.
   """
   return init_name(r"C:\x_cloned_repos_x")


if __name__ == "__main__":
   inst = init_main()
   out = inst.root / inst.output_filename
   print(f"wrote repository index to: {out}")

