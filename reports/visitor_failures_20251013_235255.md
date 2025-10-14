# Visitor Failure Report — 2025-10-13T23:52:55.304910+00:00

- Workspace root: `c:\x_runner_x`
- Run started at: 2025-10-13T23:51:08.061430+00:00
- Run completed at: 2025-10-13T23:52:55.304715+00:00
- Total repositories examined: 14
- Total tool executions: 70
- Failing tool executions: 15
- Cache hits: 2

## Failures

- [ ] `x_0_make_all_x` · `ruff_fix` — ruff_fix failed for x_0_make_all_x (exit 1) cwd: c:\x_runner_x\x_0_make_all_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_0_make_all_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T23:51:13.331946+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC002 Move third-party import `x_make_common_x.telemetry.TelemetryEvent` into a type-checking block
    >   --> interface\gui\app.py:16:39
    >    |
    > 15 | from x_make_common_x import log_error, register_listener
    > 16 | from x_make_common_x.telemetry import TelemetryEvent
    > …

- [ ] `x_0_make_all_x` · `black` — black failed for x_0_make_all_x (exit 1) cwd: c:\x_runner_x\x_0_make_all_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T23:51:13.7300…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_0_make_all_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T23:51:15.495935+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_0_make_all_x\interface\gui\app.py	2025-10-13 23:37:43.632940+00:00
    > +++ C:\x_runner_x\x_0_make_all_x\interface\gui\app.py	2025-10-13 23:51:15.192304+00:00
    > @@ -219,11 +219,13 @@
    >          self._repo_files.setdefault(repo, set()).add(rel_path)
    >          row = self._append_row(repo, rel_path)
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\app.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 1 file would be reformatted, 13 files would be left unchanged.

- [ ] `x_0_make_all_x` · `ruff_check` — ruff_check failed for x_0_make_all_x (exit 1) cwd: c:\x_runner_x\x_0_make_all_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_0_make_all_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T23:51:15.860604+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC002 Move third-party import `x_make_common_x.telemetry.TelemetryEvent` into a type-checking block
    >   --> interface\gui\app.py:16:39
    >    |
    > 15 | from x_make_common_x import log_error, register_listener
    > 16 | from x_make_common_x.telemetry import TelemetryEvent
    > …

- [ ] `x_0_make_all_x` · `mypy` — mypy failed for x_0_make_all_x (exit 1) cwd: c:\x_runner_x\x_0_make_all_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --d…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_0_make_all_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T23:51:18.472233+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_common_x\telemetry.py:45: error: Explicit "Any" is not allowed  [explicit-any]
    > c:\x_runner_x\x_make_common_x\telemetry.py:49: error: Expression type contains "Any" (has type "tuple[str, list[Any]]")  [misc]
    > c:\x_runner_x\x_make_common_x\telemetry.py:49: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    > c:\x_runner_x\x_make_common_x\telemetry.py:61: error: Expression type contains "Any" (has type "tuple[str, dict[Any, Any]]")  [misc]
    > c:\x_runner_x\x_make_common_x\telemetry.py:61: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    > …

- [ ] `x_legatus_acta_schedae_x` · `mypy` — mypy failed for x_legatus_acta_schedae_x (exit 1) cwd: c:\x_runner_x\x_legatus_acta_schedae_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T23:51:28.272266+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_common_x\telemetry.py:45: error: Explicit "Any" is not allowed  [explicit-any]
    > c:\x_runner_x\x_make_common_x\telemetry.py:49: error: Expression type contains "Any" (has type "tuple[str, list[Any]]")  [misc]
    > c:\x_runner_x\x_make_common_x\telemetry.py:49: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    > c:\x_runner_x\x_make_common_x\telemetry.py:61: error: Expression type contains "Any" (has type "tuple[str, dict[Any, Any]]")  [misc]
    > c:\x_runner_x\x_make_common_x\telemetry.py:61: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    > …

- [ ] `x_legatus_acta_schedae_x` · `pyright` — pyright failed for x_legatus_acta_schedae_x (exit 1) cwd: c:\x_runner_x\x_legatus_acta_schedae_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T23:51:28.355299+00:00 duration…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T23:51:31.607440+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_legatus_acta_schedae_x\tests\test_automation_service.py
    >   c:\x_runner_x\x_legatus_acta_schedae_x\tests\test_automation_service.py:59:26 - error: "Request" is not a known attribute of module "httpx" (reportAttributeAccessIssue)
    >   c:\x_runner_x\x_legatus_acta_schedae_x\tests\test_automation_service.py:61:32 - error: "Request" is not a known attribute of module "httpx" (reportAttributeAccessIssue)
    >   c:\x_runner_x\x_legatus_acta_schedae_x\tests\test_automation_service.py:61:50 - error: "Response" is not a known attribute of module "httpx" (reportAttributeAccessIssue)
    >   c:\x_runner_x\x_legatus_acta_schedae_x\tests\test_automation_service.py:63:22 - error: "Response" is not a known attribute of module "httpx" (reportAttributeAccessIssue)
    > …

- [ ] `x_make_common_x` · `ruff_fix` — ruff_fix failed for x_make_common_x (exit 1) cwd: c:\x_runner_x\x_make_common_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_make_common_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T23:51:32.766562+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >  --> telemetry.py:7:29
    >   |
    > 5 | import json
    > 6 | import threading
    > …

