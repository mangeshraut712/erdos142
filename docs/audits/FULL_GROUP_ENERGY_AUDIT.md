<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Full-group audit of the uniform coarse arithmetic energy theorem

Date: 2026-09-14. Offline. No internet. Python standard library only.

STATUS: (D) NEW RIGOROUS PARTIAL THEOREM

The full-group case Omega = Z_p of the energy theorem is neither proved
nor refuted. What is proved: the theorem is trivially true at the sparse
end of its own cutoff; every eligible Behrend/sphere/digit set, every
affine image, and every random thinning is a trivial YES instance; the
theorem, in the form needed for the iteration, is at least as strong as
a Roth bound r_3(N) <= N exp(-c (log N)^(1/4)); and a much weaker
statement (rank a^(-c), c<1/2, density >= epsilon/log n) already suffices
for the local target. The target r_4(N)=o(N/log N) remains OPEN.
Official Erdős #142 is not addressed. No literature novelty is claimed.

## 0. The statement audited

From ENDPOINT_INCIDENCE_AUDIT.md section 5, specialized to rank r=0,
Omega=Z_p, n=p:

(ENERGY_p) There exist absolute eta>0, C>0 such that for every prime
p>3 and every nonempty 4AP-free A subset Z_p of density a=|A|/p<=4/5
with p >= 8 a^(-3), there are s <= ceil(C log(2/a)) nonzero characters
xi_1..xi_s and rotations t_1..t_s in R/Z such that the factor F with cells

    V_omega = {x : frac(xi_j x/p - t_j) in [omega_j/4,(omega_j+1)/4), all j},
    omega in {0,1,2,3}^s,

satisfies Var(E(1_A|F)) := sum_V mu(V)(a_V-a)^2 >= eta a^2, where
mu(V)=|V|/p and a_V=|A cap V|/|V|.

Notation: f=1_A-a, fhat(xi)=(1/p) sum_x f(x) e(-xi x/p), so
sum_xi |fhat(xi)|^2 = ||f||_2^2 = a(1-a) <= a, and fhat(0)=0.

## 1. The sparse end is trivially TRUE — PROVED

**Theorem 1 (trivial regime).** If p <= 4^s with s <= ceil(C log(2/a)),
then (ENERGY_p) holds for A with eta=1/4, using the characters
xi_j = 4^(j-1) (j=1..s) and rotations t_j=0.

Proof. Since p is an odd prime, 4^(j-1) is a nonzero character. The arc
index of x under xi_j is floor(4 frac(4^(j-1) x/p)), the j-th base-4 digit
of x/p in [0,1). If two points 0<=x<x'<p share their first s digits then
|x-x'|/p < 4^(-s) <= 1/p, impossible. So every cell is a singleton,
E(1_A|F)=1_A, and Var = a(1-a) >= a^2 (1-a)/a >= a^2/4 for a<=4/5.

Consequence. Under the cutoff p >= 8a^(-3), the trivial regime
p <= (2/a)^(C log 4) is nonempty for small a exactly when C >= 3/log 4
(about 2.16). For such C the smallest permitted densities a ~ 2p^(-1/3)
are in the trivial regime. The theorem has nontrivial content only when

    p > 4^ceil(C log(2/a)) = (2/a)^(C log 4 + o(1)),

i.e. only for sets that are DENSE relative to 4^s, including the whole
target regime a = epsilon/log p. The suspicion in the request that the
theorem fails because it allows very sparse sets is therefore reversed:
the sparse end is where it is trivially true and useless (singleton
cells cannot continue an iteration); the danger is the dense end.

Verified: `verification/scripts/verify_full_group_energy.py` checks singleton cells for
(p,s) = (61,3),(101,4),(251,4),(1021,5).

## 2. Exact Fourier translation of factor energy (Part I) — PROVED

Let chi_omega = 1_[omega/4,(omega+1)/4) on R/Z with Fourier coefficients
c_(omega,m), |c_(omega,m)| = |sin(pi m/4)|/(pi|m|) for m != 0,
c_(omega,0)=1/4, and c_(omega,m)=0 for 4|m, m != 0. Write
lambda(m) = sum_j m_j xi_j mod p for m in Z^s and

    w(0)=1/4,  w(m)=sum_omega |c_(omega,m)|^2 = 4 sin^2(pi m/4)/(pi^2 m^2),
    W(m)=prod_j w(m_j),  sum_(m in Z^s) W(m)=1.

