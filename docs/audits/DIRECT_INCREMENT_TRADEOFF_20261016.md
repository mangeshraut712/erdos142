# Direct cell gain versus size loss: the logarithmic penalty is avoidable

16 October 2026, continuation cycle. Offline. **PROVED quantitative
refinement lemma and conditional closure.** The local target remains OPEN.
This strengthens the ledger in `LOG_DENSITY_ATTACK_20261016.md` without
assuming new phase correlations. No literature novelty is asserted.

## 1. The retained tradeoff

Let B=1_A on a nonempty finite relative window Omega, with mean 0<a<1,
and let a unit phase z have correlation
`delta=|E_Omega(B-a)conjugate(z)|>0`. The direct quarter-cell proof (L2)
chooses a single cell C with discrepancy

    m=E_Omega(B-a)1_C >= kappa delta/8, kappa=2sqrt(2)/pi.

Write `mu_C=|C|/|Omega|`, `a'=|A cap C|/|C|`,
`gamma=a'/a-1`, and `eta=kappa delta/(8a)`. Then exactly

    mu_C gamma=m/a >= eta.                            (T1)

This contains more information than the two separate bounds
`gamma>=eta` and `mu_C>=a eta`. The second follows from
`m<=mu_C(1-a)`, giving the slightly stronger
`mu_C>=a eta/(1-a)`. A small cell necessarily has a large density gain.

For completeness, the choice of C uses uniformly rotated four-arc
partitions. Their midpoint quantization Q_theta satisfies
`E_theta Q_theta(z)=kappa z`. Some rotation therefore has
`|E(B-a)conjugate(Q_theta)|>=kappa delta`. Its four real discrepancies
sum to zero, so their positive parts sum to at least kappa delta/2;
one is at least kappa delta/8. Thus (T1) applies to the SAME cell, with
no Gram orthogonality, nonempty-cell assumption, or second selection.

