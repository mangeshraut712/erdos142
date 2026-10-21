# Three-Branch Fourier Amplification, Exact Linear Residual Pairing \(R_1\), and Endpoint Signal Audit — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with exact Branch III linear-residual Fourier pairing, exact \(h^2\) vs \(h^3\) splitting of \(R_1\), rigorous audit of the endpoint signal claim across trivial vs general factors, and weakened collective-energy replacement ledger).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 & Phase 1 — Reconstruction and Audit of the Three-Way Dichotomy

Let \(p>3\) be prime, \(\Omega\subset\mathbb{Z}_p\) have size \(n=wp\), \(A\subset\Omega\) be cyclically 4-AP-free for nonzero differences, \(B=1_A\), \(F\) be a partition of \(\Omega\), \(g=\mathbb{E}_\Omega[B\mid F]\), and \(u=B-g\) (all extended by zero outside \(\Omega\)). Define:
\[
X := w(S_E + S_M) \ge 0, \qquad
Y := \frac{1}{2}R_3 + R_4, \qquad
T := R_0 + \frac{1}{2}R_1 + \frac{w(U - a^2 - v)}{p}, \tag{1.1}
\]
where \(a = \mathbb{E}_\Omega B\), \(v = \operatorname{Var}_\Omega(g)\), and \(U = \mathbb{E}_\Omega[u^2] = a(1-a)-v\).

**Theorem 1 (Unconditional Three-Way Dichotomy with Exact Diagonal Terms).**
For every cyclically 4-AP-free set \(A\subset\Omega\) and every partition \(F\) of \(\Omega\), we have the exact identity \(X + Y = T\). Consequently, for any parameter \(c_0 \in (0, 1/2)\), at least one of the following three branches holds:
- **Branch I (Two-channel completion pairing)**:
  \[
  X = w(S_E + S_M) \ge c_0 R_0; \tag{1.2a}
  \]
- **Branch II (Cubic-plus-quartic residual & operator form)**:
  \[
  Y = \frac{1}{2}R_3 + R_4 \ge c_0 R_0 + \frac{w(U - a^2 - v)}{p}; \tag{1.2b}
  \]
- **Branch III (Negative linear-residual progression count)**:
  \[
  R_1 \le -2(1 - 2c_0)R_0 \qquad \bigl(\text{while } R_1 \ge -4R_0 \text{ unconditionally from } D_3 = 4R_0 + R_1 \ge 0\bigr). \tag{1.2c}
  \]

*Choice of \(c_0\)*: Taking \(c_0 = 1/4\) balances all three branches symmetrically: Branch I gives \(X \ge \frac{1}{4}R_0\), Branch II gives \(Y \ge \frac{1}{4}R_0 + \frac{w(U-a^2-v)}{p}\), and Branch III gives \(R_1 \le -R_0\) (with \(-4R_0 \le R_1 \le -R_0\)).
**Important audit qualification**: At the `SELECT` variance ceiling \(v \le \zeta a^{9/4}\), Branch III is **not** automatically excluded by the generic Cauchy–Schwarz bound \(|R_1| \le 12a\rho v + 4\sqrt{b}v^{3/2} = O(a^{31/8})\), because \(a^{31/8} \gg a^4\) as \(a\to 0\). We therefore attack Branch III directly in Phases 2 & 3 below.

---

## Phase 2 & Phase 3 — Exact Linear Residual Formula for \(R_1\) and Attack on Branch III

