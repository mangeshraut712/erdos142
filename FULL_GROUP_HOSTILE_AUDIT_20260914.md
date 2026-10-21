# Hostile full-group audit of coarse arithmetic energy

14 September 2026. Offline. **(E) OPEN — ONE EXACT REMAINING STATEMENT.**

Neither the full-group ENERGY assertion nor its negation is established.
The target r_4(N)=o(N/log N) remains unproved here. This audit does not
return to general controlled windows. Auxiliary results below have complete
derivations; no literature novelty is claimed.

Write E for the uniform average on Z_p, p>3 prime, B=1_A, a=E B,
f=B-a, and fhat(lambda)=E_x f(x) exp(-2 pi i lambda x/p).
All variances use this probability measure. Quarter arcs are half-open,
equally spaced, and may be rotated independently for each character.
Zero characters can be removed without changing a factor.

## 1. Exact Fourier and discrepancy descriptions

For the nonempty cells V of any factor F, put q_V=|V|/p. Exactly,

    energy(F)=sum_V |E f 1_V|^2/q_V
             =sum_V |sum_lambda fhat(lambda) conj(1_Vhat(lambda))|^2/q_V.
                                                                    (1)

Equivalently, if P_A(V)=|A intersect V|/|A| and P_G(V)=q_V, then

    energy(F)/a^2 = sum_V (P_A(V)-P_G(V))^2/P_G(V).                    (2)

Thus the requested relative energy is exactly a chi-squared discrepancy
between the distributions of the quantized character labels under A and
under the whole group. No lower bound on the smallest cell is assumed.

A grid arc I={b,...,b+L-1} has, for nonzero centered integer m modulo p,

    Ihat(m)=e_p(-mb) (1-e_p(-mL))/(p(1-e_p(-m))),
    |Ihat(m)|<=min(L/p, 1/(2|m|)).                                  (3)

The second inequality follows from sin(pi |m|/p)>=2|m|/p.
For a cell V given by s such coordinate arcs at frequencies xi_i,

    1_Vhat(lambda)=sum_{m_1 xi_1+...+m_s xi_s=lambda}
                       product_i I_i hat(m_i),                    (4)

where all m_i run over Z_p. This is a finite exact convolution, including
collisions and all effects of rotations. Treating (4) as a sparse sum
without controlling its harmonics would be unjustified.

## 2. A quantitative harmonic cutoff without small-cell losses

Let m>=2 be an integer with p>=4m. Define

    Lambda_m(xi)={sum_i t_i xi_i mod p: |t_i|<=2(m-1)},
    M_m=sum_{lambda in Lambda_m} |fhat(lambda)|^2.

For every rank-s quarter-arc factor with these generators,

    energy(F) <= M_m + 48s/m.                                      (5)

In particular |Lambda_m|<=min(p,(4m-3)^s). Rotations do not enter the
frequency set or the error bound.

Proof. On Z_p put D_m(z)=sum_{j=0}^{m-1} e_p(jz). Orthogonality and
2(m-1)<p give

    Z=E_z |D_m(z)|^4=(2m^3+m)/3.

Indeed Z counts pairs of equal sums of two indices; their multiplicities
are 1,2,...,m-1,m,m-1,...,1, whose squares sum to this value. Let rho(z)
be the probability |D_m(z)|^4/(p Z). Its Fourier support is contained in
[-2(m-1),2(m-1)]. For t=|z|_p/p in [0,1/2],

    |D_m(z)|<=min(m,1/(2t)).

With K=floor(p/m)>=3p/(4m), splitting the first moment at K gives

    E_uniform t |D_m|^4
      <=m^4 K(K+1)/p^2 + (p^2/8) sum_{z>K} z^(-3)
      <=m^2+m^3/p+p^2/(16K^2)
      <=49m^2/36.

Here sum_{z>K} z^(-3)<=1/(2K^2) by integration. Consequently
E_rho t<=49/(24m)<3/m.

