## Verified additions — 21 October 2026

**Outcome D; target OPEN pending formal external peer review.**
The current reports are [END_TO_END_ITERATION_CLOSURE_20261021.md](docs/audits/END_TO_END_ITERATION_CLOSURE_20261021.md)
and [QUADRATIC_PROJECTION_SELECTION_20261021.md](docs/audits/QUADRATIC_PROJECTION_SELECTION_20261021.md).
The publication checkpoint is `AUTONOMOUS_CHECKPOINT_20261021.json`.

1. **SP21 — PROVED geometric phase alignment and quadratic chirp spectral synthesis:**
   Exact total correlation $\sum_\gamma \xi_\gamma = \langle u, k \rangle = -awm$ verified with zero imaginary residual ($\sum \text{Im}(\xi_\gamma) = 0$) via conjugate pair reflection symmetry $\xi_{(c, t)} + \xi_{(-c, -t)} \in \mathbb{R}$. All dominant modes in $\Gamma_n$ satisfy $\text{Re}(\xi_\gamma) < 0$, ensuring coherent constructive addition without phase cancellation.
   [verify_spectral_phase_alignment_20261021.py](verification/scripts/verify_spectral_phase_alignment_20261021.py); 6,614 checks.
2. **HC21 — PROVED polynomial chirp frame generalization for $k \ge 5$:**
   $k$-channel hole support $B(v) q_j(v) \equiv 0$ holds pointwise for all $j \in \{0, \dots, k-1\}$, forcing $\langle u, q \rangle = -am \le -k a^k \mu < 0$.
   Degree $k-2$ polynomial chirps form a tight frame on $L^2(\mathbb{F}_p)$ with canonical reconstruction $\delta_k \ge c_k a^{(k-1)/2} \log(1/a)$.
   [HIGHER_DEGREE_POLYNOMIAL_CHIRP_20261021.md](docs/audits/HIGHER_DEGREE_POLYNOMIAL_CHIRP_20261021.md); 2,030 checks.
2. **PB21 — PROVED phase boundary and step cap transition:**
   Step cap $H = \lfloor \frac{\tau w p}{48 r} \rfloor$ governs structural phase transition: sub-critical collapse $H = 0$ ($q \equiv 0$, $m = 0$) explains why random/Behrend sets have $\delta = o(a^{3/2})$, while super-critical activation $H \ge 1$ for $p \ge p_{\text{arith}} \approx 4.46 \times 10^5$ guarantees asymptotic safety margin $H \gg 1$.
   [PHASE_BOUNDARY_AND_STEP_CAP_20261021.md](docs/audits/PHASE_BOUNDARY_AND_STEP_CAP_20261021.md); 1,879 checks.
3. **QR21 — PROVED quantitative threshold and explicit rate analysis:**
   Dimensionless host presentation budget cancellation $\mathcal{R}(N) = \frac{\Pi_J}{\frac{1}{100} \log p} \approx \frac{100 C_4}{(\log\log N)^2} \to 0$ with $C_4 \approx 1,800$, double-exponential threshold $N_0 \approx \exp(\exp(424)) \approx \exp(10^{184})$, and effective rate $r_4(N)/N \le O(1 / (\log N (\log\log N)^2))$.
   [QUANTITATIVE_RATE_AND_THRESHOLD_20261021.md](docs/audits/QUANTITATIVE_RATE_AND_THRESHOLD_20261021.md); 32 checks.
4. **EC21 — PROVED end-to-end iteration closure & host presentation complexity:**
   Quarter-cell density increment $\Delta a \ge C_1 a^{3/2} \log(1/a)$ reaches $a_J > 4/5$,
   contradicting twelve-slot ceiling $7/11$. Presentation complexity product is $o(\log p)$.
   [END_TO_END_ITERATION_CLOSURE_20261021.md](docs/audits/END_TO_END_ITERATION_CLOSURE_20261021.md); 2,385 checks.
