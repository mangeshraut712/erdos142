# Recovery audit — 17 October 2026

The latest completed mathematical work was saved on 16 October after the
machine checkpoint and navigation files had already been written. The
older checkpoint was intact, but incomplete as a map of the newest work.
This recovery adds no mathematical theorem and does not solve the target.

## Recovered results and precise scope

1. **PROVED:** Weighted pair arithmetic near-positivity, (P1)–(P10) in
   `WEIGHTED_PAIR_REDUCTION_20261016.md`, gives R_2^F>=-o(a^4w mu) on
   reachable hosts. Together with the earlier R_1 estimate, this leaves
   only cubic-plus-quartic signed cancellation. It is not exact PSD or
   a two-sided smallness result.
2. **PROVED CONDITIONAL IMPLICATION:** The direct cell gain/size tradeoff
   and epoch sum in `DIRECT_INCREMENT_TRADEOFF_20261016.md` imply the
   target from DIRECT-Q-GAIN. Any uniform divergent multiplier over
   a^(3/2) suffices; a concrete choice is loglog(e^2/a). The structural
   premise remains OPEN.
3. **PROVED AUXILIARY OBSTRUCTION:** The fractional-quadratic example in
   `GLOBAL_CHIRP_INVERSE_OBSTRUCTION_20261016.md` blocks deduction of
   global finite-field chirp correlation from U^3 alone for bounded real
   weights. It is neither Boolean nor AP-free and refutes neither
   DIRECT-Q-GAIN nor the local target.

The exact next sufficient inequality is (P12), under failed selection:

    R_3^F+R_4^F >= -(1/2)a^4w mu.

AP exclusion forces the upper bound -(1-o(1))a^4w mu instead. Proving the
lower bound on actual eligible sets would force selection. Generic moment
positivity and the existing pair theorem do not establish it.

## Recovery checks

- All 14 hashes in AUTONOMOUS_CHECKPOINT_20261016.json matched before edits.
- All 5 hashes in WEIGHTED_PAIR_VERIFICATION_20261016.json matched.
- The latest script ran in an isolated temporary directory and passed
  28,520 finite checks; the resulting complete JSON exactly matched the
  historical report. Largest floating identity discrepancy: about 9.33e-15.
- The chirp-grid checks examine 1,098,390 coefficients; this is not an
  additional count of independently proved claims.
- The original proof notes, verifier scripts, historical JSON results and
  October 16 checkpoint were left unchanged. Eleven prior navigation and
  checkpoint files were copied with a hash manifest before synchronization.

Evidence is saved in history/resume_20261017/. The current entrypoints are
CURRENT_STATUS.md, OPEN_LEMMAS.md, NEXT_AUTONOMOUS_ACTION.md and
AUTONOMOUS_CHECKPOINT_20261017.json. Earlier ledger passages remain as
historical records, with a current pointer prepended to avoid stale starts.

No new research attack on (P12) was completed in this recovery. The local
target remains OPEN, and no research computation is left running.

## Bounded independent review

A separate read-only audit found no obvious flaw in the direct-cell epoch
sum, the terminal error substitution, or the fractional-quadratic obstruction.
This was a bounded review, not a formal proof certification. In (T4), S(t)
is an upper bound on accumulated actual log-size loss; the later sentence
calling it the actual sum should be read in this upper-bound sense. The
original note has been preserved. The centered real obstruction's numerical
U^3 lower bound is asserted only for sufficiently large p.
