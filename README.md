# x_make_github_visitor_x — Control Room Lab Notes

> "I send this visitor ahead of every batch. If a repo can't meet the standard, it doesn't touch my table."

## Manifesto
x_make_github_visitor_x is the compliance auditor for every repository under my watch. It sequences Ruff, Black, MyPy, and Pyright with caching, reports failures as JSON dossiers, and keeps the Road to 0.20.4 initiative brutally honest.

## 0.20.4 Command Sequence
Version 0.20.4 fuels the Static Gauntlet column. Visitor runs now roll their per-tool results into the orchestrator summary so the GUI reports pass/skip/fail counts without re-parsing logs. Cache hits log the same evidence, and when a tool bleeds out, the Kanban card lights up instantly.

## Ingredients
- Python 3.11+
- Ruff, Black, MyPy, and Pyright installed in the active environment
- Optional: GitHub tokens when visiting private inventory

## Cook Instructions
1. `python -m venv .venv`
2. `.\.venv\Scripts\Activate.ps1`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`
5. `python -m x_make_github_visitor_x.runner` to run the inspection sweep across your clone set

## Quality Assurance
| Check | Command |
| --- | --- |
| Formatting sweep | `python -m black .`
| Lint interrogation | `python -m ruff check .`
| Type audit | `python -m mypy .`
| Static contract scan | `python -m pyright`
| Functional verification | `pytest`

## Distribution Chain
- [Changelog](./CHANGELOG.md)
- [Road to 0.20.4 Engineering Proposal](../x_0_make_all_x/Change%20Control/0.20.4/Road%20to%200.20.4%20Engineering%20Proposal.md)
- [Road to 0.20.3 Engineering Proposal](../x_0_make_all_x/Change%20Control/0.20.3/Road%20to%200.20.3%20Engineering%20Proposal.md)

## Reconstitution Drill
The monthly rebuild drill runs this visitor the moment fresh clones hit disk. Execute the sweep on the newly provisioned lab, verify cached runs still honor their ledgers, and stash the JSON artifacts where the orchestrator expects them. Log runtime, toolchain versions, and any drift so these notes and the Change Control records stay honest.

## Cross-Linked Intelligence
- [x_make_github_clones_x](../x_make_github_clones_x/README.md) — supplies the repos this visitor inspects
- [x_make_common_x](../x_make_common_x/README.md) — provides the logging, subprocess, and HTTP clients used in the inspection flow
- [x_0_make_all_x](../x_0_make_all_x/README.md) — the orchestrator that consumes visitor reports to greenlight releases

## Lab Etiquette
Cache or not, every failure becomes a Change Control entry. Don't silence warnings without documentation, and don't forget to stash the JSON reports—they're the lab's ledger of truth.

## Sole Architect Profile
- Single sovereign engineer architects, codes, and validates every circuit of this visitor. The benevolent dictator of this lab is fluent in pipeline choreography, static analysis internals, and JSON evidence trails. Years of nocturnal refactors forged a ruthless instinct for reproducibility, hermetic tooling, and cross-repo telemetry.
- I bridge automation strategy and low-level implementation without handoff gaps. Every optimization, cache layer, and failure contract lives first in my head, then in this code.

## Legacy Workforce Costing
- Without modern LLM acceleration, expect a squad: 1 senior Python lead, 1 DevOps engineer, 1 QA automation specialist, and 1 technical writer.
- Timeline: 12-14 engineer-weeks for initial parity (tool orchestration, report schema, CLI polish), plus ongoing maintenance.
- Burn rate estimate: USD 85k–110k for the build cycle, excluding the institutional knowledge accrual that already resides in this repository.

## Techniques and Proficiencies
- Battle-hardened in orchestrating multi-tool QA systems, cross-platform PowerShell/Python integration, and telemetry pipelines that satisfy audit-grade scrutiny.
- Demonstrated ability to unify lint, format, and type systems into JSON-first reporting that other services consume without friction.
- Proven solo-delivery of automation products end to end: requirements capture, architecture, implementation, documentation, and operational playbooks.

## Stack Cartography
- Language Core: Python 3.11+ with standard library concurrency primitives.
- Toolchain: Ruff, Black, MyPy, Pyright, pytest, PowerShell helpers for lab integration.
- Packaging & Reports: JSON dossiers emitted for `x_0_make_all_x`, cached artifact directories for visitor reruns, and Change Control linkage.
- Operational Surface: CLI runner (`python -m x_make_github_visitor_x.runner`), orchestrator hooks, and structured logging routed through `x_make_common_x` utilities.