### 3.1 Exact physical and unwindowed Fourier pairing for \(R_1\) — PROVED
Define the factor-level endpoint and interior completion fields on \(\mathbb{Z}_p\) (using the zero-extended \(g\)):
\[
h_{E,g}(x) := \frac{1}{p}\sum_{d\in\mathbb{Z}_p} g(x+d)g(x+2d)g(x+3d), \qquad
h_{M,g}(x) := \frac{1}{p}\sum_{d\in\mathbb{Z}_p} g(x-d)g(x+d)g(x+2d). \tag{2.1}
\]
Let \(\widehat{g}(\xi) = \mathbb{E}_{x\in\mathbb{Z}_p}[g(x)e_p(-\xi x)]\) be the full-group Fourier transform of \(g\), and let
\[
K_{E,g}(\xi) := \widehat{h_{E,g}}(\xi) = \sum_{r\in\mathbb{Z}_p} \widehat{g}(2\xi+r)\widehat{g}(-\xi-2r)\widehat{g}(r), \qquad
K_{M,g}(\xi) := \widehat{h_{M,g}}(\xi) = \sum_{r\in\mathbb{Z}_p} \widehat{g}\bigl((\xi+r)/2\bigr)\widehat{g}\bigl((\xi-3r)/2\bigr)\widehat{g}(r). \tag{2.2}
\]
On \(\Omega\), define the cell-centered factor completion fields \(k_{E,g} := (I-\mathbb{E}(\cdot\mid F))h_{E,g}\big|_\Omega\) and \(k_{M,g} := (I-\mathbb{E}(\cdot\mid F))h_{M,g}\big|_\Omega\), and recall \(\psi_\xi = (I-\mathbb{E}(\cdot\mid F))e_p(\xi x)\big|_\Omega\) and \(c_\xi = \mathbb{E}_\Omega[u(x)e_p(-\xi x)]\).

**Theorem 2 (Exact Linear Residual Pairing and Unwindowed Fourier Synthesis of \(R_1\)).**
For every subset \(A\subset\Omega\) and every partition \(F\) of \(\Omega\):
1. **(Physical-space pairing)**: With \(R_{1,uE} = \Lambda_4(u,g,g,g)+\Lambda_4(g,g,g,u)\) and \(R_{1,uM} = \Lambda_4(g,u,g,g)+\Lambda_4(g,g,u,g)\),
   \[
   R_{1,uE} = 2\langle u, h_{E,g}\rangle_p = 2w\langle u, k_{E,g}\rangle_\Omega, \qquad
   R_{1,uM} = 2\langle u, h_{M,g}\rangle_p = 2w\langle u, k_{M,g}\rangle_\Omega, \tag{2.3}
   \]
   and therefore
   \[
   \boxed{R_1 = 2\langle u, h_{E,g} + h_{M,g}\rangle_p = 2w\langle u, k_{E,g} + k_{M,g}\rangle_\Omega.} \tag{2.4}
   \]
2. **(Unwindowed Fourier synthesis on proper windows)**: Pointwise on \(\Omega\),
   \[
   k_{E,g}(x) + k_{M,g}(x) = \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} \bigl(K_{E,g}(\xi) + K_{M,g}(\xi)\bigr)\psi_\xi(x), \tag{2.5}
   \]
   and
   \[
   \boxed{R_1 = 2w \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} \overline{c_\xi}\,\bigl(K_{E,g}(\xi) + K_{M,g}(\xi)\bigr).} \tag{2.6}
   \]

*Proof.* By reversal \(d\mapsto -d\) and translation \(x\mapsto x-jd\), \(\Lambda_4(u,g,g,g) = \Lambda_4(g,g,g,u) = \langle u, h_{E,g}\rangle_p\) and \(\Lambda_4(g,u,g,g) = \Lambda_4(g,g,u,g) = \langle u, h_{M,g}\rangle_p\). Since \(u\) is supported on \(\Omega\) and \(\mathbb{E}_C[u]=0\) on every cell \(C\in F\), \(\langle u, h_{E,g}\rangle_p = w\langle u, k_{E,g}\rangle_\Omega\). Expanding \(h_{E,g}+h_{M,g}\) by Fourier inversion on \(\mathbb{Z}_p\) and applying \(I-\mathbb{E}(\cdot\mid F)\) on \(\Omega\) kills \(\xi=0\) and yields (2.5)–(2.6). \(\square\)

