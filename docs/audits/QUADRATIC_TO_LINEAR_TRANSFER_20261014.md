# Centered Baseline-Free All-Chirp Identities, Analytic Hitting-Degree Terminal Bound (\(\le 53/69 < 4/5\)), and Quadratic-to-Linear Transfer — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with Phase 0 complex all-chirp audit across 5 test classes, exact centered baseline-free chirp covariance identities for \(S_E, S_M, M_E, M_M, R_4\), universal fourth-moment chirp norm obstruction, and the exact \(16/69 > 1/5\) hitting-degree terminal bound for quadratic windows).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, `COLLECTIVE-WSELECT`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 — Independent Audit of the Complex All-Chirp Identities

For any complex function \(w : \mathbb{Z}_p \to \mathbb{C}\) (\(p>3\) prime), define its quadratic chirp transform
\[
Q_w(c, r) := \mathbb{E}_{x\in\mathbb{Z}_p}\bigl[w(x)e_p(-c x^2 - r x)\bigr], \qquad (c, r)\in\mathbb{Z}_p^2. \tag{0.1}
\]
Because \(r \mapsto Q_w(c, r)\) is the ordinary normalized Fourier transform of \(x \mapsto w(x)e_p(-c x^2)\) for each fixed slope \(c\in\mathbb{Z}_p\), Parseval gives for every \(v_1, v_2, w : \mathbb{Z}_p \to \mathbb{C}\):
\[
\sum_{r\in\mathbb{Z}_p} \overline{Q_{v_1}(c, r)}\,Q_{v_2}(c, r) = \langle v_1, v_2\rangle_p \quad (\forall c\in\mathbb{Z}_p), \qquad
\sum_{c,r\in\mathbb{Z}_p} |Q_w(c, r)|^2 = p\,\mathbb{E}_{x\in\mathbb{Z}_p}|w(x)|^2. \tag{0.2}
\]

