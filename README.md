<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Erdős 142 research notebook

**Status: OPEN.** Research notes, proofs of auxiliary statements, finite
verifiers, and a record of failed approaches toward the local target

$$r_4(N)=o(N/\log N).$$

This repository does not prove that target or solve official Erdős #142.
The [official problem](docs/literature/OFFICIAL_142.md) asks for asymptotic
formulae for the progression-free extremal functions; the local target
is a related, weaker question.

By [Mangesh Raut](https://github.com/mangeshraut712). Research through
**19 October 2026**; repository integration **21 October 2026**.

[Current status](CURRENT_STATUS.md) · [Latest research report](O2_CONTINUATION_20261019.md) ·
[Proof dependencies](PROOF_DEPENDENCIES.md) · [Reproduce checks](VERIFYING.md) ·
[Next steps](docs/ROADMAP.md)

## Current results and limits

| Result in the notes | What it establishes | Limit |
|---|---|---|
| [Positive-density branch reduction](POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md) | Eligible failure sequences must have density tending to zero | Uses classical qualitative four-term Szemerédi; no quantitative rate |
| [Covariance obstruction](O2_COVARIANCE_ATTACK_20261019.md) | Booleanity and small quadratic phases alone do not force the desired energy bound at logarithmic density | Constructed sets contain a 4-AP; this does **not** refute P12 |
| [Exact quartic identity](WEIGHTED_QUARTIC_COVARIANCE_20261018.md) | Rewrites P12 as the precise energy inequality W8 | The required upper bound remains open |
| [Finite-pattern terminal bound](FINITE_PATTERN_TERMINAL_20261018.md) | A 7/11 asymptotic density ceiling under the stated M13 hypotheses | A partial terminal result, not the target bound |
| [Weighted completion certificate](WEIGHTED_COMPLETION_CERTIFICATE_20261018.md) | A sufficient phase-selection certificate when its conditions hold | Certificate existence and the low-mean branch remain open |
| [Sparse Boolean construction](BOOLEAN_TYPICAL_ALTERATION_20261018.md) | AP-free sets with small quadratic correlation at polynomially small density | Outside the logarithmic-density and negligible-diagonal regime |

These are claims with written proofs and finite audits, not a formal proof
of the research target. Read each statement's hypotheses before reusing it.

## The remaining proof gap

For eligible Boolean AP-free sets, under failed adequate phase selection,
the direct attack needs

$$\mathcal E_F(u)\le 2U^2+2R_3+a^4w\mu,\qquad U=wa(1-a).$$

The exact identity $R_4=U^2-\mathcal E_F(u)/2$ makes this **W8**, equivalent
to **P12**. Both remain open, as does **DIRECT-Q-GAIN**. The next attempt
must use the pointwise AP-free completion identities, or comparably strong
arithmetic information; a reduced weighted count alone is insufficient.
Definitions and full quantifiers: [open lemmas](OPEN_LEMMAS.md).

## Reproduce the checks

Use **Python 3.10+**. The recent Fourier checkers require **NumPy**;
the thirteen original September checkers use the standard library.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[verification]"
python verification/check_repository.py
python verification/run_current.py --suite all --output .verification-runs/latest
```

The runner executes in a temporary copy so saved JSON evidence is preserved.
`current` selects the eleven October 17–19 suites, `legacy` selects the
thirteen original suites, and `all` runs both. Earlier dated experiments
remain available separately. A passing run checks finite identities and
examples; it does not prove an asymptotic theorem. See [VERIFYING.md](VERIFYING.md)
for exact versus floating checks, optional SciPy searches, and limitations.

## Reading and repository map

- [Latest report](O2_CONTINUATION_20261019.md): the two new results and the remaining task.
- [Current status](CURRENT_STATUS.md), [theorem ledger](VERIFIED_THEOREMS.md),
  and [failed approaches](FAILED_APPROACHES.md): claims and their boundaries.
- [Documentation index](docs/README.md), [progress](docs/PROGRESS.md),
  and [roadmap](docs/ROADMAP.md): entry points for contributors.
- [Latest checkpoint](AUTONOMOUS_CHECKPOINT_20261021.json): current status and source hashes.
- Root dated Markdown, Python, and JSON files: October continuations.
- [docs/audits/](docs/audits/): original September notes;
  [verification/scripts/](verification/scripts/) and
  [verification/results/](verification/results/): their checkers and captures.
- [history/](history/): previous checkpoints, navigation snapshots, and rerun evidence.

The [September status card](docs/status.html) and its
[screenshots](docs/screenshots/) are retained as historical artifacts.
Their frontier and standard-library-only description predate the October work.

## Contributing, attribution, and citation

Contributions should state exact hypotheses, preserve failed attempts, and
include a relevant verifier or explain why a claim is purely analytic.
Follow [CONTRIBUTING.md](CONTRIBUTING.md), including signed-off commits.

Cite: Mangesh Raut, *Erdős problem 142 research pack*, 2026,
[GitHub repository](https://github.com/mangeshraut712/erdos142).
Machine-readable metadata: [CITATION.cff](CITATION.cff).

Copyright 2026 Mangesh Raut. [Apache-2.0](LICENSE), with [NOTICE](NOTICE)
and [attribution guidance](docs/PRIORITY_AND_ATTRIBUTION.md).
[Support the author](https://github.com/sponsors/mangeshraut712).
