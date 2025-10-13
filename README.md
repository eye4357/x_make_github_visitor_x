# x_make_github_visitor_x — Lab Notes from Walter White

> "I send this visitor ahead of every batch. If a repo can't meet the standard, it doesn't touch my table."

## Manifesto
x_make_github_visitor_x is the compliance auditor for every repository under my watch. It sequences Ruff, Black, MyPy, and Pyright with caching, reports failures as Markdown dossiers, and keeps the Road to 0.20.0 initiative brutally honest.

## Ingredients
- Python 3.11+
- Ruff, Black, MyPy, and Pyright installed in the active environment
- Optional: GitHub tokens when visiting private inventory

## Cook Instructions
1. `python -m venv .venv`
2. `.\.venv\Scripts\Activate.ps1`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`
5. `python x_cls_make_github_visitor_x.py` to run the inspection sweep across your clone set

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
- [Road to 0.20.0 Control Room](../x_0_make_all_x/Change%20Control/0.20.0/index.md)
- [Road to 0.20.0 Engineering Proposal](../x_0_make_all_x/Change%20Control/0.20.0/Road%20to%200.20.0%20Engineering%20Proposal%20-%20Walter%20White.md)

## Cross-Linked Intelligence
- [x_make_github_clones_x](../x_make_github_clones_x/README.md) — supplies the repos this visitor inspects
- [x_make_common_x](../x_make_common_x/README.md) — provides the logging, subprocess, and HTTP clients used in the inspection flow
- [x_0_make_all_x](../x_0_make_all_x/README.md) — the orchestrator that consumes visitor reports to greenlight releases

## Lab Etiquette
Cache or not, every failure becomes a Change Control entry. Don't silence warnings without documentation, and don't forget to stash the Markdown reports—they're the lab's ledger of truth.
