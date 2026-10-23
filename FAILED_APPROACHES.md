# Failed approaches: October 22 audit

**Status: OPEN; outcome D, partial results only.** Updated 23 October 2026.
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, P12 and W8 remain
unproved. The October 21 closure and effective-rate claims are withdrawn
because of missing proof steps, not merely pending external peer review.

Read the [authoritative proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md) and
[current checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261023_overlap.json).

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

## Previous record

The [superseded pre-correction version](history/proof_audit_20261021/before_updates/FAILED_APPROACHES.md) is preserved verbatim. Earlier dated sources remain in [docs/audits/](docs/audits/) and [history/](history/).