Let h=E(f|F). On the product grid Z_p^s extend h by assigning its cell
value to each rectangle of coordinate labels; give empty rectangles
the value 0. Every value lies in [-a,1-a]. Smooth this extension with
rho independently in each coordinate and restrict back to
x -> (xi_1 x,...,xi_s x). Call the resulting function h_m.

An integer translation by z changes a quarter-partition label on at most
4|z|_p grid points: each of its four boundaries can cross at most |z|_p
points. Each nonzero xi_i maps a uniform x bijectively onto the grid.
The union bound therefore gives

    delta=E_x |h(x)-h_m(x)| <=12s/m.

The extension has range of length at most one, so this estimate has no
cell denominator, even for singleton or empty cells. Positivity of rho
gives |h_m|<=1, and the product convolution shows supp(h_mhat) subset
Lambda_m. If e=E h^2, then

    E |h_m|^2<=e+2delta,
    e=E f h<=|E f h_m|+delta
      <=sqrt(M_m)*sqrt(e+2delta)+delta
      <=M_m/2+e/2+2delta.

This proves (5). It also covers dependent or repeated frequencies.

For a desired error tau a^2, choose

    m=ceil(48s/(tau a^2)), provided p>=4m.                         (6)

If energy>=eta a^2, take tau=eta/2; (5) forces M_m>=eta a^2/2.
Thus ENERGY forces order-a^2 Fourier mass on a bounded-harmonic span
of O(log(1/a)) generators. This is a NECESSARY conclusion. A converse
with the same quarter-arc rank is not proved: resolving all harmonics
can require additional character quantizations.

This cutoff is of order s/(tau a^2); no claim of optimality among all
possible approximations is made. Under p a^3>=8, s=O(log(1/a)), and
a->0, choosing tau=1/log(2/a) makes p>=4m eventually: 4m/p is at most
24s a log(2/a)+a^3/2, which tends to zero. For finite parameters where
p<4m, (5) is not invoked; including the full Fourier group instead gives
the always-valid but uninformative upper bound a(1-a).

A sufficient counterexample criterion is therefore: for each fixed C,
with s=floor(C log(2/a)) and m as in (6), tau->0, p>=4m, prove

    sup_{xi_1,...,xi_s} sum_{lambda in Lambda_m}|fhat(lambda)|^2=o(a^2).
                                                                    (7)

The cruder sufficient condition (4m-3)^s max_{lambda!=0}|fhat(lambda)|^2
=o(a^2) follows, but can be much stronger than necessary.

There is an additional warning about interpreting the frequency span.
Put H=2(m-1). The two generators 1 and 2H+1, with coefficients in
[-H,H], generate every integer in a consecutive interval of length
(2H+1)^2. If that length is at least p, their span modulo p is the
whole group. Then its Fourier mass is a(1-a) for EVERY indicator.
Near p of order a^(-3), the harmonic cutoff (6) already has H^2>p.
Thus the necessary concentration conclusion can be vacuous, and the
uniform sufficient condition (7) can be impossible even for otherwise
promising sets. It is not an equivalence to quarter-factor energy.

## 3. Ordinary Fourier information is quantitatively insufficient so far

For any nonzero xi, some rotated one-character quarter factor has

    energy >= (4/pi^2)|fhat(xi)|^2.                              (8)

For completeness, put c(t)=E f(x)1_[t,t+1/4)(xi x/p), t uniform on
the circle. Its two continuous Fourier coefficients at harmonics +1,-1
have total squared magnitude |fhat(xi)|^2/pi^2, by integration of the
quarter interval. Parseval gives this lower bound on integral |c(t)|^2.
For each t, the partition into that arc and its complement is coarser
than the quarter factor, and has energy |c(t)|^2/[q_t(1-q_t)]>=4|c(t)|^2.
The arcs are nonempty and proper for p>3. Averaging proves (8).

