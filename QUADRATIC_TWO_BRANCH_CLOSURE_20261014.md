# Quadratic Structure, First-Principles \(U^3\) Operator Trace, Unified All-Chirp Identities, and Architecture Comparison — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with first-principles proof of \(\operatorname{tr}(K_u^4) = \operatorname{tr}(R_u^4) \le \|u\|_{U^3}^8\), exact range of validity of \(|Y| \le a(1+2\sqrt{U})\|u\|_{U^3}^2\), unified diagonal-free all-chirp identities for Branches I & II, and elementary Gauss-sum proof of the translation-mixing obstruction for quadratic-arc windows).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, `COLLECTIVE-WSELECT`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 — Independent First-Principles Operator Audit (\(\operatorname{tr}(K_u^4) = \operatorname{tr}(R_u^4) \le \|u\|_{U^3}^8\))

Let \(p>3\) be prime and equip \(L^2(\mathbb{Z}_p)\) with the normalized inner product \(\langle f_1,f_2\rangle_p = \frac{1}{p}\sum_{x\in\mathbb{Z}_p}\overline{f_1(x)}f_2(x)\). For any real function \(u\) on \(\mathbb{Z}_p\), the operators
\[
(K_u g)(x) = \frac{1}{p}\sum_{y\in\mathbb{Z}_p} u\bigl((2x+y)/3\bigr)u\bigl((x+2y)/3\bigr)g(y), \qquad
(R_u g)(x) = \frac{1}{p}\sum_{y\in\mathbb{Z}_p} u(2x-y)u(2y-x)g(y) \tag{0.1}
\]
have real symmetric \(p\times p\) matrices \((K_u)_{x,y} = \frac{1}{p}u((2x+y)/3)u((x+2y)/3)\) and \((R_u)_{x,y} = \frac{1}{p}u(2x-y)u(2y-x)\) with respect to the standard matrix multiplication \((M g)(x) = \sum_{y\in\mathbb{Z}_p} M_{x,y}g(y)\).
Let \(\operatorname{tr}(M) := \sum_{x\in\mathbb{Z}_p} M_{x,x}\) denote the **ordinary matrix trace** (the sum of the \(p\) eigenvalues of \(M\)), as opposed to the normalized trace \(p^{-1}\operatorname{tr}(M)\).

**Theorem 1 (First-Principles Proof of \(\operatorname{tr}(K_u^4) = \operatorname{tr}(R_u^4) \le \|u\|_{U^3}^8\) and Operator Norm Bounds).**
For every real function \(u\) on \(\mathbb{Z}_p\) (\(p>3\)):
1. **(Exact fourth-power trace identity)**:
   \[
   \operatorname{tr}(K_u^4) = \operatorname{tr}(R_u^4) = \mathbb{E}_{h,k\in\mathbb{Z}_p}\bigl[F_u(2h,k)\,F_u(h,2k)\bigr] \le \|u\|_{U^3}^8, \tag{0.2}
   \]
   where \(F_u(h,k) = \mathbb{E}_{x\in\mathbb{Z}_p}[u(x)u(x+h)u(x+k)u(x+h+k)]\) and \(\|u\|_{U^3}^8 = \mathbb{E}_{h,k}[F_u(h,k)^2]\).
2. **(Operator norm and cubic field bounds)**: Because \(K_u\) and \(R_u\) are real symmetric, their eigenvalues \(\{\lambda_j(K_u)\}_{j=1}^p\) and \(\{\lambda_j(R_u)\}_{j=1}^p\) are real, so
   \[
   \|K_u\|_{\text{op}}^4 = \max_{1\le j\le p} \lambda_j(K_u)^4 \le \sum_{j=1}^p \lambda_j(K_u)^4 = \operatorname{tr}(K_u^4) \le \|u\|_{U^3}^8, \tag{0.3}
   \]
   and identically \(\|R_u\|_{\text{op}}^4 \le \operatorname{tr}(R_u^4) \le \|u\|_{U^3}^8\). Taking square roots gives \(\|K_u\|_{\text{op}}^2, \|R_u\|_{\text{op}}^2 \le \|u\|_{U^3}^4\), and hence \(\|K_u u\|_2^2 \le \|u\|_2^2 \|u\|_{U^3}^4\) and \(\|R_u u\|_2^2 \le \|u\|_2^2 \|u\|_{U^3}^4\).

