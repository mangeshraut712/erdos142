# Residual-Field Spectral Amplification, Exact Finite-\(p\) Quadratic Terminal Bounds, and Elimination of the \(W_\Gamma\) Denominator Barrier — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with exact finite-\(p\) zero-wraparound polynomial formulas for \(Z_I, \Phi_M, \Phi_E\), moment-weighted and density-thresholded completion pointwise Fourier caps eliminating the \(W_\Gamma \lesssim a^4\) denominator barrier in Branch I, and purely diagonal \(\ell^3\) dyadic-shell dichotomy in Branch II).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, `COLLECTIVE-WSELECT`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 — Independent Audit and Exact Finite-\(p\) Zero-Wraparound Quadratic Window Theorem

We independently audited `QUADRATIC_TO_LINEAR_TRANSFER_20261014.md` Theorem 2 and derived the exact finite-\(p\) discrete polynomial formulas for \(Z_I, \Phi_M(y), \Phi_E(y)\) and the off-diagonal hitting-degree inequality:

1. **Exact separation of \(d=0\) diagonal and \(d\ne 0\) nondegenerate progressions**:
   Let \(p>3\) be prime, \(\Omega\subset\mathbb{Z}_p\) have size \(n=wp\) (\(P=1_\Omega\)), and \(A\subset\Omega\) (\(B=1_A,\ a=|A|/|\Omega|\)) have no nonzero-difference 4-AP in \(\mathbb{Z}_p\). For \(d\in\mathbb{Z}_p\setminus\{0\}\), since \(p>3\), the four points \((v,v+d,v+2d,v+3d)\) are distinct. Define the strictly off-diagonal (\(d\ne 0\)) hitting degree \(h_\Omega^{\ne}(v) := \sum_{i=0}^3 \frac{1}{p}\sum_{d\in\mathbb{Z}_p\setminus\{0\}} \prod_{j\ne i}P(v+(j-i)d) = h_\Omega(v) - \frac{4}{p}P(v)\) and \(\Lambda_4^{\ne}(P) := \Lambda_4(P) - \frac{w}{p}\). Since every \(d\ne 0\) 4-AP in \(\Omega\) contains at least one hole \(v\in\Omega\setminus A\) (\(D(v) = P(v)-B(v) = 1\)), we have \(\mathbb{E}_v[D(v)h_\Omega^{\ne}(v)] \ge \Lambda_4^{\ne}(P)\) and \(\mathbb{E}_v[P(v)h_\Omega^{\ne}(v)] = 4\Lambda_4^{\ne}(P)\). For \(r(v) = D(v) - (1-a)P(v) = aP(v) - B(v)\):
   \[
   \mathbb{E}_v\bigl[r(v)h_\Omega(v)\bigr] = \mathbb{E}_v\bigl[r(v)h_\Omega^{\ne}(v)\bigr] \ge (4a - 3)\left(\Lambda_4(P) - \frac{w}{p}\right) \ge (4a - 3)\Lambda_4(P) - \frac{w}{p}. \tag{0.1}
   \]