If A is 3-AP-free, Fourier expansion of its 3-AP count gives

    a/p=a^3+sum_{xi!=0} Bhat(xi)^2 Bhat(-2xi).

With R=max_{xi!=0}|fhat(xi)|, Parseval bounds the last sum in magnitude
by R a(1-a). Hence under p a^3>=8,

    R >=(a^2-1/p)/(1-a)>=a^2.

This supplies energy at least 4a^4/pi^2, which is o(a^2) as a->0.
It neither proves ENERGY nor rules out (7). Conversely it shows why an
extremely strong maximum-coefficient sufficient condition may be
unattainable for 3-AP-free sets even when a more precise mass condition
could conceivably hold. The 4-AP problem has the additional quadratic
obstruction described in section 8.

## 4. The polynomially sparse range is automatically true

For EVERY subset A of Z_p with 0<a<=4/5 and a<=p^(-1/4), ENERGY
holds with the explicit absolute constants

    eta=1/4, C=3.                                             (SPARSE)

No AP-freeness or density cutoff is needed for this assertion.

Proof. Let t=ceil(log p/log 4). Use the characters
1,4,...,4^(t-1) modulo p, with unrotated quarter arcs. For x in
{0,...,p-1}, the label in coordinate j, starting at j=0, is

    d_j=floor(4^(j+1)x/p)-4 floor(4^j x/p).

These are precisely the first t base-four digits of x/p. Their joint
value determines floor(4^t x/p). Since 4^t>=p, these integers are
distinct for distinct x. Thus every factor cell is a singleton, including
the point zero under the half-open convention. All characters are nonzero.

The factor energy is therefore exactly a(1-a)>=a^2/4. Also

    t<=log p/log 4+1
      <=(3/4)log p+3log 2
      <=3log(2/a).

This proves (SPARSE), including the integer rank requirement.

More generally, for any fixed c>0, all a<=p^(-c) have a singleton
factor of rank at most C_c log(2/a), where

    C_c=1/(c log 4)+1/log 2.

It follows that any counterexample family with normalized energy tending
to zero for EVERY fixed C must satisfy

    log(1/a)=o(log p).                                        (20)

Otherwise a subsequence has a<=p^(-c) for some fixed c, contradicting
the singleton factor bound for that fixed C_c. In particular, densities
close to the weak cutoff a=2p^(-1/3) cannot produce the requested family.
Equation (20) still allows both Behrend-scale densities and a of order
1/log p; it does not resolve them.

## 5. Sphere hosts meet the cutoff but are visible to one character

Here is a deterministic family, analyzed rather than asserted to be a
counterexample. For integer d>=16 put q=2^d, D=(2q)^d. Choose the
largest sphere in {0,...,q-1}^d, breaking ties by the smallest squared
radius. There are d(q-1)^2+1 possible radii, so its size k satisfies

    k>=q^(d-2)/d.

Encode in base 2q and choose the least prime p>4D. The checkpoint prime
existence bound gives p<8D. A modular 3-AP among encoded points is an
integer 3-AP because p>4D. There are no carries in the corresponding
digit sums, so its digit vectors satisfy u+w=2v. Equal squared norms
then imply ||u-w||^2=0. The encoded set S is cyclic 3-AP-free.

Writing a=|S|/p, the exact useful estimates are

    1/(8d 2^(3d)) <= a <= 1/(4*2^d),
    p a^3 >= 2^(d^2-8d)/(64d^3) -> infinity,
    a log p -> 0.                                                (9)

Thus these are genuinely eligible sparse full-group examples.
But S is contained in [0,D), inside one quarter arc since p>4D.
For any A contained in a factor-measurable set U of mass b<1,
Cauchy-Schwarz over the cells in U gives

    energy(F) >= a^2(1/b-1).                                    (10)

