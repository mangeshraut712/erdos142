<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Independent frontier audit: conversion, smoothing, and iteration

Date: 2026-09-06. Scope: `RELATIVE_WINDOWS.md` sections 10–14, formulas
(25)–(33), and their proof dependencies in `SIGNED_RESEARCH.md` sections
5–8 and 13. This is an offline proof audit. No original research files were
edited. No novelty claim or final asymptotic theorem is established here.

## Verdict

The central displayed formulas (25)–(33) are **PROVED** under their stated
hypotheses and the earlier window geometry/counting inputs. The proposed
cheap smoothing and successful hybrid iteration are **CONDITIONAL / NOT
ESTABLISHED**, as the document itself acknowledges. No central displayed
formula in this lane was found false.

Three scope qualifications should remain explicit:

1. The high-signal reduction is for a globally balanced cyclic set. It is
   not a theorem for an arbitrary window-relative Fourier coefficient.
2. The relative low-Sigma signal requires stable Phi (or entry into that
   branch of the three-way theorem). A Sigma deficit alone is not the
   proof's hypothesis.
3. Equation (33) protects the actual AP baseline when discarded measure
   is small **relative to that baseline**. Absolute smallness of the
   discarded fraction is insufficient when the baseline is itself tiny.

The exact endpoint calculation below gives a sharp scalar obstruction to
obtaining an `o(1/alpha_0)` loss from the joint gain/size inequality alone.
It is an admissible numerical trajectory, not a construction of actual
AP-free windows. A stronger near-full-mass premise would pass the scale
test, but no theorem establishing that premise on every relevant branch
has been proved.

## Status table

| Statement | Classification | Conditions / qualifications |
|---|---|---|
| (25), high-signal prime-first reduction | PROVED | Globally balanced cyclic set; an explicit sufficient cutoff is prime `p >= 102400` |
| (26), capped first-Fourier-coefficient extremum | PROVED | `0 <= F <= D`, mean `alpha`, so necessarily `D >= alpha` |
| Fixed threshold greater than `2/pi` | PROVED | Constants and large-prime cutoff depend on the fixed threshold |
| High-signal total cost | PROVED | Bounds the cost of those steps; other interleaved operations need separate scale/cutoff accounting |
| (27), phase-block conversion | PROVED | Positive integers `q,L`, `qL <= N`; a useful positive gain needs `eta > 2 alpha rho` |
| (28), square-root-length conversion | PROVED | The signed checkpoint proves the large-size case; the stated singleton fallback covers the rest |
| (29), unrolled lower guarantee for log length | PROVED | Uniform `eta_j >= c alpha_j^2`; it is a lower guarantee, not an upper bound on actual surviving lengths |
| Repeated cubic branch is not ruled out | PROVED limitation | 3-AP-freeness is hereditary; this is not proof of an infinite trajectory |
| (30), smoothed convolution separator | PROVED conditional implication | Self-adjoint mean-preserving averaging and the displayed approximation hypothesis are required |
| Clipping dichotomy | PROVED | Fixed `K>1`; large coefficient or bounded separator, without a smoothing theorem |
| Quadratic-residue hostile example | PROVED | Outside the AP-free class; refutes only the relaxed inference |
| Paraboloid formulas and smoothing obstruction | PROVED | Ambient group is `F_q^3`, `q = 3 mod 4`; outside the prime-cyclic target class |
| (31), fixed-rank mass/size telescope | PROVED | Fixed `d` and fixed `K`; cannot be used with growing rank as a fixed constant |
| (32), holes/terminal criterion | PROVED | Uses the earlier baseline `C >= w^2 / 3^d`; strict size threshold is retained |
| Same-rank asymptotic bootstrap | PROVED conditional branch analysis | Applies if only that alternative is encountered and the explicit size conditions continue to hold |
| Rank-dependent stalling model | PROVED numerical model | Small starting density; not a sequence of actual windows |
| (33), baseline under deletion | PROVED | `0 <= r < 1`; its right side may be negative and then gives no information |
| Complete hybrid iteration / ultimate bound | NOT ESTABLISHED | Low-signal rank/complexity and mixed-branch conversion remain unresolved |

## 1. High-signal prime-first conversion

Let `n = floor(p/100)`. A prime `n < q < 2n` satisfies
`p/100 < q < p/50`: the lower inequality follows because the integer q is
at least `n+1`. Put `L=(q-1)/2`, so `rho=L/p<1/100`.

