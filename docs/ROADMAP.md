<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Research roadmap

The local target remains open. Start with the
[October 19 report](audits/O2_CONTINUATION_20261019.md) and the exact
[open-lemma statements](../OPEN_LEMMAS.md).

## 1. Use pointwise AP exclusion in the covariance bound

Prove W8, `E_F(u) <= 2U^2+2R3+a^4 w mu`, on the eligible Boolean
AP-free domain under failed adequate selection. The October 19 block-mask
construction rules out proving this from Boolean chirp identities, a phase
cap, and a reduced weighted count alone. Exploit `B q_j = 0`, or equally
strong arithmetic information, together with logarithmic density and the
negligible-diagonal condition.

## 2. Complete a direct phase-selection route

The [weighted completion certificate](audits/WEIGHTED_COMPLETION_CERTIFICATE_20261018.md)
is sufficient when its positive-mean hypotheses hold. Prove existence
with the stated norm bounds, and handle the small/zero completion-mean
branch. A conditional certificate alone is not DIRECT-Q-GAIN.

## 3. Keep the quantitative domain intact

The [positive-density reduction](audits/POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md)
leaves only `a -> 0` failure sequences. Retain T5, the original weight,
the logarithmic density lower bound, and the exact diagonals. Do not use
an uncontrolled qualitative threshold as a quantitative rate. Small-prime
experiments with prescribed radius zero cannot refute P12.

## How to contribute a checkable result

State the exact proposition and every changed hypothesis. Supply a complete
proof for an asymptotic claim and a finite verifier where it can check
normalizations or examples. Record failed approaches without erasing earlier
versions, update the current ledger and checkpoint, and run the relevant
checks using [VERIFYING.md](../VERIFYING.md). Preserve author attribution
and follow [CONTRIBUTING.md](../CONTRIBUTING.md).

The [September roadmap snapshot](../history/publication_20261021/public_docs_before/docs/ROADMAP.md)
and [original audits](audits/) remain available for the older energy route.
