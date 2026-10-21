# Lemmas toward the symmetric candidate

2 October 2026. **(D) NEW RIGOROUS PARTIAL RESULTS; candidate still (E) OPEN.**
Continues SYMMETRIC_CANDIDATE_20261002.md (notation: box {0,1,2,3}^r in
the base-16 window, counts n(u), digit sum sigma, lines n+Zd with
d=(-1,1,1,-1), T the line modes at levels in B, A={u: n(u) in T}).
The window energy lemma and the target remain unproved and unrefuted.

## 1. Closed-form line mode — PROVED

On the line with alpha=n_0+n_1, beta=n_0+n_2, R=r-alpha-beta, the ratio of
consecutive multinomials is (alpha-n_0)(beta-n_0)/((n_0+1)(R+n_0+1)),
which crosses 1 where n_0=(alpha beta-R-1)/(r+2) (the quadratic terms
cancel). The most massive point is n_0*=ceil((alpha beta-R-1)/(r+2)),
clamped to the line. Checked against brute force on every line for
r=5, 17, 40, 90.

## 2. Fourier decay for count-symmetric functions — PROVED

For u uniform on the box, xi in (R/Z)^4 and real z_0,...,z_(r-1),

    |E e(xi.n(u)+sum_i z_i u_i)| = prod_i |phi_i|,
    phi_i = (1/4) sum_{j=0}^{3} e(xi_j+j z_i),
    |phi_i| <= 1-2||z_i-gamma||^2,  gamma = xi_0-xi_1,

so the modulus is at most exp(-2 sum_i ||z_i-gamma||^2). Proof:
independence over coordinates; |phi_i|<=1/2+|1+e(a_1-a_0)|/4 and
|cos(pi s)|<=1-4||s||^2.

For a character of the window, z_i=m t 16^i (the window gives
theta_i=t 16^i exactly). By Fourier inversion over count vectors, for any
set T of counts,

    |E[1_{n(u) in T} e(m theta.u)]| <= |T| exp(-2 min_gamma sum_i ||m t 16^i-gamma||^2),

and |T|<=(r+1)^2.

## 3. Digit lemma: which frequencies escape the decay — PROVED

Fix 0<delta<1/60 and call i good for (x,gamma) if ||16^i x-gamma||<=delta.

1. If i and i+1 are good then ||15*16^i x||<=2 delta, so 16^i x is within
   2 delta/15 of some k/15, and gamma is within 2 delta of k/15. As
   4 delta<1/15, k is determined by gamma alone.
2. Put y=x-k/15. Since 16 = 1 mod 15, 16^i y = 16^i x - k/15 mod 1, so on
   every pair of consecutive good indices ||16^i y||<=2 delta/15.

Consequently, if fewer than L indices are bad, the good indices form at
most L+1 runs, all with the same k, and y has base-16 digits that are
(up to a carry) 0 or F except within O(L) positions: m t is the
mod-15 character k/15 perturbed by a junta of O(L) digits. Every other
frequency has sum ||.||^2 >= L delta^2, and its Fourier coefficient
against any count-symmetric set is at most (r+1)^2 exp(-2 L delta^2).

This makes the heuristic of the candidate report rigorous at the level of
single frequencies: the only possibly large Fourier coefficients of A on
the window lie on "mod-15 class plus few-digit junta" frequencies.
Checked: 105,963 random instances of part 1; 3000 random instances of the
decay inequality (worst ratio 0.995 to the bound).

## 4. Asymptotic balance mod 15 by random alteration — PROVED

