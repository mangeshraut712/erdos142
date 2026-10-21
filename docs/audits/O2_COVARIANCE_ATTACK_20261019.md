# Booleanity and small chirps do not suffice for W8, even at logarithmic density

19 October 2026. Offline. **PROVED auxiliary obstruction.** This is NOT
a counterexample to (P12), DIRECT-Q-GAIN, or the local target: the sets
below deliberately contain a nonzero-difference 4-AP. The construction
does satisfy Booleanity, the logarithmic density lower bound, the product
domain, an actual initial interval host, the original prescribed tent
weight, and negligible diagonal error. Thus AP exclusion is essential
to any proof of W8 from Boolean chirp identities. No literature novelty
is asserted.

## 1. Statement with the original weight and cubic term

For every sufficiently large prime p there are an interval

    Omega={0,...,n-1}, n=floor(p/4), w=n/p,

and an actual Boolean set `A subset Omega` such that, with

    L=log p, a=|A|/n, P=1_Omega, u=1_A-aP,
    delta=max_(c,b)!=(0,0)|E_Omega(1_A-a)e_p(-cx^2-bx)|,
    H=floor(n a^2/(48L)),
    f_H(h)=max(0,1-|h|_p/(H+1)), F(x,h)=f_H(h),
    mu=(H+1)/p,

one has

    a~1/L, delta=o(a^(3/2)),
    R_3^F+R_4^F <= (-11/20+o(1))a^4 w mu
                        < -(1/2)a^4 w mu.                (C19.1)

Every residual is from the literal expansion at `aP`, with the same F.
In particular the cubic term is retained. By the exact W7--W8 identity
in `WEIGHTED_QUARTIC_COVARIANCE_20261018.md`, W8 fails for these sets.
The construction includes `{0,1,2,3}` in A, explicitly violating AP
exclusion. These examples therefore lie outside the hypothesis of P12.

For sufficiently large p, all of the following other conditions hold:

* `a>=1/(2log|Omega|)` and `a<=4/5`;
* the rank-one presentation of this interval satisfies (T5);
* `3n<p<6n`, so Omega is an actual translated initial interval host;
* `H>=1`, `2H<p`, and `pa^3mu->infinity`.

The last condition means the Boolean diagonal `aw/p` is negligible
relative to `a^4wmu`. The obstruction therefore goes beyond the
polynomial-density examples, which failed that diagonal condition.

## 2. A finite arithmetic mask

Let q=101 and

    S={0,1,4,6,7,9,12,14,20,26,34,35,37,38,41,
       42,49,55,57,66,76,77,80,82,83,85,87,96,98}.

This is a nonzero-difference cyclically 4-AP-free subset of F_101, of
size 29. An exhaustive check of its 101*100 ordered nonzero progressions
is included in the verifier; the list also appeared in the saved finite
diagnostics. Put

    b=29/101,
    rho=1/(q b^3)=101^2/29^3=10201/24389 < 9/20 < 1/2. (C19.2)

The assertion about S is a finite checkable lemma, not an asymptotic
existence assumption. Uniform random translation of S contains any
specified residue with probability b. Four residues in an arithmetic
progression are all contained with probability b if the difference is
zero modulo q, and with probability zero otherwise.

## 3. Random block translations and independent thinning

Set `t=1/L` and `K=ceil(L^(5/2))`. For all sufficiently large p, K<=n.
Partition Omega into K consecutive blocks, whose lengths differ by at
most one; write `m=ceil(n/K)` for their maximum length. Independently
for each block j choose a uniform translation `Z_j in F_q`. Conditional
on these translations, independently include each x in Omega with
probability

    pi_x=(t/b) 1_(x mod q in S+Z_j), x in block j.

The inclusion probability is at most one eventually. Denote this random
Boolean set by B. Every x has unconditional inclusion probability t.
The translations are independent across blocks, and the Bernoulli
thinning is independent across individual vertices conditional on the
translations. Both kinds of randomness are used below.

For every deterministic unit phase chi, the independent block variables

    Y_j=sum_(x in block j)(pi_x-t)chi(x)

are mean zero and obey `|Y_j|<=(t/b)|block j|`. Thus the sum of squared
real or imaginary bounds is at most `(t/b)^2 n m`. The elementary
bounded-variable subgaussian estimate gives, for x>0,

    Prob(|sum_j Y_j|>2(t/b)sqrt(n m x))<=4e^(-x).      (C19.3)

