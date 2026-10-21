# Next autonomous action — 21 October 2026

Resume from `AUTONOMOUS_CHECKPOINT_20261021.json`, `CURRENT_STATUS.md`,
`O2_CONTINUATION_20261019.md`, and `OPEN_LEMMAS.md`.
The mathematical frontier is 19 October. Outcome D; the unconditional
local target, DIRECT-Q-GAIN, P12 and W8 remain OPEN.

The next proof attempt should exploit the original four pointwise AP-free
completion identities `Bq_j=0`, together with the logarithmic-density and
negligible-diagonal hypotheses, to establish the original-weight bound

    E_F(u)<=2U^2+2R_3^F+a^4wmu, U=wa(1-a).             (W8)

This is exactly P12 because `R4=U^2-E_F/2`. Use the original weight,
proper-host transform, exact chirp-index affine map, and cubic term.
The positive energy is subtracted. Pointwise small individual chirps and
the direct cubic Cauchy-Schwarz estimate do not provide the required bound.

Read `O2_COVARIANCE_ATTACK_20261019.md` before weakening the hypotheses.
Its Boolean block construction satisfies T5, the logarithmic density range,
initial-host geometry, original H, and negligible diagonal, yet violates
W8 with `Q<=(-11/20+o(1))a^4wmu`. It deliberately contains `{0,1,2,3}`.
It is NOT AP-free and NOT a P12 counterexample. Boolean chirp identities
and a weighted count below half the main term cannot replace actual AP
exclusion. A successful coupling of `D_s(c,t)` with
`D_s(3c+gamma,3t-beta)` must use the stronger arithmetic hypothesis.

An alternative route is O3: prove the small-l1, small-error completion
certificate in `WEIGHTED_COMPLETION_CERTIFICATE_20261018.md` using the
actual relative Gram matrix, then close its small/zero-completion-mean
branch. The certificate requires `m>0`. Four completion channels are
necessary for the original weight. Their hole projection and the
disjoint-six-point lower bound are proved; sufficient phase concentration
and a complete low-mean alternative remain OPEN.

The positive-density failure branch is closed by
`POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md`, with explicit use of
the classical qualitative four-term Szemerédi theorem. The remaining
DIRECT-Q-GAIN failure must be an eligible `a->0` sequence with bounded
`delta/a^(3/2)`. The classical theorem is not reproved, and no rate at
logarithmic density follows from its uncontrolled threshold.

Read the original framework before changing hypotheses:
`WEIGHTED_PAIR_REDUCTION_20261016.md`,
`DIRECT_INCREMENT_TRADEOFF_20261016.md`, and
`MIXED_QUADRATIC_TERMINAL_20261016.md`.
The terminal ceiling is `7/11+o(1)` under M13. Improving only that constant
does not supply the structural phase-selection step; the conditional
iteration parameters need no recalculation.

Every proposed counterexample must satisfy T5, the density range, actual
AP exclusion, original H, and the failed cap. The 76 finite witnesses,
the polynomial-density AP-free construction, and the October 19 block
construction each fail at least one condition. Refuting one fixed
multiplier is insufficient to negate the full DIRECT-Q-GAIN statement.

Use the latest checkpoint and `VERIFYING.md` for verification scope and
commands. Do not repeat unchanged suites merely to restart. Independently
audit a new proof and run the smallest relevant finite check. Preserve
historical sources, update all nine navigation/ledger files, and save a
dated checkpoint before ending. Saved notes do not imply background work.
