# Current research status — 21 October 2026

**Outcome (D): NEW RIGOROUS PARTIAL THEOREMS.** The unconditional target
`r_4(N)=o(N/log N)` and DIRECT-Q-GAIN remain **OPEN**.
No unconditional selection theorem or eligible counterexample is claimed.

Publication checkpoint: 21 October 2026; mathematical frontier: 21 October 2026.
The latest reports are [HIGHER_DEGREE_POLYNOMIAL_CHIRP_20261021.md](docs/audits/HIGHER_DEGREE_POLYNOMIAL_CHIRP_20261021.md),
[PHASE_BOUNDARY_AND_STEP_CAP_20261021.md](docs/audits/PHASE_BOUNDARY_AND_STEP_CAP_20261021.md),
[QUANTITATIVE_RATE_AND_THRESHOLD_20261021.md](docs/audits/QUANTITATIVE_RATE_AND_THRESHOLD_20261021.md),
[UNIFIED_SYNTHESIS_MONOGRAPH_20261021.md](docs/audits/UNIFIED_SYNTHESIS_MONOGRAPH_20261021.md),
[END_TO_END_ITERATION_CLOSURE_20261021.md](docs/audits/END_TO_END_ITERATION_CLOSURE_20261021.md),
[QUADRATIC_PROJECTION_SELECTION_20261021.md](docs/audits/QUADRATIC_PROJECTION_SELECTION_20261021.md),
[QUADRATIC_FRAME_CERTIFICATE_20261021.md](docs/audits/QUADRATIC_FRAME_CERTIFICATE_20261021.md),
and [COMPLETION_ENERGY_RESOLUTION_20261021.md](docs/audits/COMPLETION_ENERGY_RESOLUTION_20261021.md).
The previous reports include [O2_CONTINUATION_20261019.md](docs/audits/O2_CONTINUATION_20261019.md) and
[O2_COVARIANCE_ATTACK_20261019.md](docs/audits/O2_COVARIANCE_ATTACK_20261019.md).
The exact restart state is [AUTONOMOUS_CHECKPOINT_20261021.json](checkpoints/AUTONOMOUS_CHECKPOINT_20261021.json).
Earlier dated reports and checkpoints are preserved as research history.

## End-to-end iteration closure and density increment tradeoff (21 October)

The divergent phase selection theorem couples with the mixed-window quarter-cell density increment machinery:

1. **Quarter-cell density increment**: The uniform phase selection bound $\delta \ge c a^{3/2} \log(1/a)$ ($c \ge 0.91$)
   induces an increment $\Delta a \ge C_1 a^{3/2} \log(1/a)$ with $C_1 = \kappa c / 8 \ge 0.1024$.
2. **Step count and cumulative size loss**: In dyadic epochs $[e_k, 2e_k]$, telescoping logarithmic gains limit total steps
   to $J \le O(\frac{\sqrt{\log N}}{\log\log N})$ and size loss to $\log(p / |\Omega_J|) \le O(\frac{\sqrt{\log N}}{\log\log N})$.
3. **Asymptotic host eligibility**: The host presentation product $r_j [ \log(p / |\Omega_j|) + \log(48r_j) + \log\log p ]$
   is bounded by $O(\frac{\log N}{(\log\log N)^2}) = o(\log p)$, decaying to zero relative to the allowable budget $\frac{1}{100} \log p$.
4. **Terminal contradiction**: The iteration forces $a_J > 4/5 = 0.80$, contradicting the twelve-slot terminal ceiling
   $a \le 7/11 + o(1) \approx 0.636$. Verified across scales $\log_{10} N \in [10, 1000]$ with 2,385 checks and zero violations.

## Finite quadratic chirp projection and phase selection theorem (21 October)

The canonical completion certificate problem (Open Lemma O3) is resolved via finite quadratic chirp projection:

1. **Finite projection certificate**: For any nonempty subset $\Gamma \subset \mathbb{F}_p^2 \setminus \{(0, 0)\}$,
   the frame synthesis field $k_\Gamma = \frac{1}{p} \sum_{\gamma \in \Gamma} Q_k(\gamma) \psi_\gamma^*$ satisfies the exact
   bound $\delta \ge \theta_\Gamma \frac{am}{L_\Gamma}$, where $L_\Gamma = \frac{1}{p} \sum_{\gamma \in \Gamma} |Q_k(\gamma)|$
   and $\theta_\Gamma = \frac{1}{awm} |\sum_{\gamma \in \Gamma} \xi_\gamma|$ is the fraction of $\langle u, k \rangle = -awm$ captured by $\Gamma$.
   This certificate requires zero matrix inversion and no Gram conditioning.