Proof: sum_{V subset U} (E B1_V)^2/q_V >=a^2/b; subtract a^2.
The same follows by projecting onto {U,U^c}.
Here one quarter grid cell has mass b<=1/4+1/p, yielding

    energy(F)/a^2 >=(3p-4)/(p+4)>=2.

This holds for EVERY nonempty thinning of S, regardless of its new
density or whether that density meets the cutoff. More generally,
containment in an affine half interval gives the lower bound
(p-1)/(p+1) using two adjacent quarter cells. Standard no-wrap sphere
hosts therefore cannot serve as the requested counterexamples.

## 6. Random thinning: complete finite count and the host term

Fix a host S of size K and density beta=K/p. Let A be a uniform k-subset
of S, 1<=k<K, theta=k/K, a=k/p. For a cell V write v=|V| and t=|S intersect V|.
Then

    E |A intersect V|=theta t,
    Var(|A intersect V|)=k(K-k)t(K-t)/(K^2(K-1)).

Expanding (1) yields the exact identity

    E_A energy_A(F)=theta^2 energy_S(F)
                         +sum_V Var(|A intersect V|)/(p|V|).     (11)

In particular its normalized expectation is at least energy_S(F)/beta^2.
This is an expectation statement, not a claim that every thinning has
that lower bound. For interval-contained hosts, (10) gives the stronger
deterministic obstruction already established above.

For the simultaneous upper bound, all rotations on the p-point grid
are represented by t/(8p), 0<=t<8p: this includes every boundary event
t/(4p) and a point between consecutive events. With at most s nonzero
characters there are at most (s+1)(8p^2)^s factors. The total number of
(factor,cell) pairs is at most

    T=(s+1)(32p^2)^s.                                          (12)

Start instead with independent inclusion of each host point with
probability theta=k/K, and put L=ceil(log_2(4T(K+1))). This integer
is at least the natural logarithm of 4T(K+1), and can be computed by
integer bit length. The Bernoulli exponential
bound proved in UNIFORM_ENERGY_COUNTEREXAMPLE.md gives for every cell
with t>0

    Pr(| |A intersect V|-theta t | > sqrt(t L/2))<=2 exp(-L).

Cells with t=0 have zero error. The union bound is at most 1/[2(K+1)].
The total size has its binomial mode at k, with probability at least
1/(K+1). Thus a k-subset satisfying every cell bound exists. Selecting
the lexicographically first such subset gives a deterministic choice.
For its noise Z=1_A-theta 1_S,

    ||E(Z|F)||_2^2 <= (L/(2p)) sum_V |S intersect V|/|V|
                    <=4^s L/(2p).

The triangle inequality therefore proves, simultaneously for all F,

    sqrt(energy_A(F))/a
      <=sqrt(energy_S(F))/beta + sqrt(4^s L/(2p a^2)).             (13)

This completes the union bound without replacing the host by the whole
group. Even its noise term need not vanish uniformly from p a^3>=8
alone: near the cutoff, 4^s/(p a^2) can be of size a^(1-C log 4).
For denser hosts at sufficiently enormous p the noise bound can vanish,
but the host term remains. No equidistributed AP-free host satisfying
the necessary conclusions has been constructed here.

## 7. Affine randomization: exact moments and exact invariance

Let S have k points, V have v points, and choose u!=0 and b uniformly
from Z_p. Set X=|(uS+b) intersect V|. Transitivity on ordered distinct
pairs gives

    E X=kv/p,
    E X(X-1)=k(k-1)v(v-1)/(p(p-1)),
    Var X=k(p-k)v(p-v)/(p^2(p-1)).                              (14)

For a FIXED factor with M nonempty cells, a=k/p,

    E_{u,b} energy_{uS+b}(F)=a(1-a)(M-1)/(p-1).                 (15)

However, if E_s(A) is the supremum over all allowed factors of rank
at most s, there is the exact identity

    E_s(uA+b)=E_s(A).                                         (16)

