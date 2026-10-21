# Mixed factors without the basis lemma (proof sketch)

2 October 2026. **(D) PROOF SKETCH, NOT YET INDEPENDENTLY CHECKED; candidate
still (E) OPEN.** Sections 7-9 (added later the same day) write out the two
open points and revise sections 3-4: absorption is confined to a fixed
box, and low-order coordinates are treated exactly. The whole argument
still needs an independent check. Continues GENERIC_FACTORS_20261002.md section 3, whose
"basis lemma" this sketch tries to bypass. Notation as there. The window
energy lemma and the target r_4(N)=o(N/log N) remain unproved and
unrefuted. Nothing here should be cited as a theorem until every step
below has been written out and checked.

## 1. Goal

Let F be the factor of k=O(log r) quarter arcs of phi_1,...,phi_k, refined
by P. By GENERIC_FACTORS section 1 it suffices to show
E_n chi^2_n = o(1/(sqrt r log r)), where chi^2_n compares the cell law
given n with the cell law given sigma mod 15. We may refine F further by
any junta G=(u_(S'), sigma mod 15) with |S'| = polylog(r), since
refinement only increases the energy and juntas cost
O(|S'|/r) (SYMMETRIZATION section 2).

## 2. Use the single-centre functional, not Psi — CHECKED

For the absorption step, "structured relative to S'" must mean

    Phi_out(x) = min_gamma sum_{i not in S'} ||16^i x - gamma||^2 < T,

not Psi_out(x) < T. Psi is only a lower bound (Psi <= 4 Phi). A frequency
whose orbit sits near k1/15 on one block of digits and near k2/15 on
another has Psi = O(1) but Phi of order r ||(k1-k2)/15||^2. It is
decayed: its phase sees the partial digit sum of a block mod 15, which a
permutation-invariant A cannot see.

Checked exactly (verify_two_run_20261002.py): x = k2/15 + (k1-k2)/(15*16^(r/2))
gives Psi fixed as r grows (0.0039, 0.063 and 0.098 for the three pairs)
and Phi = r(d/2)^2 growing linearly. At r=40, the Fourier coefficient
against the candidate is 1.9e-8 and 4.4e-8 times a for (k1,k2)=(3,7) and
(0,5). For (1,2), with d=1/15, it stays near 0.08 times a up to r=40,
another slow mode of rate about r/900 (compare q=17 in RATIONAL_CLASSES).

With Phi, relatively structured frequencies have a single k/15 on all good
positions outside S', so their phase is k sigma_out/15 plus a junta plus
drift, as in CELL_BOOKKEEPING section 5.

## 3. Absorption controlled by covolume

Start with L' = 0 and S' = bad sets of the individually structured phi_j.
Fix H = r^(M') and repeat:

1. **(rank step)** If some m with |m|_inf <= H and m outside the rational
   span of L' has Phi_out(x_m) < T, add m to L' and add its bad indices
   and run tops to S'.
2. **(index step)** If some m in the saturation of L', but not in L', has
   Phi_out(x_m) < T for a representative in the fundamental parallelepiped
   of a reduced basis of L', add it to L' and update S'.

**Counting.**
- There are at most k rank steps. Each multiplies the covolume of L' by
  at most sqrt(k) H.
- Each index step divides the covolume by at least 2. The covolume is at
  least 1, so there are at most k log_2(sqrt(k) H) = O(log^2 r) index
  steps. No bound on the size of the vectors is needed.
- Each step adds at most (T/delta^2+1)(g+1) coordinates to S', so
  |S'| = polylog(r).

## 4. Coset equidistribution

Given a G-cell W, each absorbed b has phase x_b X determined up to drift
eps. So the phase vector Phi=(phi_j X)_j lies within eps of a coset of
K = Ann(L') in T^k. At the end:

- m with |m|_inf <= H outside span(L') has Phi_out >= T, hence
  |E[e(m.Phi) | n, W]| <= e^(-T/2) r^(O(1)). This is the decay lemma on
  the coordinates outside S', and dividing by P(n_out) costs only r^(O(1))
  (true only on the narrow window sqrt(r log r); see section 7).
- The characters of the component group of K (saturation/L') are decayed
  by the final index check, so the component of Phi is equidistributed
  given (n,W). The component count is at most (sqrt(k) H)^k, which is
  absorbed if T >= C k log H = O(log^2 r).
- Coordinates j with e_j in span(L') take finitely many values on the
  coset. They are handled exactly, with no smoothing. Their atoms fall
  within eps of an arc endpoint only on a junta-measurable set of
  measure poly(r) 4^(-m) (Cantor small-ball bound, CELL_BOOKKEEPING
  section 4).
- For the other coordinates, Haar measure on the coset pushes forward to
  Haar measure on T. Sandwich their arcs by Beurling–Selberg polynomials
  of degree H and restrict to the coset. The nonzero coefficients have
  total mass at most (C log H)^k, which is absorbed by e^(-T/2) if
  T >= 2k log(C log H) + O(log r). The boundary mass on the coset is
  at most 2^k k/H.
- Thin cells (P(V|class,W) at most the square root of the boundary mass)
  are bounded by E_n[(P_n+P_c)^2/P_c] <= 4P_c + 2(boundary) + 2(decayed),
  and their total measure is at most 4^k r^(-M'/2). Other cells contribute
  at most (boundary+decayed)^(3/2).
- Drift precision. The phases constrain only b.Phi, so off-coset
  displacement is at most eps ||B^+||. Here ||B^+|| <= (k max|b|)^k =
  exp(polylog r), so eps = exp(-polylog r) suffices. This needs
  g = polylog(r) run-top digits, and it keeps |S'| polylog.

Result, if every step holds: E_n chi^2_n <= r^(-M'') + O(|S'|/r), so
the energy is o(a^2/log(2/a)) for every factor of O(log r) quarter-arc
characters.

## 5. Status

If this sketch is correct, then together with the following it shows that
the candidate refutes the window energy lemma (base-16 realization, full
cutoff):
- 4-AP-freeness, density and cutoff (SYMMETRIC_CANDIDATE);
- mod-15 balance of the random-alteration B (CANDIDATE_LEMMAS section 4;
  now fully proved, since level smoothness replaced unimodality);
- juntas (SYMMETRIZATION).

It would not refute the target r_4(N)=o(N/log N); it would close one route
to it. Points needing careful write-up:
1. Cochrane-type minorants for products, restricted to cosets.
2. The representative-independence of the index check, given drift.
3. Uniformity of all constants in k=C log(2/a), for every fixed C.
(Unimodality of G is no longer needed; see CANDIDATE_LEMMAS section 4,
"Smoothness replaces unimodality".)

## 7. Revised absorption: everything inside one box

Section 3 let index-step vectors grow, and then needed decay outside the
box: that is circular. Instead, fix H = r^(M') and absorb only vectors in
B_H = [-H,H]^k.

- **Rule.** While some m in B_H \ L' has Phi_out(x_m) < T, add m to L' and
  add its bad indices and run tops to S'.
- **Termination** (checked: verify_coset_lemmas_20261002.py, 2094 rank and
  100 index cases):
  - if m is outside span_Q(L'), the rank rises and covol(L') is multiplied
    by at most |m|_2 <= sqrt(k) H;
  - otherwise covol(L') is divided by an integer at least 2.
  - covol >= 1, so there are at most k + k log_2(sqrt(k) H) = O(log^2 r)
    steps. Every absorbed vector has |b| <= H.
- **Final state.** Every m in B_H \ L' has Phi_out(x_m) >= T, hence
  |E[e(m.Phi) | n, W]| <= e^(-T/2) r^(O(1)). This uses the decay lemma
  for the single count vector n_out of the coordinates outside S'
  (Fourier inversion over count vectors costs (r+1)^3), and dividing by
  P(n_out) >= r^(-O(1)) for n in the narrow window N_r below.

**Typical window (correction).** "Typical" here must mean the narrow
window N_r = {|n_d - r/4| <= sqrt(r log r)}, not the window
|n_d - r/4| <= sqrt(r) log r used for mass estimates elsewhere. On the wide
window, P(n) gets as small as exp(-c log^2 r), and e^(-T/2) cannot absorb
dividing by that.
- On N_r, the local CLT gives P(n) >= r^(-8-3/2-o(1)).
- Hoeffding with a union bound gives P(n not in N_r) <= 8 r^(-2), which is
  o(a^2/log r) since a ~ r^(-3/4).
- Split f_2 = f_2 1_(N_r) + f_2 1_(not N_r). Both pieces are still functions
  of n, so the symmetrization argument applies to the first. The second
  has energy at most E[f_2^2 1_(not N_r)] <= 8 r^(-2) by contraction.
- n_out moves by at most |S'| = polylog, so this costs nothing.
- C_0 in T must exceed 2(19/2 + 3 + O(1)), which is still O(log r).

Checked exactly (`verify_typical_window_20261002.py`, r = 100, 400, 900,
1600). The worst exponent -log P(n)/log r on N_r is 10.2, 9.5, 9.6, 9.5
(asserted <= 12). On the wide window it is 17.6, 47.1, 68.0, 67.4 (it stops
growing only because n_d >= 0 truncates the window). The atypical mass is
6e-6, 1.6e-7, 1.0e-8, 2.3e-9, against the bound 8/r^2.

No representative choice is needed. Every frequency that occurs below lies
in B_H, and each is either in L' or decayed.

## 8. Cosets, drift, and the two former open points

**Drift.** Given W, each b in L' has b.Phi = kappa_b(W) + eta_b(u) with
|eta_b| <= eps deterministically (run-top truncation). The nearest point
of the coset x_0 + K (K = Ann(L')) is at distance <= ||B^+|| eps sqrt(k),
and ||B^+|| <= (k H^2)^k = r^(O(log r)) because |b| <= H and BB^T is a
positive-definite integer matrix. Take eps = r^(-C log r), that is
g = O(log^2 r) run-top digits. Then:
- for m in L' ∩ B_H, e(m.Phi) = e(m.x_0) + O(r^(-M));
- every trigonometric polynomial of degree <= H moves by O(r^(-M)) under
  projection to the coset.

**Coordinates.** For each j let q_j be the order of e_j in Z^k/L' (q_j=1
for individually structured phi_j).

- q_j <= H^(1/2): on the coset theta_j takes the values x_0j + l/q_j. The
  arc indicator is an exact polynomial in e(theta_j) of degree < q_j, with
  coefficient l^1-mass O(log q_j). No smoothing, no boundary.
- q_j > H^(1/2), including q_j = infinity: sandwich by Selberg polynomials
  S_j^+- of degree H, with |S_j^+| <= 3. Haar measure on the coset pushes
  forward to Haar measure on T (q_j infinite, since e_j restricted to the
  identity component is a nontrivial character) or to the uniform measure
  on a coset of (1/q_j)Z. In both cases (checked identity: averaging over
  (1/q)Z keeps only Fourier modes t with q | t)

      integral of (S_j^+ - S_j^-)(theta_j) = sum_{q_j | t, |t|<=H} (S^+-S^-)^(t) e(t x_0j)
                                           <= 2/(H+1) + 4/q_j <= 6 H^(-1/2).

**Product minorant (point 1).** The pointwise inequality

    prod a_j >= sum_j b_j^- prod_{l!=j} b_l^+ - (k-1) prod_l b_l^+

(0 <= a_j, b_j^- <= a_j <= b_j^+; checked in 20000 random cases) holds on
the coset because it holds pointwise. With b = a for exact coordinates,
the boundary mass of a cell on the coset is at most
3^(k-1) k 6 H^(-1/2) = r^(-M'/2+O(C)).

**Index check (point 2).** Taken care of by section 7. Characters m in B_H
in the saturation of L' but not in L' are decayed, like all of
B_H \ L'. The Haar integral over x_0 + K of e(m.Phi) is e(m.x_0) for
m in L' and 0 otherwise. So for every cell, both P(V|n,W) and P(V|c,W) lie
within boundary + (C log H)^k e^(-T/2) r^(O(1)) of the same Haar value.

**Mismatch near endpoints.** For exact coordinates the true theta_j is
an atom plus delta_j with |delta_j| <= r^(-M). Membership can differ from
the atom's only if an atom lies within r^(-M) of an endpoint. Then the
membership is a threshold on the drift, a linear form with geometric
run coefficients. Refining W by g' further digits of the dominant run
decides it, except on mass poly(r) 4^(-g') (Cantor small-ball bound,
CELL_BOOKKEEPING section 4). If the drift vanishes identically there is
no mismatch.

## 9. Assembly

Let G be the junta partition (u_(S'), sigma mod 15), refined as above, and
U the undecided set. Orthogonally,

    ||E(f_2 | F v G)||^2 = ||E(f_2|G)||^2 + sum_W P(W) ||E(g_2|F v G)||^2_W,

with g_2 = f_2 - E(f_2|W) on W. On each W, f_2 depends only on n_out, so
it is symmetric in the coordinates outside S'. The symmetrization identity
inside W gives ||E(g_2|F)||^2_W <= Var(f_2|W) E_n chi^2_n(W). Hence

    energy <= 2 Y_G^2 + 2 E[f_2^2] max_(good W) E_n chi^2_n(W)
              + 2 E[(1_A+w) 1_U] + 16 r^(-2),

where the last term is the atypical part (section 7, typical window).

- Y_G^2: density-free junta bound, o(a^2/log r) since |S'| = polylog
  (PARAMETER_AUDIT section 3).
- chi^2_n(W) <= r^(-M'') for good W: thin cells are bounded as in section 4,
  and every other cell has relative deviation r^(-M'/4+O(C)).
- E[f_2^2] <= a.
- U: E[1_A 1_U] <= w mu(U) + Y_G mu(U)^(1/2), with mu(U) = r^(-M).

**Parameters.** H = r^(M') with M' = O(C);
T = 2k log(C log H) + C_0 log r = O(log r log log r); g = O(log^2 r);
there are O(log^2 r) steps, so |S'| = O(log^5 r log log r).

If every step above holds, every factor of C log(2/a) quarter-arc
characters has energy o(a^2/log(2/a)) on the candidate. The candidate then
refutes the window energy lemma in the base-16 realization with the full
cutoff, and the target r_4(N) = o(N/log N) is unaffected.

**Remaining risk.** This is a complete sketch, not a checked proof. Before
anything is cited, it needs:
- an independent line-by-line check;
- ~~explicit Selberg constants~~ DONE. With Vaaler's polynomial V_N and
  the error bound |V_N - psi| <= Delta_(N+1)/(2N+2) (Vaaler 1985), take
  S^(+-) = (beta-alpha) + V(x-beta) - V(x-alpha)
           +- (Delta(x-beta) + Delta(x-alpha))/(2N+2).
  Then:
  - |S^(+-) - 1_I| <= 2 sup Delta/(2N+2) <= 2, so |S^(+-)| <= 3;
  - the coefficients of S^+ - S^- are (1-|t|/(N+1))(e(-t beta) + e(-t alpha))/(N+1),
    so each has size at most 2/(N+1);
  - the sum over q | t is at most 2/(N+1) + 4/q;
  - the Z_q interval indicator has l^1 Fourier mass at most 2 + log q.
  Checked (`verify_selberg_constants_20261002.py`): sandwich violation 0,
  observed sup 1.28, coefficient ratio exactly 1.0, arithmetic-sum ratio
  0.42, Z_q mass at most 0.43 (2 + log q).
- ~~an explicit typical-n window~~ DONE, with a correction (section 7). The
  window must be sqrt(r log r), not sqrt(r) log r.

What remains is the independent line-by-line check. No numerical input is
left in the sketch.

## 10. Checks (formerly section 6)

`python3 verify_two_run_20261002.py` (about 1 second): the section 2
example for r=16 to 40, asserting Psi <= 0.5, Phi >= 0.9 r(d/2)^2, and the
fast decay for (3,7) and (0,5). Output: two_run_verification_20261002.json.
The coset argument itself is asymptotic and has no finite check.
`python3 verify_coset_lemmas_20261002.py` (under 1 second) checks the
elementary facts of sections 7-8: the product minorant (20000 cases), the
(1/q)Z averaging identity (300 cases), and covolume behaviour under rank
and index absorption (2094 and 100 cases, exact rational arithmetic).
Output: coset_lemmas_verification_20261002.json.