### 3.2 Exact quadratic-vs-cubic splitting of \(R_1\) on \(\mathbb{Z}_p\) and the Branch III Spectral Theorem — PROVED
On the full group \(\mathbb{Z}_p\) (\(w=1\)), write \(g = a + h\) with \(\mathbb{E}_p[h]=0\) and \(\mathbb{E}_p[h^2]=v\). Expanding \(g=a+h\) inside \(h_{E,g}\) and \(h_{M,g}\), the constant \(a^3\) term and all three linear-in-\(h\) terms are constant on \(\mathbb{Z}_p\) (since \(\mathbb{E}_d h(x+jd) = 0\)), so they vanish identically when paired with the mean-zero residual \(u\)! Thus \(h_{E,g} + h_{M,g}\) modulo constants splits into a **quadratic-in-\(h\) part** \(H_g^{(2)}\) and a **cubic-in-\(h\) part** \(H_g^{(3)}\):
\[
\begin{aligned}
H_g^{(2)}(x) &:= a\mathbb{E}_d\bigl[h(x+d)h(x+2d) + h(x+d)h(x+3d) + h(x+2d)h(x+3d) \\
&\qquad\qquad + h(x-d)h(x+d) + h(x-d)h(x+2d) + h(x+d)h(x+2d)\bigr], \\
H_g^{(3)}(x) &:= \mathbb{E}_d\bigl[h(x+d)h(x+2d)h(x+3d) + h(x-d)h(x+d)h(x+2d)\bigr],
\end{aligned} \tag{2.7}
\]
giving the exact decomposition
\[
R_1 = R_{1,(2)} + R_{1,(3)}, \qquad R_{1,(2)} := 2\langle u, H_g^{(2)}\rangle_p, \qquad R_{1,(3)} := 2\langle u, H_g^{(3)}\rangle_p. \tag{2.8}
\]

**Theorem 3 (Elimination of \(R_{1,(2)}\) under `SELECT` Failure and Exact Branch III Spectral Bound).**
On \(\mathbb{Z}_p\) (\(p>3\)):
1. **(Exact Fourier formula and \(L^2\) bound for \(H_g^{(2)}\))**: For every \(\xi\ne 0\),
   \[
   \widehat{H_g^{(2)}}(\xi) = a\Bigl[2\widehat{h}(-\xi)\widehat{h}(2\xi) + \widehat{h}(-2\xi)\widehat{h}(3\xi) + \widehat{h}(3\xi)\widehat{h}(-2\xi) + \widehat{h}(-\xi/2)\widehat{h}(3\xi/2) + \widehat{h}(\xi/3)\widehat{h}(2\xi/3)\Bigr]. \tag{2.9}
   \]
   By Cauchy–Schwarz and Parseval (\(\sum_\xi |\widehat{h}(\xi)|^2 = v\)),
   \[
   \sum_{\xi\ne 0} |\widehat{H_g^{(2)}}(\xi)| \le 6av, \qquad \|H_g^{(2)}\|_2 \le 6av, \qquad |R_{1,(2)}| \le 12a\rho v. \tag{2.10}
   \]
   In particular, under `SELECT` failure (\(\rho \le \sqrt{c}a^{5/4}\sqrt{\ell(a)}\)) and \(v \le \zeta a^{9/4}\),
   \[
   |R_{1,(2)}| \le 12\sqrt{c}\zeta\, a^{9/2}\sqrt{\ell(a)} = o(a^4)! \tag{2.11}
   \]
   Thus **the quadratic-in-\(h\) part \(R_{1,(2)}\) is strictly \(o(a^4)\) and cannot drive Branch III!**