Pulling back a coordinate xi x/p replaces its frequency by u xi and
its rotation by the original rotation minus xi b/p. This is a bijection
of the allowed factors, and the affine map preserves uniform measure.
Thus no choice among the p(p-1) affine maps can lower this supremum.
For example a sphere host has a fixed-factor mean given by (15), but
EVERY affine image has a rank-one energy witness from (10).
An argument interchanging expectation and the supremum would fail.

## 8. A Boolean quadratic example separates U3 from the required energy

This example is NOT AP-free and is NOT a counterexample to ENERGY.
It demonstrates why the accepted U3 lower bound alone cannot imply it,
including at the target density range.

For primes tending to infinity let L=floor(p/log p), I={0,...,L-1},
and A={x: x^2 mod p is in I}. Put B=1_A and a=E B. Then

    a=L/p+O((1+log p)/sqrt(p)) ~ 1/log p,
    max_{lambda!=0}|fhat(lambda)| <=(1+log p)/sqrt(p).            (17)

The constants in the O term can be taken as one. To prove this, (3)
gives sum_{k!=0}|Ihat(k)|<=1+log p. For L/p<=1/2, it also gives
sum_k |Ihat(k)|<=L/p+1+log((p-1)/2)<=1+log p.
For k!=0, the normalized Gauss sum
E_x e_p(kx^2+lambda x) has magnitude p^(-1/2): square the unnormalized
sum, write x=y+h, and sum e_p(2khy) over y; only h=0 survives.
Expanding I(x^2) proves (17), including the mean error.

For each fixed C take s=floor(C log(2/a)), tau=1/log(2/a), and m from
(6). Then m=O_C((log p)^2(log log p)^2), so p>=4m eventually and

    (4m-3)^s=exp(O_C((log log p)^2))=p^o(1).

Equations (5) and (17) prove, uniformly over all allowed rank-s factors,

    energy(F)/a^2 -> 0.                                      (18)

Yet its quadratic correlation is large. Expanding as above,

    |E f(x)e_p(-x^2)|
      >= |Ihat(1)|-(1+log p)/sqrt(p)-a/sqrt(p),
    |Ihat(1)|=sin(pi L/p)/(p sin(pi/p))>=2L/(pi p).

For all sufficiently large p this is at least a/2. The inequality
|E g|<=||g||_U3 follows by three applications of Cauchy-Schwarz;
quadratic phases have cube derivative one, so multiplying by e_p(-x^2)
does not change U3. Hence ||f||_U3>=a/2, which exceeds a^(3/2)/2.
Also p a^3->infinity. But for L>9 the set contains 0,1,2,3, a
nontrivial 4-AP. This missing hypothesis cannot be dropped or hidden.
No deletion or thinning preserving (18), the density cutoff, and
AP-freeness has been proved.

## 9. Construction attempts and adversarial scope

Random unions of AP-free blocks are not automatically AP-free: cross-block
progressions must also be excluded. A random projection must control
nonzero relation vectors, not merely assert that its original sphere had
no progressions. Neither approach has produced an eligible counterexample
here. Failure of these particular constructions is not a proof of ENERGY.

| Required test | Outcome of this audit |
|---|---|
| No-wrap Behrend/sphere sets | Explicit family (9) meets cutoff and satisfies rank-one energy >=2a^2. |
| Their thinnings | Same support witness applies to every nonempty subset; (11)-(13) retain the host term. |
| Affine-spread sets | Exact invariance (16), not a probabilistic escape. |
| Concentrated support | Bound (10) applies when the support is factor-measurable; no universal assertion for arbitrary supports. |
| Flat Z_13 difference set | Density 4/13 fails p a^3>=8; an arbitrary flat spectrum does not establish an eligible family. |
| Z_101 size-28 witness | p a^3=28^3/101^2<8; identities (1)-(5) still hold when their separate harmonic cutoff holds. |
| AP_RICHNESS_COUNTEREXAMPLE | Its energy conclusion was relative to its special window, not Z_p; its encoded support lies in a quarter arc in Z_p. |
| UNIFORM_ENERGY_COUNTEREXAMPLE | Same change-of-ambient issue and visible short support; not a full-group counterexample. |
| a=epsilon/log p | The quadratic example has this scale but contains APs; no proof or counterexample to ENERGY at this scale. |
| Smaller a with p a^3>=8 | Eligible sphere family explicitly checked; sparse density alone does not destroy ENERGY. |

