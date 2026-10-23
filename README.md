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
**24 October 2026**, including correction of the October 21 proof claims.

[Current status](CURRENT_STATUS.md) · [Proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md) ·
[LaTeX manuscript](docs/manuscript/README.md) · [Peer review guide](docs/PEER_REVIEW_GUIDE.md) ·
[Proof dependencies](PROOF_DEPENDENCIES.md) · [Reproduce checks](VERIFYING.md) ·
[Next steps](docs/ROADMAP.md)

## Corrected research status — 24 October 2026

The October 21 closure and explicit-rate claims are **withdrawn**. The proof
reversed a variance inequality, dropped an uncontrolled cubic term, and
assumed spectral concentration without proving it. The target, DIRECT-Q-GAIN,
and conditional P12/W8 remain open because of these gaps.

Read the [proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md),
which includes exact rational counterchecks and a corrected tight-frame
certificate. Finite diagnostics are not eligible asymptotic counterexamples.

The [October 23 continuation](docs/audits/LOW_MEAN_MOMENT_CONE_20261023.md) proves a sharp completion-mean interval and valid variance upper bound, and constructs an abstract zero-mean obstruction. The arithmetic low-mean branch remains open.

The overlap continuation improves the completion bound to q<=2aw and proves a consistent local-law obstruction through floor(1/a)+1 vertices. Neither supplies the missing uniform phase gain.

The October 24 continuation proves a weighted incidence-operator bound and constructs actual zero-completion subsets in growing patterns. The missing transfer from arbitrary triples to weighted arithmetic triples remains open.

| Retained result | Scope |
|---|---|
| Boolean expansion and quartic covariance identity | Exact identities; the W8 inequality is still missing |
| Twelve-slot terminal theorem | 7/11 ceiling under the stated M13 regime |
| Positive-density branch reduction | Uses classical qualitative Szemerédi; no quantitative rate |
| October 19 covariance obstruction | Contains a 4-AP; does not refute P12 |
| Tight-frame reconstruction and partial-spectrum certificate | No automatic concentration, coefficient bound, or phase selection |
| Universal Boolean chirp fourth moment | Holds even for AP-rich sets; does not imply the missing cross-spectrum concentration |

The manuscript and disputed drafts are clearly marked withdrawn, with
previous versions preserved. Lean formalization remains incomplete and
contains an admitted lemma and additional axioms.

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
`current` selects twenty-three current suites and diagnostics, `legacy` selects the
thirteen original suites, and `all` runs both (36 scripts). Earlier dated experiments
remain available separately. A passing run checks finite identities and
examples; it does not prove an asymptotic theorem. See [VERIFYING.md](VERIFYING.md)
for exact versus floating checks, optional SciPy searches, and limitations.

## Reading and repository map

- [Latest report](docs/audits/GROWING_OVERLAP_SYSTEMS_20261024.md): sparse completion triples, growing arithmetic constructions, and incidence energy.
- [Current status](CURRENT_STATUS.md), [theorem ledger](VERIFIED_THEOREMS.md),
  and [failed approaches](FAILED_APPROACHES.md): claims and their boundaries.
- [Documentation index](docs/README.md), [progress](docs/PROGRESS.md),
  and [roadmap](docs/ROADMAP.md): entry points for contributors.
- [Latest checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261024.json): current status and source hashes.
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
