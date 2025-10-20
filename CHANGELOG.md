# x_make_github_visitor_x — Production Ledger

I record every material change to this visitor here. The format mirrors [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and Semantic Versioning so future audits can trace cause and effect without inference.

## [0.20.4] - 2025-10-15
### Changed
- README updated for the Road to 0.20.4 campaign, detailing how visitor reports feed the Static Gauntlet Kanban column and orchestrator summary.
- Documented the aggregation flow that rolls per-tool results into pass/skip/fail counts without re-running inspections.

## [0.20.3] - 2025-10-14
### Added
- Per-file diagnostics appended to audit events and JSON reports so every failure pinpoints the file and message without guesswork.

### Changed
- README and roadmap references aligned to the 0.20.3 control brief, documenting the JSON-first visitor protocol.

## [0.20.2] - 2025-10-14
### Changed
- Rewired documentation to document the 0.20.2 inspection overhaul, detailing the stricter serialization and reporting guardrails now enforced by the visitor.

## [0.20.1] - 2025-10-13
### Changed
- Introduced `inspection_flow.run_inspection` so the orchestrator delegates visitor orchestration through a single helper.
- Updated documentation to point straight at the Road to 0.20.1 control-room ledger—the inspection brief lives there now.

## [0.20.0-prep] - 2025-10-12
### Added
- Rewrote documentation in the control-room voice to standardize the visitor protocol across the lab.
- Connected the inspector to the Road to 0.20.0 control room for instantaneous breach reporting.

### Changed
- Clarified the expectation that every failure becomes Change Control evidence—no exceptions, no half measures.
