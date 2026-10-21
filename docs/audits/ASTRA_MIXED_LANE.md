<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Astra task — negative relative mixed-form increment

STATUS STANDARD: official Erdős #142 stays OPEN. The local target

    r_4(N) = o(N / log N)

also stays OPEN unless you produce a complete, peer-verifiable proof.
Finite checks are not a proof. Do not write "solved", "proved #142",
or "new asymptotic". Even a correct increment theorem here would be a
quantitative k=4 advance, not a solution of official #142.

TIME BOX: one 30-minute run. One lane. Stop at the end of that lane.

## Do not rediscover

Accept as checkpointed. Do not reprove, rewrite, or re-audit them:

- `CORE_AUXILIARY_IDENTITIES.md` auxiliary U³ / atom / spectral identities
- `INCREMENT_ATTEMPT.md` one-step half-group increment
- `PHASE2_AUDIT.md` α^(3/2) lemma and the C<2 actual-U³ no-go
- `SIGNED_RESEARCH.md` signed operator identities
- `RELATIVE_WINDOWS.md` controlled-window theorem (12)–(15),
  interval refinement (18), high-signal prime-first reduction (25)

Canonical commands already passed. Do not rerun them unless you add a
new lemma that needs a new checker.

## One lane only

Negative relative mixed form. After Φ is controlled, the checkpoint
already gives the exact signed alternative

    M := Λ(g, B, B, g)  ≤  − (1/2) a⁴ C     (RELATIVE_WINDOWS (15))

with C = Λ₄(W), W = 1_Ω, A ⊂ Ω 4-AP-free, g = 1_A − a W, a = |A|/|Ω|.
There is an identity and no increment theorem. Manufacture one theorem,
or prove the target below is impossible under the checkpoint hypotheses.

## Required theorem shape

Either prove, with explicit hypotheses copied from the window class in
RELATIVE_WINDOWS.md §4–§6, a statement of the form

    M ≤ −c a⁴ C
        ⟹
    a′ ≥ a + c′ a^s
    and
    log(|Ω| / |Ω′|) ≤ C_* a^{−t}

with an iteration-compatible relation such as

    s + t < 2

(or an extra endpoint saving that is equally strong at a = ε / log N),
or prove rigorously that no such (s, t, c, c′, C_*) exist for this
signed hypothesis alone.

Ω′ must remain in the hereditary window class, and A ∩ Ω′ must remain
4-AP-free for nonzero differences. State Δa and the size ratio
explicitly. Vague “some structured increment” is a failed run.

## Three mandatory tests

Every proposed statement is false until it survives all three:

1. Z_11 wrap obstruction (`INCREMENT_ATTEMPT.md`):
   A = {6,8,9,10} ⊂ Z_11. Integer-interval 4AP-freeness is not cyclic
   4AP-freeness. Do not treat a wrap as a legal next ambient group.
2. Affine-spread 3-AP-free family (`SIGNED_RESEARCH.md` §9):
   no universal near-full-mass increment on integer progressions.
3. Full iteration budget (`RELATIVE_WINDOWS.md` §14):
   at a = ε / log N, high-signal / same-rank steps may cost about
   log log N; a usable mixed increment must not blow the remaining
   log N budget. Record the implied total loss
   a^{−(s+t−1)} when s+t−1 > 0.

If a candidate fails a test, record the counterexample and stop that
line. Do not repair it by dropping 3^d, holding a growing rank fixed,
identifying an eigenvector with a quadratic phase, or inferring
smoothing from clipping.

## Forbidden moves

- Do not work the low-signal cubic / low-Σ lane.
- Do not claim official #142, or even the local little-o bound, from a
  one-step lemma.
- Do not post comments, issues, or any public text.
- Do not install packages. Python stdlib only if you add a checker.
- Do not change the existing verifiers unless a new lemma needs a
  new file.

## Write-up

Write only `MIXED_INCREMENT.md` in this folder, in this shape:

- User-reported result: the checkpoint already has (15) and no increment
- Locally verified result: exact new command, if any, and what passed
- Increment attempt: one statement, proof status, or impossibility
- The three tests: pass / fail / not applicable, with witnesses
- Mathematical status: official #142 OPEN; local target OPEN unless
  the little-o bound is fully proved
- Next verification step: one concrete check, not a roadmap

If you add a checker, call it `verification/scripts/verify_mixed.py` and capture stdout in
`verification/results/mixed_verification.json`.
