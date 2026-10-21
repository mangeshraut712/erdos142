# Autonomous Two-Branch Closure: Proper-Window \(D_3\) Reduction, Operator \(U^3\) Variance Bound \(\|K_u^{(3)}\|_2^2 \le 4U\|u\|_{U^3}^4\), and Peak-versus-Diffuse Dichotomy — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with Phase 0 bilateral multiplier repair, exact proper-window two-branch reduction, operator-norm / \(U^3\) completion-variance bound \(\|K_u^{(3)}\|_2^2 \le 4U\|u\|_{U^3}^4\), universal arbitrary-factor residual \(U^3\) theorem, and peak-versus-diffuse projection dichotomy).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, `COLLECTIVE-WSELECT`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 — Independent Audit of Theorems A–E and the Bilateral Multiplier Repair

We independently audited `FINAL_STRUCTURAL_BOTTLENECK_20261014.md`:
1. **Theorems A–D**: All one-sided physical truncation bounds (`D_3 \ge 4a^4 - 6a^3\sqrt{v}`, `R_1 \ge -6a^3\sqrt{v} - 16a v^{3/2} - 4v^2`, `T \ge a^4 - 3a^3\sqrt{v} - 4a v^{3/2} - v^2 + (U-a^2-v)/p`), the \(K^{(2)}/K^{(3)}\) splitting, and the clipped completion identities hold unconditionally with their stated normalizations.
2. **Audit of Theorem E (`\Gamma_\alpha(\tau)` indexing) and Bilateral Strengthening**:
   In `FINAL_STRUCTURAL_BOTTLENECK_20261014.md` Theorem E, \(\Gamma_\alpha(\tau)\) was defined as \(\{\xi\ne 0 : |\widehat{u}(\alpha\xi)| \ge \tau\} = \alpha^{-1}\operatorname{Spec}_\tau(u)\). For \(\xi\in\Gamma_\alpha(\tau)\), the pointwise threshold \(\ge \tau\) holds at the **image frequency** \(\alpha\xi\), while the energy lower bound \(\sum_{\xi\in\Gamma_\alpha(\tau)}|\widehat{u}(\xi)|^2 \ge \frac{|T_u+S_u|}{4\rho}\) was evaluated at the **preimage frequency** \(\xi\).
   We repair and strengthen Theorem E so that **both** \(\xi\) and \(\alpha\xi\) lie in the large spectrum simultaneously:

**Theorem 1 (Bilateral Multiplier-Rich Set \(\Gamma_\alpha^*(\tau)\)).**
Let \(u\) be any mean-zero function on \(\mathbb{Z}_p\) (\(p>3\)) with \(\|u\|_2^2 = U > 0\) and \(\max_{\xi\ne 0}|\widehat{u}(\xi)| = \rho\). If \(M := |T_u + S_u| > 0\), then at least one invertible multiplier \(\alpha \in \{-2, -3, -3/2\}\pmod p\) satisfies \(\sum_{\xi\ne 0}|\widehat{u}(\xi)|^2|\widehat{u}(\alpha\xi)| \ge \frac{1}{2}M\). Put \(\tau := \frac{M}{4U}\) and define the **bilaterally thresholded multiplier set**:
\[
\Gamma_\alpha^*(\tau) := \Bigl\{\xi\in\mathbb{Z}_p\setminus\{0\} : |\widehat{u}(\xi)| \ge \frac{\tau}{\sqrt{2}} \ \text{ AND }\ |\widehat{u}(\alpha\xi)| \ge \tau\Bigr\}
= \operatorname{Spec}_{\tau/\sqrt{2}}(u) \cap \alpha^{-1}\operatorname{Spec}_\tau(u). \tag{1.1}
\]
Then:
1. \(|\Gamma_\alpha^*(\tau)| = |\alpha\Gamma_\alpha^*(\tau)| \le \frac{U}{\tau^2} = \frac{16 U^3}{M^2}\).
2. \(\sum_{\xi\in\Gamma_\alpha^*(\tau)} |\widehat{u}(\xi)|^2 |\widehat{u}(\alpha\xi)| \ge \frac{1}{8}M\).
3. Both \(\Gamma_\alpha^*(\tau)\) and its multiplicative image \(\alpha\Gamma_\alpha^*(\tau)\) carry large residual Fourier energy:
   \[
   \sum_{\xi\in\Gamma_\alpha^*(\tau)} |\widehat{u}(\xi)|^2 \ge \frac{M}{8\rho}, \qquad
   \left(\sum_{\xi\in\Gamma_\alpha^*(\tau)} |\widehat{u}(\xi)|^2\right)\left(\sum_{\eta\in\alpha\Gamma_\alpha^*(\tau)} |\widehat{u}(\eta)|^2\right) \ge \frac{M^2}{64\rho^2}. \tag{1.2}
   \]

