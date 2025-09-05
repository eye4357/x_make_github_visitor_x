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
   On construction the instance will validate the root and immediate
   children; it will NOT write any JSON. Use `inspect(json_name)` to
   produce index files.
   """

   def __init__(self, root_dir: str | Path, *, output_filename: str = "repos_index.json") -> None:
      self.root = Path(root_dir)
      if not self.root.exists() or not self.root.is_dir():
         raise AssertionError(f"root path must exist and be a directory: {self.root}")

      # assert root is not itself a git repository
      if (self.root / ".git").exists():
         raise AssertionError(f"root path must not be a git repository: {self.root}")

      # store output filename default but do not write here
      self.output_filename = output_filename

      # examine immediate child directories and assert they are git repos
      children = [p for p in self.root.iterdir() if p.is_dir()]
      # assert there is at least one child directory
      if not children:
         raise AssertionError(f"root path contains no child directories: {self.root}")
      bad = [p for p in children if not (p / ".git").exists()]
      if bad:
         names = ", ".join(str(p) for p in bad)
         raise AssertionError(f"the following child directories are not git repos (missing .git): {names}")

   # --- Modularized operations for inspect command -------------------------------------------------
   def inspect(self, json_name: str) -> None:
      """Run the verification and write the index to `json_name` at root.

      The `json_name` argument is required and will be used as the
      filename written into the configured root directory.
      """
      # verify children are proper repos and build index
      children = [p for p in self.root.iterdir() if p.is_dir()]
      # assert there is at least one child directory
      if not children:
         raise AssertionError(f"root path contains no child directories: {self.root}")

      bad = [p for p in children if not (p / ".git").exists()]
      if bad:
         names = ", ".join(str(p) for p in bad)
         raise AssertionError(f"the following child directories are not git repos (missing .git): {names}")

      index: dict[str, list[str]] = {}
      for child in sorted(children):
         relkey = str(child.relative_to(self.root))
         files: list[str] = []
         for p in child.rglob("*"):
            if not p.is_file():
               continue
            if ".git" in p.parts or "__pycache__" in p.parts:
               continue
            files.append(str(p.relative_to(child).as_posix()))

         index[relkey] = sorted(files)

      out_path = self.root / json_name
      with out_path.open("w", encoding="utf-8") as fh:
         json.dump(index, fh, indent=4, sort_keys=True)

   def body(self) -> None:
      """Placeholder for step 2 of the inspect flow. Implement analysis here."""
      # intentionally blank (user will implement)
      return None

   def cleanup(self) -> None:
      """Placeholder for cleanup (step 4). Implement teardown here if needed."""
      # intentionally minimal; user can override or extend
      return None

   def run_inspect_flow(self) -> None:
      """Run the inspect flow in four steps:
      1) a-priori run -> writes `x_index_a_a_priori_x.json`
      2) body() (blank)
      3) a-posteriori run -> writes `x_index_b_a_posteriori_x.json`
      4) cleanup()
      """
      # Step 1: a-priori inspect
      self.inspect("x_index_a_a_priori_x.json")
      p1 = self.root / "x_index_a_a_priori_x.json"
      assert p1.exists() and p1.stat().st_size > 0, f"step1 failed: {p1} missing or empty"

      # Step 2: body (placeholder) — any exception will naturally propagate
      self.body()

      # Step 3: a-posteriori inspect
      self.inspect("x_index_b_a_posteriori_x.json")
      p2 = self.root / "x_index_b_a_posteriori_x.json"
      assert p2.exists() and p2.stat().st_size > 0, f"step3 failed: {p2} missing or empty"

      # Step 4: cleanup
      self.cleanup()
   # --- end inspect command -----------------------------------------------------------------------


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
   # run the inspect flow which writes the a-priori and a-posteriori files
   inst.run_inspect_flow()
   print(f"wrote a-priori and a-posteriori index files to: {inst.root}")

