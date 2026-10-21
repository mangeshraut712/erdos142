> **17 October 2026 recovery:** The latest operative frontier is in
> [CURRENT_STATUS.md](CURRENT_STATUS.md), [OPEN_LEMMAS.md](OPEN_LEMMAS.md),
> and [RESUME_AUDIT_20261017.md](RESUME_AUDIT_20261017.md). The late-16-October
> pair theorem reduces the gap to R_3^F+R_4^F; DIRECT-Q-GAIN replaces the
> stronger old threshold. The target remains OPEN. Earlier entries below
> are historical and retain their original scope and later corrections.

# Offline Erdős 142 research attempt — 2026-09-06

STATUS: (E) OPEN — SINGLE FINAL OBSTRUCTION

Mixed factors completed as a sketch (2 October):
[MIXED_FACTORS_20261002.md](MIXED_FACTORS_20261002.md) sections 7-9 write
out the two open points. Absorption is confined to a fixed box (the
covolume bounds the steps, removing the circularity). Low-order coordinates
are exact Z_q polynomials, and product minorants hold pointwise on cosets.
They also assemble the energy bound. This is a complete sketch, NOT an
independently checked proof. Run `python3 verify_coset_lemmas_20261002.py`
and `python3 verify_selberg_constants_20261002.py`. The second checks the
explicit Selberg/Vaaler constants (|S±| <= 3, coefficient bound 2/(N+1),
Z_q l¹ mass <= 2 + log q). Correction: in the decay step the typical
count window must be |n_d - r/4| <= sqrt(r log r), where P(n) >= r^(-O(1)).
On the wider window sqrt(r) log r, P(n) gets as small as exp(-c log² r).
Run `python3 verify_typical_window_20261002.py` (exact multinomials).

Parameter audit (2 October):
[PARAMETER_AUDIT_20261002.md](PARAMETER_AUDIT_20261002.md) checks every
threshold for fixed C. It corrects the density of the random-alteration B
(a ~ r^(-3/4), not r^(-1/2)), which broke the old junta allowance, and
proves a density-free junta bound Y^2/a^2 <= 16 s log^2 r/r + O(s^4 log^4 r/r^2).
The leading term matches the exact energies to 1e-6. Only the mixed-factor
sketch remains. Run `python3 verify_parameter_audit_20261002.py` and
`python3 verify_linear_junta_20261002.py`.

Mixed factors (2 October, PROOF SKETCH):
[MIXED_FACTORS_20261002.md](MIXED_FACTORS_20261002.md) sketches how to
bypass the basis lemma. Condition on the structured phases, work on a coset
of the torus, and bound absorption steps by covolume rather than by
coefficients (O(log^2 r) steps, polylog junta). It also corrects the
structure detector: use the single-centre sum, not Psi; checked by
`python3 verify_two_run_20261002.py`. If the sketch survives a careful
write-up, the symmetric candidate refutes the window energy lemma. The
balance step no longer needs a numerical input: level smoothness replaced
unimodality (`python3 verify_level_smoothness_20261002.py`). The target
r_4(N)=o(N/log N) is unaffected.

Generic factors (2 October):
[GENERIC_FACTORS_20261002.md](GENERIC_FACTORS_20261002.md) proves the
chi-square form, energy <= a * E_n chi^2(Law(cell|n) || Law(cell|sigma mod 15)).
It also proves that strongly generic factors (all combinations with
Psi >= O(log r log log r)) have energy O(a k^2/r^2). For mixed factors the
absorption runs without a tower, and everything reduces to one OPEN basis
lemma: bounded coefficients for the structured combination lattice. Run
`python3 verify_chi_square_20261002.py`.

Symmetrization (2 October):
[SYMMETRIZATION_20261002.md](SYMMETRIZATION_20261002.md) proves that, for
permutation-invariant A, the energy of any factor is controlled by how
cell probabilities depend on the count vector under the uniform measure.
Consequences: step 1 (junta plus residue) is PROVED for juntas of size
o(sqrt(r)/log r), and every factor of exceptional characters is PROVED to
have energy o(a^2/log(2/a)) on the balanced candidate. What remains is a
statement about the uniform measure alone (generic characters). Run
`python3 verify_symmetrization_20261002.py`.

Orbit decay and rational classes (2 October):
[RATIONAL_CLASSES_20261002.md](RATIONAL_CLASSES_20261002.md) proves a
gamma-free Fourier decay, |E[1_T(n) e(xX)]| <= (r+1)^2
exp(-(1/2) sum ||15*16^i x||^2). Corollary: residues X mod q reveal only
sigma mod gcd(q,15) beyond juntas, with decay constant >= 1/(4q^2), tight
at q=17 (a smeared parity of sigma). The mixed-factor counting problem
stays OPEN. Run `python3 verify_rational_classes_20261002.py`.