*Proof.* On \(\{\xi\ne 0 : |\widehat{u}(\alpha\xi)| < \tau\}\), \(\sum |\widehat{u}(\xi)|^2|\widehat{u}(\alpha\xi)| < \tau U = \frac{1}{4}M\). On \(\{\xi\in\Gamma_\alpha(\tau) : |\widehat{u}(\xi)| < \tau/\sqrt{2}\}\), since \(|\widehat{u}(\alpha\xi)|\ge \tau \implies |\widehat{u}(\alpha\xi)| \le \tau^{-1}|\widehat{u}(\alpha\xi)|^2\), we have \(\sum_{\xi\in\Gamma_\alpha(\tau),\,|\widehat{u}(\xi)|<\tau/\sqrt{2}} |\widehat{u}(\xi)|^2|\widehat{u}(\alpha\xi)| \le \frac{\tau^2}{2}\sum_{\eta\in\operatorname{Spec}_\tau(u)} |\widehat{u}(\eta)| \le \frac{\tau^2}{2}\frac{U}{\tau} = \frac{1}{2}\tau U = \frac{1}{8}M\). Subtracting \(\frac{1}{4}M + \frac{1}{8}M = \frac{3}{8}M\) from \(\frac{1}{2}M\) proves (2), and Cauchy–Schwarz proves (1.2). \(\square\)

---

## Phase 1 — Proper-Window Two-Branch Reduction and Window-Marginal \(\ell^1\) Bound

We now extend Theorem A to any proper narrow coordinate window \(\Omega\subset\mathbb{Z}_p\) of size \(n=wp\) (\(W=1_\Omega\), \(C=\Lambda_4(W)\ge w^2/3^d\), \(K = w^2/C \le 3^d\)):

**Theorem 2 (Proper-Window Two-Branch Reduction and \(\ell^1\) Window-Marginal Bound).**
Let \(A\subset\Omega\subset\mathbb{Z}_p\) be cyclically 4-AP-free for nonzero differences, let \(F\) be any partition of \(\Omega\), and write \(g = \mathbb{E}_\Omega[B\mid F] = aW + h\), \(u = B - g\), \(v = \mathbb{E}_\Omega[h^2]\), and \(\rho_\Omega = \max_{\xi\ne 0}|\mathbb{E}_\Omega[u(x)e_p(-\xi x)]|\). Then:
1. **(Upper bound on \(R_0\) on \(\Omega\))**:
   \[
   R_0 = \Lambda_4(g,g,g,g) \le a^4 C + a^3 \sum_{i=0}^3 \Lambda_4\bigl(h\text{ at }i,\ W\text{ at }\ne i\bigr) + 6w^2 a^2 v + 4a(wv)^{3/2} + (wv)^2. \tag{2.1}
   \]