*Proof of (0.2).* Using symmetry \((R_u)_{x,y} = (R_u)_{y,x}\) and renaming \((x_1,x_2,x_3,x_4) = (y,z,y',z')\), the ordinary matrix trace of \(R_u^4\) is
\[
\operatorname{tr}(R_u^4) = \sum_{y,z,y',z'\in\mathbb{Z}_p} (R_u)_{y,z}(R_u)_{y',z}(R_u)_{y',z'}(R_u)_{y,z'}
= \mathbb{E}_{y,y',z,z'\in\mathbb{Z}_p}\bigl[u(2y-z)u(2z-y)\,u(2y'-z)u(2z-y')\,u(2y-z')u(2z'-y)\,u(2y'-z')u(2z'-y')\bigr].
\]
Notice that the four factors of \(1/p\) in \((R_u)_{x,y}\) match the four summation variables \((y,y',z,z')\in\mathbb{Z}_p^4\), producing the exact normalized expectation \(\mathbb{E}_{y,y',z,z'}\) with no leftover factor of \(p\). Setting \(y'=y+h\), \(z'=z+k\), \(a=2y-z\), and \(c=2z-y\) (an invertible linear bijection of \(\mathbb{Z}_p^2\) since \(\det\begin{pmatrix}2&-1\\-1&2\end{pmatrix} = 3 \not\equiv 0\pmod p\)) yields \(\operatorname{tr}(R_u^4) = \mathbb{E}_{h,k}[F_u(2h,-k)F_u(-h,2k)]\).
Similarly, in \(\operatorname{tr}(K_u^4) = \mathbb{E}_{y,y',z,z'}[K_u(y,z)K_u(y',z)K_u(y',z')K_u(y,z')]\), setting \(y'=y+3h\), \(z'=z+3k\), \(a=(2y+z)/3\), and \(c=(y+2z)/3\) (\(\det = 1/3 \not\equiv 0\pmod p\)) transforms the eight arguments of \(u\) into \((a, c),\ (a+2h, c+h),\ (a+2h+k, c+h+2k),\ (a+k, c+2k)\), which gives \(\operatorname{tr}(K_u^4) = \mathbb{E}_{h,k}[F_u(2h,k)F_u(h,2k)]\). Since \(F_u(-s,-t) = F_u(s,t)\) by translating \(x\mapsto x+s+t\), replacing \((h,k)\mapsto (-h,-k)\) proves \(\operatorname{tr}(K_u^4) = \operatorname{tr}(R_u^4)\). Finally, Cauchy–Schwarz and invertibility of \(2\pmod p\) give \(\mathbb{E}_{h,k}[F_u(2h,k)F_u(h,2k)] \le \|u\|_{U^3}^8\). \(\square\)

---

## Phase 1 — Exact Range of Validity of the Arbitrary-Factor Residual \(U^3\) Theorem

In `TWO_BRANCH_AUTONOMOUS_CLOSURE_20261014.md` Theorem 5 (`(4.2)`–`(4.3)`), we proved the exact identity
\[
Y = \frac{1}{2}R_3 + R_4 = a(T_u + S_u) + \left\langle \frac{1}{2}u + h,\ K_u^{(3)}\right\rangle_p \tag{1.1}
\]
and the unconditionally valid estimate
\[
|Y| \le 2a\sqrt{U}\,\|u\|_{U^2}^2 + \sqrt{U(U + 4v)}\,\|u\|_{U^3}^2 \le \Bigl(2a\sqrt{U} + \sqrt{U(U + 4v)}\Bigr)\,\|u\|_{U^3}^2. \tag{1.2}
\]

