# Visitor Failure Report — 2025-10-13T21:06:52.933540+00:00

- Workspace root: `C:\x_runner_x`
- Run started at: 2025-10-13T21:05:31.228985+00:00
- Run completed at: 2025-10-13T21:06:52.933348+00:00
- Total repositories examined: 14
- Total tool executions: 70
- Failing tool executions: 15
- Cache hits: 0

## Failures

- [ ] `x_0_make_all_x` · `mypy` — mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-un…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T21:05:38.538320+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > x_cls_make_all_x.py:373: error: Explicit "Any" is not allowed  [explicit-any]
    > x_cls_make_all_x.py:374: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:375: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:381: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:382: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > …

- [ ] `x_0_make_all_x` · `pyright` — pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T21:05:38.538854+00:00 duration: 1.791s tool_version: pyright 1.1…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T21:05:40.329835+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_0_make_all_x\interface\gui\app.py
    >   c:\x_runner_x\x_0_make_all_x\interface\gui\app.py:34:25 - error: "QtGui" is unknown import symbol (reportAttributeAccessIssue)
    > c:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py
    >   c:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py:417:24 - error: Cannot assign to attribute "force_reclone" for class "object"
    >   Â Â Attribute "force_reclone" is unknown (reportAttributeAccessIssue)
    > …

- [ ] `x_make_github_clones_x` · `ruff_fix` — ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T21:05:58.674063+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >   --> x_cls_make_github_clones_x.py:19:29
    >    |
    > 17 | import time
    > 18 | import urllib.request
    > …

- [ ] `x_make_github_clones_x` · `ruff_check` — ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T21:06:00.397073+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >   --> x_cls_make_github_clones_x.py:19:29
    >    |
    > 17 | import time
    > 18 | import urllib.request
    > …

- [ ] `x_make_github_clones_x` · `mypy` — mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable -…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T21:06:01.252005+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > x_cls_make_github_clones_x.py:608: error: Explicit "Any" is not allowed  [explicit-any]
    > x_cls_make_github_clones_x.py:619: error: "object" has no attribute "force_reclone"  [attr-defined]
    > x_cls_make_github_clones_x.py:663: error: Expression type contains "Any" (has type "Callable[..., object] | None")  [misc]
    > x_cls_make_github_clones_x.py:664: error: Expression type contains "Any" (has type "Callable[..., object] | None")  [misc]
    > x_cls_make_github_clones_x.py:676: error: Expression type contains "Any" (has type "Callable[..., object] | None")  [misc]
    > …

- [ ] `x_make_github_clones_x` · `pyright` — pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T21:06:01.252504+00:00 duration: 1.477s tool_vers…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T21:06:02.729763+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py
    >   c:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py:619:16 - error: Cannot assign to attribute "force_reclone" for class "object"
    >   Â Â Attribute "force_reclone" is unknown (reportAttributeAccessIssue)
    > 1 error, 0 warnings, 0 informations

- [ ] `x_make_pip_updates_x` · `ruff_fix` — ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T21:06:28.968048+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TRY003 Avoid specifying long messages outside the exception class
    >    --> update_flow.py:115:11
    >     |
    > 113 |     if last_exc is not None:
    > 114 |         raise last_exc
    > …

- [ ] `x_make_pip_updates_x` · `black` — black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T21:06:28.968585…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T21:06:30.639708+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-13 18:14:22.470723+00:00
    > +++ C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-13 21:06:30.375285+00:00
    > @@ -110,11 +110,13 @@
    >          except TypeError as exc:
    >              last_exc = exc
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_make_pip_updates_x\update_flow.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 1 file would be reformatted, 4 files would be left unchanged.

- [ ] `x_make_pip_updates_x` · `ruff_check` — ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 s…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T21:06:30.941347+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TRY003 Avoid specifying long messages outside the exception class
    >    --> update_flow.py:115:11
    >     |
    > 113 |     if last_exc is not None:
    > 114 |         raise last_exc
    > …

- [ ] `x_make_pip_updates_x` · `mypy` — mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --dis…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T21:06:31.734685+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > update_flow.py:19: error: Explicit "Any" is not allowed  [explicit-any]
    > update_flow.py:144: error: Unused "type: ignore" comment  [unused-ignore]
    > Found 2 errors in 1 file (checked 5 source files)

- [ ] `x_make_pypi_x` · `ruff_fix` — ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T21:06:39.281355+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC002 Move third-party import `x_0_make_all_x.manifest.ManifestEntry` into a type-checking block
    >   --> publish_flow.py:13:37
    >    |
    > 11 | from typing import Protocol, TypeVar, cast
    > 12 |
    > …

- [ ] `x_make_pypi_x` · `black` — black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T21:06:39.281821+00:00 duratio…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T21:06:41.227683+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-13 17:01:12.302995+00:00
    > +++ C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-13 21:06:40.773264+00:00
    > @@ -478,13 +478,11 @@
    >          "anc": context.ancillary_rel,
    >      }
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_make_pypi_x\publish_flow.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 1 file would be reformatted, 1 file would be left unchanged.

- [ ] `x_make_pypi_x` · `ruff_check` — ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T21:06:41.701345+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC002 Move third-party import `x_0_make_all_x.manifest.ManifestEntry` into a type-checking block
    >   --> publish_flow.py:13:37
    >    |
    > 11 | from typing import Protocol, TypeVar, cast
    > 12 |
    > …

- [ ] `x_make_pypi_x` · `mypy` — mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unim…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T21:06:42.563591+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > publish_flow.py:13: error: Skipping analyzing "x_0_make_all_x.manifest": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    > publish_flow.py:13: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    > publish_flow.py:14: error: Skipping analyzing "x_make_common_x": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    > publish_flow.py:23: error: Explicit "Any" is not allowed  [explicit-any]
    > publish_flow.py:91: error: Argument 1 to "options_to_kwargs" becomes "Any" due to an unfollowed import  [no-any-unimported]
    > …

- [ ] `x_make_pypi_x` · `pyright` — pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T21:06:42.563998+00:00 duration: 1.655s tool_version: pyright 1.1.4…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T21:06:44.218928+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_pypi_x\publish_flow.py
    >   c:\x_runner_x\x_make_pypi_x\publish_flow.py:13:6 - error: Import "x_0_make_all_x.manifest" could not be resolved (reportMissingImports)
    >   c:\x_runner_x\x_make_pypi_x\publish_flow.py:14:6 - error: Import "x_make_common_x" could not be resolved (reportMissingImports)
    > 2 errors, 0 warnings, 0 informations

---

_Generated by x_make_github_visitor_x_; actionable items are tracked as unchecked tasks._
