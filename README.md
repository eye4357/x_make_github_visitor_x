# x_make_github_visitor_x — Auditor's Field Manual

I built this visitor to walk every clone, interrogate it with Ruff, Black, MyPy, and Pyright, and file the evidence before the orchestrator moves a muscle. Every run produces JSON ledgers the GUI and change board trust. No repo graduates without the stamp from this inspector.

## Mission Log
- Walk every child repository discovered under the designated workspace root.
- Cache prior results so repeat offenders do not waste the lab's time.
- Emit per-tool diagnostics and aggregate summaries the orchestrator ingests without post-processing.
- Capture runtime, environment, and failure detail in a report the Change Control index can audit months later.

## Instrumentation
- Python 3.11 or newer.
- Ruff, Black, MyPy, and Pyright installed in the active environment.
- Optional GitHub token if you expect to touch private clones.

## Operating Procedure
1. `python -m venv .venv`
2. `\.venv\Scripts\Activate.ps1`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`
5. `python -m x_make_github_visitor_x.runner`

The runner discovers immediate child clones, executes the tool suite, and drops a timestamped JSON dossier under `reports/`. The orchestrator and GUI expect those artefacts in that location.

## Evidence Checks
| Check | Command |
| --- | --- |
| Formatting sweep | `python -m black .` |
| Lint interrogation | `python -m ruff check .` |
| Type audit | `python -m mypy .` |
| Static contract scan | `python -m pyright` |
| Functional verification | `pytest` |

## System Linkage
- [Changelog](./CHANGELOG.md)
- [Road to 0.20.4 Engineering Proposal](../x_0_make_all_x/Change%20Control/0.20.4/Road%20to%200.20.4%20Engineering%20Proposal.md)
- [Road to 0.20.3 Engineering Proposal](../x_0_make_all_x/Change%20Control/0.20.3/Road%20to%200.20.3%20Engineering%20Proposal.md)

## Reconstitution Drill
During the monthly rebuild I drop this visitor onto a sterile machine, rerun the sweep, and compare the JSON fingerprints to prior runs. Cache hits must still line up, failure payloads must stay richly annotated, and the orchestrator summary must hydrate from the new dossier without a hiccup. Any drift becomes Change Control fodder and is reconciled before the next inspection cycle.

## Cross-Referenced Assets
- [x_make_github_clones_x](../x_make_github_clones_x/README.md) — produces the clone set this visitor inspects.
- [x_make_common_x](../x_make_common_x/README.md) — supplies logging, subprocess harnesses, and validators.
- [x_0_make_all_x](../x_0_make_all_x/README.md) — orchestrator that consumes the visitor's evidence trail.

## Conduct Code
Every failure becomes a record. If a tool coughs, log it, store the JSON, and elevate through Change Control. No quiet fixes; the lab's memory lives in these dossiers.

## Sole Architect's Note
I designed, built, and hardened this inspector alone. Tool orchestration, cache semantics, schema validation, and downstream integration are mine end to end. I speak the language of automation strategy and low-level Python, so the plan and the implementation never diverge.

## Legacy Staffing Estimate
- Without LLM acceleration, you would mobilize: 1 senior Python lead, 1 DevOps engineer, 1 QA automation specialist, and 1 technical writer.
- Delivery timeline: 12–14 engineer-weeks to build the visitor, validation harness, and documentation to this standard.
- Budget bands: USD 85k–110k for the initial campaign, not counting the institutional knowledge already condensed here.

## Technical Footprint
- Language Core: Python 3.11+, standard library concurrency, and deterministic filesystem sweeps.
- Toolchain: Ruff, Black, MyPy, Pyright, pytest, and PowerShell entry points for Windows operators.
- Reports: JSON dossiers stored under `reports/`, schema validation enforced by `x_make_common_x`.
- Integration Surface: CLI entry point (`python -m x_make_github_visitor_x.runner`) with orchestrator hooks and structured logging routed through `x_make_common_x`.