**Theorem 2 (Exact Range of Validity of \(\sqrt{U(U+4v)} \le a\) and Unconditional Bound).**
Let \(0 < a < 1\), \(0 \le v \le a(1-a)\), and \(U = a(1-a) - v\). Then:
1. **(Exact polynomial identity)**:
   \[
   a^2 - U(U + 4v) = a^3(2 - a) - 2a(1 - a)v + 3v^2. \tag{1.3}
   \]
2. **(Exact validity range of \(\sqrt{U(U+4v)} \le a\))**:
   - Whenever \(v \le a^2\) (in particular, throughout the entire low-energy regime \(v \le \zeta a^{9/4}\)), we have \(2a(1-a)v \le 2a^3(1-a) \le a^3(2-a)\), so \(a^2 - U(U+4v) \ge 3v^2 \ge 0\) and hence \(\sqrt{U(U+4v)} \le a\), giving:
     \[
     |Y| \le a\bigl(1 + 2\sqrt{U}\bigr)\,\|u\|_{U^3}^2 \qquad \forall v \in [0, a^2]. \tag{1.4}
     \]
   - Moreover, for \(a \ge 1 - \frac{\sqrt{3}}{2} \approx 0.13397\), the discriminant of (1.3) in \(v\) is \(4a^2(1 - 8a + 4a^2) \le 0\), so (1.4) holds for **all** \(v \in [0, a(1-a)]\).
3. **(Unconditional bound for all \(a, v\))**: Since \(U(U+4v) = (b-v)(b+3v) \le \frac{4}{3}b^2\) where \(b = a(1-a)\) (attained at \(v = b/3\)), we have \(\sqrt{U(U+4v)} \le \frac{2}{\sqrt{3}}a(1-a)\) and \(|Y| \le a\bigl(\frac{2}{\sqrt{3}}(1-a) + 2\sqrt{U}\bigr)\|u\|_{U^3}^2\) unconditionally for all \(a, v\).

---

## Phase 2 & Phase 4 — Unified All-Chirp Identities for Branch I and Branch II

For any function \(w\) on \(\mathbb{Z}_p\) (\(p>3\)), define its quadratic chirp transform
\[
Q_w(c, r) := \mathbb{E}_{x\in\mathbb{Z}_p}\bigl[w(x)e_p(-c x^2 - r x)\bigr], \qquad (c, r)\in\mathbb{Z}_p^2. \tag{2.1}
\]

**Theorem 3 (General All-Chirp Operator Identities and Unified Branch I / Branch II Chirp Representations).**
1. **(General trilinear chirp identities for \(K_w\) and \(R_w\))**: For any functions \(v_1, v_2, w\) on \(\mathbb{Z}_p\) (\(p>3\)) with real \(w\):
   \[
   \begin{aligned}
   \langle v_1, K_w v_2\rangle_p &= \sum_{c,r\in\mathbb{Z}_p} \overline{Q_{v_1}(c,r)}\,Q_{v_2}(c,r)\,|Q_w(3c,3r)|^2 - \langle v_1,v_2\rangle_p\,\|w\|_2^2 + \frac{1}{p}\mathbb{E}_x\bigl[\overline{v_1(x)}v_2(x)w(x)^2\bigr], \\
   \langle v_1, R_w v_2\rangle_p &= \sum_{c,r\in\mathbb{Z}_p} \overline{Q_{v_1}(3c,3r)}\,Q_{v_2}(3c,3r)\,|Q_w(c,r)|^2 - \langle v_1,v_2\rangle_p\,\|w\|_2^2 + \frac{1}{p}\mathbb{E}_x\bigl[\overline{v_1(x)}v_2(x)w(x)^2\bigr].
   \end{aligned} \tag{2.2}
   \]
2. **(Exact diagonal-free Branch I chirp identities for \(S_E\) and \(S_M\))**: For any 4-AP-free set \(A\subset\mathbb{Z}_p\) and any factor \(F\) (\(u = B - g,\ U = \mathbb{E}[u^2]\)), taking \(v_1 = u, v_2 = w = B\) in (2.2) cancels the \(\frac{1}{p}U\) diagonal identically and gives:
   \[
   \begin{aligned}
   a U - S_E &= \sum_{c,r\in\mathbb{Z}_p} \operatorname{Re}\bigl(\overline{Q_u(c,r)}\,Q_B(c,r)\bigr)\,|Q_B(3c,3r)|^2, \\
   a U - S_M &= \sum_{c,r\in\mathbb{Z}_p} \operatorname{Re}\bigl(\overline{Q_u(c,r)}\,Q_B(c,r)\bigr)\,|Q_B(c/3,r/3)|^2.
   \end{aligned} \tag{2.3}
   \]