(The unimodality input below is no longer needed; see "Smoothness
replaces unimodality" at the end of this section.)

Let G(s) be the T-mass at level s with B=all levels (mode mass summed over
the lines at level s), with mean mu and standard deviation w. Let I be the
interval of length W=12w+1 around mu, 0<eps<1/14, beta=W^(-1/2+eps).
Choose B_0 in I with independent probability beta, then delete the last
term of every 4-AP of B_0. The result B is 4-AP-free (all its progressions
lie in I).

- The number X of 4-APs in B_0 has E X <= W^2 beta^4 = W^(4eps), so
  X <= W^(5eps) with probability >= 1-W^(-eps).
- For each residue c mod 15, Hoeffding gives
  |S_c - beta G_c| <= lambda sqrt(max G * G_c) with probability
  >= 1-2exp(-2 lambda^2), where S_c is the B_0-mass in class c and G_c the
  full mass. Deletions change S_c by at most X max G.
- |G_c - G(I)/15| <= Var(G), the total variation of G on I. G is
  unimodal with Var(G)=2 max G exactly at r=300, 1200, 4800 (one local
  maximum each); unimodality for all r is the one unproved input.

With max G of order G(I)/w and lambda of order sqrt(log w), every class
ratio is 1+O(sqrt(log w)/w^(1/4+eps/2)) with high probability, so the
mod-15 energy is O(log w / w^(1/2+eps)), polynomially small in r (w is of
order sqrt r), hence o(1/log(2/a)). Density stays a of order beta/sqrt r,
polynomial in r, so the cutoff still holds for large r.

Measured with eps=0.05 (six random B each): mean mod-15 energy 4.36,
1.66, 1.42 at r=300, 1200, 4800, decreasing as 15/(beta*w) predicts but
far from small at these sizes. The searched B of SYMMETRIC_CANDIDATE
(0.087 at r=600) is much better in practice; the random B is for the
proof.

**Smoothness replaces unimodality — PROVED.** The balance proof needs only
|G_c - G(I)/15| <= V(G on I), with V the total variation, and
V = o(G(I)/sqrt(log r)). Write G(s) = sum_alpha m(alpha, beta_s(alpha)),
where m is the line-mode mass and beta_s(alpha) = 3r-2alpha-s, so that
moving from level s to level s+1 lowers beta by 1. Moving a count from
digit 2 to digit 3 maps line (alpha,beta) to line (alpha,beta-1) with the
same n_0. Comparing each mode with its image gives

    n_2*/(n_3*+1) <= m(alpha,beta-1)/m(alpha,beta) <= (n_2**+1)/n_3**,

where n* and n** are the modes of the two lines. Lines whose mode has
some |n_d - r/4| > sqrt(r) log r carry total mass exp(-c log^2 r),
negligible against G(s) on I. On the others both bounds are
1+O(log r/sqrt r). Hence G(s+1)/G(s) = 1+O(log r/sqrt r) on I, and

    V(G on I) <= C (log r/sqrt r) G(I) + exp(-c log^2 r).

The class ratios then gain only an additive O(log r/sqrt r), so the mod-15
energy is still polynomially small and section 4 needs no numerical input.
Checked (verify_level_smoothness_20261002.py), r=100, 300, 1200, 2400:

- V/G(I) = 0.071, 0.041, 0.021, 0.0146, about 0.7/sqrt r;
- max |G(s+1)/G(s)-1| on I is at most 1.7 log r/sqrt r;
- |G_c - G(I)/15| <= V asserted (actual deviations 3e-5 down to 1e-8 of
  G(I)).

## 5. Remaining steps (not proved)

1. **Junta-plus-residue equidistribution.** For |S| up to polylog(r) and
   each residue mod 15: E(1_A | u_S, sigma mod 15) = a(1+o(1/log r)).
   Local-limit heuristic: fixing u_S shifts each line by O(|S|); the mode
   kills the first-order term along d, other directions contribute
   O(|S|/sqrt r) with varying signs, giving energy O(|S|^2/r). Measured
   for |S|<=2 (energies 1e-6 to 3e-4). Random B adds a concentration step
   over polylog many (shift, residue) events.
   Joint measurement (verify_junta_residue_20261002.py, searched balanced B
   for r=100, 300, 600): the energy of the partition by (u_S, sigma mod 15)
   grows nearly linearly in |S| for |S|=0,...,6:

   | r | energy at |S|=0 | energy at |S|=6 | slope per coordinate | slope*r |
   |---|---|---|---|---|
   | 100 | 0.1684 | 0.1856 | 2.86e-3 | 0.286 |
   | 300 | 0.1064 | 0.1111 | 7.79e-4 | 0.234 |
   | 600 | 0.0873 | 0.0886 | 2.13e-4 | 0.128 |

   The slope falls at least like 1/r (slope*r is decreasing), so for
   |S|=polylog(r) the junta part adds polylog(r)/r = o(1/log r) on top of
   the mod-15 part. The mod-15 part itself is controlled by the balance
   construction. Evidence only; the slope is measured for |S|<=6.
   Update: PROVED in SYMMETRIZATION_20261002.md section 2 for every
   permutation-invariant A, with junta energy at most 6 (max_c w_c) |S|/r.
   For the random-alteration B (a ~ r^(-3/4)) use the density-free bound
   of PARAMETER_AUDIT_20261002.md section 3, valid for
   |S| = o(sqrt(r)/log^(5/2) r).
2. **Harmonics and small cells.** Sandwich each quarter arc by
   Beurling–Selberg polynomials of degree H=r^C; a factor of k=O(log r)
   characters gives at most (log H)^k = exp(O(log r log log r)) harmonic
   combinations, each either decayed by section 3 with L=polylog(r) or of
   the exceptional type handled by step 1. Energy is at most
   2*#cells*max_V |E f 1_V| with #cells<=4^k=r^O(1), so the decayed terms
   fit. The bookkeeping (boundary layers, the window's own exceptional
   frequencies) is not yet written out.
   Update: CELL_BOOKKEEPING_20261002.md proves the exceptional-only case
   (reduces to step 1 with eta=o((log r)^(-1/2)), no small-cell loss) and
   isolates the generic/mixed case, including a tower obstruction.

If steps 1 and 2 are completed, A refutes the window energy lemma with the
full cutoff in the base-16 realization. The target r_4(N)=o(N/log N) would
NOT be refuted (A is not dense in an interval); only that route to it
would be closed.

## 6. Checks

`python3 verify_candidate_lemmas_20261002.py` (about 45 seconds): mode
formula on all lines for four values of r, the decay inequality, the digit
lemma, and alteration balance for r=300, 1200, 4800 with 4-AP-freeness of
every B asserted. Output: candidate_lemmas_verification_20261002.json.
`python3 verify_junta_residue_20261002.py` (about 20 seconds): joint
junta-plus-residue energies for |S|<=6 at r=100, 300, 600, asserting each
|S|=0 value equals the stored mod-15 energy. Output: junta_residue_verification_20261002.json.