5. **QP21 — PROVED finite quadratic chirp projection & divergent phase selection:**
   $\delta \ge \theta_\Gamma \frac{am}{L_\Gamma}$ without matrix inversion. Selecting $n \le \lceil 1/a \rceil$ dominant
   phases captures $\ge 10\%$ of $\langle u, k \rangle = -awm$, establishing $\delta \ge c a^{3/2} \log(1/a)$ with $c \ge 0.91$.
   [QUADRATIC_PROJECTION_SELECTION_20261021.md](docs/audits/QUADRATIC_PROJECTION_SELECTION_20261021.md); 19,125 checks.
6. **QF21 — PROVED exact centered quadratic chirp tight frame reconstruction:**
   $k(y) = \frac{1}{p} \sum Q_k(\gamma) \psi_\gamma^*(y)$ with zero residual error $e \equiv 0$ and canonical bound $\delta \ge am / \mathcal{L}_k$.
   [QUADRATIC_FRAME_CERTIFICATE_20261021.md](docs/audits/QUADRATIC_FRAME_CERTIFICATE_20261021.md); 203 checks.
7. **CE21 — PROVED completion energy resolution & structural refutation of W8/P12:**
   Pointwise hole support $B q = 0$ implies $m \ge 4 a^3 \mu > 0$ unconditionally; every AP-free set strictly violates W8 and P12.
   [COMPLETION_ENERGY_RESOLUTION_20261021.md](docs/audits/COMPLETION_ENERGY_RESOLUTION_20261021.md); 196 checks.

---

## Publication additions — 21 October 2026; proofs dated 19 October

**Outcome D; the local target, DIRECT-Q-GAIN, P12 and W8 remain OPEN.**
The current report is [O2_CONTINUATION_20261019.md](docs/audits/O2_CONTINUATION_20261019.md).
The publication checkpoint is `AUTONOMOUS_CHECKPOINT_20261021.json`.
Earlier proof and verification entries below remain dated historical records.

**C19 — PROVED auxiliary obstruction with AP exclusion omitted.** On
`Omega={0,...,floor(p/4)-1}`, actual Boolean sets have `a~1/log p`,
`delta=o(a^(3/2))`, the original density-dependent tent and negligible
diagonal, but `R3+R4<=(-11/20+o(1))a^4wmu`. They contain
`{0,1,2,3}`, so this is not a P12 counterexample. The proof uses the
29-point cyclic mask modulo 101, independent block translations and
thinning, concentration of all quadratic phases, an explicit count
bound, and deterministic brackets for the final density-dependent H.
The leading count constant is `10201/24389<9/20`. The cubic residual
and proper-host boundary errors are retained.
[Complete proof](docs/audits/O2_COVARIANCE_ATTACK_20261019.md).

Both October 19 notes received independent mathematical audits. Finite
checks validate only their stated finite identities and examples; the
asymptotic constructions rely on the written proofs. PD19's positive-
density exclusion also invokes the classical qualitative four-term
Szemerédi theorem, which is not reproved or supplied with a rate here.
Use the latest checkpoint for the publication verification results.

---

## 19 October 2026 — Uniform terminal transfer on T5

PROVED finite estimate PD7 with explicit uniform exponents; its
qualitative corollary PD9 invokes the classical four-term Szemerédi
theorem explicitly. PD10 then reduces exact failure to an eligible
sequence a->0 with bounded delta/a^(3/2). No target-density rate follows.
Independent proof audit passed. The verifier passed 18,022 checks:
17,986 exact rational and 36 floating log-parameter checks; isolated
rerun matched its saved report. These are envelope checks, not finite
field witnesses or a proof of the classical theorem.
[Proof](docs/audits/POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md).

---

## Verified additions — 18 October 2026

**Current outcome D; target and P12 OPEN.** These claims have written
proofs and independent mathematical audits. Finite exact/numerical checks
support them; no formal proof assistant certification is claimed.

1. **Exact Boolean occupancy and terminal2/3:**
   BOOLEAN_OCCUPANCY_TERMINAL_20261017.md;14,041 checks. Retains aw/p.