3. **(Exact Branch II chirp identities for \(R_4\) and \(\langle h, K_u^{(3)}\rangle_p\))**:
   - Taking \(v_1 = v_2 = w = u\) in (2.2) gives
     \[
     R_4 = \Lambda_4(u,u,u,u) = \sum_{c,r\in\mathbb{Z}_p} |Q_u(c,r)|^2\,|Q_u(3c,3r)|^2 - U^2 + \frac{1}{p}\mathbb{E}_x[u(x)^4]. \tag{2.4}
     \]
   - Taking \(v_1 = h = g - a, v_2 = w = u\) in (2.2), since \(\langle h, u\rangle_p = 0\), **the baseline term \(-\langle h,u\rangle_p U\) vanishes identically**:
     \[
     \langle h, K_u^{(3)}\rangle_p = \sum_{c,r\in\mathbb{Z}_p} \operatorname{Re}\bigl(\overline{Q_h(c,r)}\,Q_u(c,r)\bigr)\,\Bigl(|Q_u(3c,3r)|^2 + |Q_u(c/3,r/3)|^2\Bigr) + \frac{2}{p}\mathbb{E}_x\bigl[h(x)u(x)^3\bigr], \tag{2.5}
     \]
     and its \(c = 0\) (linear Fourier) part is bounded unconditionally by \(2\rho^2\sqrt{v U} = O(a^{33/8}\ell(a)) = o(a^4)\) under `SELECT` failure and \(v \le \zeta a^{9/4}\), without any \(\ell^1\) assumption on \(\widehat{h}\)!

---

## Phase 3 & Phase 5 — Comparison of Architecture A (Linear Quarter-Arc) vs Architecture B (Quadratic Factor / Subprogression)

We prove an elementary Gauss-sum theorem explaining why Architecture A (linear coordinate windows) closes the iteration ledger (`NEW_RESULTS_20261002.md`), whereas Architecture B (quadratic coordinate windows or subprogression linearization) encounters two structural obstructions:

**Theorem 4 (Quadratic Window Translation-Mixing Obstruction & Architecture Comparison).**
Let \(p>3\) be prime, \(c \in \mathbb{Z}_p\setminus\{0\}\), \(r\in\mathbb{Z}_p\), \(I\subset\mathbb{Z}_p\) be a residue interval of density \(w = |I|/p\), and \(\Omega_{\text{quad}} := \{x\in\mathbb{Z}_p : c x^2 + r x \bmod p \in I\}\). Then:
1. **(Universal translation mixing for every nonzero shift \(h\ne 0\))**: For **every** \(h \in \mathbb{Z}_p\setminus\{0\}\),
   \[
   \Bigl|\frac{|\Omega_{\text{quad}} \cap (\Omega_{\text{quad}} + h)|}{p} - w^2\Bigr| \le \frac{\|\widehat{1_I}\|_{\ell^1(\mathbb{Z}_p)}^2 - w}{\sqrt{p}} \le \frac{(2 + \log p)^2}{\sqrt{p}}, \tag{3.1}
   \]
   and consequently the relative boundary loss under **every** nonzero cyclic shift \(h\ne 0\) is at least:
   \[
   \frac{|\Omega_{\text{quad}} \setminus (\Omega_{\text{quad}} + h)|}{|\Omega_{\text{quad}}|} \ge 1 - w - O\bigl(w^{-1} p^{-1/2}\log^2 p\bigr) \ge \frac{3}{4} - o(1) \qquad (\text{for } w \le 1/4). \tag{3.2}
   \]
2. **(Comparison of Architectures A and B)**:

