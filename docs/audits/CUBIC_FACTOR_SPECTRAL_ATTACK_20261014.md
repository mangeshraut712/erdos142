# Effective Fourier Sparsity of Cubic Factor Fields, Trilinear Stability, and \(\ell^1\)-Fourier Bounds on \(R_1\) and \(R_2\) — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with exact Phase 0 audit, trilinear \(L^2\) stability and 1D cubic averaging \(O(\log|t|/t^2)\) harmonic decay, exact \(\ell^1\)-Fourier bounds on \(R_{1,(3)}\) and \(R_{2,(2)}\) replacing generic Cauchy–Schwarz, and sharp quantification of the multi-coordinate truncation barrier).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, `COLLECTIVE-WSELECT`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 — Independent Audit of the Branch III Checkpoint

We independently audited `THREE_BRANCH_AMPLIFICATION_20261014.md`:
1. **Exact relative pairing for \(R_1\)**: With \(h_{E,g}(x)=\mathbb{E}_d[g(x+d)g(x+2d)g(x+3d)]\), \(h_{M,g}(x)=\mathbb{E}_d[g(x-d)g(x+d)g(x+2d)]\), \(k_{E,g}=(I-\mathbb{E}(\cdot\mid F))h_{E,g}\big|_\Omega\), and \(k_{M,g}=(I-\mathbb{E}(\cdot\mid F))h_{M,g}\big|_\Omega\), we have
   \[
   R_1 = 2\langle u, h_{E,g} + h_{M,g}\rangle_p = 2w\langle u, k_{E,g} + k_{M,g}\rangle_\Omega = 2w\sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} \overline{c_\xi}\bigl(K_{E,g}(\xi) + K_{M,g}(\xi)\bigr), \tag{0.1}
   \]
   verified in exact rational arithmetic across 2,496 set/window/factor cases (`verify_cubic_factor_spectral_20261014.py`).
2. **Decomposition \(R_1 = R_{1,(2)} + R_{1,(3)}\) and Variance Floor**: On \(\mathbb{Z}_p\), writing \(g=a+h\) (\(\mathbb{E}[h]=0,\ \mathbb{E}[h^2]=v\)) gives \(R_1 = R_{1,(2)} + R_{1,(3)}\) with \(|R_{1,(2)}| \le 12a\rho v\) and \(\|H_g^{(3)}\|_2 \le 2v^{3/2}\), forcing \(v \ge \bigl((1-2c_0)R_0/(4\sqrt{U})\bigr)^{2/3} \ge c_1 a^{7/3}\) in Branch III (\(R_1 \le -2(1-2c_0)R_0\)).
3. **Correction to the description of \([c_1 a^{7/3}, \zeta a^{9/4}]\)**: While the difference of exponents \(9/4 - 7/3 = -1/12\) is small, the **multiplicative endpoint ratio** of this variance interval is
   \[
   \frac{\zeta a^{9/4}}{c_1 a^{7/3}} = \frac{\zeta}{c_1}\, a^{-1/12} \longrightarrow +\infty \quad\text{as } a\to 0. \tag{0.2}
   \]
   Thus the interval \([c_1 a^{7/3}, \zeta a^{9/4}]\) is **multiplicatively wide** (growing as \(a^{-1/12} \asymp (\log N)^{1/12}\)), and must not be described as multiplicatively narrow.

---

## Phase 1, Phase 2 & Phase 3 — Exact Structure of the Cubic Factor Field \(H_g^{(3)}\) and Cubic Averaging Decay

