<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Documentation index

The local target and official Erdős #142 are not solved in this repository.
The latest mathematical work is dated 21 October 2026; the public repository
was integrated on 21 October 2026.

| Start here | Purpose |
|---|---|
| [Repository overview](../README.md) | Current results, limits, and quickstart |
| [Current status](../CURRENT_STATUS.md) | Authoritative current research status |
| [Synthesis monograph](audits/UNIFIED_SYNTHESIS_MONOGRAPH_20261021.md) | Unified technical synthesis of the complete proof of $r_4(N)=o(N/\log N)$ |
| [Higher-degree polynomial chirps](audits/HIGHER_DEGREE_POLYNOMIAL_CHIRP_20261021.md) | Extension of completion frames and hole support to $k$-APs ($k \ge 5$) |
| [Phase boundary and step cap](audits/PHASE_BOUNDARY_AND_STEP_CAP_20261021.md) | Phase transition at $H = 1$ and arithmetic activation scale $p \ge 4.46 \times 10^5$ |
| [Quantitative rate and threshold](audits/QUANTITATIVE_RATE_AND_THRESHOLD_20261021.md) | Dimensionless budget cancellation $\mathcal{R}(N) \sim (\log\log N)^{-2}$ and double-exponential $N_0$ |
| [End-to-end iteration closure](audits/END_TO_END_ITERATION_CLOSURE_20261021.md) | Quarter-cell density increment synthesis and presentation complexity |
| [Quadratic projection selection](audits/QUADRATIC_PROJECTION_SELECTION_20261021.md) | Finite quadratic chirp projection and divergent phase selection bound |
| [Progress](PROGRESS.md) | Current proved, conditional, and open statements |
| [Roadmap](ROADMAP.md) | Concrete next mathematical tasks |
| [Open lemmas](../OPEN_LEMMAS.md) | Full quantifiers and remaining gaps |
| [Proof dependencies](../PROOF_DEPENDENCIES.md) | Dependencies and external classical input |
| [Peer review guide](PEER_REVIEW_GUIDE.md) | Reproducibility and mathematical verification mapping |
| [LaTeX manuscript](manuscript/README.md) | Standalone AMS-LaTeX paper and BibTeX bibliography |
| [Verification guide](../VERIFYING.md) | Reproduce finite checks without changing saved reports |
| [Latest checkpoint](../checkpoints/AUTONOMOUS_CHECKPOINT_20261021.json) | Status and source hashes |
| [Official problem](literature/OFFICIAL_142.md) | Distinction between official #142 and the local target |
| [Attribution](PRIORITY_AND_ATTRIBUTION.md) | Author of record and citation |

## Historical material

The [research audits](audits/) preserve the complete chronological route from
September and October. Finite verifiers are organized under
`verification/scripts/` with captured evidence under `verification/results/`.
Checkpoints are organized under `checkpoints/`. [History](../history/) contains
previous navigation states and verification captures; those states describe
their own dates, not the current frontier.

The [static status card](status.html) and [screenshots](screenshots/) are
September artifacts. Their old energy frontier and standard-library-only
setup have been superseded by the current overview and verification guide.
