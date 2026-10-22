# Open lemmas

**Status: OPEN; outcome D, partial results only.** Updated 22 October 2026.
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, P12 and W8 remain
unproved. The October 21 closure and effective-rate claims are withdrawn
because of missing proof steps, not merely pending external peer review.

Read the [authoritative proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md) and
[current checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261022.json).

DIRECT-Q-GAIN requires: for each epsilon>0, constants and a function
F_epsilon(a)>=1 tending to infinity as a->0, chosen uniformly before all
eligible instances, such that delta>=c_epsilon a^(3/2) F_epsilon(a).
Eligibility includes actual cyclic 4-AP exclusion, mixed interval hosts,
`r[log(1/w)+log(48r)+loglog p]<=log p/100`, and
`epsilon/(2log|Omega|)<=a<=4/5`, with r>=1.

The original P12 statement retains its failed-selection antecedent.
AP exclusion giving the opposite signed bound is its intended contradiction,
not a refutation of that conditional implication. No eligible counterexample
has been supplied. The positive-density failure branch is excluded using
classical qualitative Szemerédi; an eligible a->0 failure sequence remains
possible. The finite correction examples fail T5 and prescribed H.

For genuinely eligible AP-free hosts under failed adequate phase selection,
prove `E_F(u)<=2U^2+2R3+a^4wmu`, where `U=wa(1-a)`, or prove adequate
phase selection directly. Use the pointwise completion identities `Bq_j=0`
together with T5, logarithmic density, original weight, and exact diagonals.
Retain the cubic term. Do not replace one-sided pair bounds by equalities.

A direct completion route needs a uniform cross-spectrum concentration
bound and control of the orthogonal residual, plus the small/zero completion
mean branch. The exact frame alone does not provide any of these.


## Previous record

The [superseded pre-correction version](history/proof_audit_20261021/before_updates/OPEN_LEMMAS.md) is preserved verbatim. Earlier dated sources remain in [docs/audits/](docs/audits/) and [history/](history/).