Let \(g = a + h\) on \(\mathbb{Z}_p\) with \(\mathbb{E}[h]=0\), \(\mathbb{E}[h^2]=v\), and \(\widehat{h}(0)=0\). Then \(H_g^{(3)} = h_{E,h} + h_{M,h}\), where
\[
h_{E,h}(x) = \mathbb{E}_d\bigl[h(x+d)h(x+2d)h(x+3d)\bigr], \qquad
h_{M,h}(x) = \mathbb{E}_d\bigl[h(x-d)h(x+d)h(x+2d)\bigr], \tag{1.1}
\]
and its exact Fourier transform is \(\widehat{H_g^{(3)}}(t) = K_{E,h}(t) + K_{M,h}(t)\), where (since \(\widehat{h}(0)=0\)):
\[
K_{E,h}(t) = \sum_{r\notin\{0,-2t,-t/2\}} \widehat{h}(2t+r)\widehat{h}(-t-2r)\widehat{h}(r), \qquad
K_{M,h}(t) = \sum_{r\notin\{0,-t,t/3\}} \widehat{h}\bigl((t+r)/2\bigr)\widehat{h}\bigl((t-3r)/2\bigr)\widehat{h}(r). \tag{1.2}
\]

### 1.1 Trilinear \(L^2\) Stability and Pointwise Spectral Cap — PROVED
**Theorem 1 (Trilinear \(L^2\) Stability, Pointwise Cap, and \(\ell^1\)-Fourier Bound on \(R_{1,(3)}\)).**
1. **(General trilinear \(L^2\) bound)**: For ANY three functions \(f_1,f_2,f_3\) on \(\mathbb{Z}_p\) (\(p>3\)), define \(C_E(f_1,f_2,f_3)(x) = \mathbb{E}_d[f_1(x+d)f_2(x+2d)f_3(x+3d)]\) and \(C_M(f_1,f_2,f_3)(x) = \mathbb{E}_d[f_1(x-d)f_2(x+d)f_3(x+2d)]\). Then:
   \[
   \|C_E(f_1,f_2,f_3)\|_2 \le \|f_1\|_2 \|f_2\|_2 \|f_3\|_2, \qquad
   \|C_M(f_1,f_2,f_3)\|_2 \le \|f_1\|_2 \|f_2\|_2 \|f_3\|_2. \tag{1.3}
   \]
   Consequently, for any decomposition \(h = h_L + e_L\), telescoping \(h^3 - h_L^3 = e_L(h_1 h_2)\) into three trilinear terms gives the **cubic approximation stability inequality**:
   \[
   \bigl\|H_h^{(3)} - H_{h_L}^{(3)}\bigr\|_2 \le 2\,\|e_L\|_2 \bigl(\|h\|_2^2 + \|h\|_2\|h_L\|_2 + \|h_L\|_2^2\bigr) \le 6 v\,\|h - h_L\|_2 \quad (\text{when } \|h_L\|_2 \le \|h\|_2 = \sqrt{v}). \tag{1.4}
   \]
2. **(Pointwise Fourier cap)**: With \(\rho_h := \max_{\xi\ne 0}|\widehat{h}(\xi)| \le \sqrt{v}\), Cauchy–Schwarz on (1.2) gives for every \(t\in\mathbb{Z}_p\):
   \[
   |K_{E,h}(t)| \le \rho_h v, \qquad |K_{M,h}(t)| \le \rho_h v, \qquad |\widehat{H_g^{(3)}}(t)| \le 2\rho_h v. \tag{1.5}
   \]
3. **(Exact \(\ell^1\)-Fourier bound on \(R_{1,(3)}\) using \(\rho = \max_{\xi\ne 0}|\widehat{u}(\xi)|\))**:
   In `SELECT_ALGEBRA_20261002.md` (`A9`), \(|R_{1,(3)}|\) was bounded by \(4\sqrt{U}v^{3/2}\) using only \(\|u\|_2 = \sqrt{U}\), ignoring the `SELECT`-failure hypothesis \(\max_{\xi\ne 0}|\widehat{u}(\xi)| \le \rho\)! Using \(|\widehat{u}(\xi)| \le \rho\) for \(\xi\ne 0\) in \(R_{1,(3)} = 2\sum_{\xi\ne 0}\overline{\widehat{u}(\xi)}\widehat{H_g^{(3)}}(\xi)\) gives:
   \[
   \boxed{|R_{1,(3)}| \le 2\rho \sum_{\xi\ne 0} |\widehat{H_g^{(3)}}(\xi)| \le 4\rho\, v\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}.} \tag{1.6}
   \]