For completeness, a real mean-zero variable Y with |Y|<=M satisfies
`E exp(lambda Y)<=cosh(lambda M)<=exp(lambda^2 M^2/2)` by convexity of
the exponential and the power series of cosh. Multiply these bounds
over the independent blocks and optimize the exponential Markov bound.
Apply the resulting two-sided bound separately to real and imaginary
parts to obtain (C19.3).

Conditional on the translations, the variables `1_B(x)-pi_x` are
independent centered Bernoulli differences, with total variance at most
`nt/b`. The elementary Bernstein proof in
`BOOLEAN_ALTERATION_CHIRP_20261018.md`, applied to their real and
imaginary phase-weighted parts, gives uniformly over the translations

    Prob(|sum_(x in Omega)(1_B(x)-pi_x)chi(x)|
                      >2sqrt(nt x/b)+x)<=4e^(-x).     (C19.4)

Take `x=5L`, and union bound each estimate over all p^2 phases
`chi=e_p(-cy^2-by)`, including the constant phase. With probability at
least `1-8p^(-3)`,

    max_(c,b)|E_Omega(1_B-t)e_p(-cy^2-by)|<=M_p,
    M_p=2(t/b)sqrt(5Lm/n)+2sqrt(5Lt/(bn))+5L/n.       (C19.5)

Let `a_B=|B|/n`. Including the constant phase gives `|a_B-t|<=M_p`.
Centering at this actual density, rather than its expectation, costs
another M_p. Since `m/n=1/K+O(1/n)`,

    M_p=O(L^(-7/4)+n^(-1/2)+L/n),
    M_p/t=O(L^(-3/4))+o(1),
    M_p/t^(3/2)->0.                                 (C19.6)

These estimates are simultaneous over every global quadratic phase.
No claim of independence between different phases is used.

## 4. Weighted count, including block crossings and the diagonal

First fix any deterministic integer H with `1<=H`, `3H<n`, `2H<p`.
Let `mu_H=(H+1)/p` and use the tent f_H. For h=0, the expected
contribution to `Lambda_(f_H)(1_B)` is exactly `tw/p`.

For h!=0, the four vertices are distinct in F_p. If they lie in Omega,
their ordinary integer representatives have a common signed difference
`h in [-H,H]`. When they lie in the same block, translation averaging
and conditional independence of the thinning give

    E product_(i=0)^3 1_B(x+ih)
       =t^4/b^3 if q divides h,
       =0 otherwise.                               (C19.7)

When these four vertices cross a block boundary but remain in Omega,
their conditional inclusion probability is at most `(t/b)^4`.
**This fourth power is retained:** bounding it by one would lose the
required asymptotic error. For each signed h, at most `3K|h|` starting
vertices can cross a boundary. Hence their total expected contribution
is at most

    (t/b)^4 (3KH/p)mu_H.                            (C19.8)

There are at most n eligible starting vertices for every h. For the
weighted multiples of q one has the elementary estimate

    (1/p)sum_(|h|<=H, q divides h) f_H(h)
                     <=mu_H/q+1/p.                  (C19.9)

One way to check (C19.9) is to write `z=(H+1)/q`, `r=z-floor(z)`;
the unnormalized sum equals `z+r(1-r)/z`. Its excess over z is at
most one. The contribution h=0 may be included in this upper bound
even though it was already handled separately, since only an upper
bound is being asserted.

Combining these observations gives the finite, explicit bound

    E Lambda_(f_H)(1_B)
      <=tw/p +(t^4/b^3)w(mu_H/q+1/p)
                  +(t^4/b^4)(3KH/p)mu_H.             (C19.10)

No host or block boundary has been discarded from this estimate.

## 5. The prescribed H depends on the final density

This dependency is handled before choosing the successful realization.
Put `eta=L^(-1/2)` and define deterministic brackets

    a_-=t(1-eta), a_+=t(1+eta),
    H_-=floor(n a_-^2/(48L)),
    H_+=floor(n a_+^2/(48L)), mu_+=(H_++1)/p.

Both H brackets tend to infinity and `H_+/H_-=1+o(1)`.
Also `K H_+/n=O(L^(-1/2))`, so (C19.10) at H_+ gives

    E Lambda_(f_(H_+))(1_B)
                          <=(rho+o(1))t^4wmu_+.     (C19.11)

Indeed the other normalized errors are
`1/(pt^3mu_+)=O(L^6/p)` and `1/(p mu_+)=O(L^3/p)`.

Since rho<9/20, Markov's inequality gives a probability bounded away
from zero that

    Lambda_(f_(H_+))(1_B)<=(9/20)t^4wmu_+.            (C19.12)