2. **Exact finite-\(p\) zero-wraparound formulas for \(Z_I, \Phi_M(y), \Phi_E(y)\)**:
   Let \(I = \{0, 1, \dots, L-1\} \subset \mathbb{Z}_p\) with \(1 \le L \le \frac{p+3}{4}\) (\(w = L/p\)). By Fourier inversion on \(\mathbb{Z}_p\):
   - \(p^3 Z_I = p^3 \sum_{t\in\mathbb{Z}_p} |\widehat{1_I}(t)|^2 |\widehat{1_I}(3t)|^2 = \#\{(z_1,z_2,z_3,z_4)\in I^4 : (z_1-z_2) - 3(z_4-z_3) \equiv 0 \pmod p\}\),
   - \(p^2 \Phi_M(y) = \#\{(z_1,z_2,z_3)\in I^3 : (z_1-z_2) - 3(y-z_3) \equiv 0 \pmod p\}\),
   - \(p^2 \Phi_E(y) = \#\{(z_1,z_2,z_3)\in I^3 : (y-z_3) - 3(z_1-z_2) \equiv 0 \pmod p\}\).
   Because \(z_1,z_2,z_3,z_4,y \in \{0,\dots,L-1\}\), the integer combinations \((z_1-z_2) - 3(y-z_3)\) and \((y-z_3) - 3(z_1-z_2)\) have absolute value at most \(4(L-1) < p\)! Thus **modular congruence modulo \(p\) is equivalent to exact integer equality in \(\mathbb{Z}\) with zero wraparound!**

**Theorem 1 (Exact Finite-\(p\) Polynomial Bounds for \(Z_I, \Phi_M, \Phi_E\) and the \(53/69 < 4/5\) Terminal Bound).**
For every prime \(p>3\) and integer \(1 \le L \le \frac{p+3}{4}\) (\(w = L/p\)), put \(M = \lfloor (L-1)/3\rfloor\) and \(r = L - 3M \in \{1, 2, 3\}\). Then:
1. **(Exact formula for \(Z_I\))**:
   \[
   p^3 Z_I = L^2 + 2\sum_{u=1}^M (L - u)(L - 3u) = \frac{8}{27}L^3 + \operatorname{rem}_r(L) \ge \frac{8}{27}L^3 + \frac{1}{3}L, \qquad
   Z_I \ge \frac{8}{27}w^3 + \frac{w}{3p^2}, \tag{0.2}
   \]
   where \(\operatorname{rem}_1(L) = \frac{7}{9}L - \frac{2}{27}\), \(\operatorname{rem}_2(L) = \frac{7}{9}L + \frac{2}{27}\), and \(\operatorname{rem}_3(L) = \frac{1}{3}L\).
2. **(Exact upper bounds on \(\Phi_M(y), \Phi_E(y)\), and \(H(y) = 2\Phi_E(y)+2\Phi_M(y)\) on \(I\))**:
   For every \(y\in\{0,\dots,L-1\}\),
   \[
   \begin{aligned}
   \Phi_M(y) &\le \frac{1}{3}w^2 + \frac{r(3-r)}{3p^2} \le \frac{1}{3}w^2 + \frac{2}{3p^2}, \\
   \Phi_E(y) &\le \frac{11}{36}w^2 + \frac{2w}{3p} + \frac{1}{3p^2}, \\
   H(y) = 2\Phi_E(y) + 2\Phi_M(y) &\le \frac{23}{18}w^2 + \frac{4w}{3p} + \frac{2}{p^2}.
   \end{aligned} \tag{0.3}
   \]
3. **(Finite-\(p\) terminal density bound on \(\Omega_{\text{quad}}\))**:
   Combining (0.1)–(0.3) with \(\Lambda_4(1_{\Omega_{\text{quad}}}) \ge Z_I - (2+\log p)^4/\sqrt{p}\) and \(h_{\Omega_{\text{quad}}}(v) \le H(q(v)) + 4(2+\log p)^3/\sqrt{p}\) (\(v\ne r_0\)) proves \(a \le \frac{53}{69} + O(w^{-3}p^{-1/2}\log^4 p) < \frac{4}{5}\).

---

## Phase 1 — Audit of Centered Baseline-Free All-Chirp Identities

We independently verified Theorem 3 of `QUADRATIC_TO_LINEAR_TRANSFER_20261014.md`:
- For each nonzero slope \(c \in \mathbb{Z}_p\setminus\{0\}\), \(\sum_{r\in\mathbb{Z}_p}|Q_u(c,r)|^2 = U\), \(\sum_{r\in\mathbb{Z}_p}|Q_B(c,r)|^2 = a\), and \(\sum_{r\in\mathbb{Z}_p}\operatorname{Re}(\overline{Q_u(c,r)}Q_B(c,r)) = \langle u, B\rangle_p = U\).
- Because \(r \mapsto 3r\) and \(r \mapsto r/3\) are bijections of \(\mathbb{Z}_p\), the centered fluctuations \(\widetilde{W}_u(c,r) = |Q_u(c,r)|^2 - U/p\), \(\widetilde{W}_B(c,r) = |Q_B(c,r)|^2 - a/p\), and \(\widetilde{C}_{u,B}(c,r) = \operatorname{Re}(\overline{Q_u(c,r)}Q_B(c,r)) - U/p\) have **exact zero sum over \(r\in\mathbb{Z}_p\)** for every \(c\ne 0\).
- Subtracting those constant \(r\)-means cancels \((p-1) \cdot p \cdot \frac{U}{p}\cdot\frac{a}{p} = (1 - 1/p)aU\) from \(S_E, S_M, M_E, M_M\) and \((1 - 1/p)U^2\) from \(R_4\), leaving only the \(c=0\) linear Fourier terms and the \(O(1/p)\) diagonals as stated in `(2.2)`–`(2.4)` of `QUADRATIC_TO_LINEAR_TRANSFER_20261014.md`.

---

## Phase 2 & Phase 4 — Moment-Weighted and Density-Thresholded Completion Hierarchy (Eliminating the \(W_\Gamma \lesssim a^4\) Denominator Barrier in Branch I)

In all earlier reports (`SIXTH_ORDER_FOURIER_ATTACK_20261012.md`, `COMPLETION_PROJECTION_20261013.md`, `TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` §12.1, `OPEN_LEMMAS.md` Sublemma 2A), the projection denominator \(W_\Gamma(\lambda) = \|P_\Gamma k_\lambda\|_2^2\) on a frequency packet \(\Gamma\) of size \(|\Gamma|\) was bounded only by the **total spatial variance** \(W(\lambda) \le 2a\,\mathbb{E}[q_\lambda] \asymp a^4\), which gave \(\Delta E \ge \frac{\kappa^2(\lambda^T S)^2}{4 W(\lambda)} \gtrsim a^4\) and left an apparent \(a^{3/2}\ell(a)\) denominator gap between \(W(\lambda) \lesssim a^4\) and the required \(a^{11/2}/(|\Gamma|R(a))\).

We now prove that **pointwise nonnegativity of the completion fields in physical space imposes an exact \(\ell^\infty\) Fourier cap in frequency space**, completely eliminating the \(W_\Gamma\) denominator barrier:

**Theorem 2 (Moment-Weighted & Density-Thresholded Completion Pointwise Fourier Caps and Direct Amplification).**
Let \(\Omega\subset\mathbb{Z}_p\) have size \(n=wp\), let \(A\subset\Omega\) be cyclically 4-AP-free for nonzero differences, let \(F\) be any partition of \(\Omega\), \(g = \mathbb{E}_\Omega[B\mid F]\), \(u = B - g\), and \(c_\xi = \mathbb{E}_\Omega[u(x)e_p(-\xi x)]\). For any \(\lambda = (\lambda_E,\lambda_M)^T \in \mathbb{R}_{\ge 0}^2\) and integer \(m\ge 0\), define on \(\mathbb{Z}_p\):
\[
\phi_\lambda^{(m)}(x) := 1_\Omega(x)\,g(x)^m\,q_\lambda(x) \ge 0, \qquad
S^{(m)}(\lambda) := \mathbb{E}_{x\in\Omega}\bigl[g(x)^m\,q_\lambda(x)\bigr], \tag{2.1}
\]
and for any cell-density threshold \(\gamma \in (0, 1)\), define on \(\mathbb{Z}_p\):
\[
\phi_\lambda^{\ge \gamma a}(x) := 1_\Omega(x)\,1_{g(x)\ge \gamma a}\,q_\lambda(x) \ge 0, \qquad
S_{\ge \gamma a}(\lambda) := \mathbb{E}_{x\in\Omega}\bigl[1_{g(x)\ge \gamma a}\,g(x)\,q_\lambda(x)\bigr]. \tag{2.2}
\]
Then:
1. **(Exact unwindowed Fourier synthesis and pointwise Fourier caps)**:
   For every \(x\in\Omega\) and every \(\xi\in\mathbb{Z}_p\):
   \[
   \begin{aligned}
   g_C^m k_\lambda(x) &= \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} \widehat{\phi_\lambda^{(m)}}(\xi)\,\psi_\xi(x), &\qquad
   -S^{(m+1)}(\lambda) &= \langle u, g_C^m k_\lambda\rangle_\Omega = \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} \overline{c_\xi}\,\widehat{\phi_\lambda^{(m)}}(\xi), \\
   1_{g_C\ge \gamma a} k_\lambda(x) &= \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} \widehat{\phi_\lambda^{\ge \gamma a}}(\xi)\,\psi_\xi(x), &\qquad
   -S_{\ge \gamma a}(\lambda) &= \langle u, 1_{g_C\ge \gamma a} k_\lambda\rangle_\Omega = \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} \overline{c_\xi}\,\widehat{\phi_\lambda^{\ge \gamma a}}(\xi),
   \end{aligned} \tag{2.3}
   \]
   and by pointwise nonnegativity on \(\mathbb{Z}_p\), **every** Fourier coefficient \(\xi\in\mathbb{Z}_p\) satisfies:
   \[
   \boxed{
   \bigl|\widehat{\phi_\lambda^{(m)}}(\xi)\bigr| \le \widehat{\phi_\lambda^{(m)}}(0) = w\,S^{(m)}(\lambda), \qquad
   \bigl|\widehat{\phi_\lambda^{\ge \gamma a}}(\xi)\bigr| \le \widehat{\phi_\lambda^{\ge \gamma a}}(0) = w\,\mathbb{E}_\Omega\bigl[1_{g\ge \gamma a}q_\lambda\bigr] \le \frac{w}{\gamma a}\,S_{\ge \gamma a}(\lambda)!!
   } \tag{2.4}
   \]
