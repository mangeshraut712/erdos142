# Offline Erdős 142 research attempt — 2026-09-06

STATUS: (E) OPEN — SINGLE FINAL OBSTRUCTION

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