2. **(Proper-window conservation law lower bound)**: Combining (2.1) with `FINAL_STRUCTURAL_BOTTLENECK_20261014.md` `(1.2)` gives:
   \[
   \begin{aligned}
   T = w(S_E + S_M) + \left(\frac{1}{2}R_3 + R_4\right)
   \ge\ & a^4 C + \frac{1}{2}a^3 \sum_{i=0}^3 \Lambda_4\bigl(u - h\text{ at }i,\ W\text{ at }\ne i\bigr) \\
   &- 3w^2 a^3\sqrt{v} - 6w^2 a^2 v - 4a(wv)^{3/2} - (wv)^2 + \frac{w(U - a^2 - v)}{p}.
   \end{aligned} \tag{2.2}
   \]
3. **(Exact \(\ell^1\)-Fourier and Cauchy–Schwarz bounds on the window-marginal terms)**:
   For each slot \(i\in\{0,1,2,3\}\), let \(W_i(x) = \mathbb{E}_d\prod_{j\ne i}W(x+(j-i)d) = \frac{C}{w}r_i(x)\). Then \(\|\widehat{W_i}\|_{\ell^1(\mathbb{Z}_p)} \le w\,\|\widehat{W}\|_{\ell^1(\mathbb{Z}_p)} \le w(2+\log p)^d\), and:
   \[
   \Bigl|\sum_{i=0}^3 \Lambda_4\bigl(u\text{ at }i,\ W\text{ at }\ne i\bigr)\Bigr| \le \min\Bigl(4w^2 \rho_\Omega\,\|\widehat{W}\|_{\ell^1(\mathbb{Z}_p)},\ 4C\sqrt{(K-1)U}\Bigr), \qquad
   \Bigl|\sum_{i=0}^3 \Lambda_4\bigl(h\text{ at }i,\ W\text{ at }\ne i\bigr)\Bigr| \le 4C\sqrt{(K-1)v}. \tag{2.3}
   \]
   *(This resolves `Sublemma 2C` of `OPEN_LEMMAS.md`: at \(v \le \zeta a^{9/4}\), all variance error terms in (2.2) are \(O(K a^{1/8}\cdot a^4 C) = o(a^4 C)\) whenever \(K a^{1/8}\to 0\), and if \(\frac{1}{2}a^3\sum_i \Lambda_4(u\text{ at }i, W\text{ at }\ne i) \le -\frac{1}{4}a^4 C\), (2.3) immediately supplies a single relative Fourier coefficient \(\rho_\Omega \ge \frac{a}{8 K \|\widehat{W}\|_{\ell^1}}\).)*

---

## Phase 2 — Operator-Norm / \(U^3\) Completion-Variance Bound and Peak-versus-Diffuse Dichotomy

### 2.1 Exact Fourier Splitting of \(Q_0 K_B Q_0, Q_0 R_B Q_0\) and \(U^3\) Bound on \(\|K_u^{(3)}\|_2^2\) — PROVED
Let \(Q_0 = I - |1\rangle\langle 1|\) be the projection onto mean-zero functions on \(\mathbb{Z}_p\). For any mean-zero function \(u\) on \(\mathbb{Z}_p\), define the centered completion operators
\[
(K_u g)(x) := \mathbb{E}_y u\bigl((2x+y)/3\bigr)u\bigl((x+2y)/3\bigr)g(y), \qquad
(R_u g)(x) := \mathbb{E}_y u(2x-y)u(2y-x)g(y). \tag{3.1}
\]