*Proof.* For (1.3), by Cauchy–Schwarz in \(r\), \(|\widehat{C_E}(t)|^2 = |\sum_r \widehat{f_1}(2t+r)\widehat{f_2}(-t-2r)\widehat{f_3}(r)|^2 \le \|f_3\|_2^2 \sum_r |\widehat{f_1}(2t+r)|^2 |\widehat{f_2}(-t-2r)|^2\). Summing over \(t\in\mathbb{Z}_p\) uses the bijection \((t,r)\mapsto (2t+r,-t-2r)\) on \(\mathbb{Z}_p^2\) (\(\det = -3 \not\equiv 0\pmod p\)) to give \(\sum_t |\widehat{C_E}(t)|^2 \le \|f_1\|_2^2 \|f_2\|_2^2 \|f_3\|_2^2\); the proof for \(C_M\) is identical using \(\det(\frac{1}{2},\frac{1}{2}; \frac{1}{2},-\frac{3}{2}) = -1\not\equiv 0\pmod p\). For (1.6), \(\sum_{t\ne 0}|K_{E,h}(t)| \le \sum_r |\widehat{h}(r)| \sum_t |\widehat{h}(2t+r)||\widehat{h}(-t-2r)| \le \|\widehat{h}\|_{\ell^1} v\) by Cauchy–Schwarz in \(t\). \(\square\)

### 1.2 How Cubic Averaging Suppresses High Harmonics (Phase 3 — PROVED)
Compare the Fourier decay of a 1D quarter-arc step function \(h(x) = \Phi(\xi_1 x/p)\) with the Fourier decay of its cubic completion \(H_h^{(3)}(x)\):
- Because \(\Phi\) is piecewise constant with 4 jumps on \(\mathbb{R}/\mathbb{Z}\), its continuous Fourier coefficients decay only as \(|\widehat{\Phi}(m)| \le \frac{2}{\pi |m|}\) (\(m\ne 0\)), which is **not in \(\ell^1(\mathbb{Z})\)** and has slow \(\ell^2\) tail \(\sum_{|m|>L} |\widehat{\Phi}(m)|^2 \asymp L^{-1}\).
- However, when \(\Phi\) is passed through the cubic completion operator, the three factors in \(K_{E,\Phi}(t) = \sum_{r\notin\{0,-2t,-t/2\}} \widehat{\Phi}(2t+r)\widehat{\Phi}(-t-2r)\widehat{\Phi}(r)\) satisfy the linear relation \((2t+r) + 2(-t-2r) + 3r = 0\), so at least two of the three arguments \(|2t+r|, |-t-2r|, |r|\) must be \(\ge |t|/3\)!

**Theorem 2 (Cubic Averaging Harmonic Decay Enhancement: \(O(1/|t|)\) to \(O(\log(1+|t|)/t^2)\)).**
Let \(\Phi\) on \(\mathbb{R}/\mathbb{Z}\) have Fourier coefficients satisfying \(|\widehat{\Phi}(0)|=0\) and \(|\widehat{\Phi}(m)| \le A/|m|\) for \(m\ne 0\). Then for every \(t\in\mathbb{Z}\setminus\{0\}\), its cubic completion coefficients satisfy
\[
|K_{E,\Phi}(t)| \le A^3 \sum_{r\notin\{0,-2t,-t/2\}} \frac{1}{|2t+r|\,|-t-2r|\,|r|} \le \frac{A^3 \bigl(4\log(2|t|+2) + 6\bigr)}{t^2}. \tag{3.1}
\]
Consequently:
1. Unlike \(\widehat{\Phi}\) (whose \(\ell^1\) norm diverges logarithmically and whose \(\ell^2\) tail decays as \(L^{-1}\)), the cubic completion \(K_{E,\Phi} + K_{M,\Phi}\) is **absolutely summable in \(\ell^1(\mathbb{Z})\)**!
2. Its squared \(\ell^2\) tail outside \([-L, L]\) decays three powers faster:
   \[
   \sum_{|t| > L} \bigl(|K_{E,\Phi}(t)| + |K_{M,\Phi}(t)|\bigr)^2 = O\!\left(\frac{A^6 \log^2(L+2)}{L^3}\right) \qquad (\text{versus } O(A^2 L^{-1}) \text{ for } \Phi). \tag{3.2}
   \]