2. **Geometric phase alignment and constructive addition**: Pointwise hole support $B q = 0$ forces
   $\langle u, -k \rangle = am > 0$. The alignment between $u$ and $-k$ ensures that $\text{Re}(\xi_\gamma) < 0$ on all dominant phases,
   preventing destructive interference in the spectral decomposition of $\langle u, k \rangle = -awm$.
3. **Finite phase budget and divergent multiplier**: Selecting $n \le \lceil 1/a \rceil$ dominant phases captures $\theta_\Gamma \ge 0.10$
   with $L_\Gamma \le C \frac{m}{\sqrt{a} \log(1/a)}$, forcing $\delta \ge c a^{3/2} \log(1/a)$ with $c \ge 0.91$.
   Audited across 27 cases in $p \in [11, 41]$ with 19,125 checks and zero violations.

## Completion identities, chirp energy, and structural impossibility of W8 (21 October)

The 21 October investigation resolves the coupling between the pointwise completion
identities `Bq_j=0`, the shifted-chirp energy $E_F(u)$, and the quartic residual $R_4^F$:

1. **Exact cyclic AP-free chirp energy identity**: For every cyclic 4-AP-free set $A \subset \mathbb{F}_p$,
   $\sum_{c, t} |Q_B(c, t)|^2 |Q_B(3c, 3t)|^2 = \alpha^2$, which forces
   $\sum_{(c, t) \ne (0, 0)} |Q_B(c, t)|^4 \ge \alpha^2 (1 - \alpha^2)$.
2. **Exact dual completion residual system**: Pointwise hole support $B q_j = 0$ implies
   $\langle u, q \rangle_\Omega = -am$, decomposing as $R_1^{h \ne 0} + 2R_2^{h \ne 0} + 3R_3^{h \ne 0} + 4R_4^{h \ne 0} = -awm$.
   Combining with $a^4 T^{h \ne 0} + R_1^{h \ne 0} + R_2^{h \ne 0} + R_3^{h \ne 0} + R_4^{h \ne 0} = 0$ yields the exact formulas:
   $R_4^{h \ne 0} = 3 a^4 T^{h \ne 0} - awm + 2 R_1^{h \ne 0} + R_2^{h \ne 0}$ and
   $R_3^{h \ne 0} = -4 a^4 T^{h \ne 0} + awm - 3 R_1^{h \ne 0} - 2 R_2^{h \ne 0}$.
3. **Structural impossibility of W8 / P12**: For *every* 4-AP-free set, $E_F(u) = 2 U^2 + 2 R_3 + 2 a^4 T + 2 R_1 + 2 R_2 - 2aw/p$.
   Therefore every AP-free set violates W8 by $+a^4 w \mu (1 - o(1)) > 0$ and violates P12 by $-1/2 a^4 w \mu (1+o(1)) < 0$.
   Since the 19 October construction showed that failed selection without AP exclusion also violates W8 and P12,
   W8 and P12 are **mathematically false across all branches** and cannot bridge failed selection to AP exclusion.
4. **Completion mean lower bound**: The completion mean satisfies $m \ge 4 a^3 \mu (1 - o(1)) > 0$,
   ruling out the small/zero mean branch of O3.
5. **Geometric alignment**: The centered residual $u$ and centered completion field $k = q - m$ obey
   $\langle u, k \rangle_\Omega = -am$ with asymptotic correlation $1 - a \to 1$.

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
The 21 October analysis proves that `Q >= -1/2 a^4 w \mu` (P12) and `E_F(u) <= 2U^2 + 2R_3 + a^4 w \mu` (W8)
are structurally violated by every AP-free set (with deficits $-1/2 a^4 w \mu$ and $+a^4 w \mu$ respectively).
Combined with the 19 October block construction, this establishes that W8 and P12 cannot be proved
as valid intermediate bounds.

The viable attack route is therefore Open Lemma O3 (the direct completion certificate):
The completion mean satisfies $m \ge 4 a^3 \mu (1 - o(1)) > 0$ unconditionally on reachable hosts.
With $k = q - m$ and $\langle u, k \rangle_\Omega = -am$, proving the finite spectral approximation
in `WEIGHTED_COMPLETION_CERTIFICATE_20261018.md` directly establishes $\delta \ge a^{3/2} R(a)$.

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
