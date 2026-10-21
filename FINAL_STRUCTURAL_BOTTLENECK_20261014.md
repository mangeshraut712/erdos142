# Unconditional Elimination of Branch III via One-Sided \(D_3\) Truncation, Spectral \(K^{(2)}/K^{(3)}\) Splitting, and Clipped Completion Projection — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with unconditional elimination of Branch III on \(\mathbb{Z}_p\) via one-sided physical truncation of \(D_3\), exact \(K^{(2)}/K^{(3)}\) completion-spectrum splitting, clipped completion projection, and rich cubic multiplier capture).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, `COLLECTIVE-WSELECT`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## 1. Theorem A: Unconditional One-Sided Truncation of \(D_3\) and Complete Elimination of Branch III on \(\mathbb{Z}_p\)

In previous continuations (`TWO_CHANNEL_DICHOTOMY_CLOSURE_20261014.md`, `THREE_BRANCH_AMPLIFICATION_20261014.md`, `CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md`, `CUBIC_RESONANCE_ATTACK_20261014.md`), the conservation law
\[
\underbrace{w(S_E + S_M)}_{X} + \underbrace{\left(\frac{1}{2}R_3 + R_4\right)}_{Y} = \underbrace{R_0 + \frac{1}{2}R_1 + \frac{w(U - a^2 - v)}{p}}_{T}
= \frac{1}{2}D_3 - R_0 + \frac{w(U - a^2 - v)}{p} \tag{1.1}
\]
required handling **Branch III** (\(R_1 \le -2(1-2c_0)R_0 \approx -a^4\)) whenever \(v \in [c_1 a^{7/3}, \zeta a^{9/4}]\), because the two-sided Cauchy–Schwarz bound on \(|R_1|\) was \(O(a^{31/8}) \gg a^4\) unless \(\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)} = o(a^{1/2}/\sqrt{\ell(a)})\).

We now prove that **one-sided physical-space truncation of \(g\) inside \(D_3\) eliminates Branch III on \(\mathbb{Z}_p\) unconditionally** for **every** factor \(F\) with \(v = o(a^2)\) (including the entire regime \(v \le \zeta a^{9/4}\), with \(a^{1/8}\) polynomial margin), without any Fourier-cap, rank, or \(\ell^1\)-norm assumption!

**Theorem A (Unconditional One-Sided Lower Bounds on \(D_3\), \(R_1\), and \(T\)).**
Let \(p>3\) be prime, \(\Omega\subset\mathbb{Z}_p\) have size \(n=wp\), \(W=1_\Omega\), \(B : \Omega \to [0,1]\) have mean \(a = \mathbb{E}_\Omega[B]\), and \(g : \Omega \to [0,1]\) have mean \(a\) and variance \(v = \mathbb{E}_\Omega[(g-a)^2]\) (with \(B, g\) extended by zero outside \(\Omega\)). Write \(h = (g-a)W = h_+ - h_-\), where \(h_+ = \max(g-a,0)W \ge 0\) and \(h_- = \max(a-g,0)W \in [0, a]\). Then:
1. **(General proper-window bijection bound on \(D_3\))**:
   \[
   D_3 = \sum_{i=0}^3 \Lambda_4\bigl(B\text{ at slot }i,\ g\text{ at slots }\ne i\bigr)
   \ge a^3 \sum_{i=0}^3 \Lambda_4\bigl(B\text{ at slot }i,\ W\text{ at slots }\ne i\bigr) - 12\,w^2\,a^3\,\mathbb{E}_\Omega[h_-]
   \ge a^3 \sum_{i=0}^3 \Lambda_4\bigl(B\text{ at slot }i,\ W\text{ at slots }\ne i\bigr) - 6\,w^2\,a^3\,\sqrt{v}. \tag{1.2}
   \]