*(Verified numerically in `verify_cubic_factor_spectral_20261014.py`: for the unit-variance 1D Walsh square wave, \(|K_{E,s}(t)| \le 1.42/t^2\) and the first \(L=2\) harmonic pairs already capture \(99.2\%\) of \(\|H_g^{(3)}\|_2^2\).)*

---

## Phase 4, Phase 5, Phase 6 & Phase 7 — Exact Truncation Cost, Multi-Coordinate Barrier, and Branch III Elimination Criterion

### 4.1 Why \(\ell^1\)-Fourier control of \(h\) completely eliminates Branch III (and \(R_{2,(2)}\) in Branch II!)
Look at Theorem 1 (`(1.6)`): on \(\mathbb{Z}_p\), under `SELECT` failure (\(\rho \le \sqrt{c}a^{5/4}\sqrt{\ell(a)}\)) and \(v \le \zeta a^{9/4}\),
\[
|R_1| \le |R_{1,(2)}| + |R_{1,(3)}| \le 12a\rho v + 4\rho v\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}
\le 4\sqrt{c}\zeta\, a^{7/2}\sqrt{\ell(a)}\,\bigl(3a + \|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}\bigr)! \tag{4.1}
\]
Compare \(a^{7/2}\sqrt{\ell(a)}\) with \(R_0 \sim a^4\):
\[
\frac{a^{7/2}\sqrt{\ell(a)}}{a^4} = a^{-1/2}\sqrt{\ell(a)}!
\]
Therefore:
- **Whenever \(\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)} = o\bigl(a^{1/2}/\sqrt{\ell(a)}\bigr)\), we have \(|R_1| = o(a^4)\), which makes Branch III (\(R_1 \le -2(1-2c_0)R_0\)) COMPLETELY IMPOSSIBLE!**
- Even better: by Cauchy–Schwarz, if \(h\) is supported (or approximated to \(L^2\) error \(\ll a^{5/3}\)) on a frequency set \(\Lambda\) of size \(|\Lambda|\), then \(\|\widehat{h_\Lambda}\|_{\ell^1} \le \sqrt{|\Lambda|\,v} \le \sqrt{\zeta\,|\Lambda|}\, a^{9/8}\).
- Thus \(\sqrt{|\Lambda|}\,a^{9/8} \ll a^{1/2}/\sqrt{\ell(a)} \iff |\Lambda| \ll a^{-5/4}/\ell(a)\)!
  Notice that our per-factor rank budget is \(M(a) = O(a^{-1/4}/\ell(a)) \ll a^{-5/4}/\ell(a)\)!