For any step with 0<gamma<=1, put `s_C=log(1/mu_C)`. Since
`mu_C log(1/mu_C)<=1/e` and `log(1+gamma)>=gamma/2`, (T1) gives

    eta s_C <= mu_C gamma log(1/mu_C)
             <=gamma/e <=(2/e)log(1+gamma),
    s_C <= [2/(e eta)] log(a'/a).                      (T2)

Here e is Euler's number, not a density epoch. If gamma>1, the density
more than doubles. This step instead obeys

    s_C<=log(1/(a eta)).                               (T3)

Both inequalities are finite and exact in their stated ranges. If eta is
replaced by any smaller positive guaranteed lower bound, they remain true.
Neither says a small cell has a universally large measure.

## 2. Exact epoch ledger

Suppose at every current density a<=4/5 the selection hypothesis supplies
a unit polynomial phase whose direct-cell step has guaranteed eta(a),
where 0<eta(a)<=1/4. Starting from density t, divide the range into
successive epochs `[e_j,min(2e_j,4/5)]`, e_j=2^j t, with half-open shared
endpoints and the last upper endpoint included. Put

    m_j=inf_(a in epoch j) eta(a)>0,
    B_j=1+ceil(2log 2/m_j).

There are at most B_j steps starting in epoch j: every step multiplies
density by at least 1+m_j, and all but the final step still have starting
density at most 2e_j. Use log(1+m_j)>=m_j/2.

At most one step with gamma>1 starts in an epoch, because it leaves the
epoch. Its size cost is at most `log(1/(e_j m_j))` by (T3). For all steps
with gamma<=1 starting in that epoch, the sum of their logarithmic gains
is at most log 4. If the exit is a small-gain step, its final density is
at most 4e_j. If the exit is a large-gain step, the small-gain steps stop
before it and have total gain at most log 2. Density never decreases.
Apply (T2) to these steps. The resulting exact bounds are

    D(t)=sum_j B_j,
    S(t)=sum_j [4log 2/(e m_j)+log(1/(e_j m_j))],       (T4)

where the number of additional phase constraints is at most D(t) and
`log(|Omega_initial|/|Omega_final|)<=S(t)`. S is a sum of the actual
cell size losses. The occupied-mass telescope is compatible with it,
but the earlier estimate that charged log(1/eta) at EVERY step is no
longer needed. Big jumps pay that logarithm at most once per epoch.

This replaces an avoidable factor ell(t) in the old size-loss ledger.
It does not change the proof of the direct-cell lemma or the class of
windows obtained by its refinements.

## 3. Any divergent improvement over a^(3/2) is sufficient

The following is a precise OPEN structural hypothesis, called
**DIRECT-Q-GAIN**. For each epsilon>0, there exist c_epsilon>0,
p_epsilon, and a function F_epsilon:(0,4/5]->[1,infinity) with

    F_epsilon(a)->infinity as a->0,

such that every prime p>=p_epsilon, mixed interval window Omega with

    r>=1,
    r[log(p/|Omega|)+log(48r)+loglog p] <= log p/100,    (T5)

and every cyclically 4-AP-free Boolean A subset Omega with

    epsilon/(2log|Omega|) <= a <=4/5

has a nonconstant polynomial P of degree at most two satisfying

    |E_Omega(B-a)e_p(-P)|
          >= c_epsilon a^(3/2)F_epsilon(a).            (T6)

The constants, function and p threshold precede the quantifiers over
windows, densities and sets. No claim of (T6) is proved in this note.
One may restrict to windows retaining the initial interval constraint
or to an explicitly defined reachable class, as in the preceding note.
There is an alternative linear-only version on linear-only windows.

Without loss of sufficiency, clip F_epsilon from above by a^(-1/4).
The clipped function still tends to infinity and is at least one.
Reduce c_epsilon so that C=kappa c_epsilon/8<=1/100. The guaranteed gain
parameter is

    eta(a)=C sqrt(a)F_epsilon(a), 0<eta(a)<=1/100.

Let f_j=inf_(a in epoch j)F_epsilon(a)>=1. Then

    m_j>=C sqrt(e_j)f_j,
    B_j<=2+2log 2/(C sqrt(e_j)f_j),
    log(1/(e_j m_j))<=log(1/C)+(3/2)log(1/e_j).        (T7)

Multiplying the reciprocal-m_j sums by sqrt(t) reduces them to a
constant times

    sum_(j in epochs) 2^(-j/2)/f_j.                    (T8)

This sum tends to zero as t->0. To see uniformity without assuming
continuity or monotonicity of F_epsilon, choose any fixed J. For every
j<=J the entire epoch tends to zero, hence f_j->infinity. The remaining
tail is at most `sum_(j>J)2^(-j/2)`, independently of t, and tends to
zero as J->infinity. The additive rank terms are O(log(1/t)), and the
logarithmic size terms in (T7) sum to O_C(log(1/t)^2). Therefore

    D(t)=o_epsilon(t^(-1/2)),
    S(t)=o_epsilon(t^(-1/2)).                           (T9)

This is a complete summation argument. There is no hidden regularity
assumption on the divergent factor. The exact finite bounds are (T4).
For larger initial t, the estimates are uniform over t>=epsilon/log N:
below any fixed cutoff use the preceding tail argument, and above it
the bound F_epsilon>=1 supplies a finite uniform epoch bound. Equivalently
split at a cutoff where F_epsilon>=K, obtaining a multiple of
`t^(-1/2)/K` plus a constant depending on the cutoff and C, and the
explicit additive logarithmic sums. Then let K grow after N.

## 4. Complete conditional implication

Assume DIRECT-Q-GAIN. Suppose for a fixed epsilon>0 and arbitrarily large
N there is an AP-free A subset [N] of density t>=epsilon/log N. Take a
prime 3N<p<6N, using the elementary prime-interval proof in
`NEW_RESULTS_20261002.md`. Cyclic APs supported in [N] are ordinary APs:
both second differences have magnitude <2N<p and so vanish as integers.

Begin with Omega=[N], a linear interval constraint, and apply (T6) followed
by (T1) while a<=4/5. Each step adds exactly one polynomial interval
constraint. It preserves Booleanity and cyclic AP exclusion. No arbitrary
intermediate factor is introduced; B-a always uses the current mean.

At t>=epsilon/log N, (T9) implies, uniformly over the run,

    r<=1+D(t)=o(sqrt(log p)),
    log(p/|Omega|)<=log 6+S(t)=o(sqrt(log p)).          (T10)

Thus the product in (T5) is o(log p). At any alleged first failure of
eligibility, the ledger from all preceding valid steps makes (T5) hold
for sufficiently large N, a contradiction. Also
`log|Omega|=log N-o(log N)` and a never decreases, so
`a>=epsilon/log N>=epsilon/(2log|Omega|)`. The finite epoch bound forces
the run to reach a>4/5.

The independently proved mixed-window terminal theorem (M12) now applies.
For explicit domain-wise errors, use tau=1/log p and (T5):

    mu_0>=p^(-1/50), w>=p^(-1/100), r<=log p,
    a<=3/4+1/(8log p)
       +(log p)(2+log p)/(2p^(49/100))
       +(1/2)p^(-12/25)+(5/4)p^(-97/100).              (T11)

Its size condition H>=1 holds for sufficiently large p because
`wp>=p^(99/100)`. The right side is eventually less than 4/5,
contradicting the final density. Thus

    DIRECT-Q-GAIN => r_4(N)=o(N/log N).                 (T12)

The implication is proved, and its structural premise is OPEN.
This argument uses the new terminal proof with its own diagonal and
window losses; it does not borrow a translation-packing statement for
quadratic windows.

## 5. A concrete threshold and exact remaining gap

For a concrete research target take
`R(a)=loglog(e^2/a)` and seek correlation `c_epsilon a^(3/2)R(a)`.
R is bounded below by a positive constant on (0,4/5], so replacing it by
max(1,R) changes only the allowed constant; clipping as above preserves
the lower-bound implication. Summing (T4) using the two halves of the
density epochs, or using the geometric series directly, gives

    D(t)=O_epsilon(t^(-1/2)/R(t)+ell(t)),
    S(t)=O_epsilon(t^(-1/2)/R(t)+ell(t)^2),
    ell(t)=log(2/t).                                   (T13)

For a summation check, epochs with e_j<=sqrt(t) have R>=R(t)/2 for
sufficiently small t, and their reciprocal square roots sum geometrically.
Later epochs contribute O(t^(-1/4)ell(t)), absorbed by the leading term.
The additive log size terms give the displayed ell(t)^2. Constants may
depend on epsilon through c_epsilon, never on p or the generators.

At t=epsilon/log N, L=log N, this is

    rank=O_epsilon(sqrt(L)/loglog L+log L),
    log-size loss=O_epsilon(sqrt(L)/loglog L+(log L)^2),
    rank times log-size loss=o(L).                    (T14)

The new squared threshold is a^3R(a)^2, and the required gain over an
available squared signal a^4 is a^(-1)R(a)^2. At a=epsilon/log N this is
of order `epsilon^(-1)log N [logloglog N]^2`, still divergent. This removes
the extra factor ell(a) from the preceding product-budget threshold on
the SAME host domain. There is no claim of an unconditional correlation.

More generally (T6) shows that no particular logarithmic multiplier is
forced by this ledger: any uniform divergent improvement over a^(3/2)
is sufficient. An amplitude only c a^(3/2) gives the upper bounds
D,S=O(t^(-1/2)), whose product is O(t^(-1)); without suitably strong
constants these estimates do not establish the small-o target. This is
a limitation of the available bounds, not a proof that every endpoint
iteration or counting method must fail.

## 6. Relation to the weighted residual attack

On the reachable windows (T10), choose tau=a^2/log p for the weighted
count. The original first-residual estimate and the new near-positive
pair theorem give

    R_1^F=o(a^4w mu), R_2^F>=-o(a^4w mu).

For AP-free A, the remaining cancellation therefore lies in R_3^F+R_4^F.
Under failure of the concrete phase threshold c_epsilon a^(3/2)R(a),
prove the one-sided inequality (P12) in
`WEIGHTED_PAIR_REDUCTION_20261016.md`, or obtain the correlation directly.
Both are OPEN. Generic pair PSD has been replaced by a proved arithmetic
near-positivity bound; the quartic obstruction has not been removed.

## 7. Verification scope

The verifier tests exact discrepancies, density gains, small/large jump
classification, direct size-loss inequalities, and complete synthetic
finite trajectories. Such trajectories check the ledger algebra only;
they do not construct phase correlations or actual asymptotic AP-free
examples. The first-principles proofs above establish the conditional
statements. Historical proofs and outputs remain unchanged.
