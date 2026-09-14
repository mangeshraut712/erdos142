# Codex task — Erdős 142 density increment

SUPERSEDED for the next Astra run by `ASTRA_MIXED_LANE.md`.
Keep this file only as the earlier broad increment brief.

STATUS STANDARD: the problem stays OPEN unless you produce a complete, peer-verifiable proof of r_4(N) = o(N/log N). Finite checks are not a proof. Do not write "solved" or "proved" from examples.

## Folder facts

This folder is an offline 2026-09-06 attempt. Canonical files:

- `README.md` — claimed auxiliary identities, rejected shortcuts, unresolved step
- `verify_core.py` — exact rational finite checks
- `verification.json` — last captured result

Canonical command:

```bash
python3 verify_core.py
```

## Goal for this session

One lane only: try to turn the already-verified auxiliary estimates into a **density-increment** mechanism on a sufficiently large set.

In the write-up model, density gain `c alpha^s` and logarithmic size loss `C alpha^(-t)` with `s >= 1`, `t >= 0` give total loss of order `alpha^(-(s+t-1))` when `s+t-1 > 0`. Little-o at `alpha = epsilon / log N` needs exponent below 1, or an extra saving at the endpoint. No such increment theorem exists here yet.

## Required method

1. Read `README.md`, `verify_core.py`, and `verification.json`.
2. Run `python3 verify_core.py` and record the output.
3. Do not reuse a rejected shortcut as progress:
   - Z_7, A={0,1,3}: successive residual pairs are not a deterministic composition
   - Z_5, A={0,1}: residual correlation sign is not the pair-indicator sign
   - same Z_5 spectral kernel counterexample
   - Z_13, A={0,1,3,9}: flat nonzero squared Fourier magnitudes
   - |Lambda_4(g)| <= U3(g)^4 fails for g=(1,1/2,1/2,1/2,1/2) on Z_5
4. Propose at most one concrete increment lemma, with explicit hypotheses.
5. Test that lemma on the existing finite examples and any new small examples you add. If it fails, record the counterexample and stop that line.
6. If an identity looks true on examples, try to prove it algebraically. If the proof is incomplete, say so.
7. Write results to `INCREMENT_ATTEMPT.md` using this shape:
   - User-reported result: this folder claimed auxiliary identities only
   - Locally verified result: exact command and what passed
   - Increment attempt: statement, proof status, counterexamples
   - Mathematical status: conservative theorem status
   - Next verification step: one concrete check
8. Do not post anything public. Do not expand into a broad research program. Stop after one increment attempt plus checks.

## Budget

Prefer exact rational arithmetic. Keep new code in this folder, Python stdlib only. Do not spend the session rewriting the existing verifier unless a check is broken.
