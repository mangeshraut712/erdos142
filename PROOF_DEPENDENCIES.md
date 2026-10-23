# Proof dependencies

**Status: OPEN; outcome D, partial results only.** Updated 23 October 2026.
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, P12 and W8 remain
unproved. The October 21 closure and effective-rate claims are withdrawn
because of missing proof steps, not merely pending external peer review.

Read the [authoritative proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md) and
[current checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261023.json).

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

Dependency chain: exact frame and completion identities -> MISSING residual
and spectral concentration bounds -> MISSING DIRECT-Q-GAIN -> conditional
increment iteration -> local target. The first arrow has not been proved.
The proposed explicit rate and higher-degree selection claims depend on
that missing arrow and are not established. Qualitative Szemerédi is an
external classical input only to the positive-density branch reduction.

## October 23 research continuation

The new note contains a Mermaid dependency graph and all residual/diagonal definitions. Shortest route: prove P12/W8 under failed selection on reachable hosts, contradict the AP counting identity, then use the proved direct-cell iteration and terminal bound. Alternatively prove DIRECT-Q-GAIN. Completion methods must resolve both mean regimes.

[Exact statements, proofs, obstruction and dependency graph](docs/audits/LOW_MEAN_MOMENT_CONE_20261023.md).

## Previous record

The [superseded pre-correction version](history/proof_audit_20261021/before_updates/PROOF_DEPENDENCIES.md) is preserved verbatim. Earlier dated sources remain in [docs/audits/](docs/audits/) and [history/](history/).