2. **(Automatic denominator bound & complete cancellation of \(S_{\ge \gamma a}(\lambda)\))**:
   If \(S_{\ge \gamma a}(\lambda) > 0\) and a frequency packet \(\Gamma \subset \mathbb{Z}_p\setminus\{0\}\) of size \(|\Gamma|\) captures a fraction \(\theta \in (0, 1]\) of the pairing \(S_{\ge \gamma a}(\lambda)\) (i.e. \(\bigl|\sum_{\xi\in\Gamma}\overline{c_\xi}\widehat{\phi_\lambda^{\ge \gamma a}}(\xi)\bigr| \ge \theta\,S_{\ge \gamma a}(\lambda)\)), then (2.4) implies:
   \[
   \boxed{
   \sum_{\xi\in\Gamma} |c_\xi| \ge \frac{\theta\,\gamma\,a}{w}, \qquad
   \sum_{\xi\in\Gamma} |c_\xi|^2 \ge \frac{\theta^2\,\gamma^2\,a^2}{|\Gamma|\,w^2}, \qquad
   \max_{\xi\in\Gamma} |c_\xi|^2 \ge \frac{\theta^2\,\gamma^2\,a^2}{|\Gamma|^2\,w^2}!!
   } \tag{2.5}
   \]
   In particular, if \(|\Gamma| \le \frac{\theta\gamma}{w\sqrt{c}}\,a^{-1/8}\ell(a)^{-1/2}\), then **a SINGLE character \(\xi^*\in\Gamma\) satisfies the full `SELECT` threshold \(|c_{\xi^*}|^2 \ge c\,a^{5/2}\ell(a)\)** (and on \(\mathbb{Z}_p\) where \(w=1\) and \(G_\Gamma = I\), adjoining any packet \(\Gamma\) of size \(|\Gamma| \le \frac{\theta\gamma}{\sqrt{c}}\,a^{-1/4}\ell(a)^{-1/2}\) achieves \(\Delta E(\Gamma) \ge \kappa^2 \frac{\theta^2\gamma^2 a^2}{|\Gamma|} \ge \kappa^2 c\,|\Gamma|\,a^{5/2}\ell(a)\))!
