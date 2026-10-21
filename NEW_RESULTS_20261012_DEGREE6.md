# Degree-six continuation: new results — 12 October 2026

**(D) NEW RIGOROUS PARTIAL THEOREM.** SELECT and the local r4 target remain
unresolved. No actual counterexample or complete proof is claimed.

PROVED in DEGREE_SIX_ATTACK_20261012.md:

1. All cardinality-preserving fifth/sixth extensions of the October 12
   fourth moments admit the exact parametrization (23), with new harmonic
   corrections z_5 and z_6. The canonical choice sets both corrections zero.
2. That canonical choice fails at degree five: on a five-point progression,
   for n>=400 and k>=5, m_5^0<-ρ_5/4, whereas an AP multiplier forces zero.
3. An explicit degree-six SOS certificate gives
   L(H_v²)>=[mρ_3]²/(1-a) for a vertex's m completing triples.
4. Any degree-six PSD extension must have average disjoint-completion
   sixth moment >=ρ_6+a^7/8 whenever k>=6 and m a^4>=36. This exposes
   a required positive correlation absent from the canonical lift.
5. A degree-eight sum-of-squares identity proves the global completion
   energy inequality (31) for every fixed-size AP-free Boolean set.
6. The direct relative Fourier inequality (32) ties residual coefficients
   to completion mean, variance and spectral l1 mass. Its sufficient
   estimates (33) are unproved, so it does not establish SELECT.
7. Cardinality plus nonnegative moments through degree k gives a global
   k-subset law; cap products through degree k+2 enforce pointwise caps.
   This endpoint is too large to give the desired quantitative proof.

AUDITED: the previous degree-four theorem and verifier remain valid.
The verifier rerun is identical to the preserved prior output.

EXACT FINITE CERTIFICATE: the averaged-trade moments at p=23, k=5
have a global law on AP-free five-sets, with 19 positive rational
affine-orbit weights. This gives an all-degree extension in this small
instance, below the n>=200 theorem range. The weights are in
degree_six_finite_extension_20261012.json and are independently verified
by expanding the distribution. It is not an asymptotic counterexample.

OPEN: simultaneous feasibility of the corrections z_5,z_6 under cubic
PSD, local laws, AP multipliers and degree-six Fourier-cap localizers.
The canonical failure must not be promoted to infeasibility of all such
extensions. No degree-eight feasible extension is asserted.

Verification is saved in DEGREE_SIX_VERIFICATION_20261012.json; the separate
script is verify_degree_six_20261012.py. Exact symbolic proofs establish the
asymptotic claims; the large scalar witness is checked by rational bounds,
not by enumerating its ambient group.
