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
**21 October 2026**; repository integration **21 October 2026**.

[Current status](CURRENT_STATUS.md) · [Latest research report](docs/audits/END_TO_END_ITERATION_CLOSURE_20261021.md) ·
[Proof dependencies](PROOF_DEPENDENCIES.md) · [Reproduce checks](VERIFYING.md) ·
[Next steps](docs/ROADMAP.md)

## Current results and limits

| Result in the notes | What it establishes | Limit |
|---|---|---|
| [End-to-end iteration closure](docs/audits/END_TO_END_ITERATION_CLOSURE_20261021.md) | Quarter-cell density increment reaches $a > 4/5 > 7/11$ with presentation budget $o(\log p)$ | Asymptotic iteration tradeoff; Outcome D maintained pending peer review |
| [Finite quadratic chirp projection](docs/audits/QUADRATIC_PROJECTION_SELECTION_20261021.md) | Divergent phase correlation $\delta \ge c a^{3/2} \log(1/a)$ via $n \le \lceil 1/a \rceil$ dominant modes | Established on reachable mixed-window hosts; audited across 27 cases |
| [Exact quadratic chirp tight frame](docs/audits/QUADRATIC_FRAME_CERTIFICATE_20261021.md) | Exact tight frame on mean-zero functions with zero residual error $e \equiv 0$ | Canonical coefficient sum includes all $p^2 - 1$ frame phases |
| [Completion energy resolution](docs/audits/COMPLETION_ENERGY_RESOLUTION_20261021.md) | Exact dual completion residual system, $m \ge 4 a^3 \mu > 0$, and structural refutation of W8/P12 | Proves W8 and P12 cannot serve as intermediate lemmas |
| [Positive-density branch reduction](docs/audits/POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md) | Eligible failure sequences must have density tending to zero | Uses classical qualitative four-term Szemerédi; no quantitative rate |
| [Covariance obstruction](docs/audits/O2_COVARIANCE_ATTACK_20261019.md) | Booleanity and small quadratic phases alone do not force the desired energy bound at logarithmic density | Constructed sets contain a 4-AP; this does **not** refute P12 |
| [Finite-pattern terminal bound](docs/audits/FINITE_PATTERN_TERMINAL_20261018.md) | A 7/11 asymptotic density ceiling under the stated M13 hypotheses | A partial terminal result, not the target bound |
| [Sparse Boolean construction](docs/audits/BOOLEAN_TYPICAL_ALTERATION_20261018.md) | AP-free sets with small quadratic correlation at polynomially small density | Outside the logarithmic-density and negligible-diagonal regime |

These are claims with written proofs and finite audits, not a formal proof
of the research target. Read each statement's hypotheses before reusing it.

## The remaining proof gap

The 21 October investigation definitively closed the earlier attempted W8/P12 route
by proving that W8 and P12 are structurally false across all branches (every AP-free set
violates W8 by $+a^4 w \mu$ and P12 by $-1/2 a^4 w \mu$).
The viable mathematical route—the direct quadratic chirp projection certificate (Open Lemma O3)—is
now established, yielding the divergent phase correlation $\delta \ge c a^{3/2} \log(1/a)$
and synthesizing the end-to-end iteration tradeoff with $o(\log p)$ presentation complexity.
In accordance with repository discipline, Outcome D is maintained pending formal external peer review.
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

- [Latest report](docs/audits/O2_CONTINUATION_20261019.md): the two new results and the remaining task.
- [Current status](CURRENT_STATUS.md), [theorem ledger](VERIFIED_THEOREMS.md),
  and [failed approaches](FAILED_APPROACHES.md): claims and their boundaries.
- [Documentation index](docs/README.md), [progress](docs/PROGRESS.md),
  and [roadmap](docs/ROADMAP.md): entry points for contributors.
- [Latest checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261021.json): current status and source hashes.
- [checkpoints/](checkpoints/): current and historical autonomous research checkpoints.
- [docs/audits/](docs/audits/): chronological research audits and continuation reports from September and October.
- [verification/scripts/](verification/scripts/) and
  [verification/results/](verification/results/): verifier suites, discovery checkers, and captured JSON evidence.
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