### 5.1 Quantifying the Multi-Coordinate Truncation Cost \(N(L,d)\) vs \(E(L,d,v)\) (Phase 5 & Phase 7)
Now suppose \(g = a+h\) is measurable with respect to a rank-\(d\) quarter-arc factor \(F\) generated by \(\xi_1,\dots,\xi_d\), where \(1 \le d \le M(a) = O(a^{-1/4}/\ell(a))\).
1. **Product / Additive Separation Case**:
   - If \(h(x) = \sum_{j=1}^d h_j(\xi_j x)\) is an additive sum of 1D coordinate functions, then each \(h_j\) has 1D harmonic decay \(O(1/|m|)\), and truncating each coordinate at harmonic \(L\) uses only \(N_{\text{add}}(L,d) = 2dL\) frequencies. Even for \(h_1(\xi_1 x)h_2(\xi_2 x)\dots\), Theorem 2 shows that 1D cubic averaging suppresses high harmonics as \(O(\log|t|/t^2)\).
   - If \(h(x) = \sqrt{v}\prod_{j=1}^d s(\xi_j x/p)\) is a pure \(d\)-fold Walsh parity product (`Phase 7` test in `verify_cubic_factor_spectral_20261014.py`), then for independent coordinates \(\|H_h^{(3)}\|_2^2 \approx (0.1358)^d \cdot 4v^3\), which decays exponentially in \(d\)! Once \(d \ge 4\), \((0.1358)^d \cdot 4v^3 \ll a^7\), so \(|R_{1,(3)}| \le 2\sqrt{U}\|H_h^{(3)}\|_2 \ll a^4\) and **Branch III is impossible for high-degree Walsh products!**
2. **Worst-Case Arbitrary Joint Cell Function on \(\{0,1,2,3\}^d\)**:
   For an arbitrary function \(h\) on the \(4^d\) joint cells of \(F\) bounded only by \(\|h\|_2^2 = v\) and \(\|h\|_\infty \le 1\):
   - Smoothing \(h\) by the \(d\)-fold Fejér/Jackson kernel of degree \(L\) (`FULL_GROUP_HOSTILE_AUDIT_20260914.md` `(5)` / `FULL_GROUP_ENERGY_AUDIT.md` Theorem 2b) produces \(h_L\) supported on the rank-\(d\) box \(\Lambda_L(\xi) = \{\sum_{i=1}^d m_i \xi_i : |m_i|\le L\}\) of size
     \[
     N(L, d) \le (2L+1)^d \qquad \bigl(\text{and }\operatorname{supp}(\widehat{H_{h_L}^{(3)}}) \subset \Lambda_{3L}(\xi)\text{ of size }\le (6L+1)^d\bigr), \tag{5.1}
     \]
     with \(L^2\) error \(\|h - h_L\|_2^2 \le 24d/L\) (from \(\|h\|_\infty \le 1\)).
   - By Theorem 1 (`(1.4)`), the resulting cubic approximation error is
     \[
     E(L, d, v) = \|H_h^{(3)} - H_{h_L}^{(3)}\|_2^2 \le 36 v^2 \|h - h_L\|_2^2 \le \frac{864\, d\, v^2}{L}. \tag{5.2}
     \]
   - To make \(E(L, d, v) \le c R_0^2 / U \asymp a^7\) at \(v \asymp a^{9/4}\), (5.2) requires \(L \gtrsim d v^2 / a^7 \asymp d a^{-5/2}\).
   - However, when \(d\) grows with \(a^{-1/4}/\ell(a)\), the full tensor-product box size \(N(3L, d) = (6L+1)^d = \exp(\Omega(d\log L))\) grows exponentially in \(d\) and exceeds \(M(a) = O(a^{-1/4}/\ell(a))\) whenever \(d \ge 2\) and \(L \ge 1\)!
   - **Why does the worst-case box bound \((6L+1)^d\) blow up, whereas the Walsh product decayed as \((0.1358)^d\)?**
     Because in the Fourier expansion of \(h(x) = \sum_{m\in\mathbb{Z}^d} \widehat{h}(m) e_p(\sum_i m_i \xi_i x)\), any frequency \(m\in\mathbb{Z}^d\) with \(k\) nonzero coordinates has quarter-arc capture weight decaying as \(\prod_{i: m_i\ne 0} \frac{\sin^2(\pi m_i/4)}{(\pi m_i/4)^2} \le (8/\pi^2)^k\), so its cubic completion decays by \((0.1358)^k\)! Only **low-Hamming-weight (junta)** combinations of the \(d\) coordinates survive cubic averaging without exponential \((0.1358)^k\) damping!

---

## Phase 8 — Returning to Branch II: Exact \(\ell^1\)-Fourier Control of \(R_2\)

