# Next autonomous action — recovered 17 October 2026

Read `AUTONOMOUS_CHECKPOINT_20261017.json`, `CURRENT_STATUS.md`, and
`OPEN_LEMMAS.md`, then the three late-16-October notes listed there.
The old 09:03 October 16 checkpoint predates those notes.

The first research task is **OPEN_LEMMAS.md O2 / (P12)** in
`WEIGHTED_PAIR_REDUCTION_20261016.md`, or direct selection O1.
For actual Boolean AP-free sets on the reachable mixed hosts, R_1 is small
and R_2 is already near-nonnegative. The remaining cancellation is R_3+R_4.

Start with an exact weighted cubic/quartic decomposition retaining all
host indicators and the h=0 diagonal. Under failure of correlation
`c_epsilon a^(3/2)loglog(e^2/a)`, seek

    R_3^F+R_4^F >= -(1/2)a^4 w mu.

Compare to the AP-forced upper bound (P11). Keep any finite search strictly
labelled diagnostic; an example must satisfy the actual Boolean/AP-free
and window hypotheses to bear on this route.

For direct selection, use DIRECT-Q-GAIN: any uniform divergent multiplier
over a^(3/2) suffices on domain (T5). Do not reintroduce the obsolete extra
sqrt(log(2/a)) threshold or the old size-loss charge at every step.
Do not substitute a U^3 lower bound for global finite-field phase correlation.

The latest verifier was rerun successfully during recovery: 28,520 checks,
exactly matching its saved report. Run `verify_weighted_pair_20261016.py`
after relevant mathematical changes, in isolation to preserve old output.
Recheck earlier dependencies only when used or changed. Save a new dated
checkpoint after a research cycle. No background computation is running.