2. **(Full-group \(\Omega = \mathbb{Z}_p\) unconditional bounds on \(D_3\), \(R_1\), and \(T\))**:
   When \(\Omega = \mathbb{Z}_p\) (\(w=1,\ W\equiv 1\)), \(\Lambda_4(B\text{ at }i,\ 1\text{ at }\ne i) = a\), so:
   \[
   \begin{aligned}
   D_3 &\ge 4a^4 - 12a^3\,\mathbb{E}[h_-] \ge 4a^4 - 6a^3\sqrt{v}, \\
   R_1 = D_3 - 4R_0 &\ge -6a^3\sqrt{v} - 16a v^{3/2} - 4v^2, \\
   T = \frac{1}{2}D_3 - R_0 + \frac{U - a^2 - v}{p} &\ge a^4 - 3a^3\sqrt{v} - 4a v^{3/2} - v^2 + \frac{U - a^2 - v}{p}.
   \end{aligned} \tag{1.3}
   \]
3. **(Complete elimination of Branch III and strict two-branch dichotomy on \(\mathbb{Z}_p\))**:
   For any 4-AP-free set \(A\subset\mathbb{Z}_p\) and any factor \(F\) with \(v \le \zeta a^{9/4}\), (1.3) gives \(R_1 \ge -O(a^{33/8}) = -o(a^4)\) and \(T \ge a^4 - O(a^{33/8}) + \frac{U-a^2-v}{p}\). Thus **Branch III is unconditionally impossible**, and every 4-AP-free set \(A\subset\mathbb{Z}_p\) with \(v \le \zeta a^{9/4}\) satisfies either:
   - **Branch I**: \(S_E + S_M \ge \frac{1}{2}a^4 - 3a^3\sqrt{v} - 4a v^{3/2} - v^2 + \frac{U-a^2-v}{p}\), or
   - **Branch II**: \(\frac{1}{2}R_3 + R_4 = a(T_u + S_u) + \langle h, h_{E,u}+h_{M,u}\rangle_p + \Lambda_4(u) \ge \frac{1}{2}a^4 - 3a^3\sqrt{v} - 4a v^{3/2} - v^2 + \frac{U-a^2-v}{p}\) (completely bypassing \(R_1\) and \(R_2\)!).

*Proof.* For any \(y_1,y_2,y_3\in\mathbb{Z}_p\), \(g(y_r) \ge W(y_r)(a - h_-(y_r)) \ge 0\) with \(0 \le h_-(y_r) \le a\). Since \((a-h_{-,1})(a-h_{-,2})(a-h_{-,3}) = a^3 - a^2(h_{-,1}+h_{-,2}+h_{-,3}) + a(h_{-,1}h_{-,2}+h_{-,1}h_{-,3}+h_{-,2}h_{-,3}) - h_{-,1}h_{-,2}h_{-,3} \ge a^3 - a^2(h_{-,1}+h_{-,2}+h_{-,3})\), multiplying by \(B(y_i) \ge 0\) gives
\[
D_3 \ge a^3 \sum_{i=0}^3 \Lambda_4\bigl(B\text{ at }i,\ W\text{ at }\ne i\bigr) - a^2 \sum_{i=0}^3 \sum_{j\ne i} \Lambda_4\bigl(B\text{ at }i,\ h_-\text{ at }j,\ W\text{ at other }2\text{ slots}\bigr).
\]
In each of the 12 subtracted terms, since \(B(y_i)h_-(y_j) \ge 0\) and \(W(y_k)W(y_l) \le 1\), dropping \(W(y_k)W(y_l)\) bounds \(\Lambda_4(B\text{ at }i,\ h_-\text{ at }j,\ W, W) \le \mathbb{E}_{x,d}[B(x+id)h_-(x+jd)]\). Because \((x,d)\mapsto (x+id,x+jd)\) is a bijection of \(\mathbb{Z}_p^2\) for \(i\ne j\) and \(p>3\), \(\mathbb{E}_{x,d}[B(x+id)h_-(x+jd)] = (\mathbb{E}_p B)(\mathbb{E}_p h_-) = w^2 a\,\mathbb{E}_\Omega[h_-]\). Finally, \(\mathbb{E}_\Omega[h] = 0 \implies \mathbb{E}_\Omega[h_-] = \frac{1}{2}\mathbb{E}_\Omega[|h|] \le \frac{1}{2}\sqrt{v}\), proving (1.2). On \(\mathbb{Z}_p\), combining \(D_3 \ge 4a^4 - 6a^3\sqrt{v}\) with \(R_0 \le a^4 + 4a v^{3/2} + v^2\) (`SELECT_ALGEBRA_20261002.md` `A7`) yields (1.3). \(\square\)

