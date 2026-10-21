# Actual Boolean AP-free sets with small quadratic correlations at polynomial density

18 October 2026. Offline. **PROVED domain-separation theorem.**
The local target, DIRECT-Q-GAIN on its stated logarithmic-density domain,
and (P12) remain OPEN. This is an actual arithmetic construction, not an
abstract four-point distribution. It is outside the target density and
diagonal-error regimes and is not a counterexample to either open claim.

## 1. Statement

Fix a real number `theta` with `2/5<theta<1/2`. For every sufficiently
large prime p there is a nonzero-difference cyclically 4-AP-free Boolean
set `A subset F_p` whose density a and maximal centered quadratic phase
correlation satisfy

    a=(1+o(1))p^(-theta),
    delta=max_(c,b)!=(0,0) |E_x (1_A(x)-a)e_p(-cx^2-bx)|,
    delta/a^(3/2) -> 0.                                      (B1)

The error bounds are uniform over all p^2 quadratic/linear phase
coefficients. The threshold on p and the asymptotic constants can depend
on theta. Constant terms in the phase only change a unit scalar and do
not affect delta. A quantitative upper bound is

    delta/a^(3/2)
       =O_theta(p^(theta-1/2)sqrt(log p)
                 +p^(-1+3theta/2)log p
                 +p^(1-5theta/2)log p).                      (B2)

All three terms tend to zero in the stated open interval for theta.
For example theta=9/20 makes their power exponents respectively
`-1/20`, `-13/40`, and `-1/8`.

## 2. Elementary simultaneous concentration

Choose a random set B by including each residue independently with
probability `t=p^(-theta)`. Let `X_y=1_B(y)-t`. For any complex numbers
`z_y` of modulus at most one, both real and imaginary parts of `X_y z_y`
are independent, mean-zero real variables of absolute value at most one
and total variance at most `v=pt`.

Here is the concentration estimate used, including its elementary
justification. If independent real mean-zero variables Y_j satisfy
`|Y_j|<=1` and `sum E Y_j^2<=v`, expansion of the exponential and the
inequality `k!>=2*3^(k-2)` for `k>=2` give, for `0<lambda<3`,

    E exp(lambda Y_j)
      <=1+(E Y_j^2)lambda^2/[2(1-lambda/3)],
    log E exp(lambda sum_j Y_j)
      <=v lambda^2/[2(1-lambda/3)].

The same inequality holds after replacing every Y_j by -Y_j. For v>0,
Markov's inequality with `lambda=s/(v+s/3)` therefore gives

    Prob(|sum_j Y_j|>=s)<=2 exp(-s^2/[2(v+s/3)]).       (B3)

The case v=0 is deterministic. If `s=sqrt(2vx)+2x/3`, direct squaring
shows `s^2>=2x(v+s/3)`. Applying (B3) to the real and imaginary parts
shows, for x>0,

    Prob(|sum_y X_y z_y|>2sqrt(pt x)+x)<=4e^(-x).      (B4)

Indeed `sqrt(2)s=2sqrt(pt x)+(2sqrt(2)/3)x` is no larger than the
displayed threshold. No Gauss-sum estimate or independence between
different phases is needed.

Apply (B4) to each of the p^2 choices
`z_y=e_p(-cy^2-by)`, including `(c,b)=(0,0)`. Put

    x_p=5log p,
    L_p=2sqrt(pt x_p)+x_p.

A union bound shows that with probability at least `1-4p^(-3)`,

    max_(c,b)|sum_y (1_B(y)-t)e_p(-cy^2-by)|<=L_p.    (B5)

In particular, for the sampled density `a0=|B|/p`,

    |a0-t|<=L_p/p,
    max_(c,b)|E_y (1_B(y)-a0)e_p(-cy^2-by)|<=2L_p/p. (B6)

The second inequality subtracts `(a0-t)E_y e_p(-cy^2-by)` and uses
the elementary upper bound one for its phase average. Thus centering by
the actual random density is fully accounted for.

## 3. Deletion of all cyclic 4-APs

Let Z be the number of ordered pairs `(x,h)` with `h!=0` and all four
of `x,x+h,x+2h,x+3h` in B. Since p>3, the four vertices are distinct.
Therefore

    E Z=p(p-1)t^4<=p^2t^4,
    Prob(Z>p^2t^4 log p)<=1/log p.                   (B7)

Combining (B5) and (B7), the two desired events hold simultaneously with
probability at least

    1-4p^(-3)-1/log p,

which tends to one and is positive for all sufficiently large p.

Fix a realization satisfying both events. Repeatedly delete one vertex
from a surviving nonzero-difference cyclic 4-AP. This process terminates
in an AP-free set A. Deletions cannot create a new progression, and each
step destroys at least one progression present initially. Consequently
the number d of deleted vertices satisfies

    d<=Z<=p^2t^4 log p.                              (B8)

Every arithmetic progression here is genuinely in F_p; the argument
does not replace it by an abstract pattern distribution.

