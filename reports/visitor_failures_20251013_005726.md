# Visitor Failure Report — 2025-10-13T00:57:26.208697+00:00

- Workspace root: `C:\x_runner_x`
- Run started at: 2025-10-13T00:56:46.824960+00:00
- Run completed at: 2025-10-13T00:57:26.208495+00:00
- Total repositories examined: 14
- Total tool executions: 70
- Failing tool executions: 16
- Cache hits: 14

## Failures

- [ ] `x_0_make_all_x` · `ruff_fix` — ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T00:56:50.623082+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TRY003 Avoid specifying long messages outside the exception class
    >   --> interface\gui\app.py:19:11
    >    |
    > 17 |       from PySide6 import QtWidgets as _QtWidgetsRaw
    > 18 |   except ModuleNotFoundError as exc:  # pragma: no cover - import guard
    > …

- [ ] `x_0_make_all_x` · `ruff_check` — ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T00:56:52.550522+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TRY003 Avoid specifying long messages outside the exception class
    >   --> interface\gui\app.py:19:11
    >    |
    > 17 |       from PySide6 import QtWidgets as _QtWidgetsRaw
    > 18 |   except ModuleNotFoundError as exc:  # pragma: no cover - import guard
    > …

- [ ] `x_0_make_all_x` · `mypy` — mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-un…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: mypy 3.4.3 (compiled: yes)
  - Captured at: 2025-10-13T00:56:57.467811+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > x_cls_make_all_x.py:592: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:593: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > x_cls_make_all_x.py:1611: error: Expression type contains "Any" (has type "Any | None")  [misc]
    > Found 3 errors in 1 file (checked 14 source files)

- [ ] `x_0_make_all_x` · `pyright` — pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:56:57.468278+00:00 duration: 0.072…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:56:57.540009+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_legatus_acta_schedae_x` · `black` — black failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff sta…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T00:57:01.799822+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\tui\controller.py	2025-10-12 22:19:43.751272+00:00
    > +++ C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\tui\controller.py	2025-10-13 00:57:01.237147+00:00
    > @@ -165,6 +165,5 @@
    >          for task in self._ctx.task_service.list_tasks():
    >              if task.id == task_id:
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\tui\controller.py
    > would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\cli\main.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 2 files would be reformatted, 93 files would be left unchanged.

- [ ] `x_legatus_acta_schedae_x` · `pyright` — pyright failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:02.480595+0…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:02.553378+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_common_x` · `pyright` — pyright failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:04.735916+00:00 duration: 0.0…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_common_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:04.803405+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_github_visitor_x` · `pyright` — pyright failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:10.011886+00:…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:10.093373+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_graphviz_x` · `pyright` — pyright failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:12.622424+00:00 duration:…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_graphviz_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:12.697027+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_markdown_x` · `pyright` — pyright failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:14.937740+00:00 duration:…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_markdown_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:15.016104+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_mermaid_x` · `pyright` — pyright failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:17.478828+00:00 duration: 0…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_mermaid_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:17.550367+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_persistent_env_var_x` · `pyright` — pyright failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:18.30…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_persistent_env_var_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:18.374259+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_pip_updates_x` · `pyright` — pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:20.357919+00:00 dur…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:20.426300+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_py_mod_sideload_x` · `pyright` — pyright failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:21.272177+0…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_py_mod_sideload_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:21.340497+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_pypi_x` · `pyright` — pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:21.468832+00:00 duration: 0.086s …
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:21.554781+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

- [ ] `x_make_yahw_x` · `pyright` — pyright failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:57:26.146534+00:00 duration: 0.061s …
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_yahw_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:57:26.207882+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > To use the fastapi command, please install "fastapi[standard]":
    > 
    > 	pip install "fastapi[standard]"
  - Stderr preview:
    > Traceback (most recent call last):
    >   File "<frozen runpy>", line 198, in _run_module_as_main
    >   File "<frozen runpy>", line 88, in _run_code
    >   File "C:\Users\eye43\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyright\__main__.py", line 3, in <module>
    >     main()
    > …

---

_Generated by x_make_github_visitor_x_; actionable items are tracked as unchecked tasks._