**Theorem 3 (Fourier Operator Decomposition and \(U^3\) Completion-Variance Inequality).**
1. **(Exact decomposition on \(1^\perp\))**: For \(B = a + f\) on \(\mathbb{Z}_p\) (\(p>3\)), in the orthonormal basis \(\{e_r\}_{r\in\mathbb{Z}_p\setminus\{0\}}\) of \(1^\perp\):
   \[
   Q_0 K_B Q_0 = a\,L_{E,f} + Q_0 K_f Q_0, \qquad Q_0 R_B Q_0 = a\,L_{M,f} + Q_0 R_f Q_0, \tag{3.2}
   \]
   where \(\langle e_r, L_{E,f} e_s\rangle_p = \widehat{f}(3r)1_{s\equiv -2r} + \widehat{f}(-3s)1_{r\equiv -2s}\) and \(\langle e_r, L_{M,f} e_s\rangle_p = \widehat{f}(-r)1_{s\equiv 2r} + \widehat{f}(s)1_{r\equiv 2s}\) are 2-sparse monomial shift matrices satisfying \(\|L_{E,f}\|_{\text{op}}, \|L_{M,f}\|_{\text{op}} \le 2\rho\) and \(\langle u, L_{E,f} u\rangle_p + \langle u, L_{M,f} u\rangle_p = 2(T_u + S_u) + 2\sum_{r\ne 0}[\widehat{u}(r)^2\widehat{h}(-2r) + \widehat{u}(r)\widehat{u}(2r)\widehat{h}(-3r)]\).
2. **(Fourth-power trace and operator norm of \(K_u, R_u\))**: For any real mean-zero function \(u\) on \(\mathbb{Z}_p\), \(K_u\) and \(R_u\) are real symmetric operators satisfying
   \[
   \operatorname{tr}(K_u^4) = \operatorname{tr}(R_u^4) = \mathbb{E}_{h,k}\bigl[F_u(2h,-k)F_u(-h,2k)\bigr] \le \|u\|_{U^3}^8, \qquad
   \|K_u\|_{\text{op}}^2 \le \|u\|_{U^3}^4, \qquad \|R_u\|_{\text{op}}^2 \le \|u\|_{U^3}^4. \tag{3.3}
   \]
3. **(Exact \(U^3\) bound on the cubic completion spectrum \(K_u^{(3)}\))**: Since \(h_{E,u} = K_u u\) and \(h_{M,u} = R_u u\), the Fourier transform \(K_u^{(3)}(t) = \widehat{h_{E,u}}(t) + \widehat{h_{M,u}}(t)\) (\(t\ne 0\)) satisfies both the pointwise \(\widehat{\ell^3}\) cap and the global \(U^3\) variance bound:
   \[
   \boxed{
   \max_{t\in\mathbb{Z}_p\setminus\{0\}} |K_u^{(3)}(t)| \le 2\sum_{\xi\ne 0} |\widehat{u}(\xi)|^3 \le 2\sqrt{U}\,\|u\|_{U^2}^2, \qquad
   \sum_{t\in\mathbb{Z}_p\setminus\{0\}} |K_u^{(3)}(t)|^2 \le \|h_{E,u} + h_{M,u}\|_2^2 \le 4 U\,\|u\|_{U^3}^4!
   } \tag{3.4}
   \]
   In particular, for \(u = f = B - a\), the total variance of \(q_E + q_M\) on \(\mathbb{Z}_p\) satisfies:
   \[
   \boxed{\operatorname{Var}_p(q_E + q_M) \le 72 a^3 \rho^2 + 8 a(1-a)\,\|f\|_{U^3}^4 + \frac{8a}{p^2}.} \tag{3.5}
   \]