Intersect this event with the probability-1-o(1) event (C19.5). Their
intersection is nonempty for all sufficiently large p; independence of
these two events is unnecessary.

Choose such a B and define `A=B union {0,1,2,3}`. This forces a genuine
nonzero-difference 4-AP in the final set. It changes the relative mean
by at most `4/n` and every centered relative phase correlation by at
most `8/n`. Equations (C19.5)--(C19.6) therefore imply

    a~t, delta<=2M_p+8/n=o(a^(3/2)),
    a_-<=a<=a_+                                      (C19.13)

eventually: `M_p+4/n=o(eta t)`. Thus the ORIGINAL prescribed H satisfies
`H_-<=H<=H_+`, and `mu/mu_+->1`. The tents increase pointwise with H.

Adding one vertex changes a Boolean weighted 4-AP count by at most
`4mu_+/p`: for each of its four possible slots, the total incident
weight is exactly `mu_+/p` before any other indicators are imposed.
Adding four vertices therefore changes that count by at most
`16mu_+/p=o(t^4wmu_+)`. Using monotonicity of the tents in H and (C19.12),

    Lambda_F(1_A)<=(9/20+o(1))a^4wmu.                (C19.14)

The weight in this conclusion is exactly `H=floor(n a^2/(48L))` for
the final A. The deterministic bracket was only a proof device.

## 6. Literal residuals on the initial interval

For this rank-one linear weight every anchored full-field degree is
exactly mu. Erode Omega by 3H at each end and let bnd denote the density
removed, so `bnd<=6H/p`. If an occupied slot is in the eroded interval,
all four slots lie in Omega whenever F is nonzero. It follows directly
that, with `T=E_(x,h)F product_j P(x+jh)`,

    (w-bnd)mu<=T<=wmu,
    |R_1^F|<=4a^3mu bnd.                            (C19.15)

For each full-field pair form, Fourier expansion gives

    E_(x,h)f_H(h)u(x+ih)u(x+jh)
      =sum_r fhat_H((j-i)r)|uhat(r)|^2>=0,

because the tent has nonnegative Fourier coefficients. Restoring the
two other host indicators changes each pair term by at most mu*bnd.
Therefore

    R_2^F>=-6a^2mu bnd.                             (C19.16)

These statements include the diagonal. The boundary estimates imply

    T=(1+o(1))wmu,
    |R_1^F|/(a^4wmu)<=24H/(an)=O(a/L)=o(1),
    R_2^F/(a^4wmu)>=-36H/(a^2n)>=-3/(4L)=o(1).      (C19.17)

The last notation is a lower error bound tending to zero, not an
assertion that R_2 itself tends to zero on this scale. The exact Boolean
expansion, now without imposing AP exclusion, gives

    R_3^F+R_4^F=Lambda_F(1_A)-a^4T-R_1^F-R_2^F.

Substitute (C19.14) and (C19.17) to obtain (C19.1).

## 7. Interpretation for the covariance attack

Every set here is genuinely Boolean. Consequently all exact Boolean
chirp convolution identities, row constraints, frame constraints, and
the identity `u^2=(1-2a)u+a(1-a)P` hold automatically. Nevertheless its
shifted-chirp covariance violates W8 at the required scale while every
individual global quadratic correlation is `o(a^(3/2))`.

The initial host has `r=1`, `log(p/n)=log 4+o(1)`, and hence satisfies
(T5) for large p. Also

    mu~w a^2/(48L),
    pa^3mu~wp a^5/(48L)~p/(192L^6)->infinity.

Thus the former sparse-example diagonal escape does not explain this
failure. The missing hypothesis is explicit actual AP exclusion. A
successful proof of the requested W8 must exploit that hypothesis in a
way stronger than the count deficit alone: the present sets already
have the weighted count below half the random main term.

This result does not exclude a W8 proof that uses AP exclusion. It does
not construct an eligible AP-free sequence, negate the exact quantifier
statement, or settle the local target.

## 8. Verification scope

`verify_o2_covariance_attack_20261019.py` independently checks the finite
101-residue mask, the translation probabilities, the exact tent-multiple
bound, the crossing count, the expectation estimate, the original
linear-pair positivity, forced-AP insertion cost, and residual expansion.
Its finite geometry examples need not satisfy the asymptotic K, H, or
density prescriptions; they are labeled finite diagnostics. Fourier
sweeps use floating arithmetic, while AP, probability, weighted-count,
and residual checks use exact modular integer/Fraction arithmetic.

The asymptotic conclusion follows from the proof, not from extrapolating
finite correlations. No finite target-domain counterexample is claimed.