Cell bookkeeping (2 October):
[CELL_BOOKKEEPING_20261002.md](CELL_BOOKKEEPING_20261002.md) proves that,
for the symmetric candidate, factors built from exceptional characters
reduce to junta-plus-residue equidistribution with polylog juntas and no
small-cell loss, needing only relative error o((log r)^(-1/2)). Generic
and mixed factors stay OPEN: aliasing of multiples, and a tower
obstruction showing naive regularization overshoots at k of order log r.
Run `python3 verify_cell_bookkeeping_20261002.py`.

Junta plus residue (2 October): for the symmetric candidate, conditioning
on up to 6 coordinates together with sigma mod 15 adds energy linearly in
the number of coordinates, with slope 0.286/r, 0.234/r, 0.128/r at r=100,
300, 600 (see CANDIDATE_LEMMAS_20261002.md section 5, step 1). Evidence
that polylog-size juntas cost o(1/log r); not a proof. Run
`python3 verify_junta_residue_20261002.py`.

Candidate lemmas (2 October):
[CANDIDATE_LEMMAS_20261002.md](CANDIDATE_LEMMAS_20261002.md) proves a
Fourier-decay bound for count-symmetric sets on the base-16 window and a
digit lemma showing the only escaping frequencies are "mod-15 character
plus a few-digit junta"; proves asymptotic mod-15 balance for a random
4-AP-free B (one numerical input). Two steps remain before the candidate
refutes the window energy lemma. Run `python3 verify_candidate_lemmas_20261002.py`.

Symmetric candidate (2 October):
[SYMMETRIC_CANDIDATE_20261002.md](SYMMETRIC_CANDIDATE_20261002.md)
gives a provably 4-AP-free, permutation-symmetric set of density about
r^(-1/2) in a rank-(r+1) window {0,1,2,3}^r that meets the full cutoff.
Its energy on digit juntas is negligible and on the sigma mod 15 class
falls to 0.4 times the target scale by r=600. Generic characters and
asymptotic balance are unproved: a CANDIDATE against the window energy
lemma, not a refutation. Run `python3 verify_symmetric_balance_20261002.py`.

Bounded-rank vacuity (2 October):
[BOUNDED_RANK_VACUITY_20261002.md](BOUNDED_RANK_VACUITY_20261002.md)
shows (with one cited geometry-of-numbers input) that windows of any fixed
rank embed into integer intervals with constant loss, so under the target
they hold no 4-AP-free sets of density eps/log n. Window counterexamples
need rank tending to infinity, as both existing ones have (rank ~ log n).
An interval-window energy experiment up to n=16000 finds only a boundary
effect. Run `python3 verify_interval_window_energy_20261002.py`.

Mod-3 increment refuted (2 October):
[MOD3_INCREMENT_20261002.md](MOD3_INCREMENT_20261002.md) shows three
far-apart translates of a 4-AP-free set stay 4-AP-free and are exactly
balanced mod 3, so mod-3 classes alone give no increment; an exact extremal
set at n=30 is balanced too. Slab/character cells are required. Run
`python3 verify_mod3_increment_20261002.py`.

Window lattice model (2 October):
[WINDOW_LATTICE_MODEL_20261002.md](WINDOW_LATTICE_MODEL_20261002.md)
proves every rank-r controlled window is 4-AP-isomorphic to the lattice
points of a convex body in Z^r, that such sets contain a 4-AP once they
exceed 3^r points, and that a whole rank-(d+1) window of size 3^d is
4-AP-free. So the 3^r factor in the cutoff n>=8*3^r*a^(-3) is necessary.
Gives a sharp endpoint-pair supply |A|(8a^(-2)-1) under the cutoff. The
window energy lemma stays OPEN. Run `python3 verify_window_lattice_20261002.py`.

Structural result (2 October):
[VACUITY_OF_FULL_GROUP_OPEN_20261002.md](VACUITY_OF_FULL_GROUP_OPEN_20261002.md)
proves that the full-group (OPEN) statement follows from the target itself
and has non-vacuous content only if the target fails. Refuting it at density
eps/log p is therefore as hard as disproving r_4(N)=o(N/log N); by Green–Tao
it is vacuously true for a > C_0(log p)^(-c_0). Counterexample effort belongs
in the hereditary/window version. Literature check: no published bound gives
r_4(N)=o(N/log N). Run `python3 verify_vacuity_20261002.py`.

Rank-one hostile search (2 October):
[RANK1_HOSTILE_SEARCH_20261002.md](RANK1_HOSTILE_SEARCH_20261002.md)
finds that greedy and hostile 4-AP-free sets in Z_p (p up to 797) carry
no rank-one quarter-factor energy beyond the random-set noise floor; hostile
sets fall to 0.66 times it. Rank one alone cannot drive the open statement.
Finite diagnostics only. Run `python3 verify_rank1_hostile_search_20261002.py`.

