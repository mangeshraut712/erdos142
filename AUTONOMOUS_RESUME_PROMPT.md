# Resume prompt

**Status: OPEN; outcome D, partial results only.** Updated 24 October 2026.
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, P12 and W8 remain
unproved. The October 21 closure and effective-rate claims are withdrawn
because of missing proof steps, not merely pending external peer review.

Read the [authoritative proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md) and
[current checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261024.json).

For genuinely eligible AP-free hosts under failed adequate phase selection,
prove `E_F(u)<=2U^2+2R3+a^4wmu`, where `U=wa(1-a)`, or prove adequate
phase selection directly. Use the pointwise completion identities `Bq_j=0`
together with T5, logarithmic density, original weight, and exact diagonals.
Retain the cubic term. Do not replace one-sided pair bounds by equalities.

A direct completion route needs a uniform cross-spectrum concentration
bound and control of the orthogonal residual, plus the small/zero completion
mean branch. The exact frame alone does not provide any of these.

Resume from the October 24 checkpoint. The previous claimed closure is
withdrawn; do not restore it from historical notes or green CI. Current
verification selects 23 current and 13 legacy scripts. Lean files contain
an admitted lemma and four additional axioms; neither Lean compilation nor
a complete formal proof has been established. No background work is implied.

## October 23 research continuation

Resume from the October 23 checkpoint and LM23 note. The low-mean moment interval is sharp and permits zero mean at small density; VB23 is a valid upper variance bound but insufficient for compression. Next attack overlapping allowed triples under failed phase selection. Preserve the October 21 withdrawal. The current suite now selects 23 current and 13 legacy scripts; finite tests do not prove selection. No background research continues after this execution.

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

## Previous record

The [superseded pre-correction version](history/proof_audit_20261021/before_updates/AUTONOMOUS_RESUME_PROMPT.md) is preserved verbatim. Earlier dated sources remain in [docs/audits/](docs/audits/) and [history/](history/).
