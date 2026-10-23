# Research journal: 22 October correction

**Status: OPEN; outcome D, partial results only.** Updated 23 October 2026.
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, P12 and W8 remain
unproved. The October 21 closure and effective-rate claims are withdrawn
because of missing proof steps, not merely pending external peer review.

Read the [authoritative proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md) and
[current checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261023_overlap.json).

The repository was found at commit 51854a2 with closure and effective-rate
claims. Independent mathematical audits identified missing estimates,
a reversed norm inequality, an arithmetic error in the correlation bound,
and a discarded hypothesis in the supposed P12 refutation. These claims
are withdrawn. Exact identities were retained and finite regression checks
were added. Source drafts, old public summaries, and their hashes are
preserved; the current result is not a solution of the target.

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

October 23 cycle: reconstructed P12/W8 and exact diagonals; solved the occupancy feasibility problem; expanded an explicit zero-mean law; proved the bounded-completion variance upper bound; isolated extendable-triple exclusion at m=0. Independent rational enumeration passed 26,477 assertions. No proof of the unconditional target or eligible asymptotic counterexample resulted.

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

The [superseded pre-correction version](history/proof_audit_20261021/before_updates/RESEARCH_JOURNAL.md) is preserved verbatim. Earlier dated sources remain in [docs/audits/](docs/audits/) and [history/](history/).
