# Visitor Failure Report — 2025-10-13T20:42:13.926052+00:00

- Workspace root: `C:\x_runner_x`
- Run started at: 2025-10-13T20:40:08.141228+00:00
- Run completed at: 2025-10-13T20:42:13.925761+00:00
- Total repositories examined: 14
- Total tool executions: 70
- Failing tool executions: 24
- Cache hits: 17

## Failures

- [ ] `x_0_make_all_x` · `mypy` — mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-un…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T20:40:20.249943+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > x_cls_make_all_x.py:373: error: Explicit "Any" is not allowed  [explicit-any]
    > x_cls_make_all_x.py:374: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:375: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:381: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:382: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > …

- [ ] `x_0_make_all_x` · `pyright` — pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T20:40:20.250318+00:00 duration: 1.868s tool_version: pyright 1.1…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:40:22.118766+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_0_make_all_x\interface\gui\app.py
    >   c:\x_runner_x\x_0_make_all_x\interface\gui\app.py:34:25 - error: "QtGui" is unknown import symbol (reportAttributeAccessIssue)
    > c:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py
    >   c:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py:417:24 - error: Cannot assign to attribute "force_reclone" for class "object"
    >   Â Â Attribute "force_reclone" is unknown (reportAttributeAccessIssue)
    > …

- [ ] `x_legatus_acta_schedae_x` · `ruff_fix` — ruff_fix failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ver…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:40:24.361005+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > W191 Indentation contains tabs
    >   --> x_legatus_acta_schedae_x\__init__.py:8:1
    >    |
    >  7 | for candidate in (_PACKAGE_ROOT, _WORKSPACE_ROOT):
    >  8 |     candidate_str = str(candidate)
    > …

- [ ] `x_legatus_acta_schedae_x` · `black` — black failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T20:40:2…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T20:40:26.892209+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\__init__.py	2025-10-13 20:34:55.423002+00:00
    > +++ C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\__init__.py	2025-10-13 20:40:25.693651+00:00
    > @@ -3,12 +3,12 @@
    >  
    >  _PACKAGE_ROOT = Path(__file__).resolve().parents[1]
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\__init__.py
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\tests\test_tui_controller.py
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\core\services\ai_service.py
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\core\services\automation_service.py
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\api\server.py
    > …

- [ ] `x_legatus_acta_schedae_x` · `ruff_check` — ruff_check failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:40:27.203314+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > W191 Indentation contains tabs
    >   --> x_legatus_acta_schedae_x\__init__.py:8:1
    >    |
    >  7 | for candidate in (_PACKAGE_ROOT, _WORKSPACE_ROOT):
    >  8 |     candidate_str = str(candidate)
    > …

- [ ] `x_legatus_acta_schedae_x` · `pyright` — pyright failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T20:40:42.125552+00:00 duration: 3.322s tool_…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:40:45.447763+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\api\server.py
    >   c:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\api\server.py:128:6 - error: Argument of type "() -> CoroutineType[Any, Any, dict[str, Any]]" cannot be assigned to parameter "func" of type "_F@__call__" in function "__call__"
    >   Â Â Type "() -> CoroutineType[Any, Any, dict[str, Any]]" is not assignable to type "RouteHandler"
    >   Â Â Â Â Type "() -> CoroutineType[Any, Any, dict[str, Any]]" is not assignable to type "(*args: object, **kwargs: object) -> (object | Awaitable[object])"
    >   Â Â Â Â Â Â Parameter "*args" has no corresponding parameter
    > …

- [ ] `x_make_github_clones_x` · `ruff_fix` — ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:40:46.860022+00:00
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
  - Captured at: 2025-10-13T20:40:48.997074+00:00
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
  - Captured at: 2025-10-13T20:40:54.752417+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > x_cls_make_github_clones_x.py:608: error: Explicit "Any" is not allowed  [explicit-any]
    > x_cls_make_github_clones_x.py:619: error: "object" has no attribute "force_reclone"  [attr-defined]
    > x_cls_make_github_clones_x.py:663: error: Expression type contains "Any" (has type "Callable[..., object] | None")  [misc]
    > x_cls_make_github_clones_x.py:664: error: Expression type contains "Any" (has type "Callable[..., object] | None")  [misc]
    > x_cls_make_github_clones_x.py:676: error: Expression type contains "Any" (has type "Callable[..., object] | None")  [misc]
    > …

- [ ] `x_make_github_clones_x` · `pyright` — pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T20:40:54.752849+00:00 duration: 1.731s tool_vers…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:40:56.483435+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py
    >   c:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py:619:16 - error: Cannot assign to attribute "force_reclone" for class "object"
    >   Â Â Attribute "force_reclone" is unknown (reportAttributeAccessIssue)
    > 1 error, 0 warnings, 0 informations

