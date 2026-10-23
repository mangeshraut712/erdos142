# Reproducing finite checks

Updated 23 October 2026. **Finite checks do not prove the local target.**
The [proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md)
explains why the October 21 closure claims were withdrawn even though their
sample-based scripts passed. DIRECT-Q-GAIN and conditional P12/W8 remain open.

## Environment and isolated execution

Use Python 3.10 or newer. Current Fourier diagnostics require NumPy; the
thirteen original September checkers use the standard library. Install the
optional verification dependency in an isolated environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[verification]"
python verification/check_repository.py
python verification/run_current.py --suite all --output .verification-runs/latest
```

The runner selects 21 current suites/diagnostics and 13 original suites
(34 total). `--suite current` and `--suite legacy` select either group.
These choices do not include every historical experiment. The runner
copies the research tree to a temporary directory, sets module paths,
keeps assertions enabled, and records exit statuses, source hashes,
runtime versions, and logs. It does not overwrite saved report captures.
In-repository log destinations must be under `.verification-runs/`, which
Git ignores. Checkers themselves run offline; dependency installation may
need network access. Do not use `python -O` or `PYTHONOPTIMIZE`.

For only the original standard-library suite:

```bash
python verification/run_current.py --suite legacy
```

Some discovery scripts additionally require SciPy:

```bash
python -m pip install -e ".[exploration]"
```

The declared lower Python version is also used by GitHub Actions. CI runs
the repository checker and both selected finite suites on Python 3.10 and
3.12, then uploads narrowly scoped diagnostic logs. It does not prove any
analytic statement or compile Lean or LaTeX.

## What the results mean

- **Exact checks:** integer/modular enumeration and rational arithmetic
  establish the tested finite identities without rounding error.
- **Floating checks:** Fourier and matrix calculations use explicit
  tolerances. Last-digit differences across runtimes are expected; inspect
  the tolerance and normalization instead of silently replacing evidence.
- **Asymptotic and probabilistic claims:** need complete written arguments.
  Neither seeded examples nor finite phase sweeps establish a uniform
  concentration theorem, a divergent multiplier, or an asymptotic rate.
- **Classical input:** the positive-density reduction invokes qualitative
  four-term Szemerédi. The verifier does not prove that theorem or a rate.
- **Eligibility:** the correction's finite examples fail T5 and prescribed
  radius. They diagnose auxiliary errors, not eligible P12 counterexamples.

The new [correction verifier](verification/scripts/verify_oct21_closure_correction_20261021.py)
checks the reversed variance bound, false correlation bound, and finite
phase-budget overclaims. It also checks the universal Boolean fourth-moment
identity on AP-rich and AP-free sets. The [saved report](verification/results/OCT21_CLOSURE_CORRECTION_VERIFICATION_20261021.json)
separates exact and floating calculations.

Older October 21 script names, counters, and archived reports sometimes use
words such as “theorem” or “divergent.” These are finite observations on the
listed examples, not certified universal conclusions. Their corrected scope
is controlled by the proof audit, not by those historical labels.

## Reports and preservation

Some scripts write next to `__file__`, others relative to the working
directory. Running an individual script directly may overwrite a saved
JSON file; changing only the working directory is not sufficient isolation.
Use the runner, or a separate complete checkout, to preserve captures.

Current source groups are under `docs/audits/`, `verification/scripts/`,
and `verification/results/`. Historical captures and pre-edit copies are
under `history/`; checkpoints live under `checkpoints/`. The
[October 23 checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261023.json)
binds the corrected current files to their hashes. A historical checkpoint
records its own snapshot, not a certification of later edited sources.

The repository checker tests Python syntax, JSON parsing, current local
navigation links, and latest checkpoint hashes. A successful check is not a
mathematical proof. A nonzero exit, missing input, or skipped suite is not a
successful verification.

## Lean and manuscript limitations

The [Lean draft](formalization/lean/README.md) contains an admitted lemma
and four extra axioms. No successful Lean build or complete formalization
is claimed. The [manuscript](docs/manuscript/README.md) is withdrawn and
marked accordingly; no PDF compilation is claimed by this correction.

The [October 23 verifier](verification/scripts/verify_low_mean_moments_20261023.py) adds 26,477 exact rational assertions for the moment cone, low-mean laws, completion fields, diagonal corrections, and variance bounds. Its small arithmetic examples test universal identities, not eligible-host phase selection.