2. **(Exact \(L^2\) bound and spectral projection for the cubic-in-\(h\) part \(H_g^{(3)}\))**:
   By Cauchy–Schwarz on \(\widehat{h_{E,h}}(\xi) = \sum_r \widehat{h}(2\xi+r)\widehat{h}(-\xi-2r)\widehat{h}(r)\), we have \(\sum_\xi |\widehat{h_{E,h}}(\xi)|^2 \le (\sum_r |\widehat{h}(r)|^2)^3 = v^3\) and similarly \(\sum_\xi |\widehat{h_{M,h}}(\xi)|^2 \le v^3\), so
   \[
   \|H_g^{(3)}\|_2^2 = \sum_{\xi\ne 0} |\widehat{H_g^{(3)}}(\xi)|^2 \le 4v^3. \tag{2.12}
   \]
   Consequently, if Branch III holds (\(R_1 \le -2(1-2c_0)R_0\)), then for all sufficiently small \(a\) under `SELECT` failure,
   \[
   |R_{1,(3)}| = 2|\langle u, H_g^{(3)}\rangle_p| \ge 2(1-2c_0)R_0 - 12a\rho v \ge (1-2c_0)R_0 \sim (1-2c_0)a^4. \tag{2.13}
   \]
   In particular, \(4\sqrt{U}v^{3/2} \ge |R_{1,(3)}| \ge (1-2c_0)R_0\) forces a **minimum factor variance floor for Branch III**:
   \[
   \boxed{\text{Branch III requires } v = \operatorname{Var}(g) \ge \left(\frac{(1-2c_0)R_0}{4\sqrt{U}}\right)^{2/3} \gtrsim a^{7/3}!} \tag{2.14}
   \]
   Moreover, for any character set \(\Gamma\subset\mathbb{Z}_p\setminus\{0\}\) such that \(\sum_{\xi\notin\Gamma\cup\{0\}} |\widehat{H_g^{(3)}}(\xi)|^2 \le \frac{(1-2c_0)^2 R_0^2}{64 U}\), Cauchy–Schwarz on \(\Gamma\) gives the collective residual Fourier capture:
   \[
   \boxed{\sum_{\xi\in\Gamma} |\widehat{u}(\xi)|^2 \ge \frac{(1-2c_0)^2 R_0^2}{16 \sum_{\xi\in\Gamma} |\widehat{H_g^{(3)}}(\xi)|^2} \ge \frac{(1-2c_0)^2 R_0^2}{64 v^3} \gtrsim \frac{a^8}{v^3} \ge \frac{a^{5/4}}{64\zeta^3}!} \tag{2.15}
   \]

**Significance of Theorem 3 (`(2.14)`–`(2.15)`)**:
- First, (2.14) proves that **Branch III is impossible whenever \(v \ll a^{7/3}\)** (improving our earlier \(a^{8/3}\) threshold to \(a^{7/3}\); the only remaining variance band where Branch III can occur at all is \(c_1 a^{7/3} \le v \le \zeta a^{9/4}\), a narrow \(a^{1/12}\)-width band!).
- Second, in that narrow band \(v \in [c_1 a^{7/3}, \zeta a^{9/4}]\), because \(\|H_g^{(3)}\|_2^2 \le 4v^3 \le 4\zeta^3 a^{27/4}\) is **tiny** (much smaller than \(a^4\)), the denominator \(64v^3 \lesssim a^{27/4}\) in (2.15) is so small that any character set \(\Gamma\) capturing the bulk of \(H_g^{(3)}\) forces \(\sum_{\xi\in\Gamma}|\widehat{u}(\xi)|^2 \gtrsim a^8 / v^3 \ge a^{5/4}\), which **exceeds the entire stopping energy \(\zeta a^{9/4}\) by a factor of \(a^{-1}\)**!
- Why is that not yet an unconditional proof of Branch III closure? Because while \(g\) is measurable with respect to the current factor \(F\) (which has rank \(s \le M(a) = O(a^{-1/4}/\ell(a))\)), the quarter-arc indicator of \(F\) has slow harmonic decay (`FULL_GROUP_ENERGY_AUDIT.md` Theorem 2b: capturing all of \(g\) to \(L^2\) error \(\tau\) uses side \(H \sim (s/\tau)^{3/2}\) and box size \((2H+1)^s\)). Proving that \(H_g^{(3)}\) (the 3-AP completion of \(h=g-a\)) concentrates on a small set \(\Gamma\) of size \(O(a^{-1/4}/\ell(a))\) is the exact remaining requirement for Branch III in the band \(v\in[c_1 a^{7/3}, \zeta a^{9/4}]\).