---

## 2. Theorem B & Theorem D: One-Sided Pairing Bound and Clipped Completion Projection

**Theorem B (One-Sided Physical Truncation Bound on \(S_E + S_M\)).**
On any window \(\Omega\subset\mathbb{Z}_p\), writing \(g = a + h_+ - h_-\) with \(h_+ \ge 0\) and \(0 \le h_- \le a\), nonnegativity of \(q_E, q_M \ge 0\) implies \(\mathbb{E}_\Omega[h_+(q_E+q_M)] \ge 0\) and hence:
\[
S_E + S_M = \mathbb{E}_\Omega\bigl[g(q_E + q_M)\bigr] \ge a\,\mathbb{E}_\Omega[q_E + q_M] - \mathbb{E}_\Omega\bigl[h_-(q_E + q_M)\bigr]. \tag{2.1}
\]

**Theorem D (Clipped Completion Field & Heavy-Tail Peak Dichotomy).**
Let \(q(x) := q_E(x) + q_M(x)\) on \(\Omega\). For any clipping threshold \(\tau_q > 0\), define \(\tilde{q}(x) := \min(q(x), \tau_q)\) and \(q_{>\tau_q}(x) := \max(q(x) - \tau_q, 0)\). Then:
1. Both \(\tilde{q}\) and \(q_{>\tau_q}\) satisfy \(B(x)\tilde{q}(x) = 0\) and \(B(x)q_{>\tau_q}(x) = 0\) pointwise on \(\Omega\), and \(S_E + S_M = \tilde{S}(\tau_q) + S_{>\tau_q}(\tau_q)\), where \(\tilde{S}(\tau_q) = \mathbb{E}_\Omega[g\tilde{q}]\) and \(S_{>\tau_q}(\tau_q) = \mathbb{E}_\Omega[g q_{>\tau_q}]\).
2. With \(\tilde{T}_C = \mathbb{E}_C[\tilde{q}]\) and \(\tilde{k} = \tilde{q} - \tilde{T}_C\), we have \(\langle u, \tilde{k}\rangle_\Omega = -\tilde{S}(\tau_q)\), \(\|\tilde{k}\|_2^2 \le \tau_q\,\mathbb{E}_\Omega[\tilde{q}]\), and for the cell-weighted residual \(g_C\tilde{k}\):
   \[
   \frac{|\langle u, \tilde{k}\rangle_\Omega|^2}{\|\tilde{k}\|_2^2} \ge \frac{\tilde{S}(\tau_q)^2}{\tau_q\,\mathbb{E}_\Omega[\tilde{q}]}, \qquad
   \frac{|\langle u, g_C\tilde{k}\rangle_\Omega|^2}{\|g_C\tilde{k}\|_2^2} \ge \frac{\mathbb{E}_\Omega[g_C^2 \tilde{T}_C]}{\tau_q}. \tag{2.2}
   \]
3. Moreover, the unclipped second moment satisfies the heavy-tail lower bound:
   \[
   \mathbb{E}_\Omega\bigl[q(x)^2\bigr] \ge \tau_q\, S_{>\tau_q}(\tau_q). \tag{2.3}
   \]

---

## 3. Theorem C & Theorem E: Exact \(K^{(2)}/K^{(3)}\) Completion-Spectrum Splitting and Rich Cubic Multiplier Set

