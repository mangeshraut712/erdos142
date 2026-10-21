# Reproducing the finite checks

The checkers test finite identities, examples, and explicit error estimates.
A successful run does **not** prove the local target
`r_4(N)=o(N/log N)`, the missing phase-selection statement, or official
Erdős problem 142. Start with [CURRENT_STATUS.md](CURRENT_STATUS.md) for
the mathematical status and [PROOF_DEPENDENCIES.md](PROOF_DEPENDENCIES.md)
for dependencies between claims.

## Environment

Use Python **3.10 or newer**. Several later scripts use `int.bit_count()`,
so the original Python 3.9 metadata does not describe the requirements of
the entire research collection.

The original September checkers use the standard library. Several later
checkers in `verification/scripts/` use **NumPy** for Fourier calculations
and numerical linear algebra. **SciPy** is used by the `discover_*.py`
exploration scripts, not by the verification suites listed below.

For a separate environment on macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[verification]"
```

Install SciPy only if running the exploration scripts:

```bash
python -m pip install -e ".[exploration]"
```

The checkers themselves run locally and do not need service credentials
or network access. Installing dependencies may need network access.
For a reproducibility record, capture the interpreter and packages used:

```bash
python --version
python -m pip freeze
```

Do not use `python -O`: these scripts use assertions, which optimization
can disable.

## Recommended isolated runner

```bash
python verification/check_repository.py
python verification/run_current.py --suite all --output .verification-runs/latest
```

`current` runs the fifteen October 17–21 entry points; `legacy` runs the
thirteen original September verifiers; `all` runs both (28 scripts).
These options select the publication suites, not every historical experiment.
The runner copies the complete research tree to a temporary directory,
sets the local module paths, keeps assertions enabled, and records exit
statuses, source hashes, runtime versions, and logs. Original saved reports
are never overwritten. Fresh logs under `.verification-runs/` are ignored
by Git. The repository checker verifies Python syntax, JSON parsing,
current navigation links, and latest checkpoint hashes.
GitHub Actions runs the same checks on Python 3.10 and 3.12; passing CI
certifies only those finite and repository checks.

## Start with the standard-library checks

Run commands **from the repository root**. Verifiers are organized under
`verification/scripts/`.

```bash
python verification/scripts/verify_core.py
python verification/scripts/verify_boolean_occupancy_20261017.py
python verification/scripts/verify_finite_pattern_terminal_20261018.py
python verification/scripts/verify_positive_density_branch_20261019.py
```

These commands respectively check the original finite algebra, Boolean
occupancy identities, the twelve-slot terminal argument, and the
positive-density branch's finite error estimates. They do not need
NumPy. The positive-density verifier does not prove the classical
qualitative Szemerédi theorem invoked in that note.

To rerun the original September suite:

```bash
for script in verification/scripts/verify_*.py; do
    python "$script" || exit 1