**Theorem 2a (rotation-average identity).** For fixed characters and
uniformly random independent rotations t in (R/Z)^s,

    E_t sum_omega |<f,1_(V_omega)>|^2 = sum_(m in Z^s) W(m) |fhat(lambda(m))|^2.

Proof. For fixed x, t -> prod_j chi_(omega_j)(xi_j x/p - t_j) has the
product Fourier series sum_m prod_j c_(omega_j,m_j) e(m_j xi_j x/p)
e(-m.t), convergent in L^2((R/Z)^s). Summing over x with weight f(x)/p
gives <f,1_V(t)> = sum_m [prod_j c_(omega_j,m_j)] e(-m.t) fhat(-lambda(m)).
Parseval in t and |fhat(-lambda)|=|fhat(lambda)| give the claim; summing
over omega replaces prod_j |c|^2 by W(m).

So the numerators of the energy are an exact W-weighted average of
|fhat|^2 over the rank-s lattice {lambda(m)}. The weights decay like
prod_j m_j^(-2): the capture efficiency of a frequency sum m_j xi_j is
4w(m_j) per coordinate, namely 1, 0.81, 0.405, 0.090, 0, 0.032, ...
for |m_j| = 0,1,2,3,4,5. Frequencies with many nonzero or large
coordinates are captured exponentially poorly. The denominators mu(V)
prevent a two-sided identity for Var itself, but give the sharp
one-sided bound below.

**Theorem 2b (quantitative upper bound with explicit tail).** For any
H>=2, with Lambda_H = {lambda(m): |m|_inf <= H} (so |Lambda_H| <= (2H+1)^s),

    Var(E(f|F)) <= 2 sum_(lambda in Lambda_H) |fhat(lambda)|^2
                   + 2 s ||f||_2 (132 (H+1)^(-2/3) + 64/p)^(1/2).

Proof. Let g=E(f|F)=sum_omega g_omega 1_(V_omega), |g_omega|<=1,
Var=||g||_2^2=<f,g>. Let sigma_H be the Fejér mean of order H, so
0<=sigma_H chi_omega<=1 and sum_omega sigma_H chi_omega = 1. Put
gtilde = sum_omega g_omega prod_j sigma_H chi_(omega_j)(theta_j(x)),
theta_j(x)=frac(xi_j x/p - t_j). Each product is a trigonometric
polynomial in x with frequencies in Lambda_H. Telescoping the products
and summing over omega, using sum_omega chi_omega = sum_omega sigma_H
chi_omega = 1, gives pointwise

    |g(x)-gtilde(x)| <= sum_(k=1)^s D(theta_k(x)),
    D(theta) = sum_omega |chi_omega - sigma_H chi_omega|(theta).

Since x -> theta_k(x) is a bijection onto a shifted p-grid, ||D(theta_k(.))||_2^2
is a grid average of D^2. Let J={0,1/4,1/2,3/4}. If dist(theta,J)>=delta,
each term is at most the Fejér tail int_(|u|>=delta) F_H <= 1/(2(H+1)delta)
(using F_H(u) <= 1/(4(H+1)u^2)), so D <= 2/((H+1)delta). Otherwise D<=4,
and at most 4(2 delta p+1) grid points are within delta of J. Hence

    ||D||_2^2 <= 128 delta + 64/p + 4/((H+1)^2 delta^2)
             = 132 (H+1)^(-2/3) + 64/p     at delta=(H+1)^(-2/3).

So ||g-gtilde||_2 <= s (132(H+1)^(-2/3)+64/p)^(1/2) =: s tau. Let P be the
Fourier projection onto Lambda_H. Then <f,g> = <Pf,g> + <f,(I-P)(g-gtilde)>,
|<Pf,g>| <= ||Pf||_2 sqrt(Var), |<f,(I-P)(g-gtilde)>| <= ||f||_2 s tau.
From x^2 <= bx + c, x <= b + sqrt(c), so Var <= 2||Pf||_2^2 + 2 s tau ||f||_2.

**Corollary 2c (what ENERGY forces).** If Var >= eta a^2, then with
H+1 = ceil((92 s/eta)^3 a^(-9/2)) and p >= 4096 s^2 a^(-3)/eta^2,

    sum_(lambda in Lambda_H) |fhat(lambda)|^2 >= eta a^2/4,