---

## Phase 6 — Rigorous Audit of the Endpoint Signal Claim Across All Three Branches

We audit the exact statement of the "scale \(a^4\) endpoint signal" across full groups vs proper windows and trivial (\(v=0\)) vs general (\(v>0\)) factors:

| Setting & Branch | Exact Proved Fourier Lower Bound | Transform Type | Single vs Collective | Exact Dependencies |
| --- | --- | --- | --- | --- |
| **1. Trivial factor (\(v=0\)) on full group \(\mathbb{Z}_p\), Branch II (\(X < \frac{1}{2}a^4\))** | \(\max_{\xi\ne 0}|\widehat{f}(\xi)|^2 > \frac{25 a^4}{64(1-a)^2}\) (when \(pa^3\ge 8\)) | Full-group \(\widehat{f}(\xi)=\widehat{u}(\xi)\) | **Single** character \(\xi\ne 0\) | Zero \(R_1,R_2\) error (\(R_1=R_2=0\) at \(v=0\)); no window loss (\(w=1\)) |
| **2. Trivial factor (\(v=0\)) on full group \(\mathbb{Z}_p\), Branch I (\(X \ge \frac{1}{2}a^4\))** | If \(\rho \le \frac{5}{8}a^2\), then \(\operatorname{Var}(q_E+q_M) \ge \frac{a^7}{4}\), and for any \(\Gamma\) with tail \(\delta_\Gamma^2 \le \frac{a^7}{16}\), \(\sum_{\xi\in\Gamma}|\widehat{f}(\xi)|^2 \ge \frac{a^8}{16 W_\Gamma} \ge \frac{a^4}{32}\) | Full-group \(\widehat{f}(\xi)=\widehat{u}(\xi)\) | **Collective** on \(\Gamma\) (requires tail bound on \(q_E+q_M\)) | Uses \(0\le q_E+q_M\le 2a \implies W \le 2a\mathbb{E}[q_E+q_M] \lesssim a^4\); \(|\Gamma|\) bound open |
| **3. General factor (\(0<v\le \zeta a^{9/4}\)) on proper window \(\Omega\), Branch I (\(X \ge c_0 R_0\))** | For any \(\Gamma,\lambda\) with \(\varepsilon_\Gamma(\lambda,v)^2 \le \frac{(\lambda^T S)^2}{4U}\), \(\Delta E \ge \frac{\kappa^2 (\lambda^T S)^2}{4 D_{\text{reg}}(\lambda,v)} \gtrsim \frac{R_0^2}{w^2 a^4} \sim a^4 \frac{C^2}{w^4}\) | Relative \(\Omega\)-characters via regularized Gram \(M_\Gamma\) | **Collective** quarter-arc gain \(\Delta E\) on \(\Gamma\) | Depends on window baseline \(C=\Lambda_4(1_\Omega)\ge w^2/3^d\) and tail bound \(\varepsilon_\Gamma\) |
| **4. General factor (\(0<v\le \zeta a^{9/4}\)) on proper window \(\Omega\), Branch II (\(Y \ge c_0 R_0\))** | \(R_3 \le -2(2-c_0)R_0 - 3R_1 - 2R_2 + \frac{4w(a^2+v)}{p}\) and \(R_4 \ge (3-2c_0)R_0 + 2R_1 + R_2\) | Full-group zero-extended \(u,g\) | Constrained cubic/quartic sums \(R_3, R_4\) | For \(v>0\), affected by \(3R_1+2R_2\) (where \(|R_2|=O(a^{13/4})\)) and window factor \(w\) |
| **5. General factor (\(c_1 a^{7/3}\le v\le \zeta a^{9/4}\)) on \(\mathbb{Z}_p\), Branch III (\(R_1 \le -2(1-2c_0)R_0\))** | For any \(\Gamma\) with \(\sum_{\xi\notin\Gamma}|\widehat{H_g^{(3)}}(\xi)|^2 \le \frac{(1-2c_0)^2 R_0^2}{64U}\), \(\sum_{\xi\in\Gamma}|\widehat{u}(\xi)|^2 \ge \frac{(1-2c_0)^2 R_0^2}{64 v^3} \gtrsim a^{5/4}\) | Full-group \(\widehat{u}(\xi)\) (or relative via \(K_{E,g}+K_{M,g}\)) | **Collective** on \(\Gamma\) (requires tail bound on \(H_g^{(3)}\)) | Uses Theorem 3 (`|R_{1,(2)}|=o(a^4)` and \(\|H_g^{(3)}\|_2^2 \le 4v^3\)) |

