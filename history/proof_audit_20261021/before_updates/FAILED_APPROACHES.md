## 21 October 2026 — Structural impossibility and definitive closure of W8 and P12

**REFUTED: W8 ($E_F(u) \le 2U^2 + 2R_3 + a^4 w \mu$) and P12 ($R_3 + R_4 \ge -\frac{1}{2} a^4 w \mu$) as direct sublemmas across all branches.**
By Theorem 3 of [COMPLETION_ENERGY_RESOLUTION_20261021.md](docs/audits/COMPLETION_ENERGY_RESOLUTION_20261021.md), for every 4-AP-free set $A$:
$$E_F(u) = 2U^2 + 2R_3 + 2a^4 T + 2R_1 + 2R_2 - 2aw/p.$$
Every AP-free set strictly violates W8 by $+a^4 w \mu (1 - o(1)) > 0$ and violates P12 by $-1/2 a^4 w \mu (1+o(1)) < 0$.
Meanwhile, the October 19 block construction violates them under failed selection without AP exclusion.
Thus W8 and P12 are **mathematically false across all branches** and cannot serve as intermediate steps.
Never attempt to prove W8 or P12 again; the direct completion certificate (Open Lemma O3) is the operative route.

**REFUTED: Gram matrix pseudo-inversion for frame projection certificates.**
Attempting to project $k$ via $(G^\dagger)_{\gamma, \gamma'}$ requires bounding the condition number of the non-orthogonal Gram matrix $G_{\gamma, \gamma'} = \langle \psi_\gamma, \psi_{\gamma'} \rangle$, which degenerates when $n \ge p-1$.
The canonical tight frame partial synthesis $k_\Gamma = \frac{1}{p} \sum_{\gamma \in \Gamma} Q_k(\gamma) \psi_\gamma^*$ bypasses matrix inversion completely, yielding the unconditional certificate $\delta \ge \theta_\Gamma \frac{am}{L_\Gamma}$ with zero Gram matrix conditioning.

---

## Publication update — 21 October 2026; obstruction proved 19 October

**REFUTED: W8 from Booleanity, small individual chirps and a count deficit
without actual AP exclusion.** The construction in
[O2_COVARIANCE_ATTACK_20261019.md](docs/audits/O2_COVARIANCE_ATTACK_20261019.md)
has `a~1/log p`, `delta=o(a^(3/2))`, T5, an actual initial interval,
original prescribed H, `pa^3mu->infinity`, and
`R3+R4<=(-11/20+o(1))a^4wmu`. All exact Boolean identities hold.
It deliberately contains `{0,1,2,3}`. The omitted AP-free hypothesis is
essential: this refutes the enlarged assertion, not P12 or DIRECT-Q-GAIN.

A proof must exploit AP exclusion more strongly than a weighted count
below half the random main term. The next route is the pointwise
completion identities `Bq_j=0` together with the original density and
diagonal conditions. Completion-certificate existence, its low-mean
branch, W8 and the local target remain OPEN. The positive-density failure
branch is closed by PD19 with explicit use of qualitative Szemerédi;
substituting a shrinking density into its uncontrolled threshold remains
invalid. Current state: `AUTONOMOUS_CHECKPOINT_20261021.json`.
Older exclusions below retain their original scope.

---

## 19 October 2026 — Positive-density counterexample branch excluded

A sequence of eligible T5 hosts with AP-free relative density bounded
away from zero is impossible, by the uniform finite-pattern estimate and
explicit use of the classical qualitative four-term theorem. Thus do not
continue searching that branch of DIRECT-Q-GAIN's general negation.
The lower-density branch remains OPEN. Substituting a0=epsilon/log p into
a theorem with an uncontrolled p0(a0) would be invalid and does not prove
the target. [Proof](docs/audits/POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md).

---

## New exclusions and insufficient estimates — 18 October 2026

**Outcome D; the target and P12 are still OPEN.** These entries distinguish
refuted enlarged claims from estimates that merely fail to close the gap.

- **REFUTED enlarged all-density selection:** Boolean AP exclusion alone
  does not force delta>=c a^(3/2), even for genuine sets. For every fixed
  1/3<theta<1/2 the typical-alteration theorem has a~p^-theta and
  delta/a^(3/2)->0. It fails the required logarithmic density AND diagonal
  regimes; do not label this a counterexample to DIRECT-Q-GAIN or P12.
- **REFUTED unconditional residual positivity:** The actual full-host
  p19 witness in O2_CONTINUATION_20261018.md has R3<0 and R4<0.
  It refutes any nontrivial nonnegative linear combination claimed always
  nonnegative. It is ineligible and even has Q/main>-1/2.
- **INSUFFICIENT single-edge Boolean moments:** The abstract2/3 law is
  sharp for that moment argument; a lower-density law has proper Bernoulli
  moments and quartic deficit. These laws are not arithmetic sets.
  Twelve overlapping slots improve the terminal constant to7/11 only.
- **INSUFFICIENT direct cubic estimate:** Under the failed target cap,
  its spectral envelope has normalized scale (w/mu)a^-1/2 R(a);
  its original boundary envelope2/(a logp) is not o(1). Smaller tau fixes
  only boundary loss and changes F. This does not prove impossibility of
  sharper cubic control.
- **INVALID positivity inference from quartic energy:** Exact R4=U²-E_F/2
  subtracts a nonnegative energy. The required upper bound W8 is unproved.
  Pointwise small chirps plus the known energy norm do not supply its
  a^4wmu precision by the estimates currently available.
- **UNPROVED completion shortcut:** Disjoint-six-point energy and hole
  projection do not establish the small-l1 phase approximation. Small or
  zero completion mean must be handled separately. Original F need not
  be reversal invariant, so merging four channels into two is invalid.
- **INELIGIBLE finite violations:** All76 saved records fail T5 and have
  original prescribedH0. Bare numerical Q/main<-1/2 in some records is
  not an eligible P12 counterexample; every assumption must be tested.

Sources: O2_CONTINUATION_20261018.md and its linked complete notes.

---

> **17 October 2026 recovery:** The latest operative frontier is in
> [CURRENT_STATUS.md](CURRENT_STATUS.md), [OPEN_LEMMAS.md](OPEN_LEMMAS.md),
> and [RESUME_AUDIT_20261017.md](docs/audits/RESUME_AUDIT_20261017.md). The late-16-October
> pair theorem reduces the gap to R_3^F+R_4^F; DIRECT-Q-GAIN replaces the
> stronger old threshold. The target remains OPEN. Earlier entries below
> are historical and retain their original scope and later corrections.

# Failed and Refuted Approaches — 14 October 2026

This ledger records approaches that were rigorously tested and proved insufficient or false, preventing circular revisitation.

1. **Actual-\(U^3\) Inverse Bound with Exponent \(C < 2\) (`PHASE2_AUDIT.md` §6 — REFUTED)**:
   - *Claim*: \(\sup_{\|\Psi\|_\infty\le 1}|\langle f,\Psi\rangle| \ge c\|f\|_{U^3}^C\) with \(C < 4/3\) (or any \(C < 2\)) for 4-AP-free sets with \(p\alpha^3 \ge 2\).
   - *Reason for failure*: Interval-supported Behrend sphere encodings in \([0, m)\) (\(m = \lambda p\)) are 3-AP-free and satisfy \(\|f\|_{U^3} \ge \alpha/(2\sqrt{2\lambda})\), whereas \(|\langle f,\Psi\rangle| \le 2\alpha\), forcing \(C \ge 2\). Any valid inverse step must be density-calibrated rather than a power of the actual \(U^3\) norm.

2. **Universal Near-Full-Mass Integer-Progression Increment (`SIGNED_RESEARCH.md` §9 — REFUTED)**:
   - *Claim*: Every 4-AP-free \(A\subset [N]\) admits a true integer progression \(P\) retaining half the mass of \(A\) with density gain \(\ge c\alpha^2\).
   - *Reason for failure*: Random affine images of 3-AP-free sphere sets in \(\mathbb{Z}_p\) have discrepancy \(o(\alpha^R)\) on all integer progressions of length \(\ge \alpha p/2\). Coordinate windows in a fixed \(\mathbb{Z}_p\) must be used instead.

3. **Unlabeled Spectral / Trace-Power / Schur Extraction (`ROUTE_INCIDENCE_MOMENTS_20261002.md` §3 — REFUTED)**:
   - *Claim*: Eigenvalues, trace powers \(\operatorname{tr}(K_B^m)\), and Schur-complement PSD inequalities of the endpoint operator \(K_B\) force low-rank character energy.
   - *Reason for failure*: Simultaneously permuting vertex labels preserves all spectral and PSD invariants while reducing low-rank character energy to \(O(4^d d\log p/p) = o(a^2)\). Arithmetic labels must be retained.

4. **Linear Quarter-Factor Approximation of Arbitrary Quadratic Phases (`STRUCTURAL_GEOMETRY_20261002.md` §2 — REFUTED)**:
   - *Claim*: The expanded rank budget \(s = O(\sqrt{\log p}/\log\log p)\) approximates genuine quadratic phases \(e_p(cx^2)\) or makes Boolean quadratic interval hosts \(1_S(q(x))\) visible.
   - *Reason for failure*: Gauss-sum and \(\ell^1\)-interval bounds prove \(\|\mathbb{E}_\Omega[e_p(q)\mid F]\|_2^2 \le 4^s p^{-1/2}w^{-1}(2+\log p)^{d+s} = \exp(-\frac{1}{2}\log p + o(\log p))\). Instead, quadratic interval hosts are ruled out because they contain \(\ge c\beta^3 w^2/3^d\) nonzero 4-APs (`STRUCTURAL_GEOMETRY_20261002.md` §4A).

5. **Degree-Two and Degree-Four Polynomial Preordering Certificates (`SELECT_DISCOVERY_20261002.md`, `SELECT_POSITIVE_MOMENTS_20261012.md` — REFUTED)**:
   - *Claim*: The degree-4 polynomial preordering generated by Boolean equalities, exact cardinality, quartic AP equations \(X_e=0\), 4-variable local probability laws, and Fourier caps \(\tau - |c_\xi|^2 \ge 0\) certifies `SELECT` at \(\tau \sim a^{5/2}\log(2/a)\).
   - *Reason for failure*: Averaging admissible triple-balanced 8-vertex trades constructs an exact feasible degree-4 moment functional satisfying all constraints down to \(\tau = 120a/n = o(a^{5/2}\log(2/a))\).

6. **Canonical Cardinality-Preserving Lift to Degree Five/Six (`DEGREE_SIX_ATTACK_20261012.md` §3–5 — REFUTED)**:
   - *Claim*: The canonical harmonic lift \(m_5^0, m_6^0\) of the degree-4 trade moments remains valid at degrees 5 and 6.
   - *Reason for failure*: \(m_5^0(S) < -\rho_5/4 < 0\) on 5-term APs, and \(m_6^0\) violates the degree-6 completion-square SOS certificate \([H_v - s(1-X_v)]^2 - 2s X_v H_v \ge 0\) (which forces disjoint-completion excess \(\ge a^7/8\)).

7. **Correlation-Size-Only Conversion of Sixth-Order Excess (`SIXTH_ORDER_FOURIER_ATTACK_20261012.md` §6 — REFUTED)**:
   - *Claim*: Any bounded function \(0\le f\le 1\) of mean \(a\) with sixth-order completion excess \(\mathbb{E}[h_f^2] - a^6 \ge a^7/8\) must have a large linear Fourier coefficient.
   - *Reason for failure*: The quadratic-resonant weight \(f_p(x) = a F(x^2/p)/M_p\) has \(\mathbb{E}[h_f^2] \ge a^6(1+2\beta^6)\) while \(\max_{\xi\ne 0}|\widehat{f_p}(\xi)| \le O(a/\sqrt{p})\). However, it has positive covariance \(\operatorname{Cov}(f_p, h_f) > 0\), violating \(B q_E = B q_M = 0\).

8. **Mixed-Count Positivity \(D_k \ge 0\) Alone Implies `SIGNED` (`MIXED_COUNT_CLOSURE_20261014.md` Theorem 2 & `SIGNED_QUARTIC_ATTACK_20261014.md` Theorem 1 — REFUTED)**:
   - *Claim*: Nonnegativity of all 10 reflection-symmetric mixed progression counts \(L_I(g,B)\ge 0\), \(S_E,S_M\ge 0\), and \(R_1=R_2=R_3=0\) implies \(R_1+R_2+R_3+R_4 \ge -\frac{3}{8}a^4\), or that \(F_{\text{SIGNED}} = w(S_E+S_M)+\frac{1}{2}R_3+R_4 \ge 2R_0 - \frac{3}{8}a^4 + \frac{1}{2}R_1 - \frac{2w(a^2+v)}{p}\) holds as an identity.
   - *Reason for failure*: \(R_4 = \Lambda_4(u)\) appears only in \(D_0 = aw/p\), so the explicit 10-block witness \((a^4,0,0,0,aw/p-a^4)\) is feasible, and \(F_{\text{SIGNED}}\) collapses identically to \(D_0 + R_0 + \frac{1}{2}R_1 - \frac{2w(a^2+v)}{p}\).

9. **Pure Quadratic-Arc Windows for Terminal \(h\)-Cycle Packing (`QUADRATIC_TWO_BRANCH_CLOSURE_20261014.md` Theorem 4 — REFUTED)**:
   - *Claim*: Replacing linear character quarter-arcs \(\xi x\in I\) by quadratic character arcs \(cx^2+rx\in I\) (\(c\ne 0\)) preserves the terminal \(h\)-cycle run-packing contradiction (`NEW_RESULTS_20261002.md` §5).
   - *Reason for failure*: By elementary Gauss sums (and exact vanishing of the \(k_1+k_2\equiv 0,\ k_2\ne 0\) cross modes), every nonzero shift \(h\ne 0\) satisfies \(\bigl||\Omega_{\text{quad}}\cap(\Omega_{\text{quad}}+h)|/p - w^2\bigr| \le (\|\widehat{1_I}\|_{\ell^1}^2 - w)/\sqrt{p}\), so every nonzero shift loses \(\ge 1-w-o(1) \ge 3/4-o(1)\) of \(\Omega_{\text{quad}}\).


## 15 October 2026 audit additions

- Small-packet completion capture uniformly over all densities is FALSE:
  actual AP-free sets at density comparable to p^(-3/5) have nonzero
  completion pairing and vanishing capture on every budget-sized packet.
  Proof: RESIDUAL_FIELD_AUDIT_20261015.md (A6)–(A7). This does not refute SELECT.
- Inferring packet existence from a pointwise Fourier upper bound fails:
  (A2) has a capture premise. It is not a concentration theorem.
- An unqualified finite-p terminal density below 4/5 for every quadratic
  interval is false: p=7, q=x^2, I={0}, Omega=A={0}. The asymptotic terminal
  bound with a suitable size hypothesis survives and is strengthened in QL15.
- Treating failure of single-shift packing as failure of every terminal
  argument is invalid. Weighted localization proves a<=3/4+o(1) for a
  single quadratic interval host; a complete quadratic iteration remains open.

## 16 October 2026 — New failures and scope limits

- **REFUTED:** Nonnegative Fourier tent weights imply PSD of the actual
  arithmetic pair kernel. The explicit p=53, H=26, q=x^2 vector in
  LOG_DENSITY_ATTACK_20261016.md has pair form -8242732/2047761.
  The bounded function B=1/2+v/100 has R_2=-2060683/20477610000.
  This is a weighted-function witness, not an AP-free Boolean example.
- **INSUFFICIENT LEDGER:** Even a hypothetical phase correlation merely
  of order a^(3/2), fed into the proved direct-cell extraction, gives
  rank O(t^(-1/2)) and log-size loss O(t^(-1/2)ell(t)); these estimates
  do not meet the new product budget at t=epsilon/log N. This is failure
  of a particular bound, not impossibility of every quadratic method.
- **FAILED RANDOM EXTENSION:** Independent sampling at epsilon/log p is
  AP-free with probability at most exp(-floor(p/4)(epsilon/log p)^4),
  which tends to zero. The sparse proof cannot simply be reused there.
  This does not rule out correlated constructions or prove SELECT.
- **NO COUNTEREXAMPLE FOUND, NOT PROVED:** finite searches for negative
  weighted R_2 among actual small AP-free sets found none in the tested
  configurations. Generic PSD nevertheless fails as above. Search scripts
  are preserved under history/log_density_20261016/.
- **RESOLVED FOR THE NEW METHOD:** the old obstruction that repeated
  quadratic refinements leave the single-arc class is addressed by MT16.
  Failure of translation packing is still valid and does not affect the
  new weighted terminal count. The missing inverse/selection input remains.
