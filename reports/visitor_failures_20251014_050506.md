# Visitor Failure Report — 2025-10-14T05:05:06.899220+00:00

- Workspace root: `C:\x_runner_x`
- Run started at: 2025-10-14T05:03:00.889345+00:00
- Run completed at: 2025-10-14T05:05:06.898996+00:00
- Total repositories examined: 14
- Total tool executions: 70
- Failing tool executions: 5
- Cache hits: 37

## Failures

- [ ] `x_0_make_all_x` · `ruff_fix` — ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: `C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-14T05:03:20.860544+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > PLR0915 Too many statements (71 > 50)
    >    --> interface\gui\app.py:120:9
    >     |
    > 118 |     telemetry_event = QtCore.Signal(object)
    > 119 |
    > …

- [ ] `x_0_make_all_x` · `black` — black failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-14T05:03:21.8048…
  - Command: `C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-14T05:03:23.775011+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py	2025-10-14 05:02:52.726405+00:00
    > +++ C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py	2025-10-14 05:03:23.377147+00:00
    > @@ -714,11 +714,13 @@
    >                  ctx=ctx,
    >                  repo_parent_root=repo_root,
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py
    > would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\app.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 2 files would be reformatted, 12 files would be left unchanged.

- [ ] `x_0_make_all_x` · `ruff_check` — ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311…
  - Command: `C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-14T05:03:24.677394+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > PLR0915 Too many statements (71 > 50)
    >    --> interface\gui\app.py:120:9
    >     |
    > 118 |     telemetry_event = QtCore.Signal(object)
    > 119 |
    > …

- [ ] `x_0_make_all_x` · `mypy` — mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --d…
  - Command: `C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-14T05:03:27.194859+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > x_cls_make_all_x.py:498: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:501: error: Expression type contains "Any" (has type "Any | str")  [misc]
    > x_cls_make_all_x.py:502: error: Expression type contains "Any" (has type "Any | str")  [misc]
    > x_cls_make_all_x.py:502: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:511: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > …

- [ ] `x_make_common_x` · `black` — black failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-14T05:03:48.53…
  - Command: `C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_common_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-14T05:03:50.246218+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_common_x\telemetry.py	2025-10-14 05:02:40.197810+00:00
    > +++ C:\x_runner_x\x_make_common_x\telemetry.py	2025-10-14 05:03:49.870381+00:00
    > @@ -11,13 +11,15 @@
    >  from typing import TYPE_CHECKING, Final, Protocol, TextIO, TypedDict, cast
    >  
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_make_common_x\telemetry.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 1 file would be reformatted, 8 files would be left unchanged.

---

_Generated by x_make_github_visitor_x_; actionable items are tracked as unchecked tasks._