This table corrects any oversimplified statement that "every branch unconditionally gives a single-character \(a^4\) lower bound for arbitrary \(F\)":
- An **unconditional single-character** bound \(\max_{\xi\ne 0}|\widehat{u}(\xi)|^2 \gtrsim a^4\) is proved only in **Case 1** (trivial factor \(v=0\) on \(\mathbb{Z}_p\) in Branch II, or when \(q_E\equiv 0\) or \(q_M\equiv 0\) on \(\mathbb{Z}_p\)).
- In **Cases 2, 3, 5**, the lower bound is **collective on \(\Gamma\)** and is conditional on \(\Gamma\) capturing a constant fraction of the pairing with \(q_E+q_M\) (Branch I) or \(H_g^{(3)}\) (Branch III).
- In **Case 4** (general factor \(v>0\) in Branch II), \(R_3\) and \(R_4\) are coupled to \(R_1\) and \(R_2\), where the generic Cauchy–Schwarz bound on \(|R_2|\) is \(O(a^{13/4})\) (though \(3R_1+R_2 \ge -6R_0\) is bounded below at scale \(-O(a^4)\)).

---

## Phase 7 & Phase 8 — Amplification Analysis and Weakened Sufficient Replacement Ledger

### 8.1 Why the \(a^{-3/2}\ell(a)\) amplification is required for single-character steps
In the October 2 conditional closure (`STRUCTURAL_HYPOTHESIS_ATTACK_20261002.md` §2–3 and `SELECT_ATTACK_20261002.md` §1):
- If a single-character refinement adds \(1\) character with squared correlation \(\ge c a^\lambda \ell(a)^q\), reaching stopping energy \(\eta(a)a^2 = \zeta a^{2+\beta}\) requires \(M(a) = O(a^{-(\lambda-2-\beta)}/\ell(a)^q)\) characters per step, and summing over \(O(a^{-\beta})\) steps in a dyadic density epoch gives cumulative rank and log-size loss:
  \[
  D_t, S_t = O\bigl(t^{-(\lambda-2)} \ell(t)^{-q}\bigr). \tag{8.1}
  \]
- Because the terminal pigeonhole contradiction (`NEW_RESULTS_20261002.md` `(5.2)`) requires \(D_t S_t = o(\log N)\) at \(t = \epsilon/\log N\), the exponent in (8.1) **must satisfy \(\lambda - 2 \le 1/2 \iff \lambda \le 5/2\)** (with \(q > 0\), or a divergent slow function \(R(a)\to\infty\) such as \(R(a)=\log\log(e^2/a)\), when \(\lambda = 5/2\)).
- At the endpoint scale \(\lambda = 4\) (\(\Delta E \sim a^4\)), (8.1) gives \(D_t, S_t = O(t^{-2}) = O((\log N)^2)\), which is \((\log N)^{3/2}\log\log N\) times too large for the terminal contradiction.

### 8.2 Proved Weakened Collective-Energy Replacement Theorem (`COLLECTIVE-WSELECT`) — PROVED CONDITIONAL CLOSURE
One does **not** need a single character to have \(|c_\xi|^2 \ge c a^{5/2}R(a)\). By the regularized relative Gram theorem (`STRUCTURAL_SAMPLING_20261002.md` Theorem 3) and the `WSELECT` dyadic summation (`SELECT_ATTACK_20261002.md` §1), a **collective multi-character packet** closes the entire unconditional target chain under strictly weaker assumptions:

