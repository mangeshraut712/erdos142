# Route J: quantified failure of product-shell constructions

2 October 2026. Offline derivation. Status: **PROVED auxiliary construction
obstructions; no counterexample and no proof of the r4 target.** No claim of
literature novelty is made. These estimates exclude classes of constructions;
they do not assert anything about arbitrary AP-free sets.

## 1. Arbitrary full-product Freiman images of quadratic shells

Let Q = D_1 x ... x D_r, where D_i is a finite subset of R and
m_i = |D_i| >= 2. Suppose phi: Q -> Z_p is a Freiman-2 isomorphism:

    phi(u)+phi(v)=phi(w)+phi(z) iff u+v=w+z,  for u,v,w,z in Q.

In particular phi is injective. Let A be the image of a subset of Q contained
in the union of K level sets of positive-definite real quadratic polynomials.
The polynomials may differ between the level sets. Write L=log p and
c0=log(3/2). Then

    |A|/p <= 2 K exp(-min{L/2, sqrt(2 c0 L)}).                 (1)

This includes arbitrary generic Freiman embeddings, arbitrary prime padding,
unequal alphabet sizes, and ordinary no-carry sphere embeddings.

### Proof

Freiman preservation makes phi(u)-phi(v) depend only on u-v: two
representations of a difference give u+v'=u'+v. The inverse implication
makes the resulting map on Q-Q injective. Consequently

    p >= |Q-Q| = product_i |D_i-D_i| >= product_i (2m_i-1).   (2)

For completeness, an ordered real set d_1<...<d_m has the 2m-1 distinct
differences 0, d_j-d_1, d_1-d_j (j=2,...,m).

Choose a coordinate with m_max=max_i m_i. Holding all other coordinates
fixed, a positive-definite quadratic polynomial is a quadratic polynomial
in this coordinate with positive leading coefficient. A level equation has
at most two real roots. Every level set therefore has at most
2 |Q|/m_max points, and

    alpha=|A|/p <= 2K exp(S-L)/m_max,
    S=sum_i log m_i.                                        (3)

Since (2m_i-1)/m_i >= 3/2, (2) gives L-S>=c0 r. Also
log m_max>=S/r. Put beta=L-S+log m_max.
If S<=L/2, beta>=L/2. If S>L/2, then

    beta >= c0 r + S/r >= 2sqrt(c0 S) > sqrt(2c0 L).

Thus beta>=min{L/2,sqrt(2c0 L)}, proving (1). No asymptotic approximation,
local limit theorem, or inverse theorem is used.

### AP-freeness and limitations

A *single* strictly convex quadratic level set is 3AP-free in real space:
for distinct u,w and v=(u+w)/2,

    (Q(u)+Q(w))/2 - Q(v) = (u-w)^T H (u-w)/4 > 0

for Q(x)=x^T H x+b^T x+c, H positive definite. Its Freiman-2 image is
3AP-free in Z_p, hence 4AP-free. The union of K shells need not be AP-free;
(1) holds regardless, so it is an upper bound even before that additional
requirement is imposed.

Crucially, phi must be an isomorphism on the *full product Q*. An
isomorphism specified only on the shell need not give (2), so (1) does
not exclude compression maps defined only on A.

### Consequence at the requested density

If alpha>=c/log p for fixed c>0, then necessarily

    K >= [c/(2 log p)] exp(min{(log p)/2,
                              sqrt(2log(3/2) log p)}).        (4)

For large p this grows faster than every fixed power of log p. Therefore
even polylog(p)-many quadratic shells, with arbitrary full-product Freiman
embedding, cannot achieve the density requested in Route J. This is stronger
than merely observing that a particular chosen Behrend parameter sequence
is sparse. It says optimizing alphabet sizes, dimension, generic embedding,
and prime padding simultaneously cannot fix this class of constructions.

It does not prove the target and does not exclude nonlinear AP-preserving
embeddings defined only on a selected subset, or nonquadratic coding sets.

## 2. Small alphabets and coding subsets