3. **(Unconditional survival of \(D_3(g_{\ge a/2})\) under \(\gamma = 1/2\) thresholding)**:
   For \(\gamma = 1/2\), every \(x\in\Omega\) satisfies \(0 \le g_{< a/2}(x) = 1_{g(x) < a/2}g(x) \le h_-(x)\) and \(g_{\ge a/2}(x) = 1_{g(x)\ge a/2}g(x) \ge W(x)\max(0, a - 2h_-(x))\), so on \(\mathbb{Z}_p\):
   \[
   D_3(g_{\ge a/2}) := \sum_{i=0}^3 \Lambda_4\bigl(B\text{ at }i,\ g_{\ge a/2}\text{ at }\ne i\bigr) \ge 4a^4 - 24a^3\,\mathbb{E}[h_-] \ge 4a^4 - 12a^3\sqrt{v}. \tag{2.6}
   \]

---

## Phase 3 & Phase 5 — Purely Diagonal \(\ell^3\) Lower Bound and Dyadic Shell Dichotomy in Branch II

In `TWO_BRANCH_AUTONOMOUS_CLOSURE_20261014.md` Theorem 5, we proved that in Branch II (\(Y = \frac{1}{2}R_3 + R_4 \ge \frac{1}{2}a^4 - O(a^{33/8})\)), we have \(Y = a(T_u + S_u) + \langle \frac{1}{2}u + h, K_u^{(3)}\rangle_p\). We now prove a purely diagonal single-frequency \(\ell^3\) lower bound and a dyadic shell dichotomy for \(T_u + S_u\):