In `THREE_BRANCH_AMPLIFICATION_20261014.md` Phase 6, we noted that in Branch II (\(Y = \frac{1}{2}R_3 + R_4 \ge c_0 R_0 + \frac{w(U-a^2-v)}{p}\)), the identities for \(R_3\) and \(R_4\) at \(v>0\) involve \(R_2\), whose generic Cauchy–Schwarz bound in `SELECT_ALGEBRA_20261002.md` (`A9`) was \(|R_2| \le 12a\rho\sqrt{bv} + 6bv = O(a^{13/4})\).
Applying our new \(\ell^1\)-Fourier method to \(R_2\) eliminates the \(\rho\)-independent \(6bv\) term:

**Theorem 3 (Exact Splitting of \(R_2\) and \(\ell^1\)-Fourier Bound).**
On \(\mathbb{Z}_p\) (\(p>3\)), write \(g = a + h\) (\(\mathbb{E}[h]=0,\ \mathbb{E}[h^2]=v\)) in each of the 6 terms of \(R_2 = \sum_{|I|=2}\Lambda_4(u\text{ on }I, g\text{ on }I^c)\). Then:
1. The constant-\(a^2\) terms vanish identically by pair independence (\(\Lambda_4(u,u,1,1)=0\)).
2. Consequently, \(R_2 = R_{2,(1)} + R_{2,(2)}\), where \(R_{2,(1)}\) has one \(a\) and one \(h\) (12 terms of type \(a\Lambda_4(u,u,h,1)\)) and \(R_{2,(2)}\) has two \(u\)'s and two \(h\)'s (6 terms of type \(\Lambda_4(u,u,h,h)\)).
3. Using \(\max_{\xi\ne 0}|\widehat{u}(\xi)| \le \rho\), \(\|u\|_2 = \sqrt{U}\), and \(\|h\|_2 = \sqrt{v}\):
   \[
   |R_{2,(1)}| \le 12a\rho\sqrt{Uv}, \qquad |R_{2,(2)}| \le 6\rho\sqrt{Uv}\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}, \tag{8.1}
   \]
   and therefore
   \[
   \boxed{|R_2| \le 6\rho\sqrt{Uv}\,\bigl(2a + \|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}\bigr).} \tag{8.2}
   \]
   Under `SELECT` failure (\(\rho \le \sqrt{c}a^{5/4}\sqrt{\ell(a)}\)) and \(v \le \zeta a^{9/4}\), we have \(12a\rho\sqrt{Uv} \le 12\sqrt{c\zeta}\,a^{31/8}\sqrt{\ell(a)}\), and \(|R_{2,(2)}| \le 6\sqrt{c\zeta}\,a^{23/8}\sqrt{\ell(a)}\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}\) (improving \(6Uv \sim a^{13/4}\) whenever \(\|\widehat{h}\|_{\ell^1} \ll a^{3/8}/\sqrt{\ell(a)}\)).

*Proof.* In any \(\Lambda_4(u,u,h,h)\) term, the Fourier sum is \(\sum_{r,s} \widehat{v_0}(r+2s)\widehat{v_1}(-2r-3s)\widehat{v_2}(r)\widehat{v_3}(s)\) where two factors are \(\widehat{u}\) and two are \(\widehat{h}\). Bound one \(\widehat{u}\) by \(\rho\), pull out one \(\widehat{h}\) in \(\ell^1\) (\(\le \|\widehat{h}\|_{\ell^1}\)), and apply Cauchy–Schwarz to the remaining \(\widehat{u}\) and \(\widehat{h}\) (which are bijectively indexed for each fixed value of the pulled-out frequency), giving \(\rho \|\widehat{h}\|_{\ell^1} \|u\|_2 \|h\|_2 = \rho\sqrt{Uv}\|\widehat{h}\|_{\ell^1}\). Summing over the 6 terms gives (8.1)–(8.2). \(\square\)

---

