# Visitor Failure Report — 2025-10-14T04:16:30.867422+00:00

- Workspace root: `C:\x_runner_x`
- Run started at: 2025-10-14T04:14:45.733482+00:00
- Run completed at: 2025-10-14T04:16:30.866802+00:00
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
  - Captured at: 2025-10-14T04:14:58.506028+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > PLR0915 Too many statements (63 > 50)
    >    --> interface\gui\app.py:119:9
    >     |
    > 117 |     telemetry_event = QtCore.Signal(object)
    > 118 |
    > …

- [ ] `x_0_make_all_x` · `black` — black failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-14T04:14:59.8320…
  - Command: `C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-14T04:15:01.935049+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py	2025-10-14 04:14:58.430660+00:00
    > +++ C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py	2025-10-14 04:15:01.490432+00:00
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
  - Captured at: 2025-10-14T04:15:03.050470+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > PLR0915 Too many statements (63 > 50)
    >    --> interface\gui\app.py:119:9
    >     |
    > 117 |     telemetry_event = QtCore.Signal(object)
    > 118 |
    > …

- [ ] `x_0_make_all_x` · `mypy` — mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --d…
  - Command: `C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-14T04:15:05.871937+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > x_cls_make_all_x.py:498: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:501: error: Expression type contains "Any" (has type "Any | str")  [misc]
    > x_cls_make_all_x.py:502: error: Expression type contains "Any" (has type "Any | str")  [misc]
    > x_cls_make_all_x.py:502: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:511: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > …

- [ ] `x_make_common_x` · `black` — black failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-14T04:15:25.18…
  - Command: `C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_common_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-14T04:15:26.817220+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_common_x\telemetry.py	2025-10-14 04:14:24.153537+00:00
    > +++ C:\x_runner_x\x_make_common_x\telemetry.py	2025-10-14 04:15:26.486106+00:00
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