Target-density continuation (14 September):
[TARGET_SCALE_ENERGY_BUDGET_20260914.md](TARGET_SCALE_ENERGY_BUDGET_20260914.md)
derives the exact conditional energy gain, the four-term Fourier expansion,
and a positive quadratic resonance giving many APs in the quadratic example.
It shows conditionally that fixed polylogarithmic rank and inverse-polylogarithmic
relative energy fit the iteration budget. The target-scale AP-free structural
input remains unproved. Run `python3 verify_target_scale_20260914.py`.

Latest full-group audit (14 September):
[FULL_GROUP_HOSTILE_AUDIT_20260914.md](FULL_GROUP_HOSTILE_AUDIT_20260914.md) proves ENERGY
for all sets with density at most p^(-1/4), with eta=1/4 and C=3,
using a base-four singleton factor. It also gives an explicit harmonic
cutoff bound, exact affine invariance, and the thinning host term.
The denser full-group range remains open; no general-window extension
or target proof follows. Run `python3 verify_full_group_hostile_20260914.py`.

Full-group audit of the energy theorem (14 September, later):
[FULL_GROUP_ENERGY_AUDIT.md](FULL_GROUP_ENERGY_AUDIT.md) settles the
Omega=Z_p specialization only in part. Proved: the theorem is trivially
true for p <= 4^(C log(2/a)) (the sparse end of its own cutoff); every
interval-supported Behrend/sphere set, every affine image, and every
random thinning is a trivial YES instance; the logarithmic-rank window
version implies r_3(N) <= N exp(-c (log N)^(1/4)) via the checkpointed
bridge; and rank a^(-c), c<1/2, at density >= epsilon/(2 log n) already
suffices for the r4 target. Neither a proof nor an eligible counterexample
in the nontrivial regime was found; the Freiman-embedded sphere family is
the one remaining full-group instance. Run
`python3 verify_full_group_energy.py` for its exact finite checks.

Latest endpoint-incidence audit (14 September):
[ENDPOINT_INCIDENCE_AUDIT.md](ENDPOINT_INCIDENCE_AUDIT.md) records the
orientation convention, growing-star entropy bounds, and the exact
middle-pair incidence Gram matrix. These do not prove the full-cutoff
arithmetic energy theorem. This continuation has status
**(E) OPEN — SINGLE FINAL OBSTRUCTION**. Run
`python3 verify_endpoint_incidence.py` for its exact finite diagnostics.

Latest AP-geometry result: [AP_RICHNESS_COUNTEREXAMPLE.md](AP_RICHNESS_COUNTEREXAMPLE.md)
shows that total AP richness and density-only direction-support/entropy
bounds still do not force relative coarse energy. A small AP-rich progression
can supply all nontrivial ambient APs while avoiding A entirely. The full
checkpoint-qualified energy lemma and the r4 target remain open. Run
`python3 verify_ap_richness.py` for exact supporting checks.

14 September update: [UNIFORM_ENERGY_COUNTEREXAMPLE.md](UNIFORM_ENERGY_COUNTEREXAMPLE.md)
refutes the newly proposed uniform energy lemma when it is quantified over
every controlled window without the checkpoint size/AP-availability cutoff.
It gives a deterministic infinite family at logarithmic relative density.
The cutoff-qualified energy lemma and r_4(N)=o(N/log N) remain open. Run
`python3 verify_energy_counterexample.py` for supporting exact finite checks.

Latest continuation (13 September 2026): [LOCALIZATION_BRIDGE.md](LOCALIZATION_BRIDGE.md)
proves the signed-compression-to-factor-energy bridge and a direct terminal
window bound, and corrects gaps in the previous conditional closing claim.
The required uniform arithmetic factor is still unproved. Run
`python3 verify_localization.py` for the new exact finite diagnostics.

No proof of r_4(N) = o(N/log N), no new asymptotic bound, and no claim of
research novelty resulted from this attempt. All mathematics was developed
offline. Auxiliary statements were proved algebraically and checked on finite
examples. The finite checks are not an asymptotic proof.

## Main verified auxiliary statements

Phase 2 independently verified the alpha^(3/2) lemma and reset the arithmetic
inverse threshold to C<4/3. It also proved that a uniform correlation bound
in the **actual** U3 norm with C<2 is impossible even in the stipulated
AP-free density regime. The direct density-sensitive correlation target
remains open. See [PHASE2_AUDIT.md](PHASE2_AUDIT.md) for the complete proofs,
normalization obstruction, and exponent ledger. Run `python3 verify_phase2.py`
for the new finite checks, including an eligible 28-element set in Z_101.