Apart from finitely many boundary parameters, a phase arc of width `L/p`
contains exactly L points of the cyclic grid. Its density function F has
mean alpha and first Fourier coefficient of magnitude
`|fhat(xi)| sinc(pi rho)`. This uses the continuous arc parameter, not an
unsupported assertion that different arcs are independent.

For (26), select the top cosine arc E of measure `alpha/D` after orienting
the first coefficient. With `lambda=cos(pi alpha/D)`, the pointwise
inequality `(F-D 1_E)(cos-lambda) <= 0` integrates to the stated bound.
The derivative of `D sin(pi alpha/D)/pi` is nonnegative because
`sin t-t cos t >= 0` for `0 <= t <= pi`.

The rational margin in the document is valid:

`(3/4)sinc(pi/100) > 17997/24000 > 2319/3100 > sinc(5pi/12)`.

The lower sinc estimate follows already from `pi^2<10`. The upper one
uses `sin(5pi/12)<773/800` and `5pi/12>31/24`. Thus an arc has density
greater than `12 alpha/5`. Pulling back its cyclic progression and then
embedding in `Z_q`, where `q=2L+1`, creates no new progression: each
integer second difference has magnitude at most `2(L-1)<q`.
The new density is greater than
`(6/5)(1-1/q) alpha >= 11 alpha/10` for `q>=12`.

An explicit sufficient cutoff can be supplied from the checkpoint's own
elementary prime proof. Its contradictory binomial inequality has log gap

`h(n) = (n/3) log 4 - sqrt(2n) log(2n) - log(2n+1)`.

For `n=1024`, `log 4>1.38`, `sqrt(2048)<46`, `log(2048)<7.7`, and
`log(2049)<8` give `h(1024)>0`. Also

`h'(n)=log(4)/3 - [log(2n)+2]/sqrt(2n) - 2/(2n+1)>0`

for every `n>=1024`: both subtracted terms decrease there and their sum
at 1024 is below `9.7/45+1/1000 < 0.217`, while `log(4)/3>0.46`.
Hence the proof supplies a prime in `(n,2n)` for all `n>=1024`.
Prime `p>=102400` is therefore a sufficient finite cutoff for (25).

The high-signal step count is bounded by `log(1/alpha_0)/log(11/10)`
up to harmless integer rounding. Its own accumulated log scale loss is
at most that count times `log 100`. With only these reductions, the
remaining prime exceeds the original prime divided by a fixed power of
`log p_0`, and the cutoff eventually persists. When other steps are
interleaved, their losses cannot be omitted from that last assertion.

For any fixed relative threshold `h>2/pi`, choose `D/alpha>2` sufficiently
close to 2 that `sinc(pi alpha/D)<h`, then choose the fixed arc width small
enough to preserve the strict margin. A sufficiently large q absorbs the
factor `1-1/q`. This proves the final generalization in section 10.

## 2. Native phase conversion and exact quadratic recurrence

For (27), every residue chain has length at least L because `qL<=N`.
It can be partitioned into blocks of lengths L through `2L-1`. Their
phase oscillation is at most `rho=4pi L ||q theta||`. The approximation
cost against f is at most `rho E|f| <= 2 alpha rho`.

Writing block weights as mu, block means as m, and unit block phases as z,
the identity `sum mu m=0` and `M=max m>=0` imply

`|sum mu m z| <= M |sum mu z| + sum mu (M-m)`
`                 = M (1+|sum mu z|)`.

The block phase mean differs from the original phase mean by at most rho.
This proves (27), including its denominator. For a nonconstant exact
phase `theta=b/q` with `q|N`, the full residue-chain partition has zero
phase mean and no phase approximation error, giving gain at least eta.

The checkpoint's Dirichlet proof of (28) is sound. Its choices
`Q=floor(sqrt(alpha N/eta))` and
`L=floor(eta Q/(32 pi alpha))` give phase error at most `eta/(8 alpha)`.
The stated cutoff ensures both floors lose at most a factor 2 and that
the chains are long enough. The singleton fallback is valid because
`eta <= E|f| = 2 alpha(1-alpha)`, so `1-alpha >= 3 eta/8`.

For `eta_j>=c alpha_j^2`, the length guarantee gives exactly