done
```

## Choose a suite for the claim being checked

The following are entry points, not a claim that every archived
experiment must be rerun together.

| Topic | Command from the repository root | Extra dependency |
|---|---|---|
| Original finite algebra | `python verification/scripts/verify_core.py` | None |
| Mixed-window degree and terminal estimates | `python verification/scripts/verify_log_density_attack_20261016.py` | NumPy |
| Weighted pair near-positivity | `python verification/scripts/verify_weighted_pair_20261016.py` | NumPy |
| Boolean occupancy and the earlier 2/3 ceiling | `python verification/scripts/verify_boolean_occupancy_20261017.py` | None |
| Selection quantifiers and cubic identities | `python verification/scripts/verify_o2_cubic_quantifiers_20261017.py` | NumPy |
| Finite AP-free diagnostic examples | `python verification/scripts/verify_boolean_o2_diagnostics_20261017.py` | NumPy |
| Twelve-slot / 7/11 terminal ceiling | `python verification/scripts/verify_finite_pattern_terminal_20261018.py` | None |
| Cubic-bound audit | `python verification/scripts/verify_o2_cubic_audit_20261018.py` | NumPy |
| Exact shifted-chirp covariance identity | `python verification/scripts/verify_weighted_quartic_covariance_20261018.py` | NumPy |
| Four weighted completion channels | `python verification/scripts/verify_weighted_completion_20261018.py` | NumPy |
| Elementary sparse alteration construction | `python verification/scripts/verify_boolean_alteration_chirp_20261018.py` | NumPy |
| Typical-event alteration construction | `python verification/scripts/verify_boolean_typical_alteration_20261018.py` | NumPy |
| Covariance obstruction: finite mask, tent, and count checks | `python verification/scripts/verify_o2_covariance_attack_20261019.py` | None |
| Positive-density branch elimination: finite estimates | `python verification/scripts/verify_positive_density_branch_20261019.py` | None |

Read the associated dated Markdown note before interpreting a report.
The mathematical statements have hypotheses that are not automatically
satisfied by every small-prime diagnostic case.

The `discover_*.py` files are exploratory searches. Their output can
suggest examples or lemmas; it is not a substitute for the corresponding
proof and verifier. Some older scripts also import other local research
modules, so retain the complete repository layout.

## Generated reports and isolated runs

Use a separate clone or complete working copy when comparing results
against the saved snapshots. A number of checkers **rewrite tracked
JSON reports**. Some write next to their script via `__file__`; others
write relative to the current working directory. Changing only the
working directory therefore does not reliably isolate a run.

For example:

- `verify_core.py` prints its report to stdout.
- `verify_o2_cubic_quantifiers_20261017.py` prints its report to stdout.
- `verify_finite_pattern_terminal_20261018.py` writes
  `FINITE_PATTERN_TERMINAL_VERIFICATION_20261018.json` next to the script.
- `verify_weighted_completion_20261018.py` writes
  `WEIGHTED_COMPLETION_VERIFICATION_20261018.json` in the working directory.

Copying only one script can fail because some checkers read companion
proofs, saved input reports, or local modules. In particular, the pair
verifier reads `LOG_DENSITY_VERIFICATION_20261016.json`; several reports
also record hashes of their source notes.

After a run, inspect the exit status and the report, then review changes:

```bash
git status --short
git diff --stat
```

A nonzero exit status, assertion failure, missing dependency, or missing
input file is not a successful verification. Do not overwrite a
historical capture merely to hide a numerical difference.

## What the reports establish

**Exact arithmetic.** Checks using integers, modular arithmetic, or
`fractions.Fraction` establish the tested finite equalities or
inequalities without rounding error. Exhaustive searches establish the
stated finite search result, such as the twelve-point occupancy
certificate. They do not by themselves establish a theorem for all
primes or growing parameters.

**Floating arithmetic.** Fourier transforms, square roots, and matrix
calculations may use floating-point tolerances. Reports distinguish
these from exact checks and often give a maximum observed discrepancy.
Different Python, NumPy, or numerical-library versions can change the
last digits of serialized values. Check the asserted tolerance and
mathematical normalization before deciding whether a difference matters.

**Probabilistic constructions.** Seeded samples and finite phase sweeps
test implementation and examples. The asymptotic existence conclusions
depend on the written probability estimates, not on extrapolating those
samples.

**External mathematical input.** The positive-density branch reduction
explicitly uses qualitative four-term Szemerédi. Its checker verifies
the finite parameter estimates; it does not formalize or reprove that
classical theorem.

**Scope of obstructions.** The sparse AP-free constructions lie outside
the logarithmic-density and negligible-diagonal regime. The later
logarithmic-density block construction deliberately contains a 4-AP.
Neither supplies an eligible counterexample to P12. The exact covariance
identity W7 and its equivalence with W8 are proved; the W8 energy upper
bound remains open.

A report's check count measures its own recorded checks. It is not a
confidence percentage, a count of independent proofs, or interchangeable
with the number of Fourier coefficients evaluated.

## Saved evidence

Original captures are under `verification/results/`. Later dated reports
are at the repository root, with preserved rerun summaries and
before-update copies under `history/`. In particular:

- [October 18 rerun summary](history/continuation_20261018/verification/run_summary.json)
- [October 19 finite-envelope rerun summary](history/continuation_20261019/verification/run_summary.json)

These summaries describe specific recorded runs. A source hash binds a
capture to the files checked at that time; a changed hash means the
capture needs review against the changed source. A historical successful
run does not automatically certify a subsequently edited proof or script.