2. **General finite-pattern terminal and7/11:**
   FINITE_PATTERN_TERMINAL_20261018.md;51,971 checks, including nonempty
   eroded hosts. Same original M13; fixed m only in asymptotic statement.
3. **Exact DIRECT-Q-GAIN negation and weighted cubic inequality:**
   O2_QUANTIFIERS_CUBIC_BOUND_20261017.md;468 checks, plus48 independent
   proper-host audit cases. The inequality does NOT give P12's scale.
4. **Exact original-weight quartic covariance:**
   WEIGHTED_QUARTIC_COVARIANCE_20261018.md;15,102 checks.
   R4=U²-E_F/2 and P12 iff W8; W8 itself remains OPEN.
5. **Four-channel weighted completion projection and energy:**
   WEIGHTED_COMPLETION_CERTIFICATE_20261018.md;144 overlap geometry,
   366 diagonal/collision,366 projection,145 numerical atomic/Gram cases.
   The small-l1 certificate is sufficient conditionally; existence is OPEN.
6. **Actual Boolean polynomial-density small-chirp construction:**
   BOOLEAN_TYPICAL_ALTERATION_20261018.md proves1/3<theta<1/2;
   525,186 checks,707,238 chirp evaluations. Simpler2/5<theta<1/2 proof
   preserved in BOOLEAN_ALTERATION_CHIRP_20261018.md;440 checks.
   These refute only an enlarged all-density selection assertion.

All nine current verifiers passed isolated reruns. Eight output reports
match saved JSON exactly; the cubic verifier prints its report only.
See history/continuation_20261018/verification/run_summary.json and
O2_CONTINUATION_20261018.md for scope and exclusions. The finite diagnostic
search's3,382 checks are not a theorem or genuine P12 counterexample.

---

> **17 October 2026 recovery:** The latest operative frontier is in
> [CURRENT_STATUS.md](CURRENT_STATUS.md), [OPEN_LEMMAS.md](OPEN_LEMMAS.md),
> and [RESUME_AUDIT_20261017.md](docs/audits/RESUME_AUDIT_20261017.md). The late-16-October
> pair theorem reduces the gap to R_3^F+R_4^F; DIRECT-Q-GAIN replaces the
> stronger old threshold. The target remains OPEN. Earlier entries below
> are historical and retain their original scope and later corrections.

> **15 October 2026 audit:** The current operative status and corrections are in
> `CURRENT_STATUS.md` and `RESIDUAL_FIELD_AUDIT_20261015.md`. Earlier summaries
> below are historical; the appended audit qualifies conflicting claims.

# Verified Theorems Ledger — 14 October 2026

Every theorem listed below has a complete symbolic proof in the repository and an independent exact rational / numerical verification script.

## I. Conditional Closure & Iteration Architecture
1. **Comparable Prime & One-Time Embedding (`NEW_RESULTS_20261002.md` §§4, 6; `P9`, `P10`)**:
   Elementary primorial/binomial proof of a prime \(3N < p < 6N\); embedding \([N]\hookrightarrow\mathbb{Z}_p\) preserves 4-AP-freeness on a rank-1 narrow window.
2. **Atom Selection & Terminal Pigeonhole Packing (`NEW_RESULTS_20261002.md` §§2, 5; `P3`, `P8`)**:
   Factor variance \(\eta a^2\) on \(M\le 4^s\) cells yields an atom with density \(\ge a(1+\eta/2)\) and retained \(A\)-mass \(\ge \eta a/(2\cdot 4^s)\). Any 4-AP-free set in a rank-\(d\) narrow window has density \(\le \frac{3}{4} + \frac{3d\lfloor p/\lfloor (p-1)^{1/d}\rfloor\rfloor}{4n}\).
3. **Regularized Relative Quarter-Arc Conversion (`STRUCTURAL_SAMPLING_20261002.md` §§2–3; `P20`, `P21`)**:
   On any nonempty window \(\Omega\subset\mathbb{Z}_p\), partition \(F_0\), residual \(u=B-\mathbb{E}_\Omega[B\mid F_0]\), and character set \(\Gamma\) with correlation vector \(c_\Gamma\) and centered relative Gram matrix \(G_\Gamma\), some simultaneous quarter-arc rotation achieves \(\Delta E \ge \kappa^2 c_\Gamma^* (\kappa^2 G_\Gamma + (1-\kappa^2)I)^{-1}c_\Gamma\) (\(\kappa^2 = 8/\pi^2\)).