`L_(j+1) >= L_j/2 - C_0 - (1/2)log(1/(c alpha_0))`,

and geometric summation proves (29). At
`alpha_0=epsilon/log N_0`, its useful lower bound is exhausted after
`O(log log N_0)` iterations. This statement is about the guarantee only.

For comparison, let `k=3c/8` and take the allowed minimal recurrence

`a_(j+1)=a_j+k a_j^2`,  `u_j=1/a_j`.

Then the reciprocal recurrence is exact:

`u_j-u_(j+1)=k/(1+k a_j)`.

Until a fixed density `a_*` is reached, the decrement lies between
`k/(1+k a_*)` and k. The number of steps is therefore bounded above and
below by constant multiples of `1/a_0-1/a_*`, with integer rounding.
For `j k a_0<1`, the inequality `u_j>=u_0-kj` gives

`a_j/a_0 - 1 <= (k j a_0)/(1-k j a_0)`.

This proves the claimed `O(log log N/log N)` relative change during the
number of steps supported by the native guarantee, for fixed epsilon,c.

If A is 3-AP-free then `T=alpha/p-alpha^3` exactly and

`M=alpha^4+alpha(1-2alpha)/p`.

Thus the usual `p alpha^3>=2` cutoff makes M positive. Restrictions,
progression pullbacks, and safe embeddings preserve 3-AP-freeness. No
scarcity-depletion bound forces this cubic subcase to disappear.

## 3. Smoothing, clipping, and the paraboloid

For (30), the approximation assumption gives
`<Sf,G>=<f,SG> <= -tau/2`. The mean of `H=Sf` is zero. If
`Delta=max H`, then `Delta-H>=0`, and

`-<H,G> = <Delta-H,G>-Delta alpha^2`
`         <= Delta (||G||_infinity-alpha^2)`.

The denominator is positive whenever the negative correlation hypothesis
holds. Therefore (30) is proved. Existence of a sufficiently cheap S is
a separate, unproved premise.

For clipping, Parseval gives
`v=E(G-alpha^2)^2=sum_(xi!=0)|fhat(xi)|^4 <= R^2 b`,
where `b=alpha(1-alpha)`. Apply `(u-c)_+<=u^2/(4c)` with
`u=G-alpha^2`, `c=(K-1)alpha^2`. Because `f>=-alpha`, subtracting the
clipped tail gives the stated negative correlation. Under the variance
condition, `G_K/(K alpha^2)` is a function in `[0,1]` with correlation
at most `-c alpha/(2K)`. If the condition fails, then

`R > sqrt(2c(K-1)/(1-alpha)) alpha^(3/2)`.

Neither conclusion bounds arithmetic smoothing complexity.

For quadratic residues in `Z_29`, the standard elementary quadratic Gauss
calculation gives `R=(sqrt(29)+1)/58 < 3 alpha/4`. The residues contain
`1,5,9,13`, and symmetry gives `G(0)=alpha`. This is a valid counterexample
to the relaxed inference only; it is explicitly outside the AP-free class.

The paraboloid calculation is consistent in every normalization. In
`F_q^3`, `q=3 mod 4`, a midpoint equation forces a sum of two squares to
vanish; anisotropy makes the progression trivial. Completing squares
gives the displayed Fourier coefficients. Consequently

`G=alpha^2-alpha^2 f`, `T=-alpha^2 b`, `R=alpha^2`.

The autocorrelation of f is b at zero, zero at nonzero spatial shifts,
and `-alpha^2` at nonzero vertical shifts. For `S=mu*`, the paired
approximation in (30) requires `<f,Sf> >= b/2`, while those correlations
give `<f,Sf> <= mu(0)b`. Hence `mu(0)>=1/2`; a uniform progression of
distinct points has at most two points. The ambient size is `q^3`, so
`|G_ambient| alpha^3=1`. This is not a prime-cyclic counterexample and is
outside the target's large-cutoff regime.

## 4. Fixed rank, actual baseline, and finite cutoffs

At fixed d, K is fixed, the density multiplies by at least `1+beta_d`,
and each step retains A-mass at least `kappa_d`. The exact identity

`log(n_0/n_J)=log(a_J/a_0)+sum log(1/kappa_j)`

proves (31). A conservative sufficient bootstrap condition is