**Theorem 3 (Purely Diagonal \(\ell^3\) Lower Bound and Dyadic Shell Dichotomy).**
For any mean-zero function \(u\) on \(\mathbb{Z}_p\) (\(p>3\)) with \(\|u\|_2^2 = U \le a(1-a)\) and \(\max_{\xi\ne 0}|\widehat{u}(\xi)| = \rho\):
1. **(Purely diagonal \(\ell^3\) bound)**: By Hölder's inequality with exponents \((3, 3, 3)\) and the bijectivity of \(\xi \mapsto 2\xi, -2\xi, -3\xi\) on \(\mathbb{Z}_p\setminus\{0\}\),
   \[
   |T_u| \le \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} |\widehat{u}(\xi)|^3, \qquad
   |S_u| \le \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} |\widehat{u}(\xi)|^3, \qquad
   \boxed{\sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} |\widehat{u}(\xi)|^3 \ge \frac{1}{2}|T_u + S_u|.} \tag{3.1}
   \]
2. **(Dyadic shell dichotomy)**: Suppose \(M_3 := \frac{1}{2}|T_u + S_u| > 0\). Put \(\tau := \frac{M_3}{2U}\) and \(J := \lfloor \log_2(\max(1, \rho/\tau))\rfloor\), and partition \(\operatorname{Spec}_\tau(u)\) into the \(J+1\) dyadic shells \(\Gamma_j := \{\xi\ne 0 : 2^j\tau \le |\widehat{u}(\xi)| < 2^{j+1}\tau\}\) (\(0\le j\le J\)). Then at least one dyadic shell \(\Gamma_j\) of cardinality \(s := |\Gamma_j|\) and minimum squared coefficient \(\mathcal{E}_1 := (2^j\tau)^2\) satisfies:
   \[
   \boxed{
   s\,\mathcal{E}_1^{3/2} \ge \frac{M_3}{16(J + 1)}, \qquad
   \min_{\xi\in\Gamma_j} |\widehat{u}(\xi)|^2 \ge \mathcal{E}_1 \ge \left(\frac{M_3}{16(J+1)}\right)^{2/3} s^{-2/3}, \qquad
   \sum_{\xi\in\Gamma_j} |\widehat{u}(\xi)|^2 \ge s\,\mathcal{E}_1 \ge \left(\frac{M_3}{16(J+1)}\right)^{2/3} s^{1/3}!
   } \tag{3.2}
   \]
   In particular, when \(M_3 \ge c_1 a^3\) (so \(J+1 = O(\ell(a))\)):
   - **Small-Shell Case (\(s \le c_2 a^{-3/4}\ell(a)^{-7/2}\))**: Every frequency \(\xi \in \Gamma_j\) satisfies the single-character `SELECT` bound \(|\widehat{u}(\xi)|^2 \ge \mathcal{E}_1 \ge c\,a^{5/2}\ell(a)\) (since \(a^{(3 \cdot 2/3) - (-3/4 \cdot 2/3)} = a^{2 + 1/2} = a^{5/2}\))!
   - **Large-Shell Case (\(s > c_2 a^{-3/4}\ell(a)^{-7/2}\))**: The shell \(\Gamma_j\) is a flat spectrum of \(s > c_2 a^{-3/4}\ell(a)^{-7/2}\) frequencies of uniform magnitude \(\asymp 2^j\tau\) carrying total energy \(\sum_{\xi\in\Gamma_j}|\widehat{u}(\xi)|^2 \ge c' a^2 s^{1/3}\ell(a)^{-2/3} \ge c'' a^{7/4}\ell(a)^{-11/6} \gg \zeta a^{9/4}\).

---

## Verification Summary (`verify_residual_field_amplification_20261014.py`)
Run `python3 verify_residual_field_amplification_20261014.py` (outputs `RESIDUAL_FIELD_AMPLIFICATION_VERIFICATION_20261014.json`):
- **149** exact rational finite-\(L\) polynomial checks (`L=1..149`) and **3** zero-wraparound \(\mathbb{Z}_p\) checks (`Theorem 1`);
- **2,211** exact rational verifications of \(D_3(g_{\ge a/2}) \ge 4a^4 - 12a^3\sqrt{v}\) and **2,460** verifications of the moment-weighted and thresholded completion Fourier caps (`Theorem 2`);
- **100** verifications of the purely diagonal \(\ell^3\) lower bound \(\sum_{\xi\ne 0}|\widehat{u}(\xi)|^3 \ge \frac{1}{2}|T_u+S_u|\) and dyadic shell dichotomy (`Theorem 3`).