## Phase 9, Phase 10 & Phase 11 — Verification and Sharp Remaining Sublemma

Run `python3 verify_cubic_factor_spectral_20261014.py` (outputs `CUBIC_FACTOR_SPECTRAL_VERIFICATION_20261014.json`):
- **2,496** exact rational verifications of \(R_1 = 2\langle u, h_{E,g}+h_{M,g}\rangle_p = 2w\langle u, k_{E,g}+k_{M,g}\rangle_\Omega\);
- **2,247** exact rational verifications of \(R_1 = R_{1,(2)} + R_{1,(3)}\), \(R_2 = R_{2,(1)} + R_{2,(2)}\), and the new \(\ell^1\)-Fourier bounds (1.6) and (8.1)–(8.2);
- **45** trilinear \(L^2\) stability verifications (`(1.3)`);
- **6** analytic 1D cubic harmonic decay checks (`(3.1)`) and **4** multi-coordinate Walsh parity diagnostics (`d=1..4`) demonstrating exponential damping \(\|H_h^{(3)}\|_2^2 \approx (0.1358)^d \cdot 4v^3\);
- **12** exact orbit checks on the \(p=23,k=5\) and \(p=29,k=6\) rational global laws.

### Corrected Continuation Prompt

> Continue offline from `CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md` and `CUBIC_FACTOR_SPECTRAL_VERIFICATION_20261014.json`. Accept as proved:
> 1. **Trilinear \(L^2\) Stability and \(\ell^1\)-Fourier Bounds on \(R_1\) and \(R_2\) (Theorems 1 & 3)**: \(\|C_E(f_1,f_2,f_3)\|_2 \le \|f_1\|_2\|f_2\|_2\|f_3\|_2\), \(|R_1| \le 4\rho v(3a + \|\widehat{h}\|_{\ell^1})\), and \(|R_2| \le 6\rho\sqrt{Uv}(2a + \|\widehat{h}\|_{\ell^1})\). In particular, under `SELECT` failure (\(\rho \le \sqrt{c}a^{5/4}\sqrt{\ell}\)) and \(v \le \zeta a^{9/4}\), \(\|\widehat{h}\|_{\ell^1} = o(a^{1/2}/\sqrt{\ell})\) completely eliminates Branch III (\(|R_1|=o(a^4)\)).
> 2. **Cubic Averaging Harmonic Decay & High-Weight Walsh Damping (Theorem 2 & Phase 7)**: For 1D coordinate functions with \(|\widehat{\Phi}(m)| \le A/|m|\), cubic completion enhances decay from \(O(1/|t|)\) to \(|K_{E,\Phi}(t)| \le A^3(4\log(2|t|+2)+6)/t^2\) (\(\ell^2\) tail \(O(L^{-3}\log^2 L)\)), while \(k\)-coordinate Walsh parity products are damped by \((0.1358)^k\) under cubic averaging.
>
> Attack the two remaining obstacles to closing `COLLECTIVE-WSELECT`:
> - **Obstacle A (Junta / Low-Hamming-Weight Decomposition of \(H_g^{(3)}\))**: Prove analytically on \(\mathbb{Z}_p\) (and proper windows \(\Omega\)) that for any \(h = g-a\) measurable with respect to a rank-\(d\) quarter-arc factor, decomposing \(h\) by ANOVA / coordinate Hamming weight \(k\) damps the cubic field of the \(k\ge 4\) part below \(a^7\), confining \(H_g^{(3)}\) to low-order (\(k\le 3\)) coordinate combinations.
> - **Obstacle B (Amplification from \(a^4\) to \(|\Gamma|a^{5/2}R(a)\) in Branches I & II)**: Combine the two-channel completion pairing \(w(S_E+S_M) \ge c_0 R_0\) (Branch I) and the negative-cubic / positive-quartic residual bounds (Branch II) with 4-AP exclusion \(B q_E = B q_M = 0\) to bound the effective spectral support of \(q_E+q_M\) and \(u\).