`n_0 a_0^E >= max(K, 8*3^d*a_0^(-3))`,
`E=1+log(1/kappa_d)/log(1+beta_d)`.

It guarantees the theorem's size hypotheses at all such steps. For fixed
d and `a_0=epsilon/log N`, this holds asymptotically when `n_0` is
comparable to N. It is not automatic at arbitrary finite N.

Deleting one point destroys at most n progressions in each of its four
possible positions. This proves (32). If
`a>=1-1/(8*3^d)` and `n>2*3^d`, its lower bound is at least
`n^2/(2*3^d*p^2) > n/p^2 >= a n/p^2`, strictly above the diagonal.

On a refined window of a 3-AP-free set, `Sigma=aw/p` still holds. Thus

`Sigma/(a^3 C) <= 3^d/(a^2 n) <= a/8`

under the stated cutoff. Counting missing 3-APs does not produce a
decreasing branch budget: the property remains exact after restriction.

The numerical stalling model has the exact reciprocal update
`u_(d+1)=u_d-1/(64*3^d)`. Its total decrement from rank d_0 is
`3^(1-d_0)/128`. For a sufficiently small starting density, it never
reaches density one. It is only a model of the guarantees; setting
`A(W)=1` optimistically is not a claim that such actual windows exist.

Equation (33) is a valid application of the same holes bound. For example,
if `0<r<=beta_W/6`, then it ensures `beta_(W')>beta_W/3`. Without a
comparison between r and beta_W, the informal word "tiny" is insufficient.
Preserving this baseline still does not control `A(W)` or quantile costs.

## 5. Exact endpoint bookkeeping and the remaining potential

Suppose a repeatable refinement satisfies

`mu_j (a_(j+1)-a_j) >= kappa a_j^2`,

and let `r_j=mu_j a_(j+1)/a_j<=1` be its retained A-mass fraction. Put
`u_j=1/a_j` and `delta_u_j=u_j-u_(j+1)`. Exactly,

`r_j delta_u_j = mu_j (a_(j+1)-a_j)/a_j^2 >= kappa`.

In particular `delta_u_j>=kappa`, and

`log(1/r_j) <= log(delta_u_j/kappa) <= delta_u_j/(e kappa)`.

The second inequality is `log t/t<=1/e`. Therefore

`log(n_0/n_J) <= log(a_J/a_0)+(u_0-u_J)/(e kappa)`.

This scalar bound is sharp: as long as `e kappa a_j<1`, take

`delta_u_j=e kappa`, `r_j=1/e`,
`a_(j+1)=a_j/(1-e kappa a_j)`,
`mu_j=(1/e)(1-e kappa a_j)`.

All joint inequalities are equalities and the scale bound is attained.
Reaching a fixed density uses order `1/a_0` steps and log scale loss.
At `a_0=epsilon/log n_0`, the leading permitted loss is
`(e kappa epsilon)^(-1) log n_0`. Thus the joint inequality alone cannot
supply an `o(log n_0)` guarantee. This is not a construction of actual sets.

A stronger premise would change the answer. If each step additionally
retained `r_j>=exp(-K a_j)` and had gain at least `kappa a_j^2`, then

`log(a_(j+1)/a_j) >= log(1+kappa a_j)`
`                       >= kappa a_j/(1+kappa)`.

Summing gives the exact bound

`sum a_j <= ((1+kappa)/kappa) log(a_J/a_0)`.

The mass/size identity would then imply

`log(n_0/n_J) <= [1+K(1+kappa)/kappa] log(a_J/a_0)`.

This is `O(log(1/a_0))`, and so passes the scale test at the target
density. A direct scale-loss bound `log(1/mu_j)<=K a_j` would also pass.
Neither condition follows from the current joint inequality. The signed
checkpoint already rejects its proposed universal mass-retaining
integer-progression premise; a suitable theorem on the present windows
remains unproved. No actual charging potential covering rank growth,
Fourier algebra norm, and the mixed branch has been supplied.

## Verification and limits

This lane checked proofs and exact algebra, not just finite checkers.
The original files were read without modification. An independent
deterministic arithmetic check of the rational prime-first margin and
the reciprocal identities accompanies report verification in the task
output. Computational checks are corroboration, not proofs of the
unproved smoothing or hybrid premises. The final asymptotic target is
neither proved nor disproved by these statements.
