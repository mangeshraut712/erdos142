# Open lemmas — operative checkpoint, 16 October 2026

The local unconditional target remains OPEN. This file replaces the operative
October 15 list; its prior version is saved in history/log_density_20261015/.
The stable mixed-window terminal theorem is now PROVED, not an open lemma.

## O1. Direct quadratic selection on a precise product-budget domain

Let L_p=log p, ell(a)=log(2/a), R(a)=loglog(e^2/a). For every epsilon>0,
seek constants c_epsilon>0 and p_epsilon such that every mixed linear/
quadratic interval window Omega over F_p, p>=p_epsilon, satisfying

    r>=1,
    r[log(p/|Omega|)+log(48r)+log L_p] <= L_p/100,

and every actual cyclically 4-AP-free A subset Omega with

    epsilon/(2log|Omega|) <= a=|A|/|Omega| <= 4/5,

has a nonconstant polynomial P of degree at most two with

    |E_Omega (1_A-a)e_p(-P)|
          >= c_epsilon a^(3/2)sqrt(ell(a))R(a).

This is DIRECT-Q-P, (L10)-(L11) in LOG_DENSITY_ATTACK_20261016.md.
The implication to r_4(N)=o(N/log N), including cumulative losses,
terminal count, prime embedding and transfer, is proved there.
The existence assertion remains OPEN. One may restrict the domain to
windows retaining the initial interval constraint in [N] and the precise
reachable budgets, if that restriction is made explicit.

The linear-only version is an alternative sufficient theorem. Do not
transfer it to mixed windows. This is a trivial-factor residual B-a on
each current window; it is not a claim for an arbitrary prior B-g.

## O2. Weighted signed counting under failure of O1

For the tent progression weight F in MIXED_QUADRATIC_TERMINAL_20261016.md,
choose tau=a^2/log p and H=floor(tau |Omega|/(48r)). Let mu be its exact
persistent baseline, w=|Omega|/p, and u=B-a1_Omega. On the windows reachable
under the ledger (L12)-(L13), the zeroth term is (1+o(1))a^4 w mu, the
linear residual is o(a^4 w mu), and the exact diagonal is aw/p.
Under failure of O1, prove

    R_2^F+R_3^F+R_4^F >= -(1/2)a^4 w mu.

AP exclusion gives the opposite asymptotic value -(1+o(1))a^4 w mu, so
this inequality would force O1 along the iteration. It is OPEN.
Use actual Booleanity/AP exclusion: the generic pair-PSD shortcut is
refuted by the explicit arithmetic p=53 weighted-function witness.

## O3. Original linear packet route (still open)

The packet-existence and retention hypotheses in the October 15 O/L1-L2
list remain open under the exact factor/variance/Gram/budget hypotheses
of THREE_BRANCH_AMPLIFICATION_20261014.md Theorem 4. The conditional cap
and shell estimates remain valid; they do not prove packet existence.
Proper-window branch errors still require their own uniform estimates.
The new weighted first-residual estimate does not establish those old
unweighted formulas or all old two-branch reductions.

The sparse actual AP-free obstruction now covers 1/2<theta<2/3 with
a comparable to p^(-theta). It is outside the required logarithmic-density
regime. No target-density counterexample has been constructed.
