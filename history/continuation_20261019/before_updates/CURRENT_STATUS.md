# Current research status — 18 October 2026

**Outcome (D): NEW RIGOROUS PARTIAL THEOREMS.** The unconditional target
`r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, and O2/(P12) remain **OPEN**.
No eligible P12 counterexample or unconditional selection theorem is claimed.

The current account is [O2_CONTINUATION_20261018.md](O2_CONTINUATION_20261018.md).
The exact restart state is [AUTONOMOUS_CHECKPOINT_20261018.json](AUTONOMOUS_CHECKPOINT_20261018.json).
The October 17 recovery checkpoint is historical; new work now includes
both the recovered October 17 artifacts and the October 18 continuation.

## Established results relevant to the next step

- **PROVED:** The mixed-window terminal ceiling is now `7/11+o(1)`,
  improving the earlier `3/4` and `2/3` ceilings under the same original
  regime (M13). The general fixed-pattern ceiling is `(R-1)/(m-1)` when
  every AP-free subset of m slots has at most R elements; an elementary
  `R_4(12)=8` certificate gives 7/11. All finite errors and diagonals are
  explicit in [FINITE_PATTERN_TERMINAL_20261018.md](FINITE_PATTERN_TERMINAL_20261018.md).
- **PROVED:** The original weighted pair estimate is one-sided:
  `R_1^F=o(a^4wmu)` and `R_2^F>=-o(a^4wmu)` on reachable hosts.
  It is neither exact PSD nor an absolute smallness estimate.
- **PROVED:** The exact original-weight quartic formula is
  `R_4^F=U^2-E_F(u)/2`, where `U=wa(1-a)` and E_F is the explicitly
  defined nonnegative shifted-chirp difference energy. The pairing
  baseline and quartic diagonal are accounted for exactly. See
  [WEIGHTED_QUARTIC_COVARIANCE_20261018.md](WEIGHTED_QUARTIC_COVARIANCE_20261018.md).
- **PROVED:** Four weighted completion channels give a hole projection,
  a disjoint-six-point lower bound `m^2/(1-a)-26m/p`, and a conditional
  atomic/relative-Gram certificate for sufficient correlation. Existence
  of that certificate and its low-completion alternative remain OPEN;
  see [WEIGHTED_COMPLETION_CERTIFICATE_20261018.md](WEIGHTED_COMPLETION_CERTIFICATE_20261018.md).
- **PROVED DOMAIN SEPARATION:** For every fixed `1/3<theta<1/2`, actual
  Boolean cyclic AP-free sets exist with `a~p^-theta` and
  `delta/a^(3/2)->0`. This disproves extending phase selection to all
  densities, but these sets fail the target density range and diagonal
  regime. See [BOOLEAN_TYPICAL_ALTERATION_20261018.md](BOOLEAN_TYPICAL_ALTERATION_20261018.md).
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
Individual chirp caps do not yet control this covariance at the required
scale. The direct cubic bound has an uncontrolled spectral term
`4c(1-a)(w/mu)a^-1/2 R(a)` after normalization, plus an original-weight
boundary envelope only `O_epsilon(1)` at logarithmic density.
Keep the cubic contribution in W8.

DIRECT-Q-GAIN retains the exact domain

    r[log(1/w)+log(48r)+loglog p]<=log p/100,
    epsilon/(2log|Omega|)<=a<=4/5.

The constants and divergent function must precede every eligible instance.
Its precise negation and both sequential branches are proved in
[O2_QUANTIFIERS_CUBIC_BOUND_20261017.md](O2_QUANTIFIERS_CUBIC_BOUND_20261017.md).
All 76 finite diagnostic records fail the product budget and have
prescribed H=0. Neither those records nor the sparse asymptotic
construction is a genuine P12 counterexample.

## Verification and preservation

Nine verifiers passed in isolated reruns; all eight that write JSON
matched their saved reports exactly. The ninth prints its 468-check
report to stdout. The full counts, exact/floating distinctions, and
independent audits are in the continuation report and
[run_summary.json](history/continuation_20261018/verification/run_summary.json).
Finite checks do not prove asymptotic selection.

All 12 before-update files are preserved with verified hashes in
[before_updates](history/continuation_20261018/before_updates/).
Historical proofs and checkpoints remain intact. No background research
process is left running by this checkpoint.