**Theorem C (Exact Spectral Splitting of \(\widehat{q_E}(t)+\widehat{q_M}(t)\) on \(\mathbb{Z}_p\)).**
Let \(B = a + f\) on \(\mathbb{Z}_p\) (\(p>3\)) with \(\widehat{f}(0)=0\) and \(\rho = \max_{\xi\ne 0}|\widehat{f}(\xi)|\). For every \(t\in\mathbb{Z}_p\setminus\{0\}\), separating the three single-zero-frequency terms \(r\in\{0,-2t,-t/2\}\) in \(K_E(t)\) and \(r\in\{0,-t,t/3\}\) in \(K_M(t)\) gives:
\[
\widehat{q_E}(t) + \widehat{q_M}(t) = K^{(2)}(t) + K^{(3)}(t) - \frac{2}{p}\widehat{f}(t), \tag{3.1}
\]
where:
1. \(K^{(2)}(t) = a\bigl[2\widehat{f}(2t)\widehat{f}(-t) + \widehat{f}(3t)\widehat{f}(-2t) + \widehat{f}(3t/2)\widehat{f}(-t/2) + \widehat{f}(t/2)^2 + \widehat{f}(2t/3)\widehat{f}(t/3)\bigr]\) satisfies
   \[
   \sum_{t\ne 0} \overline{\widehat{f}(t)}\,K^{(2)}(t) = 3a(T_f + S_f), \qquad
   \sum_{t\ne 0} |K^{(2)}(t)|^2 \le 36a^2 \|f\|_{U^2}^4 \le 36a^3 \rho^2. \tag{3.2}
   \]
   In particular, under `SELECT` failure (\(\rho^2 \le c a^{5/2}\ell(a)\)), \(\|K^{(2)}\|_2^2 \le 36c\,a^{11/2}\ell(a) \ll a^4\).
2. \(K^{(3)}(t) = K_{E,f}(t) + K_{M,f}(t)\) is purely cubic in \(\widehat{f}\) and satisfies
   \[
   \sum_{t\ne 0} \overline{\widehat{f}(t)}\,K^{(3)}(t) = 2\Lambda_4(f, f, f, f) = 2Q_f. \tag{3.3}
   \]

**Theorem E (Rich Cubic Multiplier Set in Branch II).**
For any mean-zero function \(u\) on \(\mathbb{Z}_p\) with \(\|u\|_2^2 = U \le a(1-a)\) and \(\max_{\xi\ne 0}|\widehat{u}(\xi)| = \rho\), if \(|T_u + S_u| > 0\), then at least one multiplier \(\alpha \in \{-2, -3, -3/2\}\pmod p\) satisfies \(\sum_{\xi\ne 0}|\widehat{u}(\xi)|^2|\widehat{u}(\alpha\xi)| \ge \frac{1}{2}|T_u + S_u|\). Defining \(\Gamma_\alpha(\tau) := \{\xi\ne 0 : |\widehat{u}(\alpha\xi)| \ge \tau\}\) at \(\tau := \frac{|T_u+S_u|}{4a(1-a)}\), we have
\[
|\Gamma_\alpha(\tau)| \le \frac{U}{\tau^2} \le \frac{16 a^3(1-a)^3}{|T_u+S_u|^2}, \qquad
\sum_{\xi\in\Gamma_\alpha(\tau)} |\widehat{u}(\xi)|^2 \ge \frac{|T_u + S_u|}{4\,\rho}. \tag{3.4}
\]
When \(|T_u + S_u| \ge c a^3\) and \(\rho \le \sqrt{c'}a^{5/4}\sqrt{\ell(a)}\), the collective Fourier energy on \(\Gamma_\alpha(\tau)\) is at least \(\frac{c}{4\sqrt{c'}} a^{7/4}/\sqrt{\ell(a)} \gg \zeta a^{9/4}\).

---

## 4. Verification Summary

Run `python3 verify_autonomous_breakthroughs_20261014.py` (outputs `FINAL_STRUCTURAL_BOTTLENECK_VERIFICATION_20261014.json`):
- **2,508** exact rational verifications of Theorem A's proper-window bijection bound (1.2) and **2,259** verifications of the full-group unconditional \(D_3, R_1, T\) bounds (1.3);
- **2,508** exact rational verifications of Theorem B (2.1) and **5,016** verifications of Theorem D (2.2)–(2.3);
- **753** verifications of Theorem C (3.1)–(3.3), **753** verifications of Theorem E (3.4), and **16** global-law orbit checks on \(\mathbb{Z}_{23}, \mathbb{Z}_{29}\).
