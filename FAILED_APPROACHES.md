# Failed approaches: October 22 audit

**Status: OPEN; outcome D, partial results only.** Updated 24 October 2026.
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, P12 and W8 remain
unproved. The October 21 closure and effective-rate claims are withdrawn
because of missing proof steps, not merely pending external peer review.

Read the [authoritative proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md) and
[current checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261024.json).

Withdrawn October 21 steps:

- Reversing the completion variance lower bound to an upper bound.
- Dropping R3 from the completion-mean identity.
- Inferring individual spectral alignment from a negative total inner product.
- Assuming that ceil(1/a) phases capture a fixed fraction without proof.
- Treating tent decay as an exact quadratic spectral cutoff with a logarithmic gain.
- Treating the intended AP-free contradiction as a refutation of conditional P12.
- Extrapolating a numerical constant from 27 ineligible finite examples.
- Calling Lean code with `sorry` and extra axioms a completed formal proof.

The exact Boolean expansion, weighted pair near-positivity, twelve-slot
7/11 terminal ceiling under M13, completion projection identities, and
quartic covariance identity remain available with their stated hypotheses.
The October 19 positive-density reduction explicitly invokes classical
qualitative four-term Szemerédi and supplies no quantitative rate. The
October 19 covariance obstruction contains a 4-AP and does not refute P12.

The valid tight-frame identity and triangle-inequality certificate do not
prove phase concentration or a small coefficient norm. Completion-mean
positivity on the eligible domain and the small/zero-mean alternative are
unresolved. The new correction proves the universal Boolean chirp fourth
moment identity and records finite counterchecks to auxiliary overclaims.


## October 23 research continuation

October 23: solving the complete one-edge moment problem does not force a positive completion mean at small density; an explicit zero-mean law blocks a local SOS proof from those premises. The valid bounded-degree variance upper bound is too weak at m of order mu a^3. Zero mean forbids only extendable positive-weight triples, not arbitrary three-APs. None of these failures refutes DIRECT-Q-GAIN.

[Exact statements, proofs, obstruction and dependency graph](docs/audits/LOW_MEAN_MOMENT_CONE_20261023.md).

## October 23 overlapping-progression results

**OD23:** For actual cyclic four-AP-free A and the original bounded weight,
q(v)<=2aw and Var_Omega(q)<=2aw m-m^2, improving the previous constants.
The proof uses mutually exclusive completion triples at directions h and 2h.
**CL23:** Consistent local Boolean laws on every set of at most floor(1/a)+1
vertices have marginal a, pair moments a^2, zero triples, and residual
R3+R4=-a^4 on each four-coordinate edge. These are local probability laws,
not eligible arithmetic counterexamples. OC23 provides the exact modular
overlap parameterization and finite joint occupancy polytopes.

P12, W8 and DIRECT-Q-GAIN remain OPEN. The degree improvement gives no
positive mean or sufficient phase gain. Next attack a density-dependent
family of overlaps using global consistency or failed phase selection;
a fixed finite overlap alone cannot exclude CL23.

[Proofs, exact slack identity, audit and updated dependency graph](docs/audits/OVERLAP_CONSTRAINTS_20261023.md).

## October 24 growing-system results

PC24 proves that an occupied pair has at most nine possible third vertices
in a four-AP completion triple. GI24 constructs actual zero-completion
subsets of every n-vertex pattern of size at least (2sqrt(2)/9)n/sqrt(n-1).
IE24 proves the weighted completion incidence bound ||K||^2<=72aw/p,
with counting Euclidean norms. These do not supply sufficient phase gain.

The factorial threshold beyond n~1/a forces arbitrary triples, while
completion triples form a sparse arithmetic subfamily. The missing
transfer between those quantities remains OPEN. Next apply the incidence
operator to centered occupied-pair data under failed phase selection,
retaining the contribution of triples without arithmetic extensions.
The October 21 closure remains withdrawn; no eligible counterexample exists
in these new checks and no proof of the local target is claimed.

[Precise statements, proofs, failed attacks and dependency graph](docs/audits/GROWING_OVERLAP_SYSTEMS_20261024.md).

## October 24 bilinear-pair incidence obstruction (BP24)

Attempting to obtain the diverging phase factor F_epsilon(a) -> infinity in DIRECT-Q-GAIN
via the occupied-pair incidence operator K fails because of a universal a^(3/2) ceiling:
|E_Omega[psibar Kf]| <= 6w a^(3/2). Furthermore, hole-support annihilation B(v) K(v, c) = 0
forces u(v) = -a on the entire row support of K, causing exact spatial decoupling
<u, Kf> = -a <g, f> that erases all spatial phase variations of u.

[Exact proofs and ceiling audit](docs/audits/BILINEAR_PAIR_INCIDENCE_20261024.md).

## October 24 multi-scale Bohr overlap obstruction (MS24)

Attempting to bypass the single-host hole-support obstruction by coupling across
multiple Bohr hosts Omega_1, Omega_2 fails. Pointwise hole support B(v) K_{1->2}(v, c) = 0
and spatial decoupling <u_1, K_{1->2} f> = -a_1 <g_{1->2}, f> hold universally for
arbitrary pairs of hosts. Density discrepancy shifts u_1 - u_2 are constant and vanish
against zero-mean phase functions, while quadratic phases with distinct coefficients
c_1 != c_2 are asymptotically orthogonal across overlapping Bohr domains.

[Exact proofs and multi-scale audit](docs/audits/MULTISCALE_BOHR_OVERLAPS_20261024.md).

## Previous record

The [superseded pre-correction version](history/proof_audit_20261021/before_updates/FAILED_APPROACHES.md) is preserved verbatim. Earlier dated sources remain in [docs/audits/](docs/audits/) and [history/](history/).
