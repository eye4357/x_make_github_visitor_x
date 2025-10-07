# Engineering Proposal: Visitor Toolchain Remediation (October 7, 2025)

## 1. Objective
Restore a clean, automated visitor run (ruff → black → mypy → pyright) across the 13 repositories tracked in `x_summary_report_x.json`, eliminating code-quality blockers and preventing regression. The deliverable is a reproducible workflow that other agents can follow to bring every repository to a lint/type-check green state.

## 2. Current State Summary
- Latest visitor run (2025-10-07) produced **42 failures** out of 65 tool invocations.
- Failures concentrate in eight repositories with recurring patterns (e.g., pathlib migrations, broad `Exception` handling, missing namespace packages, boolean positional args, `Any` leakage).
- Tool output artifacts:
  - `x_make_github_visitor_x/x_summary_report_x.json` (aggregate stats)
  - `x_make_github_visitor_x/x_tool_failures_x.json` (full stdout/stderr per tool run)

## 3. Success Criteria
- Visitor execution completes with `had_failures == false` in `x_summary_report_x.json`.
- All repositories satisfy:
  - `python -m ruff check . --fix ...` exits 0
  - `python -m black . --check ...` exits 0
  - `python -m mypy . --strict ...` exits 0 (or approved suppression plan)
  - `python -m pyright . --level error` exits 0 (if configured for the repo)
- CI resilience: add regression guard (e.g., visitor run in scheduled workflow) or document follow-up.

## 4. Workstreams Overview
| Workstream | Scope | Dependencies |
|------------|-------|--------------|
| WS1 | Cross-cutting configuration fixes (ruff settings, namespace packaging) | None; unblock other repos |
| WS2 | Repo-focused remediation for core orchestrators (`x_make_github_visitor_x`, `x_0_make_all_x`) | WS1 |
| WS3 | Satellite tool repos (`x_make_github_clones_x`, `x_make_graphviz_x`, `x_make_mermaid_x`, `x_make_persistent_env_var_x`, `x_make_pip_updates_x`, `x_make_py_mod_sideload_x`, `x_make_pypi_x`, `x_make_yahw_x`) | WS1 |
| WS4 | Large service repo `x_legatus_acta_schedae_x` | WS1 |
| WS5 | Validation & automation (visitor rerun, optional CI wiring) | WS2–WS4 |

## 5. Detailed Execution Plan

### WS1 – Cross-Cutting Fixes
1. **Ruff configuration modernization**
   - Update `pyproject.toml` (or repo-specific config) to move `ignore`/`select` into `[tool.ruff.lint]` section as warned by ruff.
   - Standardize common ignores (e.g., `D, COM812, ISC001, T20`).
2. **Namespace package hygiene**
   - Add `__init__.py` to `tests/` packages (starting with `x_make_github_visitor_x/tests/__init__.py`).
3. **Shared helper utilities**
   - Where repeated pylint/ruff issues surface (e.g., `contextlib.suppress` pattern), draft helper functions or documented patterns to reuse across repos.

### WS2 – Core Orchestrators
#### A. `x_make_github_visitor_x`
- Remove redundant `# type: ignore` comments flagged by mypy.
- Replace `Any`-typed flows with explicit types or generics in dataclasses/helpers.
- Ensure ruff violations (namespace package, etc.) are cleared; run `black` formatting.

#### B. `x_0_make_all_x`
- Migrate `os.path` usage to `pathlib.Path` to satisfy PTH* rules.
- Refactor broad `try/except Exception` blocks to use:
  - `contextlib.suppress`
  - Scoped exception types or logging
- Break up overly complex functions (`validate_publish_manifest`, `_publish_do_publish`, etc.) to reduce `C901`/`PLR091*` flags.
- Replace boolean positional arguments with keyword-only boolean parameters.
- Address magic numbers by introducing module-level constants.

### WS3 – Satellite Tool Repositories
Apply repeated pattern fixes across the smaller repos:
1. **`x_make_github_clones_x`, `x_make_graphviz_x`, `x_make_mermaid_x`, `x_make_persistent_env_var_x`, `x_make_pip_updates_x`, `x_make_py_mod_sideload_x`, `x_make_pypi_x`, `x_make_yahw_x`**
   - Convert `collections.abc` imports to `typing.TYPE_CHECKING` blocks where appropriate (`TC003`).
   - Replace implicit namespace packages or add missing `__init__.py` files if tests/modules require.
   - Tackle `Any` usage by introducing typed structures (e.g., dataclasses, TypedDict).
   - Normalize exception handling (avoid bare `Exception`; use typed exceptions and logging).
   - Update function signatures to avoid boolean positional args; prefer keyword-only or enums.
   - Remove commented-out code flagged by ruff (`ERA001`).
   - Run `black` after structural changes.

### WS4 – `x_legatus_acta_schedae_x`
- Resolve TC003 import ordering by moving heavy imports into `if TYPE_CHECKING` blocks.
- Address mypy `Any` issues in `infrastructure/telemetry.py` by introducing typed data structures.
- Update `infrastructure/automation/webhook_client.py` to import `httpx.Client` correctly (likely `from httpx import Client`), or add stub packages.
- Ensure black formatting across `core/domain/events.py`, `core/services/*.py`, etc.
- Validate pyright by adding proper type annotations or vendoring stub files as needed.

### WS5 – Validation & Automation
1. **Iterative Visitor Runs**
   - After completing each repo’s fixes, run the visitor to confirm failure delta shrinks (capture logs for documentation).
2. **Final Sweep**
   - Once all repos pass locally, remove cached failure artifacts (`x_tool_failures_x.json`) and generate fresh run.
3. **Automation Considerations**
   - Evaluate adding a scheduled job or CI workflow that executes the visitor weekly.
   - Document how to refresh caches and interpret logs for future agents.

## 6. Acceptance & Sign-off Checklist
- [ ] Visitor run returns no failures (`had_failures == false`).
- [ ] All touched repos commit formatting/type changes and pass lint/type checks independently.
- [ ] Engineering notes updated (this proposal + final status update in repo docs).
- [ ] Optional: automation ticket created if CI enhancement is deferred.

## 7. Risk & Mitigation
| Risk | Impact | Mitigation |
|------|--------|------------|
| Large refactors breaking orchestrator flow | High | Write targeted unit/functional tests where possible; run make scripts manually (dry-run) after changes |
| Mypy strictness reveals deeper design issues | Medium | Introduce typed wrappers or gradual `TypeAlias` patterns; escalate to architecture review if invasive |
| Timeboxed effort stalls | Medium | Track progress with the visitor summary after each repo fix to ensure tangible traction |

## 8. Communication & Handoff
- Store progress updates alongside this proposal (e.g., append completion notes or link to PRs).
- When workstream completes, notify stakeholders with final visitor run log and updated `x_summary_report_x.json`.
- For partial hand-offs, list remaining repos and outstanding ruff/mypy items with direct references to `x_tool_failures_x.json` sections.

## 9. Appendix
- **Commands reference** (run from repo root):

```powershell
# Example lint + format pass
python -m ruff check . --fix --line-length 88 --target-version py311
python -m black . --line-length 88 --target-version py311
python -m mypy . --strict --no-warn-unused-configs
python -m pyright . --level error
```

- **Visitor rerun**:

```powershell
python x_cls_make_github_visitor_x.py
```

Ensure virtual environment (`.venv`) is active or prefix commands with `c:\x_runner_x\.venv\Scripts\python.exe` as needed.