**Theorem 4 (Collective Iterated-Logarithm Replacement Closure).**
Let \(R(a) = \log\log(e^2/a)\) and \(\ell(a) = \log(2/a)\). Suppose that for every \(\epsilon>0\) there exist \(\zeta\in(0,1/4]\), \(c>0\), and \(p_0(\epsilon)\) such that for every prime \(p\ge p_0(\epsilon)\), every \(H\)-window \(\Omega\subset\mathbb{Z}_p\) (\(1\le d\le\sqrt{\log p}\), \(n\ge p\exp(-\sqrt{\log p})\)), every cyclically 4-AP-free \(A\subset\Omega\) with \(\epsilon/(2\log n)\le a\le 4/5\), and every intermediate quarter-arc factor \(F\) of added rank \(< M(a) := \lceil (\zeta/(\kappa^2 c))a^{-1/4}/\ell(a)\rceil\) satisfying \(\operatorname{Var}_\Omega(g) < \zeta a^{9/4} R(a)/\ell(a)\), there exists a nonempty character packet \(\Gamma\subset\mathbb{Z}_p\setminus\{0\}\) of size \(1\le |\Gamma| \le M(a) - \operatorname{rank}(F)\) such that
\[
c_\Gamma^* \bigl(\kappa^2 G_\Gamma + (1-\kappa^2)I_{|\Gamma|}\bigr)^{-1} c_\Gamma \ge c\, |\Gamma|\, a^{5/2} R(a). \tag{8.2}
\]
Then \(r_4(N) = o(N/\log N)\) holds unconditionally.

*Proof.* By `STRUCTURAL_SAMPLING_20261002.md` Theorem 3, adjoining the quarter-arc partition of \(\Gamma\) (for an optimal simultaneous rotation) increases \(\operatorname{Var}_\Omega(g)\) by at least \(\kappa^2 c |\Gamma| a^{5/2} R(a)\) while increasing the factor rank by \(|\Gamma|\). Therefore, the ratio of energy gain to added rank is at least \(\kappa^2 c a^{5/2} R(a)\) per character, so \(\operatorname{Var}_\Omega(g)\) reaches \(\zeta a^{9/4}R(a)/\ell(a)\) within at most \(M(a)\) total added characters. By `SELECT_ATTACK_20261002.md` §1 (`WSELECT` ledger, verified across 9 trajectories in `verify_three_branch_amplification_20261014.py`), dyadic summation from \(t=\epsilon/\log N\) to \(4/5\) yields cumulative rank and log-size loss \(D_t, S_t = O_\epsilon(\sqrt{\log N}/\log\log\log N) = o(\sqrt{\log N})\) and \(D_t(S_t + \log(2D_t) + 1) = o(\log N)\), preserving all \(H\)-window eligibility conditions and contradicting the terminal packing bound \(\le 3/4 + o(1)\). \(\square\)

---

## Phase 9 & Phase 10 — Adversarial Family Testing and Verification Summary

Run `python3 verify_three_branch_amplification_20261014.py` (outputs `THREE_BRANCH_VERIFICATION_20261014.json`):
- **2,496** exact rational verifications of \(R_1 = 2\langle u, h_{E,g}+h_{M,g}\rangle_p = 2w\langle u, k_{E,g}+k_{M,g}\rangle_\Omega\) and its unwindowed Fourier synthesis across \(\mathbb{Z}_7, \mathbb{Z}_{11}\) and proper windows \((11,5), (13,6)\);
- **2,247** exact rational verifications of the full-group decomposition \(R_1 = R_{1,(2)} + R_{1,(3)}\) and the \(L^2\) bounds \(\|H_g^{(2)}\|_2 \le 6av\) and \(\|H_g^{(3)}\|_2 \le 2v^{3/2}\);
- **2,496** exact rational verifications of the three-way dichotomy (`Branch I`, `Branch II`, `Branch III` at \(c_0=1/4\));
- **10** adversarial family classifications (`sidon_z13` in Branch I, `behrend_z43` in Branch II, `ternary_cube_window` in Branch I via interior channel rescue, `digit_product_window` in Branch II, `three_point_window` in Branch I) and **12** exact orbit checks on the \(p=23,k=5\) and \(p=29,k=6\) rational global laws.