The entire subrange a<=p^(-1/4) passes ENERGY with eta=1/4,C=3 by
(SPARSE), regardless of which construction produced A.

The proposed alternatives need a logical distinction: proving ENERGY
for every 4-AP-free set and disproving it using 3-AP-free sets are not
exhaustive opposites. It could fail only for 4-AP-free sets that contain
3-APs. No such counterexample has been established either.

No density-range repair is proved or disproved. The restriction
a>=epsilon/log p excludes the sparse sphere family (9), but that family
already satisfies ENERGY and is therefore not a reason for a repair.
The quadratic example (17)-(18) persists at the target density but is
excluded by AP-freeness. It refutes only a proposed implication from
U3 size and density alone.

## 10. One exact remaining statement, confined to the full group

There exist absolute eta,C>0 such that every prime p>3 and every nonempty
4-AP-free A subset Z_p of density p^(-1/4)<a<=4/5 with p a^3>=8 admit at most
floor(C log(2/a)) nonzero frequencies and rotated quarter arcs whose
nonempty joint cells satisfy

    sum_V ((|A intersect V|/|A|)-(|V|/p))^2/(|V|/p) >= eta.     (19)

Together with (SPARSE), this is equivalent to the original full-group
assertion: take the maximum of its C and 3, and the minimum of its eta
and 1/4. It is NOT established by the necessary Fourier condition (5). The additional
content of this audit is a quantified test of that assertion and several
rigorous exclusions of proposed proof/counterexample shortcuts.
The full-group assertion alone would not license iteration inside its
cells: those are general windows, requiring a further theorem. No such
extension or iteration has been attempted in this full-group audit.

## 11. Verification and continuation

Run `python3 verify_full_group_hostile_20260914.py`. Exact rational checks cover
base-four point encodings, factor energies, support bounds, affine
moments/invariance, and fixed-size thinning. Rank comparisons involving
logarithms and the separately labelled Fourier/kernel diagnostics use
floating point. Fourier comparisons use tolerance 2e-10, with 1e-7 for
the unnormalized fourth-moment sum. None is an asymptotic proof.

Next research prompt:

> Work offline only in Z_p. Prove or refute (19) in FULL_GROUP_HOSTILE_AUDIT_20260914.md,
> now restricted to p^(-1/4)<a<=4/5. The smaller-density range is already
> proved with eta=1/4,C=3 by the base-four singleton factor. A counterexample
> family invisible for every fixed C must have log(1/a)=o(log p).
> Use the exact chi-squared interpretation (2), the proved bound
> energy<=sum_{Lambda_m}|fhat|^2+48s/m for p>=4m, and the explicit choice
> m=ceil(48s/(tau a^2)). Do not reverse this necessary Fourier implication
> without proving a converse. No-wrap sphere hosts and all their thinnings
> have a rank-one support witness; affine images preserve the full supremum
> exactly. Any random-host construction must handle host discrepancy and
> cross-block progressions explicitly. The quadratic Boolean family in
> section 8 is linearly invisible at density ~1/log p and has large U3,
> but contains 0,1,2,3. Either use actual 4-AP exclusion to rule out such
> invisibility, or construct an AP-free family retaining it and p a^3>=8.
> If a counterexample is sparse, test a>=epsilon/log p separately. Do not
> return to general windows or claim the target from a full-group result
> alone. Provide a complete proof or exactly identify the remaining gap.
