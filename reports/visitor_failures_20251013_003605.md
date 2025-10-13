# Visitor Failure Report — 2025-10-13T00:36:05.618857+00:00

- Workspace root: `C:\x_runner_x`
- Run started at: 2025-10-13T00:34:29.783788+00:00
- Run completed at: 2025-10-13T00:36:05.618505+00:00
- Total repositories examined: 14
- Total tool executions: 70
- Failing tool executions: 21
- Cache hits: 0

## Failures

- [ ] `x_0_make_all_x` · `ruff_fix` — ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T00:34:34.057949+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `pathlib.Path` into a type-checking block
    >   --> interface\gui\app.py:11:21
    >    |
    >  9 | from collections.abc import Callable, Iterable, Sequence
    > 10 | from dataclasses import dataclass
    > …

- [ ] `x_0_make_all_x` · `black` — black failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-13T…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T00:34:36.525035+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_0_make_all_x\interface\gui\commit.py	2025-10-13 00:34:34.029138+00:00
    > +++ C:\x_runner_x\x_0_make_all_x\interface\gui\commit.py	2025-10-13 00:34:35.031889+00:00
    > @@ -17,12 +17,11 @@
    >      def __call__(
    >          self,
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\commit.py
    > would reformat C:\x_runner_x\x_0_make_all_x\tests\test_gui_commit.py
    > would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\app.py
    > would reformat C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py
    > 
    > …

- [ ] `x_0_make_all_x` · `ruff_check` — ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T00:34:36.636524+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `pathlib.Path` into a type-checking block
    >   --> interface\gui\app.py:11:21
    >    |
    >  9 | from collections.abc import Callable, Iterable, Sequence
    > 10 | from dataclasses import dataclass
    > …

- [ ] `x_0_make_all_x` · `mypy` — mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-un…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: mypy 3.4.3 (compiled: yes)
  - Captured at: 2025-10-13T00:34:41.156334+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > interface\gui\commit.py:92: error: Incompatible types in assignment (expression has type "CompletedProcess[str]", variable has type "CompletedProcess[Literal['']]")  [assignment]
    > interface\gui\app.py:15: error: Unused "type: ignore" comment, use narrower [import-not-found] instead of [import] code  [unused-ignore]
    > interface\gui\app.py:22: error: Explicit "Any" is not allowed  [explicit-any]
    > interface\gui\app.py:22: error: Expression has type "Any"  [misc]
    > interface\gui\app.py:23: error: Explicit "Any" is not allowed  [explicit-any]
    > …

- [ ] `x_0_make_all_x` · `pyright` — pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:34:41.156829+00:00 duration: 0.084…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_0_make_all_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:34:41.240647+00:00
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
  - Captured at: 2025-10-13T00:34:45.188171+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\tui\controller.py	2025-10-12 22:19:43.751272+00:00
    > +++ C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\tui\controller.py	2025-10-13 00:34:44.548999+00:00
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

- [ ] `x_legatus_acta_schedae_x` · `pyright` — pyright failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:34:54.861279+0…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_legatus_acta_schedae_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:34:54.961927+00:00
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

- [ ] `x_make_common_x` · `pyright` — pyright failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:35:02.059829+00:00 duration: 0.0…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_common_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:35:02.140732+00:00
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

- [ ] `x_make_github_visitor_x` · `ruff_fix` — ruff_fix failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --li…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T00:35:10.537699+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `pathlib.Path` into a type-checking block
    >  --> tests\test_github_visitor.py:3:21
    >   |
    > 1 | from __future__ import annotations
    > 2 |
    > …

- [ ] `x_make_github_visitor_x` · `black` — black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff start…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m black . --line-length 88 --target-version py311 --check --diff`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured at: 2025-10-13T00:35:11.966477+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > --- C:\x_runner_x\x_make_github_visitor_x\tests\test_github_visitor.py	2025-10-13 00:35:10.506907+00:00
    > +++ C:\x_runner_x\x_make_github_visitor_x\tests\test_github_visitor.py	2025-10-13 00:35:11.176472+00:00
    > @@ -45,11 +45,13 @@
    >          self._last_run_failures = self._preset_had_failures
    >          self._runtime_snapshot["run_started_at"] = self._preset_run_started
    > …
  - Stderr preview:
    > would reformat C:\x_runner_x\x_make_github_visitor_x\tests\test_github_visitor.py
    > would reformat C:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py
    > 
    > Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    > 2 files would be reformatted, 1 file would be left unchanged.

- [ ] `x_make_github_visitor_x` · `ruff_check` — ruff_check failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-l…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: ruff 0.14.0
  - Captured at: 2025-10-13T00:35:12.072947+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > TC003 Move standard library import `pathlib.Path` into a type-checking block
    >  --> tests\test_github_visitor.py:3:21
    >   |
    > 1 | from __future__ import annotations
    > 2 |
    > …

- [ ] `x_make_github_visitor_x` · `mypy` — mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-re…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: mypy 3.4.3 (compiled: yes)
  - Captured at: 2025-10-13T00:35:16.456616+00:00
  - Suggested action: Investigate
  - Stdout preview:
    > tests\test_github_visitor.py:129: error: Unused "type: ignore" comment  [unused-ignore]
    > Found 1 error in 1 file (checked 3 source files)

- [ ] `x_make_github_visitor_x` · `pyright` — pyright failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:35:16.457285+00:…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_github_visitor_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:35:16.540173+00:00
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

- [ ] `x_make_graphviz_x` · `pyright` — pyright failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:35:24.055978+00:00 duration:…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_graphviz_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:35:24.149030+00:00
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

- [ ] `x_make_markdown_x` · `pyright` — pyright failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:35:31.846326+00:00 duration:…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_markdown_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:35:31.933526+00:00
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

- [ ] `x_make_mermaid_x` · `pyright` — pyright failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:35:38.592489+00:00 duration: 0…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_mermaid_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:35:38.681680+00:00
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

- [ ] `x_make_persistent_env_var_x` · `pyright` — pyright failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:35:42.93…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_persistent_env_var_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:35:43.025848+00:00
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

- [ ] `x_make_pip_updates_x` · `pyright` — pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:35:50.531975+00:00 dur…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pip_updates_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:35:50.601374+00:00
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

- [ ] `x_make_py_mod_sideload_x` · `pyright` — pyright failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:35:53.862458+0…
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_py_mod_sideload_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:35:53.922894+00:00
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

- [ ] `x_make_pypi_x` · `pyright` — pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:35:56.330053+00:00 duration: 0.064s …
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_pypi_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:35:56.394340+00:00
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

- [ ] `x_make_yahw_x` · `pyright` — pyright failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error started_at: 2025-10-13T00:36:05.550918+00:00 duration: 0.067s …
  - Command: `C:\Users\eye43\AppData\Local\Programs\Python\Python313\python.exe -m pyright . --level error`
  - Exit: exit 1
  - Repo path: `C:\x_runner_x\x_make_yahw_x`
  - Tool version: <exit 1> To use the fastapi command, please install "fastapi[standard]":

	pip install "fastapi[standard]"
  - Captured at: 2025-10-13T00:36:05.618106+00:00
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