**Theorem 1 (General Complex Trilinear All-Chirp Operator Identities).**
For any complex functions \(v_1, v_2, w : \mathbb{Z}_p \to \mathbb{C}\) (\(p>3\)), define the complex-kernel operators
\[
(K_w g)(x) := \mathbb{E}_y w\bigl((2x+y)/3\bigr)\overline{w\bigl((x+2y)/3\bigr)}g(y), \qquad
(R_w g)(x) := \mathbb{E}_y w(2x-y)\overline{w(2y-x)}g(y). \tag{0.3}
\]
Then:
\[
\begin{aligned}
\langle v_1, K_w v_2\rangle_p &= \sum_{c,r\in\mathbb{Z}_p} \overline{Q_{v_1}(c,r)}\,Q_{v_2}(c,r)\,|Q_w(3c,3r)|^2 - \langle v_1,v_2\rangle_p\,\|w\|_2^2 + \frac{1}{p}\mathbb{E}_x\bigl[\overline{v_1(x)}v_2(x)|w(x)|^2\bigr], \\
\langle v_1, R_w v_2\rangle_p &= \sum_{c,r\in\mathbb{Z}_p} \overline{Q_{v_1}(3c,3r)}\,Q_{v_2}(3c,3r)\,|Q_w(c,r)|^2 - \langle v_1,v_2\rangle_p\,\|w\|_2^2 + \frac{1}{p}\mathbb{E}_x\bigl[\overline{v_1(x)}v_2(x)|w(x)|^2\bigr].
\end{aligned} \tag{0.4}
\]
*Proof.* Expanding the four chirp factors in \(\sum_{c,r}\overline{Q_{v_1}(3c,3r)}Q_{v_2}(3c,3r)|Q_w(c,r)|^2\) and summing over \(c, r\in\mathbb{Z}_p\) gives \(p^{-2}\) times the sum over \(x, x', y, y'\in\mathbb{Z}_p\) satisfying \(3(x - x') \equiv y - y'\pmod p\) and \(3(x^2 - x'^2) \equiv y^2 - y'^2\pmod p\).
- When \(x = x'\), we have \(y = y'\), contributing \(p^{-2}\sum_{x,y}\overline{v_1(x)}v_2(x)|w(y)|^2 = \langle v_1,v_2\rangle_p\,\|w\|_2^2\).
- When \(x \ne x'\), dividing the second congruence by \(3(x-x') \equiv y-y' \not\equiv 0\pmod p\) cancels the factor of \(3\) on both sides and gives \(y + y' \equiv x + x'\pmod p\). Together with \(y - y' \equiv 3(x - x')\), this forces \(y \equiv 2x - x'\) and \(y' \equiv 2x' - x\pmod p\), which is the off-diagonal part of \(\langle v_1, R_w v_2\rangle_p\) minus its \(x=x'\) diagonal \(\frac{1}{p}\mathbb{E}_x[\overline{v_1(x)}v_2(x)|w(x)|^2]\). The proof for \(K_w\) is identical. \(\square\)
*(Verified across 375 combinations of constant functions, delta functions, linear characters, quadratic chirps, and random complex functions on \(\mathbb{Z}_7, \mathbb{Z}_{11}, \mathbb{Z}_{13}\) in `verify_quadratic_to_linear_transfer_20261014.py`.)*

---

## Phase 1 & Phase 5 — Analytic Hitting-Degree Terminal Theorem (\(\le 53/69 < 4/5\)) vs Multi-Quadratic Collapse

In `QUADRATIC_TWO_BRANCH_CLOSURE_20261014.md` Theorem 4, we proved that on a pure quadratic interval window \(\Omega_{\text{quad}} = \{x\in\mathbb{Z}_p : q(x) \in I\}\) (\(w = |I|/p \le 1/4\)), every nonzero cyclic shift \(h\ne 0\) loses \(\ge 1 - w - o(1) \ge 3/4 - o(1)\) of \(\Omega_{\text{quad}}\), so the **single-shift \(h\)-cycle translation-packing** terminal argument fails.
In Phase 1, we carefully distinguish failure of translation packing from impossibility of a terminal contradiction on \(\Omega_{\text{quad}}\), and prove an **analytic hitting-degree terminal bound** that beats \(4/5\) on any single quadratic window without translation packing:

**Theorem 2 (Universal Hitting-Degree Terminal Bound and Exact \(16/69 > 1/5\) Quadratic-Window Constant).**
1. **(Universal hitting-degree identity on any host \(\Omega\subset\mathbb{Z}_p\))**:
   Let \(P = 1_\Omega\) have density \(w = |\Omega|/p\), let \(h_\Omega(v) = \sum_{i=0}^3 \mathbb{E}_d\prod_{j\ne i}P(v+(j-i)d)\), and let \(A\subset\Omega\) be cyclically 4-AP-free for nonzero differences with relative density \(a = |A|/|\Omega|\). Then \(\mathbb{E}_p[P\,h_\Omega] = 4\Lambda_4(P)\), \(\mathbb{E}_p[(P - B)h_\Omega] \ge \Lambda_4(P) - w/p\), and for \(u = B - aP\):
   \[
   \mathbb{E}_p\bigl[(-u)\,h_\Omega\bigr] = \mathbb{E}_p\bigl[(aP - B)h_\Omega\bigr] \ge (4a - 3)\Lambda_4(P) - \frac{w}{p}. \tag{1.1}
   \]
   In particular, if \(h_\Omega(v) \le H_{\max}\) for all \(v\in\Omega\setminus E\) (with \(h_\Omega(v)\le 4\) on \(E\)), then:
   \[
   1 - a = \frac{|\Omega\setminus A|}{|\Omega|} \ge \frac{\Lambda_4(P) - (w + 4|E|)/p}{w\,H_{\max}}. \tag{1.2}
   \]
2. **(Exact continuum constants \(Z_I = \frac{8}{27}w^3\) and \(\max_I H = \frac{23}{18}w^2\) for \(0 < w \le 1/4\))**:
   For a residue interval \(I\subset\mathbb{Z}_p\) of relative length \(0 < w = |I|/p \le 1/4\), let \(C_I(y) = \mathbb{E}_z 1_I(z)1_I(z+y)\) be its tent autocorrelation. Because \(3w \le 3/4 \implies w + w/3 \le 1/3 < 1\), \(C_I(3y)\) has zero wraparound on \((-w, w)\), and the continuum limits on \(\mathbb{R}/\mathbb{Z}\) are **exact**:
   \[
   \begin{aligned}
   Z_I = \sum_{t\in\mathbb{Z}} |\widehat{1_I}(t)|^2 |\widehat{1_I}(3t)|^2 &= 2\int_0^{w/3}(w-3y)(w-y)\,dy = \frac{8}{27}w^3, \\
   \max_{y\in I} \Phi_M(y) = \max_{y\in I}(1_I * C_I(3\cdot))(y) &= \int_{-w/3}^{w/3}(w-3|z|)\,dz = \frac{1}{3}w^2, \\
   \max_{y\in I} \Phi_E(y) = \max_{y\in I}(1_I * C_I(\cdot/3))(y) &= 2\int_0^{w/6}(w-z)\,dz = \frac{11}{36}w^2, \\
   \max_{y\in I} H(y) = 2\max_{y\in I}\Phi_E(y) + 2\max_{y\in I}\Phi_M(y) &= 2\left(\frac{11}{36} + \frac{1}{3}\right)w^2 = \frac{23}{18}w^2.
   \end{aligned} \tag{1.3}
   \]
3. **(Analytic terminal contradiction \(a \le \frac{53}{69} + o(1) < \frac{4}{5}\) on a single quadratic window)**:
   For \(\Omega_{\text{quad}} = \{x\in\mathbb{Z}_p : c x^2 + r x \bmod p \in I\}\) (\(c\ne 0,\ 0 < w \le 1/4\)), combining \(\Lambda_4(1_{\Omega_{\text{quad}}}) \ge Z_I - K_I^4/\sqrt{p}\) and \(h_{\Omega_{\text{quad}}}(v) \le H(q(v)) + 4K_I^3/\sqrt{p}\) for \(v \ne r_0\) (`SELECT_DELETION_20261002.md` §2) with (1.2) and (1.3) proves that **every 4-AP-free subset \(A\subset\Omega_{\text{quad}}\) has hole fraction and relative density satisfying**:
   \[
   \boxed{
   1 - a \ge \frac{8/27}{23/18} - O\bigl(w^{-3}p^{-1/2}\log^4 p\bigr) = \frac{16}{69} - o(1) > \frac{1}{5}, \qquad
   a \le \frac{53}{69} + o(1) \approx 0.768116 < \frac{4}{5}!!
   } \tag{1.4}
   \]
   *(This improves the \(\frac{1}{24\pi^4} \approx 0.000427\) constant of `ROUTE_QUADRATIC_BOOLEAN_20261002.md` `(Q6)` by a factor of \(542\), and proves that a single quadratic window has a terminal contradiction below \(4/5\) without translation packing!)*
4. **(Why iterating \(s \ge 2\) quadratic coordinates still fails in Architecture B)**:
   - Over \(\mathbb{F}_p\), the monomial \(x^2\pmod p\) spans a 1-dimensional space: for any two quadratic phases \(q_1(x) = c_1 x^2 + r_1 x\) and \(q_2(x) = c_2 x^2 + r_2 x\) (\(c_1,c_2\in\mathbb{F}_p^\times\)), \(c_1^{-1}q_1(x) - c_2^{-1}q_2(x) \equiv (c_1^{-1}r_1 - c_2^{-1}r_2)x \pmod p\) is a **linear character**.
   - Even if one treats \(q_1(x)/p,\dots,q_s(x)/p \in \mathbb{R}/\mathbb{Z}\) as \(s\) separate torus coordinates with quarter-intervals \(I_1,\dots,I_s\) (\(w_l = 1/4\)), the simultaneous resonant 4-AP main term \(\prod_{l=1}^s Z_{I_l} = (\frac{8}{27})^s w^3\) divided by \(w \prod_{l=1}^s (\frac{23}{18}w_l^2)\) decays exponentially as \((\frac{16}{69})^s \to 0\), so the hitting-degree terminal bound (1.2) only forces \(1 - a \ge (\frac{16}{69})^s \to 0\) (which fails to contradict \(a > 4/5\) once \(s \ge 2\)).

---

## Phase 2 & Phase 3 — Exact Centered Baseline-Free All-Chirp Covariance Identities and Fourth-Moment Norm Obstruction

In `QUADRATIC_TWO_BRANCH_CLOSURE_20261014.md` Theorem 3, the all-chirp formulas for \(S_E, S_M\) (`(2.3)`) and \(R_4\) (`(2.4)`) contained the \(O(a^2)\) baselines \(aU\) and \(-U^2\). By subtracting the exact per-slope \(r\)-mean (\(\frac{U}{p}\) or \(\frac{a}{p}\) from (0.2)) at each nonzero slope \(c \in \mathbb{Z}_p\setminus\{0\}\), those \(O(a^2)\) baselines cancel identically:

**Theorem 3 (Centered Baseline-Free All-Chirp Identities and Universal Fourth-Moment Norm).**
For each slope \(c \in \mathbb{Z}_p\setminus\{0\}\) and frequency \(r\in\mathbb{Z}_p\), define the zero-mean-in-\(r\) chirp fluctuations:
\[
\widetilde{W}_u(c, r) := |Q_u(c, r)|^2 - \frac{U}{p}, \qquad
\widetilde{W}_B(c, r) := |Q_B(c, r)|^2 - \frac{a}{p}, \qquad
\widetilde{C}_{u,B}(c, r) := \operatorname{Re}\bigl(\overline{Q_u(c,r)}\,Q_B(c,r)\bigr) - \frac{U}{p}. \tag{2.1}
\]
Then for every 4-AP-free set \(A\subset\mathbb{Z}_p\) and every factor \(F\) (\(u = B - g,\ U = \mathbb{E}[u^2]\)):
1. **(Baseline-free Branch I chirp identities for \(S_E\) and \(S_M\))**:
   \[
   \begin{aligned}
   S_E &= \frac{a U}{p} - \sum_{r\ne 0} \operatorname{Re}\bigl(\overline{\widehat{u}(r)}\,\widehat{B}(r)\bigr)\,|\widehat{B}(3r)|^2
          - \sum_{c\ne 0}\sum_{r\in\mathbb{Z}_p} \widetilde{C}_{u,B}(c, r)\,\widetilde{W}_B(3c, 3r), \\
   S_M &= \frac{a U}{p} - \sum_{r\ne 0} \operatorname{Re}\bigl(\overline{\widehat{u}(r)}\,\widehat{B}(r)\bigr)\,|\widehat{B}(r/3)|^2
          - \sum_{c\ne 0}\sum_{r\in\mathbb{Z}_p} \widetilde{C}_{u,B}(c, r)\,\widetilde{W}_B(c/3, r/3).
   \end{aligned} \tag{2.2}
   \]
2. **(Baseline-free Branch II chirp identities for \(M_E, M_M\), and \(R_4\))**:
   \[
   \begin{aligned}
   M_E = \langle u, K_B u\rangle_p &= \sum_{r\ne 0} |\widehat{u}(r)|^2 |\widehat{B}(3r)|^2 + \sum_{c\ne 0}\sum_{r\in\mathbb{Z}_p} \widetilde{W}_u(c, r)\,\widetilde{W}_B(3c, 3r) + \frac{\mathbb{E}[u^2 B] - a U}{p}, \\
   M_M = \langle u, R_B u\rangle_p &= \sum_{r\ne 0} |\widehat{u}(r)|^2 |\widehat{B}(r/3)|^2 + \sum_{c\ne 0}\sum_{r\in\mathbb{Z}_p} \widetilde{W}_u(c, r)\,\widetilde{W}_B(c/3, r/3) + \frac{\mathbb{E}[u^2 B] - a U}{p}, \\
   R_4 = \Lambda_4(u,u,u,u) &= \sum_{r\ne 0} |\widehat{u}(r)|^2 |\widehat{u}(3r)|^2 + \sum_{c\ne 0}\sum_{r\in\mathbb{Z}_p} \widetilde{W}_u(c, r)\,\widetilde{W}_u(3c, 3r) + \frac{\mathbb{E}[u^4] - U^2}{p}.
   \end{aligned} \tag{2.3}
   \]
3. **(Exact fourth-moment norms of the centered chirp fluctuations)**:
   \[
   \begin{aligned}
   \sum_{c\ne 0}\sum_{r\in\mathbb{Z}_p} \widetilde{W}_u(c, r)^2 &= U^2 - \|u\|_{U^2}^4 - \frac{\mathbb{E}[u^4] - U^2}{p}, \\
   \sum_{c\ne 0}\sum_{r\in\mathbb{Z}_p} \widetilde{W}_B(c, r)^2 &= a^2 - \|B\|_{U^2}^4 - \frac{a(1 - a)}{p}, \\
   \sum_{c\in\mathbb{Z}_p}\sum_{r\in\mathbb{Z}_p} \bigl[\operatorname{Re}\bigl(\overline{Q_u(c,r)}\,Q_B(c,r)\bigr)\bigr]^2 &= \frac{3 U^2 + a U}{2} - \frac{\mathbb{E}[u^2 B]}{p}.
   \end{aligned} \tag{2.4}
   \]
   **Consequence (The Overcompleteness Norm Obstruction)**: Because the family of \(p(p-1)\) nonzero-slope chirps has total squared norm \(\sum_{c\ne 0, r}|Q_u(c,r)|^2 = (p-1)U\) and constant fourth-moment variance \(\sum_{c\ne 0, r}\widetilde{W}_u(c,r)^2 \approx U^2 \sim a^2\) for **every** function \(u\) with small \(\|u\|_{U^2}^4\), a correlation of size \(a^4\) in (2.2) or (2.3) is only an \(O(a^2)\) fraction of the Cauchy–Schwarz norm \(U^2 \sim a^2\), and by itself only forces \(\max_{c\ne 0, r}|Q_u(c,r)|^2 \ge \frac{U}{p} + \frac{c_0 a^3}{p} \asymp \frac{a}{p}\).

---

## Phase 4 — Quadratic-to-Linear Transfer Analysis

1. **Without 4-AP exclusion, quadratic-to-linear transfer is FALSE**:
   For the Boolean quadratic interval host \(B(x) = 1_I(c_0 x^2 + r_0 x)\) (\(c_0\ne 0,\ w = |I|/p \sim \epsilon/\log p\)), \(|Q_f(c_0, r_0)| \ge \frac{2}{\pi}w(1-o(1)) \sim a\) is maximal, yet every nonzero linear Fourier coefficient satisfies \(|\widehat{f}(\xi)| \le \frac{2+\log p}{\sqrt{p}}\), so any packet \(\Gamma\) of size \(\le M(a) = O(a^{-1/4}/\ell(a))\) captures linear energy \(O(M(a)p^{-1}\log^2 p) = o(a^{5/2}R(a))\).
2. **With 4-AP exclusion, why linear transfer must go through the two fields \(K_u^{(2)}\) and \(K_u^{(3)}\)**:
   By Theorem 2 (`(1.4)`), no 4-AP-free set can cover more than \(\frac{53}{69} + o(1)\) of a quadratic interval host \(\Omega_{\text{quad}}\), and by `SELECT_DELETION_20261002.md` §3 (`(6)`), any 4-AP-free subset leaving hole fraction \(\theta < 1/4\) in a host \(C\) has discrepancy \(\langle 1_{C\setminus A} - \theta 1_C, h_C\rangle_p \ge (1-4\theta)\Lambda_4(1_C) - w/p\). However, for a quadratic host \(C = \Omega_{\text{quad}}\), \(h_C(v) = H(q(v)) + O(p^{-1/2}\log^3 p)\) is itself a function of the quadratic phase \(q(v)\), so its Fourier support is quadratic rather than linear. Thus, extracting a **linear** character packet \(\Gamma\) for Architecture A must work directly with the linear Fourier spectra of the two residual completion fields \(K_u^{(2)}\) and \(K_u^{(3)}\) isolated in `TWO_BRANCH_AUTONOMOUS_CLOSURE_20261014.md` (`Sublemmas 2A'` and `2B'` in `OPEN_LEMMAS.md`).

---

## Verification Summary (`verify_quadratic_to_linear_transfer_20261014.py`)
Run `python3 verify_quadratic_to_linear_transfer_20261014.py` (outputs `QUADRATIC_TO_LINEAR_TRANSFER_VERIFICATION_20261014.json`):
- **15** Parseval checks and **375** complex trilinear chirp identity checks (`Theorem 1`) across constants, deltas, linear characters, quadratic chirps, and random complex functions;
- **100** universal hitting-degree terminal checks (`Theorem 2(1)`) and **4** exact continuum constant checks (`p=101, 257, 509, 1009`) confirming \(Z_I/w^3 \to 8/27\), \(\max_I H/w^2 \to 23/18\), and hole bound \(1 - a \ge 16/69 - o(1) > 1/5\) (`a \le 53/69 + o(1) < 4/5`);
- **2,247** verifications of the centered baseline-free chirp covariance identities (`Theorem 3(1)–(2)`) and exact fourth-moment chirp norms (`Theorem 3(3)`), plus **16** global-law orbit checks on \(\mathbb{Z}_{23}, \mathbb{Z}_{29}\).
