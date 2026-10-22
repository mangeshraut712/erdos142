# Failed approaches: October 22 audit

**Status: OPEN; outcome D, partial results only.** Updated 22 October 2026.
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, P12 and W8 remain
unproved. The October 21 closure and effective-rate claims are withdrawn
because of missing proof steps, not merely pending external peer review.

Read the [authoritative proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md) and
[current checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261022.json).

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


## Previous record

The [superseded pre-correction version](history/proof_audit_20261021/before_updates/FAILED_APPROACHES.md) is preserved verbatim. Earlier dated sources remain in [docs/audits/](docs/audits/) and [history/](history/).