- [ ] `x_make_common_x` · `black` — black failed for x_make_common_x (exit 1) cwd: c:\x_runner_x\x_make_common_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T23:51:32.76…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_make_common_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T23:51:34.257129+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_common_x\tests\__init__.py	2025-10-13 23:37:26.558942+00:00
    > +++ C:\x_runner_x\x_make_common_x\tests\__init__.py	2025-10-13 23:51:33.818417+00:00
    > @@ -2,20 +2,20 @@
    >  
    >  import sys
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_make_common_x\tests\__init__.py
    > would reformat C:\x_runner_x\x_make_common_x\tests\test_telemetry.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 2 files would be reformatted, 7 files would be left unchanged.

- [ ] `x_make_common_x` · `ruff_check` — ruff_check failed for x_make_common_x (exit 1) cwd: c:\x_runner_x\x_make_common_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_make_common_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T23:51:34.552582+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >  --> telemetry.py:7:29
    >   |
    > 5 | import json
    > 6 | import threading
    > …

- [ ] `x_make_common_x` · `mypy` — mypy failed for x_make_common_x (exit 1) cwd: c:\x_runner_x\x_make_common_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable -…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_make_common_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T23:51:36.004174+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > tests\__init__.py:19: error: Module has no attribute "HTTPError"  [attr-defined]
    > tests\__init__.py:20: error: Module has no attribute "Client"  [attr-defined]
    > telemetry.py:19: error: Unused "type: ignore" comment, use narrower [import-untyped] instead of [import] code  [unused-ignore]
    > telemetry.py:45: error: Explicit "Any" is not allowed  [explicit-any]
    > telemetry.py:49: error: Expression type contains "Any" (has type "tuple[str, list[Any]]")  [misc]
    > …

- [ ] `x_make_common_x` · `pyright` — pyright failed for x_make_common_x (exit 1) cwd: c:\x_runner_x\x_make_common_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T23:51:36.006308+00:00 duration: 1.711s tool_vers…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_make_common_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T23:51:37.717354+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_common_x\tests\__init__.py
    >   c:\x_runner_x\x_make_common_x\tests\__init__.py:19:13 - error: Cannot assign to attribute "HTTPError" for class "ModuleType"
    >   Â Â Attribute "HTTPError" is unknown (reportAttributeAccessIssue)
    >   c:\x_runner_x\x_make_common_x\tests\__init__.py:20:13 - error: Cannot assign to attribute "Client" for class "ModuleType"
    >   Â Â Attribute "Client" is unknown (reportAttributeAccessIssue)
    > …

- [ ] `x_make_github_visitor_x` · `ruff_fix` — ruff_fix failed for x_make_github_visitor_x (exit 1) cwd: c:\x_runner_x\x_make_github_visitor_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 …
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_make_github_visitor_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T23:51:43.721847+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > E501 Line too long (92 > 88)
    >    --> x_cls_make_github_visitor_x.py:180:89
    >     |
    > 178 |         if self._root_is_git_repo:
    > 179 |             _info(
    > …

- [ ] `x_make_github_visitor_x` · `ruff_check` — ruff_check failed for x_make_github_visitor_x (exit 1) cwd: c:\x_runner_x\x_make_github_visitor_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --ta…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_make_github_visitor_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T23:51:45.540474+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > E501 Line too long (92 > 88)
    >    --> x_cls_make_github_visitor_x.py:180:89
    >     |
    > 178 |         if self._root_is_git_repo:
    > 179 |             _info(
    > …

- [ ] `x_make_github_visitor_x` · `pyright` — pyright failed for x_make_github_visitor_x (exit 1) cwd: c:\x_runner_x\x_make_github_visitor_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T23:51:47.203031+00:00 duration: …
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_make_github_visitor_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T23:51:49.035495+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py
    >   c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:13:6 - error: Import "x_make_common_x" could not be resolved (reportMissingImports)
    >   c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:13:29 - error: Type of "emit_event" is unknown (reportUnknownVariableType)
    >   c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:13:41 - error: Type of "make_event" is unknown (reportUnknownVariableType)
    > c:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py
    > …

- [ ] `x_make_pip_updates_x` · `mypy` — mypy failed for x_make_pip_updates_x (exit 1) cwd: c:\x_runner_x\x_make_pip_updates_x command: c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unr…
  - Command: `c:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `c:\x_runner_x\x_make_pip_updates_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T23:52:22.520243+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_common_x\telemetry.py:45: error: Explicit "Any" is not allowed  [explicit-any]
    > c:\x_runner_x\x_make_common_x\telemetry.py:49: error: Expression type contains "Any" (has type "tuple[str, list[Any]]")  [misc]
    > c:\x_runner_x\x_make_common_x\telemetry.py:49: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    > c:\x_runner_x\x_make_common_x\telemetry.py:61: error: Expression type contains "Any" (has type "tuple[str, dict[Any, Any]]")  [misc]
    > c:\x_runner_x\x_make_common_x\telemetry.py:61: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    > …

---

_Generated by x_make_github_visitor_x_; actionable items are tracked as unchecked tasks._