### 2.2 Peak-versus-Diffuse Projection Dichotomy in Branch I — PROVED
**Theorem 4 (Peak-versus-Diffuse Projection Dichotomy).**
On any window \(\Omega\subset\mathbb{Z}_p\) (\(w = |\Omega|/p\)), let \(q(x) = q_E(x) + q_M(x)\), so \(0 \le q(x) \le 2wa\) and \(B(x)q(x) = 0\). For any threshold \(\tau_q > 0\), split \(q = \tilde{q} + q_{>\tau_q}\) where \(\tilde{q}(x) = \min(q(x), \tau_q)\) and \(q_{>\tau_q}(x) = \max(q(x)-\tau_q, 0)\), and let \(P_{\tau_q} := \{x\in\Omega : q(x) > \tau_q\} \subset \Omega\setminus A\). Set \(\tilde{k} = \tilde{q} - \mathbb{E}_F[\tilde{q}]\) and \(p_{\tau_q} = 1_{P_{\tau_q}} - \mathbb{E}_F[1_{P_{\tau_q}}]\). Then:
1. **(Diffuse projection bound — \(\tau_q\) in denominator)**:
   \[
   \langle u, \tilde{k}\rangle_\Omega = -\tilde{S}(\tau_q), \qquad
   \frac{|\langle u, \tilde{k}\rangle_\Omega|^2}{\|\tilde{k}\|_{L^2(\Omega)}^2} \ge \frac{\tilde{S}(\tau_q)^2}{\tau_q\,\mathbb{E}_\Omega[\tilde{q}]}. \tag{3.6}
   \]
2. **(Peak-set projection bound — \(\tau_q\) in numerator)**: Because \(B(x) = 0\) on \(P_{\tau_q}\) and \(q(x) \le 2wa\), we have
   \[
   -\langle u, p_{\tau_q}\rangle_\Omega = -\langle u, 1_{P_{\tau_q}}\rangle_\Omega = \mathbb{E}_\Omega\bigl[g\,1_{P_{\tau_q}}\bigr] \ge \frac{S_{>\tau_q}(\tau_q)}{2wa}, \qquad
   \|p_{\tau_q}\|_{L^2(\Omega)}^2 \le \mu_\Omega(P_{\tau_q}) \le \frac{\mathbb{E}_\Omega[q]}{\tau_q}, \tag{3.7}
   \]
   and therefore
   \[
   \frac{|\langle u, p_{\tau_q}\rangle_\Omega|^2}{\|p_{\tau_q}\|_{L^2(\Omega)}^2} \ge \frac{\tau_q\,S_{>\tau_q}(\tau_q)^2}{4w^2 a^2\,\mathbb{E}_\Omega[q]}. \tag{3.8}
   \]

---

## Phase 3 — Universal Branch II Identity and Arbitrary-Factor Residual \(U^3\) Theorem

Combining the definitions of \(K_u^{(2)}\) and \(K_u^{(3)}\) yields an exact representation of the Branch II quantity \(Y = \frac{1}{2}R_3 + R_4\) that holds for **every** intermediate factor \(F\) on \(\mathbb{Z}_p\) without any \(R_1\) or \(R_2\) error:

**Theorem 5 (Universal Branch II Identity and Arbitrary-Factor Residual \(U^3\) Lower Bound).**
For every subset \(A\subset\mathbb{Z}_p\) (\(p>3\)) and every partition \(F\) of \(\mathbb{Z}_p\) with \(g = \mathbb{E}[B\mid F] = a + h\), \(u = B - g\), \(U = \mathbb{E}[u^2]\), and \(v = \mathbb{E}[h^2]\):
1. **(Exact Fourier pairing of \(K_u^{(2)}\) and \(K_u^{(3)}\))**:
   \[
   \langle u, K_u^{(2)}\rangle_p = 3a(T_u + S_u), \qquad
   \langle u, K_u^{(3)}\rangle_p = 2R_4 = 2\Lambda_4(u,u,u,u), \qquad
   \langle h, K_u^{(3)}\rangle_p = \frac{1}{2}R_{3,(1)}, \tag{4.1}
   \]
   where \(\|K_u^{(2)}\|_2^2 \le 36a^2\|u\|_{U^2}^4 \le 36a^2\rho^2 U\) and \(\|K_u^{(3)}\|_2^2 \le 4U\,\|u\|_{U^3}^4\).
