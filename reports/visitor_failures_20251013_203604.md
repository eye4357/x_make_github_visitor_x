# Visitor Failure Report — 2025-10-13T20:36:04.993974+00:00

- Workspace root: `C:\x_runner_x`
- Run started at: 2025-10-13T20:34:38.874743+00:00
- Run completed at: 2025-10-13T20:36:04.993796+00:00
- Total repositories examined: 14
- Total tool executions: 70
- Failing tool executions: 24
- Cache hits: 2

## Failures

- [ ] `x_0_make_all_x` · `mypy` — mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-un…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: mypy 3.4.3 (compiled: yes)
  - Captured at: 2025-10-13T20:34:51.607860+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > C:\x_runner_x\x_make_pip_updates_x\update_flow.py:19: error: Explicit "Any" is not allowed  [explicit-any]
    > C:\x_runner_x\x_make_pip_updates_x\update_flow.py:144: error: Unused "type: ignore" comment  [unused-ignore]
    > C:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:34: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > C:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:35: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > C:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:41: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > …

- [ ] `x_0_make_all_x` · `pyright` — pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T20:34:51.608461+00:00 duration: 1.801…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:34:53.409574+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_0_make_all_x\interface\gui\app.py
    >   c:\x_runner_x\x_0_make_all_x\interface\gui\app.py:34:25 - error: "QtGui" is unknown import symbol (reportAttributeAccessIssue)
    > c:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py
    >   c:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py:417:24 - error: Cannot assign to attribute "force_reclone" for class "object"
    >   Â Â Attribute "force_reclone" is unknown (reportAttributeAccessIssue)
    > …

- [ ] `x_legatus_acta_schedae_x` · `ruff_fix` — ruff_fix failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:34:55.452978+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > W191 Indentation contains tabs
    >   --> x_legatus_acta_schedae_x\__init__.py:8:1
    >    |
    >  7 | for candidate in (_PACKAGE_ROOT, _WORKSPACE_ROOT):
    >  8 |     candidate_str = str(candidate)
    > …

- [ ] `x_legatus_acta_schedae_x` · `black` — black failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff sta…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T20:34:58.109798+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_legatus_acta_schedae_x\tests\test_tui_controller.py	2025-10-13 20:25:45.237216+00:00
    > +++ C:\x_runner_x\x_legatus_acta_schedae_x\tests\test_tui_controller.py	2025-10-13 20:34:56.712636+00:00
    > @@ -28,7 +28,5 @@
    >      assert _find_row(search, created.id)
    >  
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\tests\test_tui_controller.py
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\__init__.py
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\core\services\ai_service.py
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\core\services\automation_service.py
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\api\server.py
    > …

- [ ] `x_legatus_acta_schedae_x` · `ruff_check` — ruff_check failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:34:58.221433+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > W191 Indentation contains tabs
    >   --> x_legatus_acta_schedae_x\__init__.py:8:1
    >    |
    >  7 | for candidate in (_PACKAGE_ROOT, _WORKSPACE_ROOT):
    >  8 |     candidate_str = str(candidate)
    > …

- [ ] `x_legatus_acta_schedae_x` · `pyright` — pyright failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T20:35:08.928449+0…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:35:13.008772+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\api\server.py
    >   c:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\api\server.py:128:6 - error: Argument of type "() -> CoroutineType[Any, Any, dict[str, Any]]" cannot be assigned to parameter "func" of type "_F@__call__" in function "__call__"
    >   Â Â Type "() -> CoroutineType[Any, Any, dict[str, Any]]" is not assignable to type "RouteHandler"
    >   Â Â Â Â Type "() -> CoroutineType[Any, Any, dict[str, Any]]" is not assignable to type "(*args: object, **kwargs: object) -> (object | Awaitable[object])"
    >   Â Â Â Â Â Â Parameter "*args" has no corresponding parameter
    > …

- [ ] `x_make_github_clones_x` · `ruff_fix` — ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:35:17.984723+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >   --> x_cls_make_github_clones_x.py:19:29
    >    |
    > 17 | import time
    > 18 | import urllib.request
    > …

- [ ] `x_make_github_clones_x` · `ruff_check` — ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:35:19.209657+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >   --> x_cls_make_github_clones_x.py:19:29
    >    |
    > 17 | import time
    > 18 | import urllib.request
    > …

- [ ] `x_make_github_clones_x` · `mypy` — mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-retu…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: mypy 3.4.3 (compiled: yes)
  - Captured at: 2025-10-13T20:35:20.090338+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > x_cls_make_github_clones_x.py:608: error: Explicit "Any" is not allowed  [explicit-any]
    > x_cls_make_github_clones_x.py:619: error: "object" has no attribute "force_reclone"  [attr-defined]
    > x_cls_make_github_clones_x.py:663: error: Expression type contains "Any" (has type "Callable[..., object] | None")  [misc]
    > x_cls_make_github_clones_x.py:664: error: Expression type contains "Any" (has type "Callable[..., object] | None")  [misc]
    > x_cls_make_github_clones_x.py:676: error: Expression type contains "Any" (has type "Callable[..., object] | None")  [misc]
    > …

- [ ] `x_make_github_clones_x` · `pyright` — pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T20:35:20.091163+00:00…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_clones_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:35:21.891278+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py
    >   c:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py:619:16 - error: Cannot assign to attribute "force_reclone" for class "object"
    >   Â Â Attribute "force_reclone" is unknown (reportAttributeAccessIssue)
    > 1 error, 0 warnings, 0 informations

- [ ] `x_make_github_visitor_x` · `ruff_fix` — ruff_fix failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --li…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:35:22.486588+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >  --> inspection_flow.py:5:29
    >   |
    > 3 | import importlib
    > 4 | import os
    > …

