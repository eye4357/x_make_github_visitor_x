# x_make_github_visitor_x

Enhanced GitHub visitor that enforces unified code quality standards across cloned repositories.

## Features

- Sequential toolchain: Ruff (fix) → Black (check) → Ruff (check) → MyPy (strict) → Pyright (strict)
- Tight formatting and linting configuration enforced via `pyproject.toml`
- Repository-level caching to skip re-running tools when files are unchanged
- Generates a-priori, a-posteriori, and summary reports for downstream processing
- Fails fast when any tool reports violations to keep CI pipelines honest

## Usage

```python
from pathlib import Path
from x_cls_make_github_visitor_x import init_name

visitor = init_name(Path.cwd(), enable_cache=True)
visitor.run_inspect_flow()
```

Outputs are written alongside the module:

- `x_index_a_a_priori_x.json`
- `x_index_b_a_posteriori_x.json`
- `x_summary_report_x.json`
- `.tool_cache/` (per-repo cached tool outputs)

Pass `enable_cache=False` when a clean run is required.