### Corrected Continuation Prompt

> Continue offline from `THREE_BRANCH_AMPLIFICATION_20261014.md` and `THREE_BRANCH_VERIFICATION_20261014.json`. Accept as proved:
> 1. **Exact Branch III Linear-Residual Pairing and Variance Floor (Theorems 2 & 3)**: \(R_1 = 2\langle u, h_{E,g}+h_{M,g}\rangle_p = 2w\sum_{\xi\ne 0}\overline{c_\xi}(K_{E,g}(\xi)+K_{M,g}(\xi))\). On \(\mathbb{Z}_p\), \(R_1 = R_{1,(2)} + R_{1,(3)}\) where \(|R_{1,(2)}| \le 12a\rho v = O(a^{9/2}\sqrt{\ell}) = o(a^4)\) under `SELECT` failure, and \(\|H_g^{(3)}\|_2 \le 2v^{3/2}\). Thus Branch III (\(R_1 \le -2(1-2c_0)R_0\)) is impossible whenever \(v \ll a^{7/3}\), and in the narrow band \(v\in[c_1 a^{7/3}, \zeta a^{9/4}]\) any character set \(\Gamma\) capturing the bulk of \(H_g^{(3)}\) yields collective energy \(\sum_{\xi\in\Gamma}|\widehat{u}(\xi)|^2 \ge \frac{(1-2c_0)^2 R_0^2}{64 v^3} \gtrsim a^{5/4} \gg \zeta a^{9/4}\).
> 2. **Rigorous Endpoint Signal Audit (Phase 6 Table)**: The unconditional single-character \(a^4\) bound holds at \(v=0\) on \(\mathbb{Z}_p\) in Branch II; Branches I and III supply collective bounds conditional on the spectral concentration of \(q_E+q_M\) and \(H_g^{(3)}\), while Branch II at \(v>0\) is coupled to \(R_2\).
> 3. **Collective Iterated-Logarithm Replacement Closure (Theorem 4)**: A packet \(\Gamma\) of size \(|\Gamma|\le M(a)\) with regularized Gram energy \(\ge c|\Gamma|a^{5/2}\log\log(e^2/a)\) closes the entire October 2 iteration (`D_t, S_t = O(\sqrt{\log N}/\log\log\log N)`).
>
> Attack the two remaining problems to establish Theorem 4's hypothesis (`COLLECTIVE-WSELECT`):
> - **Problem 1 (Intermediate \(R_2\) and \(H_g^{(3)}\) control for \(v>0\))**: Use the low-rank quarter-arc structure of \(g = \mathbb{E}_\Omega[B\mid F]\) (\(\operatorname{rank}(F) < M(a)\)) to bound the effective Fourier support of \(H_g^{(3)}\) (closing Branch III for \(v\in[c_1 a^{7/3}, \zeta a^{9/4}]\)) and to tighten \(|R_2|\) below \(a^4\) in Branch II.
> - **Problem 2 (Multi-frequency amplification from \(a^4\) to \(|\Gamma|a^{5/2}R(a)\))**: In Branch I (\(w(S_E+S_M)\ge c_0 R_0\)) and Branch II (\(R_3 \le -2(2-c_0)R_0\), \(R_4 \ge (3-2c_0)R_0\)), prove that 4-AP exclusion \(B q_E = B q_M = 0\) and Booleanity \(B^2=B\) prevent the pairing mass from spreading flatly across \(> a^{-3/2}/R(a)\) frequencies.