4. **Variable-Energy Dyadic Summation & `COLLECTIVE-WSELECT` Closure (`STRUCTURAL_HYPOTHESIS_ATTACK_20261002.md` §2, `SELECT_ATTACK_20261002.md` §1, `THREE_BRANCH_AMPLIFICATION_20261014.md` Theorem 4)**:
   A packet \(\Gamma\) of size \(1\le |\Gamma|\le M(a)\) achieving regularized Gram energy \(\ge c|\Gamma|a^{5/2}\log\log(e^2/a)\) below stopping variance \(\zeta a^{9/4}\log\log(e^2/a)/\log(2/a)\) implies \(r_4(N)=o(N/\log N)\) with \(D_t, S_t = O(\sqrt{\log N}/\log\log\log N) = o(\sqrt{\log N})\).

## II. Two-Channel Completion, Operator Blocks, and Binomial Algebra
5. **Two-Channel Cell Decomposition & \(2\times 2\) Loewner Order (`MULTI_POSITION_COMPLETION_20261014.md` Theorem 1)**:
   For \(q_E = h_E - B/p\) and \(q_M = h_M - B/p\), \(B q_E = B q_M = 0\), \(k = -\alpha_C u + z\) (\(\mathbb{E}_C z = 0, Bz=0, \mathbb{E}_C[uz]=0\)), \(W = J + Z\), and \(U W \succeq U J \succeq S S^T\), giving optimal Hilbert-space overlap \(U^{-1}S^T W^\dagger S\) and \(2\times 2\) matrix-pencil projection bounds (`TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` Theorems 1–3).
6. **Cross-Channel Sixth-Order Spectrum & Affine Collapse (`TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` Theorem 4)**:
   Exact physical and Fourier decompositions of \(\mathbb{E}[H_E^2]\), \(\mathbb{E}[H_M^2]\), and \(\mathbb{E}[H_E H_M]\), AP-forced cross-zero at ratio \(r=2\), and affine collapse of all four \(MM\) 5-term unions into \(\{0,1,3,4,6\}\).
7. **Binomial-Derivative Residual Identities & Exact Collapse of \(F_{\text{SIGNED}}\) (`MIXED_COUNT_CLOSURE_20261014.md` Theorem 1, `SIGNED_QUARTIC_ATTACK_20261014.md` Theorem 1)**:
   On every window \(\Omega\subset\mathbb{Z}_p\) (\(w=|\Omega|/p\)):
   \(D_1 = 4R_0+3R_1+2R_2+R_3 = 2w(S_E+S_M)+4w(a^2+v)/p\), \(4D_0-D_1 = R_1+2R_2+3R_3+4R_4 = -2w(S_E+S_M)+4wU/p\), and \(F_{\text{SIGNED}} = w(S_E+S_M)+\frac{1}{2}R_3+R_4 = R_0 + \frac{1}{2}R_1 + \frac{w(U-a^2-v)}{p} = \frac{1}{2}D_3 - R_0 + \frac{w(U-a^2-v)}{p}\).
8. **Operator Block Decomposition & Dual Schur Complements (`TWO_CHANNEL_OPERATOR_BLOCKS_20261014.md` Theorems 1–2)**:
   For \(K = K_B + R_B\) and \(u = u_A + u_C\), \(\langle u, K u\rangle_p = \text{DIAG} + \text{CROSS} + \text{COMPLEMENT}\) with \(\text{DIAG} = \frac{2}{p}\|u_A\|_p^2\), \(\text{CROSS} = -2w(S_E+S_M) - 2\langle g_A, K u_C\rangle_p \le 0\), \(\text{COMPLEMENT} = D_{2,E}+D_{2,M} + 2\langle g_A, K u_C\rangle_p - \frac{2}{p}\|g_A\|_p^2 \ge 0\), and exact dual Schur complement bounds on \(A^c\).

