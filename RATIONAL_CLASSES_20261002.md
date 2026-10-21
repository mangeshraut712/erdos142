# Orbit form of the Fourier decay, and rational classes

2 October 2026. **(D) NEW RIGOROUS LEMMA plus measurements; candidate still
(E) OPEN.** Continues CELL_BOOKKEEPING_20261002.md section 6, item 1
(aliasing). Notation: box {0,1,2,3}^r, X(u)=sum u_i 16^i, A={u: n(u) in
T}, |T|<=(r+1)^2. The window energy lemma and the target remain unproved
and unrefuted.

## 1. Orbit form of the decay — PROVED

For every real x and every set T of count vectors,

    |E[1_T(n(u)) e(x X(u))]| <= (r+1)^2 exp(-(1/2) sum_{i=0}^{r-2} ||15*16^i x||^2).

Proof. CANDIDATE_LEMMAS section 2 gives the bound
(r+1)^2 exp(-2 min_gamma sum_i d_i^2) with d_i=||16^i x-gamma||. Since
15*16^i x = 16^(i+1)x - 16^i x, we have ||15*16^i x|| <= d_i + d_(i+1), so
sum_{i<=r-2} ||15*16^i x||^2 <= 2 sum_i (d_i^2+d_(i+1)^2) <= 4 sum_i d_i^2.

This removes gamma and the threshold delta: a frequency fails to decay only
if 15x has a sparse base-16 orbit (||15*16^i x|| small for most i). That is
exactly the "mod-15 class plus few-digit junta" structure, now with an
explicit rate. Checked against brute-force minimization over gamma for 300
random x at r=12 (worst ratio 0.63).

## 2. Rational frequencies — PROVED

For odd q and h with q not dividing 15h, every orbit point h*16^i/q has
||15 h 16^i/q|| >= 1/q, so the decay constant

    kappa(h/q) = min_gamma mean_i ||16^i h/q - gamma||^2 >= 1/(4q^2),

and E[1_T e(hX/q)] decays like exp(-c r/q^2). Exact values: the minimum of
kappa over such h is 0.0317 for q=7, 0.0171 for q=13, and (1/34)^2 for
q=17. **The bound 1/(4q^2) is attained at q=17**, by h=8:
16 = -1 mod 17, so 8X/17 is within 1/34 of sigma/2 at every digit, and
this character is a smeared copy of the parity of sigma. Powers of 2 in q
only see the lowest digits (a junta). Consequently the residue X mod q
reveals, beyond juntas, only sigma mod gcd(q,15), with error
exp(-c r/q^2) for every fixed q.

## 3. Measurements (greedy B, not balanced)

Energy of the partition by X mod q, divided by a^2, split into the mod-15
part (h with q | 15h) and the rest. Coefficients are exact (dynamic
program over partial count vectors).

| r | q=7 rest | q=13 rest | q=17 rest | q=51 mod-15 part | q=51 rest |
|---|---:|---:|---:|---:|---:|
| 16 | 1.5e-7 | 9.3e-7 | 0.123 | 0.054 | 0.203 |
| 24 | 3.2e-11 | 4.8e-10 | 0.042 | 0.055 | 0.157 |
| 32 | 5.0e-13 | 6.9e-13 | 0.031 | 0.001 | 0.060 |
| 40 | 4.2e-16 | 3.9e-15 | 0.0028 | 0.142 | 0.035 |

The rest decays in every case, quickly for q=7 and 13 and slowly for
q=17 (the slow parity mode of section 2). The mod-15 part does not decay,
because the greedy B is unbalanced mod 3; that part is handled by the
balance construction, not by decay.

**Caution for finite checks.** Non-exceptional frequencies can have decay
constant as small as order 1/q^2 (or as small as one likes for irrational
x near the exceptional set), so finite computations at r of a few hundred
cannot certify generic decay. The asymptotic statements rest on the
proofs above.

## 4. What this settles and what remains

Settled: the aliasing terms h*phi in a Beurling–Selberg sandwich are
harmless whenever h*phi is a rational with small odd denominator not
dividing 15h, and the exceptional ones are, by section 1, exactly those
with 15h*phi orbit-sparse. They are then handled by the junta-plus-residue
reduction (CELL_BOOKKEEPING section 5).

Remaining (OPEN): bound the coefficient mass of the sandwich polynomials
on frequencies sum_j m_j phi_j (|m_j|<=H) whose 15-multiple is
orbit-sparse but which are not individually reducible. This is the
mixed-factor problem of CELL_BOOKKEEPING section 6, items 2 and 3. Section 1
gives it a clean form: count m in [-H,H]^k with
sum_i ||15*16^i sum_j m_j phi_j||^2 <= polylog(r), weighted by prod 1/(1+|m_j|).

## 5. Checks

`python3 verify_rational_classes_20261002.py` (about 15 seconds) runs:
- the orbit inequality for 300 random x;
- the exact kappa minima, asserting kappa(17)=(1/34)^2 and kappa>=1/(4q^2);
- exact Fourier coefficients for r=16 to 40 and q in {7,13,17,51}, with
  the zero coefficient asserted equal to the density.

Output: rational_classes_verification_20261002.json.
