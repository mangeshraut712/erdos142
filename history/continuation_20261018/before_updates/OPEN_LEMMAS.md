# Open lemmas — operative checkpoint, 17 October 2026

The local unconditional target remains OPEN. This list incorporates the
later 16 October notes missed by the previous checkpoint. The earlier list
is preserved in `history/resume_20261017/before_sync/OPEN_LEMMAS.md`.
Mixed-window terminal geometry and weighted pair near-positivity are proved
under their stated budgets; neither is the current missing step.

## O1. DIRECT-Q-GAIN on the precise product domain

For every epsilon>0 seek c_epsilon>0, p_epsilon, and
F_epsilon:(0,4/5]->[1,infinity), with F_epsilon(a)->infinity as a->0,
such that every prime p>=p_epsilon and mixed linear/quadratic interval
window Omega satisfying

    r>=1,
    r[log(p/|Omega|)+log(48r)+loglog p] <= log p/100,

and every actual cyclically nonzero-4-AP-free Boolean A subset Omega with

    epsilon/(2log|Omega|) <= a=|A|/|Omega| <= 4/5

has a nonconstant polynomial P of degree at most two with

    |E_Omega (1_A-a)e_p(-P)| >= c_epsilon a^(3/2)F_epsilon(a).

The constants/function precede the quantifiers over windows and sets.
This is (T5)–(T6) of `DIRECT_INCREMENT_TRADEOFF_20261016.md`.
A concrete sufficient threshold is `c_epsilon a^(3/2)R(a)`, with
`R(a)=loglog(e^2/a)` (replace R by max(1,R) at a constant cost).
The implication to the target, including all cumulative and terminal
losses, is proved in (T1)–(T12). The selection assertion itself is OPEN.

A precisely stated reachable subclass retaining the initial interval
constraint is sufficient. A linear-only version must remain confined to
linear-only hosts. This is the current-mean residual, not an arbitrary
prior-factor residual. The old DIRECT-Q-P threshold remains sufficient
but is stronger than necessary.

## O2. Signed cubic-plus-quartic counting under failure of selection

Use the tent weight F of `MIXED_QUADRATIC_TERMINAL_20261016.md`,
`tau=a^2/log p`, `H=floor(tau |Omega|/(48r))`, persistent baseline mu,
`w=|Omega|/p` and `u=1_A-a1_Omega`. On reachable hosts in (T10),

    R_0^F=(1+o(1))a^4 w mu,
    R_1^F=o(a^4 w mu),
    R_2^F>=-o(a^4 w mu).

The last bound is the one-sided theorem (P1)–(P10) of
`WEIGHTED_PAIR_REDUCTION_20261016.md`; it does not say |R_2^F| is small.
AP exclusion and the exact diagonal aw/p force

    R_3^F+R_4^F <= -(1-o(1))a^4 w mu.

Under failure of the concrete threshold in O1, prove the incompatible
lower bound (P12)

    R_3^F+R_4^F >= -(1/2)a^4 w mu.

This sufficient statement is OPEN. Start with the actual weighted cubic
and quartic arithmetic, retaining Booleanity, host indicators and h=0.
The p=53 witness only refutes exact generic PSD; it is compatible with
the proved near-positivity. Abstract four-point moment laws still permit
R_1=R_2=R_3=0, R_4=-a^4 and cannot alone establish this lower bound.

## O3. Older packet routes and invalid shortcuts

SELECT/WSELECT/SIGNED/COLLECTIVE-WSELECT existence and retention remain
open under their original hypotheses. New weighted estimates do not
establish the old unweighted formulas on arbitrary factors/windows.
A bare U^3 signal is insufficient for global finite-field chirp selection
on bounded real weights: see `GLOBAL_CHIRP_INVERSE_OBSTRUCTION_20261016.md`.
That example is neither Boolean nor AP-free. Sparse AP-free obstructions
at a comparable to p^(-theta), 1/2<theta<2/3, are also outside the required
logarithmic-density regime. No target-density counterexample is claimed.