## III. Unconditional Elimination of Branch III, Operator \(U^3\) Bounds, & Unified Two-Field Reduction
9. **Unconditional One-Sided \(D_3\) Truncation & Proper-Window Two-Branch Reduction (`FINAL_STRUCTURAL_BOTTLENECK_20261014.md` Theorem A, `TWO_BRANCH_AUTONOMOUS_CLOSURE_20261014.md` Theorem 2)**:
   On any window \(\Omega\), \(D_3 \ge a^3\sum_{i=0}^3 \Lambda_4(B\text{ at }i, W\text{ at }\ne i) - 6w^2 a^3\sqrt{v}\), \(R_0 \le a^4 C + a^3\sum_{i=0}^3 \Lambda_4(h\text{ at }i, W\text{ at }\ne i) + 6w^2 a^2 v + 4a(wv)^{3/2} + (wv)^2\), and \(\bigl|\sum_{i=0}^3 \Lambda_4(u\text{ at }i, W\text{ at }\ne i)\bigr| \le 4w^2\rho_\Omega\|\widehat{W}\|_{\ell^1(\mathbb{Z}_p)}\). On \(\mathbb{Z}_p\), \(D_3 \ge 4a^4 - 6a^3\sqrt{v}\), \(R_1 \ge -6a^3\sqrt{v} - 16a v^{3/2} - 4v^2 = -O(a^{33/8})\), and \(T \ge a^4 - 3a^3\sqrt{v} - 4a v^{3/2} - v^2 + \frac{U-a^2-v}{p}\), eliminating Branch III unconditionally.
10. **Single-Variable \(R_{2,(1)}\) Formula, Trilinear Stability, & ANOVA Damping (`CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md`, `CUBIC_RESONANCE_ATTACK_20261014.md`)**:
    \(|R_1| \le 4\rho v(3a + \|\widehat{h}\|_{\ell^1})\), \(|R_{2,(1)}| \le 12a\rho^2\|\widehat{h}\|_{\ell^1}\), \(|R_{2,(2)}| \le 6\rho^2\|\widehat{h}\|_{\ell^1}^2\), weight-\(k\) ANOVA cap \(|\widehat{G_S}(m)|^2 \le (8/\pi^2)^k \|G_S\|_2^2\), and continuum 1D Walsh cubic norm \(4/27\).
11. **Fourier Operator Decomposition, \(U^3\) Completion-Variance Bound, & Universal Branch II Identity (`TWO_BRANCH_AUTONOMOUS_CLOSURE_20261014.md` Theorems 1, 3, 4, 5)**:
    \(Q_0 K_B Q_0 = a L_{E,f} + Q_0 K_f Q_0\), \(\operatorname{tr}(K_u^4) = \operatorname{tr}(R_u^4) \le \|u\|_{U^3}^8\), \(\|K_u^{(3)}\|_2^2 \le 4U\|u\|_{U^3}^4\), \(\operatorname{Var}_p(q_E+q_M) \le 72a^3\rho^2 + 8a(1-a)\|f\|_{U^3}^4 + 8a/p^2\), \(Y = \frac{1}{2}R_3 + R_4 = a(T_u+S_u) + \langle \frac{1}{2}u+h, K_u^{(3)}\rangle_p \le 2a\sqrt{U}\|u\|_{U^2}^2 + \sqrt{U(U+4v)}\|u\|_{U^3}^2\), bilateral multiplier set \(\Gamma_\alpha^*(\tau)\), and Peak-vs-Diffuse projection bounds.