on a rank-s frequency box of side H, |Lambda_H| <= (2H+1)^s, which for
s=C log(2/a) is exp((4.5 C + o(1)) log^2(2/a)): quasi-polynomial in 1/a.
The converse is FALSE in general because of the capture weights in 2a:
large box energy carried by high-complexity combinations need not give
factor energy. (ENERGY_p) is therefore stronger than low-rank Fourier
concentration and weaker than none of its obvious consequences.

**Regimes.** R1: p <= 4^s, trivially TRUE (Theorem 1). R3: p > (2H+1)^s,
where 2b can certify a counterexample from box-energy bounds. R2, in
between, where a rank-s side-H box can already be all of Z_p and 2b is
inconclusive. R3 requires log(2/a) < sqrt(log p/(4.5C)), i.e. density
above exp(-c sqrt(log p)). Behrend-type 3AP-free sets have
log(1/a) ~ 2.35 sqrt(log p), so for C >= 0.04 they lie in R2. Thus the
Fourier route alone cannot decide the theorem on any known dense
3AP-free family; a direct factor argument is required in R2.

Verified: 2a checked on the Z_101 witness for 50 characters against the
exact rotation average over the 4p generic rotation intervals, agreement
within the stated truncation tail (about 2e-7).

## 3. Rank one only yields a^4, not a^2 (Part VII) — PROVED

**Theorem 3.** For any character xi != 0,

    max_t Var(E(f|F_(xi,t))) >= E_t Var >= (16/pi^2)(1+4/p)^(-1) |fhat(xi)|^2.

Proof. Every rank-1 cell has at most ceil(p/4) points, so
mu(V) <= (1/4)(1+4/p) and Var >= (4/(1+4/p)) sum_omega |<f,1_V>|^2. Apply
Theorem 2a with s=1 and keep m=+-1: w(+-1)=2/pi^2.

For a 3AP-free A (no nontrivial modular 3AP) with p a^2 >= 2, the exact
count Lambda_3(1_A)=a/p and sum_(xi!=0) fhat(xi)^2 fhat(-2xi) = a/p - a^3
give max_(xi!=0)|fhat(xi)| >= (a^2-1/p)/(1-a) >= a^2 (using p>=8a^(-3)).
So every eligible 3AP-free set has a rank-1 factor with Var >= 1.6 a^4.
The gap between this forced a^4 and the claimed eta a^2 is a factor a^2:
(ENERGY_p) needs a^(-2) coherent large coefficients, not one.

## 4. 3AP-freeness does force a^2 energy, on a^(-3) frequencies — PROVED

**Theorem 4.** Let A subset Z_p be 3AP-free with p a^2 >= 2 and let
T' = {xi != 0 : |fhat(2xi)| >= a^2/4}. Then

    |T'| <= 16 a^(-3)   and   sum_(xi in T') |fhat(xi)|^2 >= a^2/8.