Write `a=|A|/p=a0-d/p`. Equations (B6) and (B8) yield

    |a-t|<=L_p/p+pt^4 log p,
    |a-t|/t<=2sqrt(x_p/(pt))+x_p/(pt)+pt^3log p=o(1). (B9)

The last conclusion uses theta<1 and theta>1/3, both implied by the
stated range. In particular a is positive and asymptotic to t.

If D is the set of deleted vertices, the difference between centered
indicators is exactly

    (1_A-a)-(1_B-a0)=-1_D+d/p.

Its correlation with every unit phase has magnitude at most `2d/p`.
Thus the final, actual Boolean AP-free set satisfies

    delta<=2L_p/p+2pt^4 log p.                       (B10)

Dividing by `a^(3/2)=(1+o(1))t^(3/2)` proves (B2), and therefore (B1).
There is no unproved concentration estimate after alteration: the entire
effect of deletion is included in the deterministic `2d/p` term.

## 4. Exact scope relative to the open target

This construction rules out an unrestricted global assertion that
Boolean cyclic AP exclusion alone forces even a fixed positive multiple
of `a^(3/2)` in one quadratic phase at every small density. Any assertion
with a divergent multiplier fails on this enlarged class as well.
It does **not** negate DIRECT-Q-GAIN as currently stated.

On the full host `Omega=F_p`, take the rank-one presentation consisting
of a nonzero linear generator and a full circular interval. Then w=1 and
the product-domain inequality (T5) reduces to

    log 48+loglog p<=log p/100,

which holds eventually. However for every fixed epsilon>0,

    a/(epsilon/(2log|Omega|)) ->0.

Thus the construction violates the required density lower bound. In
particular it is not an eligible low-density sequence for the exact
negation characterization in `O2_QUANTIFIERS_CUBIC_BOUND_20261017.md`.

There is also a separate, explicit failure of the weighted diagonal
regime. Use precisely the original rank-one linear weight

    tau=a^2/log p,
    H=floor(pa^2/(48log p)),
    F(x,h)=f(h),
    mu=(H+1)/p.

Because theta<1/2, H tends to infinity and `2H<p` eventually; the weight
is geometrically valid. On the full host `T=E F=mu` exactly, and

    mu=(1+o(1))a^2/(48log p),
    Lambda_F(1_A)=a/p,
    (a/p)/(a^4 mu)=1/(pa^3mu)
                   =(48+o(1))log p/(pa^5) -> infinity. (B11)

The middle equality includes the exact h=0 contribution, with `f(0)=1`;
all nonzero-difference terms vanish because A is AP-free. Thus the
condition `pa^3mu->infinity` needed to deduce (P11) fails in the opposite
direction. P11's main-scale negative cancellation does not follow here.
No violation of (P12) is claimed.

## 5. Comparison with the earlier very sparse random example

The earlier construction in `RESIDUAL_FIELD_AUDIT_20261015.md` used
`t=p^(-3/5)`. More generally, when theta>1/2, the expectation `p^2t^4`
tends to zero, so no alteration is required with probability tending to
one. That sparsity is useful for other Fourier-packet obstructions, but
cannot give (B1).

Indeed every Boolean A of density a obeys the exact linear Parseval
identity

    sum_(b!=0)|E(1_A-a)e_p(-by)|^2=a(1-a).

Since linear phases are among the permitted quadratic phases,

    delta/a^(3/2)
       >=sqrt((1-a)/((p-1)a^2)).                    (B12)

At `a~p^(-theta)` this is asymptotic to `p^(theta-1/2)`. It diverges
when theta>1/2 and stays bounded away from zero at theta=1/2. The present
construction crosses below theta=1/2 by explicitly removing progressions;
the extra condition theta>2/5 ensures that deletion has negligible cost
on the `a^(3/2)` scale. Endpoints are not claimed.

## 6. Verification scope

`verify_boolean_alteration_chirp_20261018.py` constructs reproducible
finite Bernoulli samples, counts ordered cyclic 4-APs using exact modular
integer arithmetic, deletes vertices, and rechecks that no such AP
remains. It evaluates every pair of quadratic/linear phase coefficients
for both the initial and final centered indicators, checks the deletion
stability inequality, and cross-checks selected FFT coefficients by direct
summation. Fourier values are floating-point checks, not exact algebraic
number certifications. Results are written to
`BOOLEAN_ALTERATION_CHIRP_VERIFICATION_20261018.json`.

The recorded run passed **440 checks**, evaluating **16,894,167** chirp
coefficients across primes 127, 257, 521, 1031, and 2053. The largest
FFT/direct-sum discrepancy was `1.4979264390648768e-17`. Three cases
required actual deletion, and all five final sets had exactly zero
nonzero-difference cyclic 4-APs. The original-weight H equals zero in
these small cases and is explicitly reported; they do not verify the
eventual positive-H conclusion. Observed finite correlation ratios are
not asserted to be small or monotone.

Finite cases are diagnostic examples only. They do not verify an
asymptotic decay rate or membership in the logarithmic target domain.
The asymptotic theorem rests on the self-contained probability and
deletion proof above. No literature novelty is asserted.