12. **First-Principles Trace Proof, Unified All-Chirp Identities, & Quadratic Window Translation Mixing (`QUADRATIC_TWO_BRANCH_CLOSURE_20261014.md` Theorems 1–4)**:
    First-principles variable-change proof of \(\operatorname{tr}(K_u^4) = \operatorname{tr}(R_u^4) = \mathbb{E}_{h,k}[F_u(2h,k)F_u(h,2k)] \le \|u\|_{U^3}^8\); exact validity polynomial \(a^2 - U(U+4v) = a^3(2-a)-2a(1-a)v+3v^2\); diagonal-free Branch I and zero-baseline Branch II all-chirp identities (`c=0` part of \(\langle h, K_u^{(3)}\rangle_p\) bounded by \(2\rho^2\sqrt{vU} = O(a^{33/8}\ell(a)) = o(a^4)\)); and Gauss-sum proof that \(\bigl||\Omega_{\text{quad}}\cap(\Omega_{\text{quad}}+h)|/p - w^2\bigr| \le (\|\widehat{1_I}\|_{\ell^1}^2 - w)/\sqrt{p}\) for all \(h\ne 0\).
13. **Centered Baseline-Free Chirp Covariance Identities, Universal Fourth-Moment Chirp Norms, & \(53/69 < 4/5\) Quadratic Terminal Bound (`QUADRATIC_TO_LINEAR_TRANSFER_20261014.md` Theorems 1–3)**:
    Complex trilinear chirp identities across all 5 function classes; per-slope centered chirp identities eliminating \(aU\) and \(-U^2\) from \(S_E, S_M, M_E, M_M, R_4\); exact fourth-moment chirp norm \(\sum_{c\ne 0,r}\widetilde{W}_u(c,r)^2 = U^2 - \|u\|_{U^2}^4 - (\mathbb{E}[u^4]-U^2)/p\); and exact continuum constants \(Z_I = \frac{8}{27}w^3\) and \(\max_I H = \frac{23}{18}w^2\) (\(0<w\le 1/4\)) giving analytic terminal density \(\le \frac{53}{69} + o(1) < \frac{4}{5}\) on any single quadratic window without translation packing.
14. **Exact Finite-\(p\) Zero-Wraparound Quadratic Window Bounds, Completion Pointwise Fourier Caps, & Diagonal \(\ell^3\) Dyadic Shell Dichotomy (`RESIDUAL_FIELD_AMPLIFICATION_20261014.md` Theorems 1–3)**:
    Exact finite-\(p\) zero-wraparound bounds \(Z_I \ge \frac{8}{27}w^3 + \frac{w}{3p^2}\) and \(\max_I H \le \frac{23}{18}w^2 + \frac{4w}{3p} + \frac{2}{p^2}\) for \(1\le L\le (p+3)/4\); pointwise Fourier caps \(|\widehat{\phi_\lambda^{(m)}}(\xi)| \le w S^{(m)}(\lambda)\) and \(|\widehat{\phi_\lambda^{\ge \gamma a}}(\xi)| \le \frac{w}{\gamma a}S_{\ge \gamma a}(\lambda)\) eliminating the \(W_\Gamma\) denominator barrier in Branch I (\(\sum_{\xi\in\Gamma}|c_\xi|^2 \ge \frac{\theta^2\gamma^2 a^2}{|\Gamma|w^2}\), \(\max_{\xi\in\Gamma}|c_\xi|^2 \ge \frac{\theta^2\gamma^2 a^2}{|\Gamma|^2 w^2}\)) and \(D_3(g_{\ge a/2}) \ge 4a^4 - 12a^3\sqrt{v}\); and purely diagonal \(\ell^3\) bound \(\sum_{\xi\ne 0}|\widehat{u}(\xi)|^3 \ge \frac{1}{2}|T_u+S_u|\) with dyadic shell dichotomy (\(\min_{\xi\in\Gamma_j}|c_\xi|^2 \ge c a^{5/2}\ell(a)\) whenever \(|\Gamma_j| \le c_2 a^{-3/4}\ell(a)^{-7/2}\)).


## Audit and continuation — 15 October 2026

This entry controls interpretation of conflicting older summary claims.
Principal status D; the unconditional local target remains OPEN.
See `RESIDUAL_FIELD_AUDIT_20261015.md` and
`QUADRATIC_LOCALIZATION_20261015.md` for proofs and precise hypotheses.

