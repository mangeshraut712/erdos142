# Current research status — recovered 17 October 2026

**Principal status: (D) RIGOROUS PARTIAL RESULTS.**
The local target `r_4(N)=o(N/log N)` remains **OPEN**.
No unconditional sufficient density increment or phase-selection theorem is claimed.

The latest mathematical work is the later 16 October continuation:

- `WEIGHTED_PAIR_REDUCTION_20261016.md`
- `DIRECT_INCREMENT_TRADEOFF_20261016.md`
- `GLOBAL_CHIRP_INVERSE_OBSTRUCTION_20261016.md`

These notes were saved after the old machine checkpoint. This recovery
synchronizes navigation with those existing results; it adds no new theorem.
See `RESUME_AUDIT_20261017.md` and `AUTONOMOUS_CHECKPOINT_20261017.json`.

## What is established

- **PROVED:** Mixed linear/quadratic interval windows have terminal AP-free
  relative density at most `3/4+o(1)` under the stated rank/size budgets,
  including resonant and repeated phases. Finite errors and diagonals are
  explicit in `MIXED_QUADRATIC_TERMINAL_20261016.md` (M1)–(M13).
- **PROVED:** Direct quarter-cell selection retains the tradeoff
  `mu_C gamma >= kappa delta/(8a)`. Small cells force larger density gains.
  Summing this tradeoff removes the extra logarithmic size-loss penalty;
  see `DIRECT_INCREMENT_TRADEOFF_20261016.md` (T1)–(T4).
- **PROVED CONDITIONAL IMPLICATION:** DIRECT-Q-GAIN implies the target.
  It asks for correlation `c_epsilon a^(3/2) F_epsilon(a)` with a uniform
  `F_epsilon(a)->infinity`, on the precise product domain (T5). A concrete
  sufficient choice is `R(a)=loglog(e^2/a)`. Existence of this correlation
  is **OPEN**. The previous `sqrt(log(2/a)) R(a)` multiplier is unnecessary.
- **PROVED:** For the specified localized tent-weighted count on reachable
  hosts, `R_1^F=o(a^4 w mu)` and `R_2^F>=-o(a^4 w mu)`. The pair theorem is
  arithmetic near-positivity, not exact PSD and not an absolute smallness
  bound. Its finite errors are (P1)–(P10) in the weighted-pair note.
- **PROVED AUXILIARY OBSTRUCTION:** A bare U^3 signal does not force the
  required global finite-field quadratic correlation for bounded real
  weights, even on an interval at logarithmic relative density. The
  fractional-quadratic construction is neither Boolean nor AP-free and
  does not refute DIRECT-Q-GAIN or the target.

## Exact remaining gap

For actual Boolean AP-free sets on reachable hosts, the weighted expansion
and its exact diagonal `aw/p` imply

    R_3^F+R_4^F <= -(1-o(1))a^4 w mu.

The sufficient missing statement, under failure of adequate phase selection,
is (P12):

    R_3^F+R_4^F >= -(1/2)a^4 w mu.

This is **OPEN**. Use actual Booleanity and arithmetic AP exclusion.
The other option is to establish DIRECT-Q-GAIN directly. With the concrete
choice R(a), the squared threshold is `a^3 R(a)^2`, still a divergent
factor `a^(-1)R(a)^2` above the available squared signal `a^4`.
The older SELECT/WSELECT/SIGNED/COLLECTIVE-WSELECT inputs remain open.

For t=epsilon/log N, L=log N, the concrete conditional ledger is

    rank = O_epsilon(sqrt(L)/loglog L + log L),
    log-size loss = O_epsilon(sqrt(L)/loglog L + (log L)^2),
    rank times log-size loss = o(L).

## Verification and preservation

On 17 October, the latest verifier passed **28,520 finite checks** in an
isolated directory. Its generated JSON exactly matched the saved report;
all 14 old checkpoint hashes and all 5 latest verification-source hashes
matched before synchronization. Finite checks are not an asymptotic proof.
The chirp tests examine 1,098,390 coefficients within the counted checks.

Evidence: `history/resume_20261017/resume_verification.json` and
`history/resume_20261017/weighted_pair_rerun.json`. Before-sync navigation
and checkpoint copies are in `history/resume_20261017/before_sync/`.
The original proof notes, scripts, historical verification outputs and
October 16 machine checkpoint are preserved. No research computation is
left running by this recovery.