2. **(Exact identity and \(U^2/U^3\) bound for \(Y = \frac{1}{2}R_3 + R_4\))**:
   \[
   \boxed{
   Y = \frac{1}{2}R_3 + R_4 = \frac{1}{3}\langle u, K_u^{(2)}\rangle_p + \left\langle \frac{1}{2}u + h,\ K_u^{(3)}\right\rangle_p
   = a(T_u + S_u) + \left\langle \frac{1}{2}u + h,\ K_u^{(3)}\right\rangle_p,
   } \tag{4.2}
   \]
   and since \(\langle u, h\rangle_p = 0 \implies \|\frac{1}{2}u + h\|_2 = \sqrt{\frac{1}{4}U + v}\), Cauchy–Schwarz and (3.4) yield:
   \[
   \boxed{|Y| \le 2a\sqrt{U}\,\|u\|_{U^2}^2 + \sqrt{U(U + 4v)}\,\|u\|_{U^3}^2 \le a\bigl(1 + 2\sqrt{U}\bigr)\,\|u\|_{U^3}^2.} \tag{4.3}
   \]
3. **(Unconditional residual \(U^3\) lower bound in Branch II for arbitrary factors)**:
   If \(A\subset\mathbb{Z}_p\) is 4-AP-free with \(v \le \zeta a^{9/4}\) and lies in Branch II (\(Y \ge \frac{1}{2}a^4 - 3a^3\sqrt{v} - 4a v^{3/2} - v^2 + \frac{U-a^2-v}{p}\)), then:
   \[
   \|u\|_{U^3}^2 \ge \frac{\frac{1}{2}a^3 - 3a^2\sqrt{v} - 4v^{3/2} - v^2/a - 1/p}{1 + 2\sqrt{U}} = \frac{a^3}{2(1 + 2\sqrt{U})}\bigl(1 - o(1)\bigr), \tag{4.4}
   \]
   and at least one of the two pairings in (4.2) has magnitude \(\ge \frac{1}{4}a^4\bigl(1 - o(1)\bigr)\):
   - **Subcase IIa (\(|\langle u, K_u^{(2)}\rangle_p| = 3a|T_u+S_u| \ge \frac{3}{4}a^4(1-o(1))\))**: Then \(\frac{|\langle u, K_u^{(2)}\rangle_p|^2}{\|K_u^{(2)}\|_2^2} \ge \frac{a^6}{64\|u\|_{U^2}^4}(1-o(1)) \ge \frac{a^5}{64\rho^2 U}(1-o(1)) \gtrsim \frac{a^{5/2}}{\ell(a)}\), and Theorem 1 supplies the bilateral multiplier set \(\Gamma_\alpha^*(\tau)\).
   - **Subcase IIb (\(\langle \frac{1}{2}u + h, K_u^{(3)}\rangle_p \ge \frac{1}{4}a^4(1-o(1))\))**: Then \(\sqrt{U(U+4v)}\,\|u\|_{U^3}^2 \ge \frac{1}{4}a^4(1-o(1))\).

---

## Verification Summary

Run `python3 verify_two_branch_closure_20261014.py` (outputs `TWO_BRANCH_CLOSURE_VERIFICATION_20261014.json`):
- **125** verifications of Theorem 1 (bilateral multiplier set \(\Gamma_\alpha^*(\tau)\));
- **300** exact rational/Fourier verifications of Theorem 2 (proper-window two-branch reduction and \(\ell^1\) window-marginal bound);
- **753** verifications of Theorem 3 (exact Fourier operator decomposition \(Q_0 K_B Q_0 = a L_{E,f} + Q_0 K_f Q_0\));
- **4,494** verifications of Theorem 4 (peak-versus-diffuse projection bounds);
- **2,247** verifications of Theorem 5 (universal Branch II identity \(Y = a(T_u+S_u) + \langle \frac{1}{2}u+h, K_u^{(3)}\rangle_p\) and arbitrary-factor residual \(U^3\) bound), plus **16** global-law orbit checks on \(\mathbb{Z}_{23}, \mathbb{Z}_{29}\).
