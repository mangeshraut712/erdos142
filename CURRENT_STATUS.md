# Current research status — 21 October 2026

**Outcome (D): NEW RIGOROUS PARTIAL THEOREMS.** The unconditional target
`r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, and O2/(P12) remain **OPEN**.
No eligible P12 counterexample or unconditional selection theorem is claimed.

Publication checkpoint: 21 October 2026; mathematical frontier: 19 October.
The current account is [O2_CONTINUATION_20261019.md](docs/audits/O2_CONTINUATION_20261019.md).
The exact restart state is [AUTONOMOUS_CHECKPOINT_20261021.json](checkpoints/AUTONOMOUS_CHECKPOINT_20261021.json).
Earlier dated reports and checkpoints are preserved as research history.

## Positive-density reduction on 19 October

The positive-density failure branch is now ruled out uniformly on the
whole T5 domain. The proof transfers the classical qualitative four-term
Szemerédi theorem through the finite-pattern terminal estimate; that
classical dependency is explicit and no quantitative rate is claimed.
See [POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md](docs/audits/POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md).
Failure of DIRECT-Q-GAIN is therefore equivalent to an eligible sequence
with a tending to zero and bounded delta/a^(3/2). The logarithmic-density
case remains OPEN. Its finite envelope verifier passed 18,022 checks.

## Covariance obstruction on 19 October: AP exclusion is essential

[The Boolean block construction](docs/audits/O2_COVARIANCE_ATTACK_20261019.md) gives
actual sets on the initial interval with `a~1/log p`,
`delta=o(a^(3/2))`, and
`R3+R4<=(-11/20+o(1))a^4wmu`. It satisfies T5, the prescribed original
weight, and the negligible-diagonal condition, but deliberately contains
`{0,1,2,3}`. It is **NOT AP-free and is NOT a P12 counterexample**.

Thus Boolean chirp identities, individual phase caps, logarithmic density
and a weighted count below half the main term do not suffice for W8
without AP exclusion. The next proof must exploit the pointwise
completion identities `Bq_j=0`, or arithmetic information of comparable
strength, with the original density and diagonal hypotheses.

## Established results relevant to the next step

- **PROVED:** The mixed-window terminal ceiling is now `7/11+o(1)`,
  improving the earlier `3/4` and `2/3` ceilings under the same original
  regime (M13). The general fixed-pattern ceiling is `(R-1)/(m-1)` when
  every AP-free subset of m slots has at most R elements; an elementary
  `R_4(12)=8` certificate gives 7/11. All finite errors and diagonals are
  explicit in [FINITE_PATTERN_TERMINAL_20261018.md](docs/audits/FINITE_PATTERN_TERMINAL_20261018.md).
- **PROVED:** The original weighted pair estimate is one-sided:
  `R_1^F=o(a^4wmu)` and `R_2^F>=-o(a^4wmu)` on reachable hosts.
  It is neither exact PSD nor an absolute smallness estimate.
- **PROVED:** The exact original-weight quartic formula is
  `R_4^F=U^2-E_F(u)/2`, where `U=wa(1-a)` and E_F is the explicitly
  defined nonnegative shifted-chirp difference energy. The pairing
  baseline and quartic diagonal are accounted for exactly. See
  [WEIGHTED_QUARTIC_COVARIANCE_20261018.md](docs/audits/WEIGHTED_QUARTIC_COVARIANCE_20261018.md).
- **PROVED:** Four weighted completion channels give a hole projection,
  a disjoint-six-point lower bound `m^2/(1-a)-26m/p`, and a conditional
  atomic/relative-Gram certificate for sufficient correlation. Existence
  of that certificate and its low-completion alternative remain OPEN;
  see [WEIGHTED_COMPLETION_CERTIFICATE_20261018.md](docs/audits/WEIGHTED_COMPLETION_CERTIFICATE_20261018.md).
- **PROVED DOMAIN SEPARATION:** For every fixed `1/3<theta<1/2`, actual
  Boolean cyclic AP-free sets exist with `a~p^-theta` and
  `delta/a^(3/2)->0`. This disproves extending phase selection to all
  densities, but these sets fail the target density range and diagonal
  regime. See [BOOLEAN_TYPICAL_ALTERATION_20261018.md](docs/audits/BOOLEAN_TYPICAL_ALTERATION_20261018.md).
- **PROVED CONDITIONAL IMPLICATION:** DIRECT-Q-GAIN still implies the
  target through the unchanged quarter-cell tradeoff
  `mu_C gamma>=kappa delta/(8a)`. Any uniform divergent multiplier above
  `a^(3/2)` suffices; `R(a)=loglog(e^2/a)` is a concrete choice.
  The stronger terminal constant changes no structural exponent.

## Exact remaining gap

Use the original F, `tau=a^2/log p`, `H=floor(tau wp/(48r))`,
`P=1_Omega`, `u=1_A-aP`, and `T=E F product_i P_i`. The exact AP-free
expansion is

    a^4T+R_1^F+R_2^F+R_3^F+R_4^F=aw/p.

Thus on reachable hosts `Q=R_3^F+R_4^F<=-(1-o(1))a^4wmu`.
Under failed adequate selection, the missing P12 lower bound is

    Q>=-(1/2)a^4wmu.

It is exactly equivalent at finite p to the OPEN bound

    E_F(u)<=2U^2+2R_3^F+a^4wmu.                         (W8)

Positivity of E_F has the wrong orientation because it is subtracted.
Individual chirp caps cannot supply this bound without using AP exclusion,
as the October 19 auxiliary construction demonstrates. The direct cubic
bound has an uncontrolled spectral term
`4c(1-a)(w/mu)a^-1/2 R(a)` after normalization, plus an original-weight
boundary envelope only `O_epsilon(1)` at logarithmic density.
Keep the cubic contribution in W8.

DIRECT-Q-GAIN retains the exact domain

    r[log(1/w)+log(48r)+loglog p]<=log p/100,
    epsilon/(2log|Omega|)<=a<=4/5.

The constants and divergent function must precede every eligible instance.
Its general two-branch negation is proved in
[O2_QUANTIFIERS_CUBIC_BOUND_20261017.md](docs/audits/O2_QUANTIFIERS_CUBIC_BOUND_20261017.md).
The October 19 reduction excludes the positive-density branch.
All 76 finite diagnostic records fail the product budget and have
prescribed H=0. Neither those records nor the sparse asymptotic
construction is a genuine P12 counterexample. The October 19 Boolean
block example also fails eligibility because it contains a 4-AP.

## Verification and preservation

In the October 18 verification capture, nine verifiers passed in isolated
reruns; all eight that write JSON matched their saved reports exactly. The ninth prints its 468-check
report to stdout. The full counts, exact/floating distinctions, and
independent audits are in the continuation report and
[run_summary.json](history/continuation_20261018/verification/run_summary.json).
Finite checks do not prove asymptotic selection.

All 12 before-update files are preserved with verified hashes in
[before_updates](history/continuation_20261018/before_updates/).
The nine navigation files before this publication update are also preserved
in [publication snapshots](history/publication_20261021/before_updates/).
The latest checkpoint records the publication verification separately.
Historical captures are evidence of their dated runs, not claims of new
verification. No background research is implied by these saved notes.