| Feature | Architecture A (Linear Quarter-Arc Windows) | Architecture B1 (Quadratic Phase Linearized on Subprogression) | Architecture B2 (Pure Quadratic Arc Windows \(\Omega_{\text{quad}}\)) |
| --- | --- | --- | --- |
| **4-AP Second Difference** | \(\xi x - 2\xi(x+d) + \xi(x+2d) = 0\) (identically zero) | Zero on subprogression | \(q(x) - 2q(x+d) + q(x+2d) = 2cd^2 \ne 0\) |
| **Per-Step Size Loss \(\log(n/n')\)** | \(O(M(a) + \log(1/(\eta a))) = O(a^{-1/4}/\ell(a))\) | \(\ge \frac{1}{2}\log n - O(\log(a/\delta(a)))\) (loses half of \(\log n\) in 1 step!) | \(O(\log(a/\delta(a)^2))\) |
| **Max Steps Before Exhausting \(\log N\)** | \(O(t^{-1/2}/\ell(t))\) rank & log-loss over \(O(t^{-1/4}\ell(t))\) steps | At most \(O(\log\log N)\) steps (`RELATIVE_WINDOWS.md` `(29)`) | Cannot use endpoint mod-3 label baseline \(w^2/3^d\) |
| **Terminal Packing Contradiction** | \(\exists h\ne 0\) with \(|\Omega\setminus(\Omega+h)|/|\Omega| \le d p^{1-1/d}/n \to 0 \implies \text{dens} \le 3/4+o(1)\) | Valid on interval, but density grows by only \(O(a_0\log\log N) = o(1)\) | **Fails**: \(\forall h\ne 0\), \(|\Omega_{\text{quad}}\setminus(\Omega_{\text{quad}}+h)|/|\Omega_{\text{quad}}| \ge 1-w \ge 3/4-o(1)\) by (3.2) |

*Proof of (3.1).* Expand \(1_I(q(x))1_I(q(x+h)) = \sum_{k_1,k_2\in\mathbb{Z}_p}\widehat{1_I}(k_1)\widehat{1_I}(k_2)e_p\bigl(c(k_1+k_2)x^2 + [2ck_2 h + r(k_1+k_2)]x + k_2(ch^2+rh)\bigr)\). The \((0,0)\) term is \(w^2\). For \(k_1+k_2 \equiv 0\pmod p\) with \(k_2\ne 0\), the \(x^2\) coefficient vanishes and the linear frequency is \(2ck_2 h \not\equiv 0\pmod p\) (since \(p>3,\ c\ne 0,\ k_2\ne 0,\ h\ne 0\)), so the \(x\)-average is **identically zero**! Those omitted terms have \(\ell^1\) weight \(\sum_{k\ne 0}|\widehat{1_I}(k)|^2 = w - w^2\). Every remaining term has \(k_1+k_2 \not\equiv 0\pmod p\), so its normalized quadratic Gauss sum in \(x\) has modulus \(p^{-1/2}\). Summing the remaining \(\ell^1\) weights gives \((\|\widehat{1_I}\|_{\ell^1}^2 - w)/\sqrt{p}\). \(\square\)

---

## Verification Summary (`verify_quadratic_two_branch_20261014.py`)
Run `python3 verify_quadratic_two_branch_20261014.py` (outputs `QUADRATIC_TWO_BRANCH_VERIFICATION_20261014.json`):
- **10** exact rational fourth-power trace checks (`\operatorname{tr}(K_u^4) = \operatorname{tr}(R_u^4) = \mathbb{E}[F_u(2h,k)F_u(h,2k)] \le \|u\|_{U^3}^8`) and **25** exact rational validity-polynomial checks (`a^2 - U(U+4v) = a^3(2-a)-2a(1-a)v+3v^2`);
- **2,247** verifications of the diagonal-free Branch I all-chirp identities (2.3) and **2,247** verifications of the zero-baseline Branch II all-chirp identities (2.4)–(2.5), plus **16** global-law orbit checks on \(\mathbb{Z}_{23}, \mathbb{Z}_{29}\);
- **3** quadratic-window translation-mixing checks (`p=53, 101, 257`) confirming (3.1)–(3.2).
