# Window counterexamples need unbounded rank; interval experiment

2 October 2026. **(D) NEW PARTIAL THEOREM (one cited standard input).**
The target r_4(N)=o(N/log N) and the window energy lemma remain OPEN.

## 1. Bounded-rank transfer

**Proposition 1.** For each r there is C(r) such that every controlled
window Omega of rank <=r admits an injective map phi:Omega->{1,...,C(r)|Omega|}
under which every 4-AP-free A in Omega has 4-AP-free image.

Proof outline. By WINDOW_LATTICE_MODEL_20261002.md Lemma 1, Omega with its
progressions is X=Z^r intersect K for a convex parallelepiped K. Take a
Minkowski-reduced basis of Z^r relative to K. Standard geometry of numbers
(Minkowski's second theorem and lattice-point/volume comparison, e.g.
Tao–Vu, *Additive Combinatorics*, section 3.5) puts X, after removing
directions in which K has lattice width <1 (which lowers the dimension),
in a box prod [0,L_i) with prod L_i <= C_1(r)|X|. Map
u -> sum u_i M_i with M_1=1, M_(i+1)=4L_i M_i. An integer relation
phi(x_0)-2phi(x_1)+phi(x_2)=0 between box points has digit coefficients of
size <4L_i and so holds coordinatewise; hence integer 4-APs in phi(A) are
4-APs of A. The image lies in an interval of length 4^r prod L_i.
The constants are r^(O(r)) and are not tracked; the geometry-of-numbers
step is cited, not reproved here.

**Corollary 2 (vacuity at bounded rank).** Assume the target. For every
fixed r and eps>0 there is n_0 such that no rank-<=r window of size n>=n_0
contains a 4-AP-free set of relative density >=eps/log n.

Proof: phi(A) is a 4-AP-free subset of an interval of length
N'<=C(r)n with density >=(eps/C(r))/log n >=(eps/(2C(r)))/log N' for
large n, contradicting the target with eps/(2C(r)) in place of eps.

Rank one needs no citation: a rank-1 window is a progression in Z_p, and
Lemma 1 of the lattice model identifies it with an integer interval.

**Consequences.**

1. Together with VACUITY_OF_FULL_GROUP_OPEN_20261002.md, the window energy
   lemma at the iteration's densities can be non-vacuous only on windows
   whose rank tends to infinity with n.
2. Both existing window counterexamples fit exactly: the binary-cube window
   (UNIFORM_ENERGY_COUNTEREXAMPLE.md) and the cube-plus-segment window
   (AP_RICHNESS_COUNTEREXAMPLE.md) have rank proportional to log n.
3. Since 3^r <= n a^3/8 under the cutoff, rank is at most
   log_3(n a^3/8). Non-vacuous counterexamples live in the band
   r(n) -> infinity, r <= log_3(n a^3/8). Future counterexample searches
   should target rank growing like a power of log n, not fixed rank.

## 2. Interval-window experiment (pre-asymptotic by Corollary 2)

Rank-one window Omega={0,...,n-1} in Z_p, p the least prime >3n. Random-
order greedy 4-AP-free sets; best single-character quarter-arc energy over
all characters and 64 rotations each; four uniform random subsets of equal
size as baseline.

| n | |A| | a | E/a^2 (AP-free) | random min-max | 1/log(2/a) |
|---|---:|---:|---:|---:|---:|
| 1000 | 192 | 0.192 | 0.074 | 0.082-0.106 | 0.427 |
| 2000 | 314 | 0.157 | 0.055 | 0.061-0.073 | 0.393 |
| 4000 | 501 | 0.125 | 0.041 | 0.045-0.072 | 0.361 |
| 8000 | 826 | 0.103 | 0.045 | 0.026-0.029 | 0.337 |
| 16000 | 1321 | 0.083 | 0.036 | 0.018-0.022 | 0.314 |

Up to n=4000 the AP-free sets sit below the random range (as in the
cyclic search). From n=8000 they exceed every baseline by a factor
1.6-1.9. The cause is a boundary effect: a fresh greedy set has relative
density 1.25-1.42 in the outer tenths of [0,n) at both n=4000 and 16000
(points near the ends lie in fewer 4-APs, so greedy keeps them more often).
This is slab energy from the coordinate character, absent in the cyclic
group, which explains why RANK1_HOSTILE_SEARCH_20261002.md saw only noise.

Interpretation: the measured energy is about 0.11 a^2/log(2/a) at
n=16000, but it reflects the edge effect, not an arithmetic consequence of
4-AP-freeness. Greedy densities also decay polynomially (about n^(-0.3)),
so these sets leave the eps/log n regime; by Corollary 2 no rank-one
experiment can reach the asymptotic regime unless the target fails.

## 3. Checks

`python3 verify_interval_window_energy_20261002.py` (about 15 minutes,
standard library). Every greedy set passes an exhaustive 4-AP check. The
edge profile above was recomputed separately with seed 5. Output:
interval_window_energy_verification_20261002.json.
