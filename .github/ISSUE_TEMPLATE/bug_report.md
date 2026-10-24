---
name: Bug Report (Tooling / Runner / Dashboard)
about: Report a bug in verifier scripts, test suite, dashboard generator, or CI.
title: "[Bug]: "
labels: ["tooling", "bug"]
assignees: ["mangeshraut712"]
---

### Environment

- Python version: `python --version` (>= 3.10)
- NumPy version: `python -c "import numpy; print(numpy.__version__)"`
- OS: (macOS / Linux / Windows)

### Steps to Reproduce

1. Command run (e.g. `python verification/run_current.py --suite current`)
2. Observed traceback or output
3. Expected behavior

### Checkpoint and Verifier State

- Checkpoint file checked: `AUTONOMOUS_CHECKPOINT_20261024.json`
- `python verification/check_repository.py` output:
