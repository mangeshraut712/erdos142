# A symmetric candidate against the window energy lemma

2 October 2026. **(E) OPEN — CANDIDATE COUNTEREXAMPLE, NOT PROVED.**
The window energy lemma (AP_RICHNESS_COUNTEREXAMPLE.md section 8, the
"one remaining theorem") is neither proved nor refuted. The target
r_4(N)=o(N/log N) is unaffected. No novelty is claimed.

Motivation: BOUNDED_RANK_VACUITY_20261002.md shows that window
counterexamples at the iteration's densities need rank tending to
infinity. This family has rank r+1 on a window of size 4^r, meets the full
cutoff, and is provably 4-AP-free.

## 1. The window — PROVED

For r>=1 let D=16^r, p a prime >100D^2, xi_j=ceil(p/16^j). The rank-(r+1)
controlled window 0<=x<D, 0<=(xi_j x mod p)<=floor(9p/40) (j=1..r) equals

    Omega_r={sum_{i<r} u_i 16^i : u_i in {0,1,2,3}},  |Omega_r|=4^r.

Proof as in WINDOW_LATTICE_MODEL_20261002.md section 3: lower digits in
{0,...,3} contribute at most 3/240 to the fractional part; digit <=3 gives
at most 3/16+3/240=1/5<9/40, digit >=4 gives at least 1/4>9/40, no wrap;
9/40<1/3. Digit coefficients in x_0-2x_1+x_2 are at most 6<8, so modular
4-APs are exactly 4-APs of u in Z^r (checked exactly for r=2,3,4).

## 2. The set and its 4-AP-freeness — PROVED

For u in {0,1,2,3}^r let n(u)=(n_0,...,n_3) count the coordinates equal to
0,...,3, and sigma(u)=sum u_i=n_1+2n_2+3n_3. Put d=(-1,1,1,-1). Let B be a
4-AP-free set of integers and T a set of count vectors with

1. sigma(T) contained in B, and
2. at most one point of T on each line n+Zd.

**Theorem.** A={u : n(u) in T} has no nontrivial 4-AP in Z^r, hence none
in Omega_r.

Proof: in a 4-AP u+jw of the box, every coordinate with w_i!=0 has
w_i=+-1 and runs through 0,1,2,3 or 3,2,1,0. With s_+, s_- such coordinates
and c the counts of the fixed ones, point j has counts
c+s_+e_j+s_-e_(3-j) and digit sum sigma(c)+3s_-+j(s_+-s_-). If s_+!=s_-
these four sums are a nontrivial 4-AP in B. If s_+=s_-=s>=1, points 0 and 1
have counts c+s(e_0+e_3) and c+s(e_1+e_2), distinct and on one d-line,
contradicting condition 2.

The line through n is indexed by alpha=n_0+n_1, beta=n_0+n_2, and
sigma=3r-2alpha-beta is constant on it. We take T to be the most massive
count vector on each line whose sigma lies in B.

## 3. Density and cutoff — COMPUTED

Density is a=sum_{n in T} multinomial(n)/4^r (log-gamma floats):
a*sqrt(r) is about 0.28-0.46 for r=50..300 with greedy B (density of B
0.2-0.32). The cutoff 4^r>=8*3^(r+1)*a^(-3) then holds from r of about 45,
with logarithmic margin 17 at r=100 and 73 at r=300. A thus has relative
density of order r^(-1/2), far above eps/log|Omega|.

## 4. Energy on the character classes we can evaluate — COMPUTED

Characters of Z_p restricted to Omega_r are theta.u mod 1 with
theta_i=t*16^i. Two classes are explicit:

- digit juntas (t with few non-negligible theta_i, including coordinate
  slabs): energy of E(1_A | k chosen coordinates), computed exactly in count
  space for k=1,2;
- t=k/15: theta is constant, so these characters see sigma mod 15. We
  report the energy of the full 15-cell partition by sigma mod 15, which
  bounds every factor built from these characters.

With B optimised to balance A-mass across residues mod 15 (4-AP-free
checked):

| r | a | k=1 junta | k=2 junta | sigma mod 15 | 1/log(2/a) |
|---|---:|---:|---:|---:|---:|
| 100 | 0.0637 | 9.0e-5 | 2.8e-4 | 0.168 | 0.290 |
| 300 | 0.0315 | 1.6e-6 | 1.5e-5 | 0.106 | 0.241 |
| 600 | 0.0199 | — | — | 0.087 | 0.217 |

(energies divided by a^2). Junta energy is negligible and falls with r.
The mod-15 energy falls (ratio to the target scale 0.58, 0.44, 0.40) but is
not yet small; it is a finite-size effect of how few sigma-levels carry
mass (width about sqrt(5r/4)), and should vanish as r grows if B can be
kept 4-AP-free and equidistributed mod 15 at that scale. That is not proved.

With random greedy B instead the mod-15 energy is 0.6-1.2: an unbalanced B
makes the lemma TRUE for that instance via one character.

## 5. What would complete or kill the candidate

To refute the window energy lemma one must show, for some choice of B:

1. (balance) B 4-AP-free with A-mass equidistributed mod 15 up to o(1/log r)
   relative error, as r tends to infinity;
2. (generic characters) for every factor of <=C log(2/a) quarter-arc
   characters theta=t(1,16,...,16^(r-1)), energy o(a^2/log(2/a)). Heuristic:
   A is permutation-symmetric, and |E[e(m theta.u) | n(u)]| is small unless
   most m theta_i are close to one common value mod 1, which forces
   m t close to k/15 (the mod-15 class) or most theta_i close to 0 (juntas).
   Small cells could amplify many small Fourier terms; the existing
   counterexamples handled this by exact cell counting, which is not yet
   done here.

Conversely, the lemma survives this family if every admissible B is
forced to correlate with sigma mod 15 (or the realization is changed:
in base b the visible modulus is b-1, and for b-1>3r sigma itself is
visible, so the lemma holds for that realization). The candidate is
therefore specific to small-base realizations.

## 6. Checks

`python3 verify_symmetric_candidate_20261002.py` (about 10 seconds): exact
exhaustive 4-AP-freeness of the actual sets for r=3..6 (up to 1333 points),
density, cutoff, junta and mod-15 energies for r=50..300 with greedy B.
`python3 verify_symmetric_balance_20261002.py` (about 90 seconds): balanced
B for r=100, 300, 600, recomputing every quantity and asserting agreement
with the first script and 4-AP-freeness of B. Window realization checked
exactly for r=2,3,4. Outputs: symmetric_candidate_verification_20261002.json,
symmetric_balance_verification_20261002.json.
