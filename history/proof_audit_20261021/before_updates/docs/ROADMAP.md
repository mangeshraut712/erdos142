<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Research roadmap

The local target remains open (Outcome D). Start with the
[end-to-end iteration report](audits/END_TO_END_ITERATION_CLOSURE_20261021.md) and the
[quadratic projection selection report](audits/QUADRATIC_PROJECTION_SELECTION_20261021.md).

## 1. Comprehensive community scrutiny & peer review

The mathematical chain is complete across the 21 October audits:
pointwise hole support $B q = 0$ $\implies$ completion positivity $m \ge 4 a^3 \mu > 0$
$\implies$ finite quadratic chirp projection $\delta \ge c a^{3/2} \log(1/a)$
$\implies$ quarter-cell density increment reaches $a > 4/5 > 7/11$ within presentation budget.
Exhaustive peer review of each step, constant, and bound is required before outcome transition.

## 2. Multi-scale stress audits and extended verification

The current verification suite comprises 19 current and 13 legacy verifiers (32 total) covering all aspects of the proof.
Extend numerical verification to higher primes, varied host parameters, and alternative
density regimes to continuously audit boundary constants.

## 3. Retain quantitative rigor and documentation integrity

Maintain strict separation between exact/modular identities and floating diagnostics.
Preserve historical captures, update checkpoint source hashes, and maintain full reproducibility
via `verification/check_repository.py` and `verification/run_current.py`.

## How to contribute a checkable result

State the exact proposition and every changed hypothesis. Supply a complete
proof for an asymptotic claim and a finite verifier where it can check
normalizations or examples. Record failed approaches without erasing earlier
versions, update the current ledger and checkpoint, and run the relevant
checks using [VERIFYING.md](../VERIFYING.md). Preserve author attribution
and follow [CONTRIBUTING.md](../CONTRIBUTING.md).

The [September roadmap snapshot](../history/publication_20261021/public_docs_before/docs/ROADMAP.md)
and [original audits](audits/) remain available for the older energy route.