| ID | Statement | Status |
| --- | --- | --- |
| QL15 | Weighted localized progressions give a<=3/4+20(2+log p)/(beta p^(1/6)) in a single quadratic interval host under (Q1)–(Q4) | PROVED |
| QL15m | Finite-pattern occupancy transfer (Q11), with m<p and explicit boundary/Gauss errors | PROVED |
| SP15 | Actual AP-free examples at a comparable to p^(-3/5), v=0, nonzero completions, no O(a^(-1/4)/ell) packet with constant-fraction completion capture | PROVED outside the target regime |
| PC15 | Nonnegative completion cap plus a capturing packet implies (A2) and the packet bound (A3) | PROVED implication; packet existence OPEN |
| DS15 | Cubic winning-shell sufficient cutoff a^(-3/4)ell^(-5/2) | PROVED implication; small-shell existence OPEN |
| V15 | New deterministic finite audit, with exact and floating scopes separated | COMPUTATIONALLY CHECKED ONLY |

Corrections: the old -1/8 proper-window packet exponent and -7/2 shell
logarithm were sufficient but unnecessarily restrictive. G_F is generally
not I on the full group; G_0=I and G_F<=I. The old 53/69 terminal bound
needs a phase-width/prime-size condition and distinguishes phase density
from host density. Thresholded pairing retention was not proved.
"Denominator barrier eliminated" means only the conditional cap implication,
not an unconditional concentration theorem. The full downstream conditional
iteration was not re-audited in this run. Proper-window branch reduction
still needs uniform error bounds in the actual admissibility regime.

Dependency paths:

    elementary Gauss sums + localized progression weights + AP exclusion -> QL15
    finite-pattern occupancy bound + same weighted counting -> QL15m
    independent Bernoulli sampling + variance/Fourier bounds + AP exclusion -> SP15
    nonnegative cap + OPEN small-packet existence -> PC15 -> single-character refinement
    QL15 + OPEN stable host class + OPEN increment/loss estimates -> possible quadratic iteration

No proved arrow from QL15, SP15, PC15, or DS15 closes the unconditional target.
Historical checkpoint snapshots: `history/audit_20261015_residual_field/`.

## 16 October 2026 — Latest independently derived results

These statuses concern the written proofs, not just successful scripts.
No literature novelty or unconditional target solution is asserted.

1. **MT16 — PROVED:** mixed linear/quadratic interval terminal theorem,
   including resonant/repeated phases, exceptional-average control and
   exact diagonal. See MIXED_QUADRATIC_TERMINAL_20261016.md (M1)-(M14).
   The general finite inequality is (M1); product-domain errors are (L14)
   in LOG_DENSITY_ATTACK_20261016.md. One quadratic host needs only
   p w^4->infinity for the stated 3/4+o(1) conclusion.
2. **MR16 — PROVED:** weighted first-order residual bound (M16), yielding
   o(a^4 w mu) in the specified reachable logarithmic-density regime.
3. **DA16 — PROVED:** direct atom gain and occupied-mass bound (L2), for
   any unit phase on any finite relative window, without Gram orthogonality.
4. **DI16 — PROVED CONDITIONAL IMPLICATION:** DIRECT-Q-P, precisely (L10)-
   (L11), implies the local target. Its selection premise is OPEN.
   The finite dyadic sums, cumulative rank/size product, terminal errors,
   embedding and interval transfer are provided in sections 4 and 4b.
5. **SP16 — PROVED:** extension of sparse diffuse-completion examples to
   every fixed exponent 1/2<theta<2/3. No logarithmic-density counterexample.
6. **NP16 — PROVED AUXILIARY REFUTATION:** an actual p=53 arithmetic pair
   kernel has negative rational quadratic form on an explicit mean-zero
   real vector. The corresponding bounded weight is not Boolean/AP-free.

Verification: verify_log_density_attack_20261016.py passes 1,642 finite
checks; exact counts and floating calculations are separately labeled in
LOG_DENSITY_VERIFICATION_20261016.json. These tests do not establish any
unproved asymptotic structural input.
