<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Progress — 21 October 2026

**Outcome D: partial results; target OPEN.** Mathematical frontier:
19 October 2026. This digest reports the written research, not a new proof
or an independent literature-status survey. The local target
`r_4(N)=o(N/log N)` remains unproved in this pack and would not by itself
settle [official #142](literature/OFFICIAL_142.md).

## Latest results

1. **Positive-density failure branch eliminated, using classical input.**
   Uniform finite error estimates on T5 hosts, combined with qualitative
   four-term Szemerédi, show that every eligible failure sequence has
   `a -> 0`. This is a qualitative reduction; the density threshold cannot
   be varied with the prime to obtain the target rate.
   [Proof and scope](../POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md).
2. **A weakened covariance claim is obstructed at logarithmic density.**
   The block-mask construction has `a ~ 1/log p`, small quadratic phases,
   and `R3+R4 < -a^4 w mu/2` with the original weight. It deliberately
   contains `{0,1,2,3}`. Thus it does not satisfy AP exclusion and does not
   refute P12. [Proof and scope](../O2_COVARIANCE_ATTACK_20261019.md).

The [October 19 report](../O2_CONTINUATION_20261019.md) explains how these
results constrain the next attempt.

## Supporting results

- [Fixed-pattern terminal theorem](../FINITE_PATTERN_TERMINAL_20261018.md):
  the twelve-slot certificate yields a 7/11 ceiling under original M13.
- [Quartic covariance identity](../WEIGHTED_QUARTIC_COVARIANCE_20261018.md):
  `R4=U^2-E_F/2` exactly, including the centered diagonal corrections.
- [Weighted completion theorem](../WEIGHTED_COMPLETION_CERTIFICATE_20261018.md):
  exact projections, collision estimates, and a conditional phase certificate.
- [Sparse alteration theorem](../BOOLEAN_TYPICAL_ALTERATION_20261018.md):
  actual AP-free Boolean examples with `delta/a^(3/2) -> 0` for
  `a ~ p^-theta`, `1/3 < theta < 1/2`. These fail the target density and
  diagonal requirements.

## Still open

**DIRECT-Q-GAIN**, **P12**, and its exact energy form **W8** remain open.
The selection statement needs a divergent multiplier over `a^(3/2)`
uniformly on the full eligible domain. The completion certificate has not
been proved to exist; its small/zero mean branch also remains unresolved.

Under failed adequate selection, W8 asks for
`E_F(u) <= 2U^2 + 2R3 + a^4 w mu` on actual AP-free eligible sets.
The established pair result is near-positivity, not exact positivity or
a two-sided smallness bound. Exact diagonals must be retained.

See [OPEN_LEMMAS.md](../OPEN_LEMMAS.md) for quantifiers and
[PROOF_DEPENDENCIES.md](../PROOF_DEPENDENCIES.md) for the dependency chain.

## Evidence and history

The [verification guide](../VERIFYING.md) separates exact finite checks,
floating diagnostics, probabilistic proofs, and the classical theorem
used in the qualitative reduction. Passing checks does not close the gap.
The [latest checkpoint](../AUTONOMOUS_CHECKPOINT_20261021.json) binds the
current files to their hashes. Earlier September energy formulations and
refuted shortcuts remain in [audits](audits/) and
[the failed-approach ledger](../FAILED_APPROACHES.md).
