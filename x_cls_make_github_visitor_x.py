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
import os
from typing import Optional
import subprocess
import sys
from datetime import datetime, timezone


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
      # storage for tool reports produced by body()
      
      
      
      self._tool_reports = {}

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
      # Write atomically: write to a temp file in the same directory, fsync,
      # then replace the target. This guarantees the file is present on disk
      # before any subsequent step (e.g. body()) begins.
      tmp_path = out_path.with_name(out_path.name + ".tmp")
      with tmp_path.open("w", encoding="utf-8") as fh:
         json.dump(index, fh, indent=4, sort_keys=True)
         fh.flush()
         try:
            os.fsync(fh.fileno())
         except Exception:
            # if fsync is not available for some reason, proceed — replace
            # will still provide an atomic rename on the same filesystem.
            pass
      # Atomic replace
      os.replace(str(tmp_path), str(out_path))

   def body(self) -> None:
      """Placeholder for step 2 of the inspect flow. Implement analysis here."""
      # Implemented: ensure tools are installed/updated, run autofix and checks
      python = sys.executable

      # 1) ensure tools are installed/updated to latest
      cmd_install = [python, "-m", "pip", "install", "--upgrade", "ruff", "black", "mypy"]
      p = subprocess.run(cmd_install, capture_output=True, text=True)
      if p.returncode != 0:
         raise AssertionError(f"failed to install/update tools: {p.stderr}")

      # default timeout per tool (seconds)
      timeout = 120

      # per-repo reports
      reports = {}

      children = [p for p in self.root.iterdir() if p.is_dir()]
      children = sorted(children)

      for child in children:
         rel = str(child.relative_to(self.root))
         repo_report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tools": {},
         }

         # 2) ruff autofix
         cmd = [python, "-m", "ruff", "check", ".", "--fix"]
         p = subprocess.run(cmd, cwd=str(child), capture_output=True, text=True, timeout=timeout)
         repo_report["tools"]["ruff_fix"] = {"cmd": " ".join(cmd), "exit": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
         # treat non-zero as failure
         if p.returncode != 0:
            raise AssertionError(f"ruff --fix failed for {rel}: {p.stderr}")

         # 3) black autofix
         cmd = [python, "-m", "black", ".", "--line-length", "79"]
         p = subprocess.run(cmd, cwd=str(child), capture_output=True, text=True, timeout=timeout)
         repo_report["tools"]["black"] = {"cmd": " ".join(cmd), "exit": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
         if p.returncode != 0:
            raise AssertionError(f"black failed for {rel}: {p.stderr}")

         # 4) ruff check (post-fix)
         cmd = [python, "-m", "ruff", "check", "."]
         p = subprocess.run(cmd, cwd=str(child), capture_output=True, text=True, timeout=timeout)
         repo_report["tools"]["ruff_check"] = {"cmd": " ".join(cmd), "exit": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
         if p.returncode != 0:
            raise AssertionError(f"ruff check failed for {rel}: {p.stderr}")

         # 5) mypy strict check
         cmd = [python, "-m", "mypy", "--strict", "--no-warn-unused-configs", "--show-error-codes", "."]
         p = subprocess.run(cmd, cwd=str(child), capture_output=True, text=True, timeout=timeout)
         repo_report["tools"]["mypy"] = {"cmd": " ".join(cmd), "exit": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
         if p.returncode != 0:
            raise AssertionError(f"mypy failed for {rel}: {p.stderr}")

         # 6) also capture resulting file index for this repo (same logic as inspect)
         files = []
         for pth in child.rglob("*"):
            if not pth.is_file():
               continue
            if ".git" in pth.parts or "__pycache__" in pth.parts:
               continue
            files.append(str(pth.relative_to(child).as_posix()))
         repo_report["files"] = sorted(files)

         reports[rel] = repo_report

      # store for merge into a-posteriori index later
      self._tool_reports = reports
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

      # Additional strict safety check: re-read the a-priori index and ensure
      # its keys exactly match the set of immediate child repo names. Fail
      # fast on any discrepancy to prevent body() from running against an
      # unexpected or stale index.
      try:
         with p1.open("r", encoding="utf-8") as fh:
            apriori = json.load(fh)
      except Exception as exc:
         raise AssertionError(f"failed to read a-priori index: {exc}")

      if not isinstance(apriori, dict):
         raise AssertionError(f"a-priori index must be a JSON object mapping repo->files: {p1}")

      current_children = sorted([str(p.relative_to(self.root)) for p in self.root.iterdir() if p.is_dir()])
      apriori_keys = sorted(list(apriori.keys()))
      if apriori_keys != current_children:
         raise AssertionError(
            f"a-priori index contents do not match immediate children.\n  expected: {current_children}\n  found: {apriori_keys}"
         )

      # Step 2: body (placeholder) — any exception will naturally propagate
      self.body()

      # Step 3: a-posteriori inspect
      self.inspect("x_index_b_a_posteriori_x.json")
      p2 = self.root / "x_index_b_a_posteriori_x.json"
      assert p2.exists() and p2.stat().st_size > 0, f"step3 failed: {p2} missing or empty"

      # merge tool reports collected during body() into the a-posteriori JSON
      try:
         with p2.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
      except Exception as exc:
         raise AssertionError(f"failed to read a-posteriori index: {exc}")

      # attach reports under each repo key
      for repo_name, report in getattr(self, "_tool_reports", {}).items():
         if repo_name in data:
            # augment existing entry
            data[repo_name] = {"files": data.get(repo_name, []), "tools": report.get("tools", {}), "files_index": report.get("files", [])}
         else:
            data[repo_name] = {"files": report.get("files", []), "tools": report.get("tools", {})}

      # write back
      with p2.open("w", encoding="utf-8") as fh:
         json.dump(data, fh, indent=4, sort_keys=True)

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