- [ ] `x_make_github_visitor_x` · `black` — black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff start…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T20:35:24.385703+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_github_visitor_x\inspection_flow.py	2025-10-13 14:49:15.838704+00:00
    > +++ C:\x_runner_x\x_make_github_visitor_x\inspection_flow.py	2025-10-13 20:35:23.338004+00:00
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

- [ ] `x_make_github_visitor_x` · `ruff_check` — ruff_check failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-l…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:35:24.493749+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `collections.abc.Callable` into a type-checking block
    >  --> inspection_flow.py:5:29
    >   |
    > 3 | import importlib
    > 4 | import os
    > …

- [ ] `x_make_github_visitor_x` · `mypy` — mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-re…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: mypy 3.4.3 (compiled: yes)
  - Captured at: 2025-10-13T20:35:25.146166+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > inspection_flow.py:10: error: Cannot find implementation or library stub for module named "x_make_common_x"  [import-not-found]
    > inspection_flow.py:10: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    > inspection_flow.py:34: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > inspection_flow.py:35: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > inspection_flow.py:41: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > …

- [ ] `x_make_github_visitor_x` · `pyright` — pyright failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T20:35:25.146845+00:…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:35:26.906993+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py
    >   c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:10:6 - error: Import "x_make_common_x" could not be resolved (reportMissingImports)
    >   c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:10:29 - error: Type of "log_error" is unknown (reportUnknownVariableType)
    >   c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:10:40 - error: Type of "log_info" is unknown (reportUnknownVariableType)
    > 3 errors, 0 warnings, 0 informations

- [ ] `x_make_pip_updates_x` · `ruff_fix` — ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:35:44.270385+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TRY003 Avoid specifying long messages outside the exception class
    >    --> update_flow.py:115:11
    >     |
    > 113 |     if last_exc is not None:
    > 114 |         raise last_exc
    > …

- [ ] `x_make_pip_updates_x` · `black` — black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at:…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T20:35:45.246060+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-13 18:14:22.470723+00:00
    > +++ C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-13 20:35:45.093358+00:00
    > @@ -110,11 +110,13 @@
    >          except TypeError as exc:
    >              last_exc = exc
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_make_pip_updates_x\update_flow.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 1 file would be reformatted, 4 files would be left unchanged.

- [ ] `x_make_pip_updates_x` · `ruff_check` — ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length …
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:35:45.356206+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TRY003 Avoid specifying long messages outside the exception class
    >    --> update_flow.py:115:11
    >     |
    > 113 |     if last_exc is not None:
    > 114 |         raise last_exc
    > …

- [ ] `x_make_pip_updates_x` · `mypy` — mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-a…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: mypy 3.4.3 (compiled: yes)
  - Captured at: 2025-10-13T20:35:46.208200+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > update_flow.py:19: error: Explicit "Any" is not allowed  [explicit-any]
    > update_flow.py:144: error: Unused "type: ignore" comment  [unused-ignore]
    > Found 2 errors in 1 file (checked 5 source files)

- [ ] `x_make_pypi_x` · `ruff_fix` — ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targe…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:35:52.314238+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC002 Move third-party import `x_0_make_all_x.manifest.ManifestEntry` into a type-checking block
    >   --> publish_flow.py:13:37
    >    |
    > 11 | from typing import Protocol, TypeVar, cast
    > 12 |
    > …

- [ ] `x_make_pypi_x` · `black` — black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T20…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T20:35:53.976727+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-13 17:01:12.302995+00:00
    > +++ C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-13 20:35:53.745948+00:00
    > @@ -478,13 +478,11 @@
    >          "anc": context.ancillary_rel,
    >      }
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_make_pypi_x\publish_flow.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 1 file would be reformatted, 1 file would be left unchanged.

- [ ] `x_make_pypi_x` · `ruff_check` — ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T20:35:54.093662+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC002 Move third-party import `x_0_make_all_x.manifest.ManifestEntry` into a type-checking block
    >   --> publish_flow.py:13:37
    >    |
    > 11 | from typing import Protocol, TypeVar, cast
    > 12 |
    > …

- [ ] `x_make_pypi_x` · `mypy` — mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unre…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: mypy 3.4.3 (compiled: yes)
  - Captured at: 2025-10-13T20:35:54.675916+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > publish_flow.py:13: error: Cannot find implementation or library stub for module named "x_0_make_all_x.manifest"  [import-not-found]
    > publish_flow.py:13: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    > publish_flow.py:14: error: Cannot find implementation or library stub for module named "x_make_common_x"  [import-not-found]
    > publish_flow.py:23: error: Explicit "Any" is not allowed  [explicit-any]
    > publish_flow.py:91: error: Argument 1 to "options_to_kwargs" becomes "Any" due to an unfollowed import  [no-any-unimported]
    > …

- [ ] `x_make_pypi_x` · `pyright` — pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T20:35:54.676587+00:00 duration: 1.746s …
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: pyright 1.1.406
  - Captured at: 2025-10-13T20:35:56.422933+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > c:\x_runner_x\x_make_pypi_x\publish_flow.py
    >   c:\x_runner_x\x_make_pypi_x\publish_flow.py:13:6 - error: Import "x_0_make_all_x.manifest" could not be resolved (reportMissingImports)
    >   c:\x_runner_x\x_make_pypi_x\publish_flow.py:14:6 - error: Import "x_make_common_x" could not be resolved (reportMissingImports)
    > 2 errors, 0 warnings, 0 informations

---

_Generated by x_make_github_visitor_x_; actionable items are tracked as unchecked tasks._