Proof. a^3/2 <= a^3 - a/p <= sum_(xi!=0) |fhat(xi)|^2 |fhat(2xi)|. Terms with
xi not in T' contribute at most (a^2/4) sum |fhat|^2 <= a^3/4. Terms with
xi in T' contribute at most ||f||_1 sum_(T') |fhat(xi)|^2 <= 2a sum_(T')|fhat|^2.
Hence sum_(T')|fhat|^2 >= a^2/8. Also |T'| = |{eta: |fhat(eta)|>=a^2/4}|
<= a/(a^4/16).

So for 3AP-free sets the energy SCALE eta a^2 in (ENERGY_p) is always
present in the spectrum, on an a priori unstructured set of at most
16 a^(-3) frequencies. (ENERGY_p) restricted to 3AP-free sets is exactly
the assertion that a positive fraction of this forced energy is captured
by a rank-C log(2/a) quarter-arc factor. Nothing analogous is available
for 4AP-free sets: the checkpointed U^3 bound ||f||_(U3) >= a^(3/2)/2 is a
consequence of 4AP-freeness, not a hypothesis, so a U^3-large object with
small linear factor energy that is NOT 4AP-free (e.g. a quadratic level
set) does not refute (ENERGY_p); it only shows (ENERGY_p) is not a
corollary of the U^3 lemma.

Verified: a 17-point 3AP-free subset of Z_101 (p a^2 = 2.86) has
|T'|=90 <= 3355 and energy 0.1306 on T' versus a^2/8 = 0.00354.

## 5. Containment in a small cell gives energy (Part II) — PROVED

**Theorem 5.** If A is contained in one cell V of some admissible factor
with mu(V) <= 1/2, then Var(E(1_A|F)) = a^2 (1-mu(V))/mu(V) + (rest >= 0)
>= a^2. If A lies in the union of two adjacent quarter arcs of one
character (e.g. A subset [0,p/2) as integers), then rank one already gives
Var >= (1/2 - 2/p) a^2 >= a^2/4 for p>=8.

Proof. Var = sum_U mu(U)(a_U-a)^2 >= mu(V)(a/mu(V)-a)^2 + (1-mu(V))a^2
= a^2(1-mu(V))/mu(V). For two arcs, the two empty arcs contribute
(1/2-2/p)a^2.

Consequences for the sphere/Behrend/digit family (Part II). Take the box
{0,...,s-1}^d, a largest shell sum x_i^2 = R (at least s^(d-2)/d points),
digit encoding in base 2s-1 into [0,(2s-1)^d), and a prime p in
(2(2s-1)^d, 4(2s-1)^d). The image is 3AP-free in Z_p, and

    a >= s^(d-2)/(4d(2s-1)^d),   p a^3 >= (s/4)^d/(32 d^3 s^6) -> infinity

for fixed s>=5 as d->infinity, so the family is eligible with p a^3
unbounded; but it lies in [0,p/2), so Theorem 5 gives Var >= a^2/4 at rank
ONE. Every Behrend/sphere/digit set embedded through an interval is a
trivial YES instance of (ENERGY_p), regardless of how it is thinned or
affinely moved (Sections 6 and 7). It cannot be a counterexample.

## 6. Affine randomization has exactly zero effect (Part IV) — PROVED

**Theorem 6.** For u in Z_p^*, v in Z_p, and any admissible factor
F=F(xi_1..xi_s; t_1..t_s), the factor F'=F(u xi_1..u xi_s; t_j - xi_j v/p)
has the same number of characters and

    Var(E(1_(uA+v)|F)) = Var(E(1_A|F')).

Hence the multiset of energies over the whole admissible family, and in
particular sup_F Var(E(1_A|F)), is an affine invariant of A.

Proof. x -> ux+v maps V_omega(F') bijectively onto V_omega(F): indeed
frac(xi_j(ux+v)/p - t_j) = frac(u xi_j x/p - (t_j - xi_j v/p)). Cell
sizes and A-counts are preserved.

The requested moments: for a fixed cell V and uniform (u,v),
E|(uS+v) cap V| = |S||V|/p and
E|(uS+v) cap V|^2 = |S||V|/p + |S|(|S|-1)|V|(|V|-1)/(p(p-1)), identical to
a uniformly random |S|-subset, because (ux+v,uy+v) is uniform over ordered
pairs of distinct points for x != y. Cell by cell an affine image looks
random; over the family it is exactly as structured as the seed. The
affine-spread 3AP-free family of SIGNED_RESEARCH.md therefore reduces to
its seed, which is interval-supported, hence a trivial YES by Theorem 5.

Verified exactly on Z_31 for three affine maps.

## 7. Random thinning cannot lower normalized energy (Part III) — PROVED

**Theorem 7.** Fix any partition F of Z_p and a host S with s_V=|S cap V|/|V|.
Let A be a Bernoulli(theta) thinning of S. Then exactly

    E Var(E(1_A|F)) = theta^2 Var(E(1_S|F))
                      + theta(1-theta)[ sum_V |S cap V|/(p|V|) - |S|/p^2 ],

and the bracket is >= 0 since |V| <= p. Hence E Var_A >= theta^2 Var_S,
E|A| = theta|S|, and E[sup_F Var_A] >= theta^2 sup_F Var_S.

Proof. E a_V^2 = theta(1-theta)|S cap V|/|V|^2 + theta^2 s_V^2 and
E a^2 = theta(1-theta)|S|/p^2 + theta^2 a_S^2; substitute in
Var_A = sum mu(V) a_V^2 - a^2.

So E|A cap V| = theta|S cap V| is the whole story: thinning inherits the
host's discrepancy proportionally and adds nonnegative noise. A random
thinning is a counterexample only if the host already is one, and then
the host itself is the simpler witness. Uniform k-subsets differ from
Bernoulli only by finite-population corrections; no claim is made for them.

Verified by exact enumeration of all 2^8 subsets on Z_31, three values of theta.

## 8. What a full-group counterexample must be (Part V)

Combining Sections 1-7, a counterexample to (ENERGY_p) must be a
4AP-free (in practice 3AP-free) set A with p a^3 >= 8 such that:

1. p > 4^ceil(C log(2/a)) (not in the trivial regime);
2. for every admissible rank-<=C log(2/a) factor, A is not inside a cell
   of measure <= 1/2 ("Bohr-spread"); in particular xi A is not inside a
   half circle for any xi != 0;
3. it is not an affine image or a thinning of an interval-supported set;
4. (sufficient, in regime R3) sum_(Lambda_H)|fhat|^2 = o(a^2) for every
   rank-s box of side H ~ s^3 a^(-9/2), by Theorem 2b — but no known dense
   3AP-free family lies in R3, so this condition is not usable as stated.

Since Fourier-pseudorandom sets have Lambda_3 ~ a^3 > a/p and are never
3AP-free, and Roth forces a coefficient >= a^2, the requirement is a
3AP-free set whose level-a^2 spectrum (Theorem 4) avoids every
log-rank quarter-arc factor. The natural candidate is a Freiman-2-
isomorphic but non-affine image of a Behrend sphere:

**Candidate family (OPEN).** Take s=d, the box {0..d-1}^d, a largest shell,
and u in (Z_p)^d with p > (4d-3)^d such that sum c_i u_i != 0 mod p for all
nonzero c in [-2(d-1),2(d-1)]^d (such u exist by counting: fewer than
((4d-3)^d - 1)p^(d-1) < p^d vectors fail). Then phi(x)=sum x_i u_i is
injective on the box and preserves x+z=2y in both directions, so
A_d=phi(shell) is 3AP-free in Z_p, with a ~ 4^(-d)/d^3, log p ~ d log(4d),
p a^3 -> infinity, and 4^(C log(2/a)) = exp(1.92 C d + o(d)) < p for
every fixed C once d > e^(1.92 C)/4: the family is in the nontrivial
regime R2 for every C. Its digit embedding u_i=(2d-1)^i is a trivial YES
(Theorem 5); the theorem is affine-invariant (Theorem 6) but is not known
to be Freiman-isomorphism-invariant. Whether generic u makes
sup_F Var(E(1_(A_d)|F))/a_d^2 -> 0 is exactly the open question. The
spectrum of phi(box) concentrates on the dual Bohr set
{lambda : ||lambda u_i/p|| <= 1/(2d) for all i}, of size about 4^d, whose
elements are high-complexity combinations of any d generators; by the
capture weights of Theorem 2a this is the mechanism by which energy could
hide from quarter-arc factors, and also why no proof of smallness is
available. Finite diagnostics are impossible: eligibility p a^3 >= 8 for
Freiman-embedded spheres forces p beyond 10^40.

## 9. Why a proof is out of reach here: the theorem's true strength (Part VI)

**Theorem 8 (strength; conditional on the checkpointed bridge).** Assume
the window version of the energy theorem (ENDPOINT_INCIDENCE_AUDIT.md
section 5) with constants eta, C, together with the proved bridge of
LOCALIZATION_BRIDGE.md sections 4-6 (atom lemma (6), recurrence (9)-(10),
terminal bound (7), interval transfer). Then there is c=c(eta,C)>0 with

    r_3(N) <= 2 N exp(-c (log N)^(1/4))   for all large N.

Proof (ledger). A 3AP-free set is 4AP-free. Let L=log(2/a_0). The bridge
gives J <= L/log(1+eta/2)+1 steps, total rank D <= 1+J(CL+1) = O(L^2),
total logarithmic size loss Lambda = O(L^2), and cutoff persistence when
log N >= C_4 L^2. Terminal bound (7) with R >= (p-1)^(1/D)/2 and
p/n_J <= 6 e^Lambda gives density <= 3/4 + 3D ceil(p/R)/(4 n_J) < 4/5 as
soon as log(p-1) >= D(Lambda + log(360 D)) = O(L^4). All requirements
hold when log N >= C_5 L^4, i.e. a_0 >= 2 exp(-(log N/C_5)^(1/4)).

To my recollection (not verifiable offline) the best published Roth
bounds are of the shape N exp(-c (log N)^kappa) with kappa <= 1/9
(Kelley-Meka 2023; Bloom-Sisask improvement); Behrend's lower bound has
exponent 1/2. (ENERGY) with log rank and constant radius would deliver
exponent 1/4 by the elementary bridge, and any improvement of the
terminal step would push it toward Behrend's 1/2. This is the precise
content of "suspiciously strong". It is not a disproof: the implied
bound does not contradict Behrend. It does mean that proving (ENERGY_p)
for 3AP-free sets is at least a major Roth-type inverse theorem, far
beyond the tools in this folder; Sections 3-4 show that the only
mechanism available from 3/4AP-freeness in linear Fourier space yields
a^4 per character, and coherence of a^(-2) frequencies at logarithmic
rank is exactly what would need to be invented.

## 10. The repair that suffices for the target (Part IX) — PROVED sufficient

The density restriction a >= epsilon/log p alone does not remove the
strength issue in the rank direction, but it does remove the Behrend-
scale implication: with log rank and a >= epsilon/log n, iterating from
a_0=epsilon/log N gives D, Lambda = O((log log N)^2) and the terminal
condition O((log log N)^4) << log N, so the 3AP-free specialization would
imply only r_3(N) = o(N/log N), consistent with results I recall as known.

More importantly, the iteration does not need logarithmic rank at all.

**Theorem 9 (sufficient relaxed statement).** Fix epsilon>0. Suppose
there are eta>0 and either c in (0,1/2) or K>=1 such that for every
controlled window Omega (rank r, size n, full cutoff) and every 4AP-free
A subset Omega with epsilon/(2 log n) <= a <= 4/5 there is a quarter-arc
factor of rank <= a^(-c) (respectively <= log^K(2/a)) with
Var_Omega(E(1_A|F)) >= eta a^2. Then r_4(N) <= epsilon N/log N for all
large N. Since epsilon is arbitrary, this gives the local target.

Proof (ledger). Start from a_0=epsilon/log N, L=log(2/a_0) ~ log log N.
Atoms per step <= 4^(a_0^(-c)); retained mass >= eta a_0 4^(-a_0^(-c))/2;
J=O(L) steps. Total rank D=O(L a_0^(-c)) = O((log N)^c log log N) and
total log-loss Lambda=O(L a_0^(-c)+L^2) = o(log N), so every window used
has log n_j >= (1/2) log N and a_j >= a_0 >= epsilon/(2 log n_j): the
hypothesis is only invoked in its stated density range. Cutoffs need
O(D) = o(log N). The terminal bound (7) needs
log p >= D(Lambda + log(360 D)) = O((log N)^(2c) (log log N)^2), which is
o(log N) exactly when c<1/2. The polylog version gives D, Lambda =
O((log log N)^(K+1)) and terminal O((log log N)^(2K+2)). Then (7) forces
density <= 3/4+o(1) against >4/5.

For 3AP-free sets, the c=1/3 version would imply only
r_3(N) <= N (log N)^(-3/2+o(1)), which is weaker than what I recall as
known. So the relaxed statement is not "suspiciously strong" in the Roth
direction, while still closing the r_4 route. The excess in the current
theorem is its logarithmic RANK, not its density range.

## 11. Mandatory tests (Part VIII)

| Test | Verdict for (ENERGY_p) |
|---|---|
| 1. Behrend/sphere 3AP-free sets | Eligible (p a^3 -> infinity) but interval-supported: TRUE with eta=1/4 at rank 1 (Thm 5). Not a counterexample. |
| 2. Random thinnings of them | E Var_A >= theta^2 Var_S (Thm 7): inherit TRUE. |
| 3. Affine-spread 3AP-free family | Family sup is affine-invariant (Thm 6); seed is interval-supported: TRUE. |
| 4. Concentrated-support AP-free sets | Thm 5: TRUE at rank 1. |
| 5. Flat/difference-set spectra (Z_13 {0,1,3,9}, Sidon sets) | Never eligible: Sidon gives |A| <= sqrt(p)+1, so p a^3 -> 0 < 8. |
| 6. Z_101 mixed witness (a=28/101) | Ineligible: cutoff needs p >= 375. Diagnostic: sup rank-1 Var/a^2 = 0.329, max|fhat|^2/a^4 = 1.61. |
| 7. AP_RICHNESS_COUNTEREXAMPLE | Relative-window object; as a subset of Z_p it has p a^3 << 1. Ineligible for the full-group statement. |
| 8. UNIFORM_ENERGY_COUNTEREXAMPLE | Same: |A_d| ~ 2^d/d, p ~ 100*64^d, p a^3 -> 0. Ineligible. |
| 9. a = epsilon/log p | Nontrivial regime R2. No proof, no counterexample. For 3AP-free sets the statement here is of Bloom-Sisask/Kelley-Meka-consequence strength; unproved by any tool in this folder. |
| 10. a ~ 2 p^(-1/3), only p a^3 >= 8 | Trivially TRUE when C >= 3/log 4 (Thm 1). The "excessive range" is the trivially true end. |

No eligible counterexample was constructed; no proof was obtained.

## 12. Output classification

Not (A): no proof of r_4(N)=o(N/log N).
Not (B): no eligible full-group counterexample; all tested families are
trivial YES instances or ineligible (Sections 5-7, 11).
Not (C) as a proved repaired theorem: Theorem 9 is a proved SUFFICIENCY
of a weaker hypothesis, not a proof of that hypothesis.
(D): Theorems 1-9 are new rigorous partial results relative to this
folder (no literature novelty claimed).

**ONE EXACT REMAINING STATEMENT (full group).** Decide (ENERGY_p) in the
nontrivial regime p > 4^ceil(C log(2/a)); the sharpest concrete instance
is the Freiman-embedded sphere family A_d of Section 8 with generic u:
does sup over rank-<=C log(2/a_d) quarter-arc factors of
Var(E(1_(A_d)|F))/a_d^2 stay bounded below by an absolute eta for all
generic u, or tend to zero for some u? A "yes for all u" leaves
(ENERGY_p) open but kills the only natural candidate; a "zero for some
u" is a full-group counterexample (B) and, by Theorem 9, would redirect
the program to the rank-a^(-c) relaxation rather than end it.

## 13. Verification

Run `python3 verification/scripts/verify_full_group_energy.py`; output in
`verification/results/full_group_energy_verification.json`. Exact rational checks: the
rotation-average identity (2a) against 4p-interval averaging for 50
characters on the Z_101 witness; the rank-1 lower bound (Thm 3) for every
character (minimum ratio 1.70); singleton digit cells (Thm 1) for four
(p,s) pairs; exact affine invariance of the rank-1 supremum (Thm 6) for
three maps on Z_31; the thinning identity (Thm 7) by enumeration of all
subsets of 8-point hosts for three theta; and, on a 17-point 3AP-free
subset of Z_101 with p a^2=2.86, the Fourier identity for a/p-a^3, the
level-a^2/4 energy bound (Thm 4), and the interval-support bound (Thm 5).
These support the proofs above on finite instances; they are not an
asymptotic proof of anything.

## 14. Continuation prompt

> Work offline from FULL_GROUP_ENERGY_AUDIT.md. Accept Theorems 1-9:
> the full-group energy theorem is trivially true for p <= 4^(C log(2/a)),
> is affine-invariant, is inherited by thinnings, holds at rank one for
> every interval-supported set, and in its logarithmic-rank window form
> implies r_3(N) <= N exp(-c(log N)^(1/4)) through the checkpointed bridge.
> Do not attempt to prove logarithmic-rank energy for 3AP-free sets.
> Two admissible directions only. (i) Attack the Freiman-embedded sphere
> family A_d = phi(shell) of Section 8 with generic u: bound
> sup_F Var(E(1_A|F))/a^2 over all quarter-arc factors of rank <= C log(2/a)
> either below by an absolute constant or above by o(1), using the dual
> Bohr set of phi(box) and the capture weights 4w(m) of Theorem 2a; a
> union bound over factors is not available (only d log p bits of
> randomness against p^(2s) factors), so the argument must be structural.
> (ii) Replace the target hypothesis by Theorem 9's relaxed statement:
> rank <= a^(-1/3) (or polylog) quarter-arc factors, density
> a >= epsilon/(2 log n), full cutoff, energy eta a^2, and attempt its
> proof for 4AP-free sets using 4AP-freeness essentially (the U^3 lower
> bound, endpoint Gram formula (4) of ENDPOINT_INCIDENCE_AUDIT.md), since
> for 3AP-free sets Theorem 4 already supplies the a^2 energy scale on
> 16 a^(-3) frequencies and only their arrangement is missing. Test every
> statement against Theorems 5-7 (trivial YES families), the ineligibility
> of all flat-spectrum and small-p witnesses, and a = epsilon/log p.
> Do not claim official #142 or the local target from finite checks.