The signed-branch continuation is in [SIGNED_RESEARCH.md](SIGNED_RESEARCH.md).
It records the exact endpoint operator and conditional endpoint distribution,
the nonnegative quadratic-phase Rayleigh identity, popular negative fibers,
and concentration/mass-retention bookkeeping. The target remains open:
no sufficient arithmetic increment follows yet. Run `python3 verify_signed.py`
for its exact subset checks and separately labelled Fourier diagnostics.
Hostile review also disproved a proposed universal near-full-mass increment
on integer progressions; the affine-spreading counterexample and the
replacement relative-window identity are preserved in that report.

Use normalized averages on Z_p, p > 3 prime, f = 1_A - alpha, and
b = alpha(1-alpha). A is progression-free for nonzero differences.

1. The exact indicator count is alpha/p, including the diagonal. The
   endpoint-balanced expansion and a mixed Cauchy–Schwarz inequality give

   ||f||_(U3)^2 >= max(0, alpha^3 - 1/p)/(1 + 2 sqrt(b)).

   In particular, p alpha^3 >= 2 implies ||f||_(U3) >= alpha^(3/2)/2.
   This improves the crude starting estimate supplied in the request. Its
   novelty is not claimed, and it supplies no density-increment scale.

2. For a fixed shift, put c = E f(x)f(x+h), theta = alpha^2+c,
   t = alpha-theta, z = 1-2alpha+theta, gamma = b+c. For gamma > 0,

   R = f(x)f(x+h) - c - (1-2alpha)c/gamma * (f(x)+f(x+h)).

   Its four atom values are (t theta, -z theta, -z theta, t z)/gamma,
   and its squared L2 norm is t z theta/gamma. Every four-atom function
   orthogonal to 1, f(x), f(x+h) is a scalar multiple of R. With a missing
   atom, that orthogonal space is zero in weighted L2. Complementary and
   constant pairs cover gamma = 0 and also have zero residual.

3. Write W_xi = |fhat(xi)|^2, S = sum W_xi^2, and

   D = S^2 - sum_(k,xi) W_k^2 W_xi W_(xi-k).

   Then, for b,S > 0,

   D = (1/2) sum_(k,xi) W_k^2 (W_xi-W_(xi-k))^2,
   D/S^2 >= S/b^2 >= 1/(p-1),
   D/S^2 >= (2/625) * (1-b^2/(pS)).

   If D/S^2 < 2/625, the stronger conclusion is
   1-b^2/(pS) <= (5/4) D/S^2.

   The last statement follows by setting mu = W^2/S, proving approximate
   convolution idempotence of mu, showing its high Fourier eigenvalues form
   a subgroup, and using primality plus mu(0)=0. Probability eigenvalues
   use SUM_k mu(k)e_p(-tk), not a normalized average.

## Explicit rejected shortcuts

- Z_7, A={0,1,3}: two identical successive residual input pairs give
  different two-step residuals. No deterministic composition from those
  inputs holds in general.
- Z_5, A={0,1}: E R_1(x)R_1(x+2) = 4/245 > 0. The sign of the forbidden
  pair-indicator correlation cannot be passed to the residual alone.
- The same Z_5 example has nu_2(0)=4/5 but (nu_1*nu_1)(0)=41473/83205,
  for nu_h proportional to |Fourier(f(x)f(x+h))|^4.
- Z_13, A={0,1,3,9}: all nonzero ordered differences occur once. This
  progression-free set has exactly flat nonzero squared Fourier magnitudes.
- For g=(1,1/2,1/2,1/2,1/2) on Z_5, Lambda_4(g)=7/50 and U3(g)^8=11/625.
  Thus the proposed general strengthening |Lambda_4(g)| <= U3(g)^4 fails.

## Verification

Run with the Python standard library:

    python3 verify_core.py

The captured result is in verification.json. The script checks all 2,208
subsets in Z_5, Z_7, Z_11, plus the Z_13 difference-set example. Extra atom
checks on Z_4 and Z_6 cover complementary-pair degeneracies. It also checks
276 general nonnegative even spectral arrays. Exhaustive identities use
exact rational arithmetic. The radical Fourier-probability values receive
a separate floating-point check with tolerance 1e-12.

## Unresolved step

There is no proved mechanism turning these estimates into a density
increment on a sufficiently large set. In a hypothetical iteration with
density gain c alpha^s and logarithmic size loss C alpha^(-t), s >= 1,
t >= 0, the total loss has order alpha^(-(s+t-1)) when s+t-1 > 0.
To obtain little-o at alpha = epsilon/log N for every fixed epsilon > 0,
this model needs exponent below 1, or a further saving at the endpoint.
No such increment theorem was established here.