Suppose Q={0,1,2}^r and phi is a full-product Freiman-2 isomorphism. The
whole box is 4AP-free in integer space: a coordinate with nonzero integer
step cannot stay in an alphabet of size three for four terms. The image
is also 4AP-free: consecutive triple equations lift by Freiman-2, and
nonzero cyclic difference implies distinct lifted points.

Nevertheless p>=5^r by (2), and every subset A of phi(Q) obeys

    |A|/p <= 3^r/p <= p^(-gamma),
    gamma=1-log(3)/log(5)>0.                                (5)

Thus arbitrary coding inside this ternary box cannot reach c/log p.
More generally, alphabets with 2<=m_i<=M fixed give
|phi(Q)|/p <= p^(-gamma_M), where

    gamma_M=min_{2<=m<=M} [1-log(m)/log(2m-1)]>0.

This bound concerns density only; alphabets of size >=4 need a separate
AP-free code.

## 3. CRT/tensor products

Let q_i>=5, G=product_i Z_(q_i), and A=product_i A_i, with each A_i
4AP-free for every nonzero difference. Then A is 4AP-free: any nonzero
vector difference has a nonzero coordinate, which would give a forbidden
coordinate progression. Its density is product_i a_i.

The q_i progressions (x,x+1,x+2,x+3) each miss a point of A_i. Summing
their occupied-point counts yields 4|A_i|<=3q_i. Hence

    a_i<=3/4,  alpha<=exp(-r log(4/3)).                      (6)

For M=product_i q_i and max_i q_i<=Q, r>=log M/log Q, so

    alpha<=exp[-log(4/3) log M/log Q].                       (7)

In particular Q<=(log M)^C for fixed C makes alpha=o(1/log M).
Thus tensoring AP-free sets in bounded or polylogarithmic moduli fails
the requested logarithmic density even before attempting prime transfer.
If some moduli are substantially larger, (7) ceases to exclude logarithmic
density; a genuinely dense AP-free seed is then needed in those moduli.

CRT identifies G with Z_M only when the moduli are pairwise coprime. It
does not identify it with a prime cyclic group. An arbitrary injection
from CRT residues into Z_p does not preserve progression-freeness. A
no-wrap integer transfer requires separate checks and cannot improve
density if p>=M and representatives remain in [0,M).

## 4. Existing symmetric candidate: relative density is insufficient

The checked candidate lives in Omega_r of size 4^r and is embedded with
p>100*16^(2r). Whatever its relative density, |A|<=4^r, so

    alpha_cyclic=|A|/p <=4^r/p,
    alpha_cyclic log p <=4^r log(p)/p ->0.                  (8)

The last limit is uniform over all allowed p: log(t)/t decreases for t>e,
so its maximum occurs at the minimum permitted p. Thus the right side is
at most 64^(-r)(log100+2r log16)/100.

The random-alteration relative density is r^(-3/4+epsilon/2), according
to PARAMETER_AUDIT_20261002.md, correcting the earlier r^(-1/2) heuristic.
Neither value changes (8). Its mixed-factor invisibility remains a sketch;
even a complete proof of it would only refute a hereditary-window energy
claim, not the cyclic target-scale conjecture.

## 5. What random block unions do and do not accomplish

If p is partitioned into disjoint blocks of width h and at most one copy
of an s-point seed is placed in each block, then |A|/p<=s/h (with the
obvious floor correction). Translation randomization cannot improve the
seed density. Cross-block 4APs must additionally be eliminated; internal
AP-freeness of every copy does not eliminate them. No purported complete
construction in this run survives these two checks.

Arbitrary overlapping or variable-width random embeddings are not covered
by this elementary packing observation. No impossibility theorem for all
random embeddings has been proved here.

## 6. Remaining construction question

No set with density c/log p and the required universal low-factor energy
has been constructed. A genuinely new successful construction would have
to bypass at least one of: full-product Freiman preservation, few strictly
convex quadratic shells, bounded/polylog CRT seed moduli, or unchanged
block seed density. Failure of these construction families supplies no
structure-versus-count theorem for arbitrary Boolean AP-free sets.

Verification: route_constructions_checker_20261002.py checks the finite
shell counts, difference cardinality, actual Freiman embeddings and lifted
AP-freeness, and the numerical parameter inequality. These are supporting
checks; the displayed proofs establish the general statements.