- [ ] `x_make_github_visitor_x` · `ruff_fix` — ruff_fix failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:40:57.181483+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >  --> inspection_flow.py:5:29
    >   |
    > 3 | import importlib
    > 4 | import os
    > …

- [ ] `x_make_github_visitor_x` · `black` — black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T20:40:57.…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T20:40:59.503566+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_github_visitor_x\inspection_flow.py	2025-10-13 14:49:15.838704+00:00
    > +++ C:\x_runner_x\x_make_github_visitor_x\inspection_flow.py	2025-10-13 20:40:58.284764+00:00
    > @@ -13,11 +13,13 @@
    >  class VisitorProtocol(Protocol):
    >      def run_inspect_flow(self) -> None: ...
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_make_github_visitor_x\inspection_flow.py
    > would reformat C:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 2 files would be reformatted, 3 files would be left unchanged.

- [ ] `x_make_github_visitor_x` · `ruff_check` — ruff_check failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:40:59.789479+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >  --> inspection_flow.py:5:29
    >   |
    > 3 | import importlib
    > 4 | import os
    > …

- [ ] `x_make_github_visitor_x` · `mypy` — mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured at: 2025-10-13T20:41:05.077590+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > inspection_flow.py:10: error: Skipping analyzing "x_make_common_x": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    > inspection_flow.py:10: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    > inspection_flow.py:34: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > inspection_flow.py:35: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > inspection_flow.py:41: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > …

- [ ] `x_make_github_visitor_x` · `pyright` — pyright failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T20:41:05.078090+00:00 duration: 1.872s tool_ve…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:41:06.950301+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py
    >   c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:10:6 - error: Import "x_make_common_x" could not be resolved (reportMissingImports)
    >   c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:10:29 - error: Type of "log_error" is unknown (reportUnknownVariableType)
    >   c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:10:40 - error: Type of "log_info" is unknown (reportUnknownVariableType)
    > 3 errors, 0 warnings, 0 informations

- [ ] `x_make_pip_updates_x` · `ruff_fix` — ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:41:41.753607+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TRY003 Avoid specifying long messages outside the exception class
    >    --> update_flow.py:115:11
    >     |
    > 113 |     if last_exc is not None:
    > 114 |         raise last_exc
    > …

- [ ] `x_make_pip_updates_x` · `black` — black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T20:41:41.754036…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T20:41:43.588178+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-13 18:14:22.470723+00:00
    > +++ C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-13 20:41:43.322859+00:00
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
  - Captured at: 2025-10-13T20:41:43.896177+00:00
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
  - Captured at: 2025-10-13T20:41:48.932220+00:00
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
  - Captured at: 2025-10-13T20:41:52.017781+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC002 Move third-party import `x_0_make_all_x.manifest.ManifestEntry` into a type-checking block
    >   --> publish_flow.py:13:37
    >    |
    > 11 | from typing import Protocol, TypeVar, cast
    > 12 |
    > …

- [ ] `x_make_pypi_x` · `black` — black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T20:41:52.018324+00:00 duratio…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T20:41:53.602404+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-13 17:01:12.302995+00:00
    > +++ C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-13 20:41:53.321988+00:00
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
  - Captured at: 2025-10-13T20:41:53.891527+00:00
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
  - Captured at: 2025-10-13T20:41:56.902798+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > publish_flow.py:13: error: Skipping analyzing "x_0_make_all_x.manifest": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    > publish_flow.py:13: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    > publish_flow.py:14: error: Skipping analyzing "x_make_common_x": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    > publish_flow.py:23: error: Explicit "Any" is not allowed  [explicit-any]
    > publish_flow.py:91: error: Argument 1 to "options_to_kwargs" becomes "Any" due to an unfollowed import  [no-any-unimported]
    > …

- [ ] `x_make_pypi_x` · `pyright` — pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-13T20:41:56.903482+00:00 duration: 2.261s tool_version: pyright 1.1.4…
  - Command: `C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:41:59.164255+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_pypi_x\publish_flow.py
    >   c:\x_runner_x\x_make_pypi_x\publish_flow.py:13:6 - error: Import "x_0_make_all_x.manifest" could not be resolved (reportMissingImports)
    >   c:\x_runner_x\x_make_pypi_x\publish_flow.py:14:6 - error: Import "x_make_common_x" could not be resolved (reportMissingImports)
    > 2 errors, 0 warnings, 0 informations

---

_Generated by x_make_github_visitor_x_; actionable items are tracked as unchecked tasks._
