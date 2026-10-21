# Arithmetic Resonance, Single-Variable \(R_{2,(1)}\) Repair, and ANOVA Cubic Damping — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with exact Phase 0/Phase 6 repair of \(R_{2,(1)}\) and \(R_{2,(2)}\) via \(\rho^2\), exact continuum constant \(4/27\) for 1D Walsh cubic completion, rigorous weight-\(k\) ANOVA Fourier cap \((8/\pi^2)^k\) on \(\mathbb{T}^d\) and dissociated factors, and resonant-factor rank reduction).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, `COLLECTIVE-WSELECT`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 & Phase 6 — Audit of the \(R_2\) Scale Gap and Exact Single-Variable Repair of \(R_{2,(1)}\)

### 0.1 Audit of the October 14 \(R_2\) Estimate
In `CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md` Theorem 3 (`(8.1)`–`(8.2)`), we decomposed \(R_2 = R_{2,(1)} + R_{2,(2)}\) on \(\mathbb{Z}_p\) (using \(g=a+h\)) and bounded:
\[
|R_{2,(1)}| \le 12a\rho\sqrt{Uv}, \qquad |R_{2,(2)}| \le 6\rho\sqrt{Uv}\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}.
\]
As the prompt notes: under `SELECT` failure (\(\rho \le \sqrt{c}a^{5/4}\sqrt{\ell(a)}\)) and \(v \le \zeta a^{9/4}\), we have \(\rho\sqrt{Uv} = O(a^{5/4 + 1/2 + 9/8}\sqrt{\ell(a)}) = O(a^{23/8}\sqrt{\ell(a)})\). Therefore:
- Multiplying by \(2a\) gives \(12a\rho\sqrt{Uv} = O(a^{31/8}\sqrt{\ell(a)})\), which is **larger than \(a^4\)** as \(a \to 0\) (since \(31/8 = 3.875 < 4\)) regardless of how small \(\|\widehat{h}\|_{\ell^1}\) is!
- Why did `SELECT_ALGEBRA_20261002.md` and `CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md` lose a power of \(a\) in \(R_{2,(1)}\) and \(R_{2,(2)}\)? Because both \(R_{2,(1)}\) and \(R_{2,(2)}\) have **TWO factors of \(u\)**, whereas the old bound bounded only ONE factor of \(\widehat{u}\) by \(\rho\) and bounded the second factor of \(\widehat{u}\) in \(\ell^2\) by \(\sqrt{U} \sim a^{1/2}\)!

### 6.1 Exact Single-Variable Fourier Formula for \(R_{2,(1)}\) and \(\rho^2\) Repair of \(R_2\) — PROVED
In each of the 12 terms of \(R_{2,(1)}\), two slots carry \(u\), one slot carries \(h\), and the fourth slot carries the constant \(a\)! Because one slot is constant, the 4-AP average \(\mathbb{E}_{x,d}\) reduces to a **three-point configuration** of \((u, u, h)\), whose Fourier expansion is a **single-variable frequency sum** over \(t\in\mathbb{Z}_p\setminus\{0\}\)!

**Theorem 1 (Exact Single-Variable Fourier Formula for \(R_{2,(1)}\) and \(\rho^2\)-Bounds on \(R_{2,(1)}, R_{2,(2)}\)).**
On \(\mathbb{Z}_p\) (\(p>3\)) with \(g = a + h\) (\(\widehat{u}(0)=\widehat{h}(0)=0\)):
1. **(Exact single-variable Fourier identity for \(R_{2,(1)}\))**:
   Grouping the 12 terms of \(R_{2,(1)}\) into the 6 terms where the constant \(a\) is at an endpoint slot \(\{0,3\}\) (leaving a 3-AP on the remaining three slots) and the 6 terms where \(a\) is at an interior slot \(\{1,2\}\) (leaving a \((1,3)\)-triple on \(\{0,1,3\}\) or \(\{0,2,3\}\)), we have the exact identity:
   \[
   \begin{aligned}
   R_{2,(1)} = 2a \operatorname{Re} \sum_{t\in\mathbb{Z}_p\setminus\{0\}} \Bigl[
     &\widehat{u}(t)^2\widehat{h}(-2t) + 2\widehat{u}(t)\widehat{u}(-2t)\widehat{h}(t) \\
     &+ \widehat{u}(2t)\widehat{u}(-3t)\widehat{h}(t) + \widehat{u}(2t)\widehat{u}(t)\widehat{h}(-3t) + \widehat{u}(-3t)\widehat{u}(t)\widehat{h}(2t)
   \Bigr].
   \end{aligned} \tag{1.1}
   \]
2. **(Improved \(\rho^2\) bound on \(R_{2,(1)}\))**: Bounding both factors of \(\widehat{u}\) in (1.1) by \(\rho = \max_{\xi\ne 0}|\widehat{u}(\xi)|\) and summing \(|\widehat{h}|\) over the bijective multiples \(\{-2t, t, -3t, 2t\}\) gives:
   \[
   \boxed{|R_{2,(1)}| \le 12a\,\rho^2\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}.} \tag{1.2}
   \]
   Under `SELECT` failure (\(\rho^2 \le c a^{5/2}\ell(a)\)), (1.2) yields:
   \[
   |R_{2,(1)}| \le 12c\, a^{7/2}\ell(a)\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)} \qquad \bigl(\text{improving } O(a^{31/8}\sqrt{\ell}) \text{ whenever } \|\widehat{h}\|_{\ell^1} = o(a^{3/8}/\sqrt{\ell})\bigr), \tag{1.3}
   \]
   and in particular \(|R_{2,(1)}| = o(a^4)\) whenever \(\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)} = o\bigl(a^{1/2}/\ell(a)\bigr)\)!
3. **(Improved \(\rho^2\) bound on \(R_{2,(2)}\))**: In each of the 6 terms of \(R_{2,(2)} = \sum_{|I|=2}\Lambda_4(u\text{ on }I, h\text{ on }I^c)\), the Fourier sum is indexed by two independent frequencies \((r,s)\in\mathbb{Z}_p^2\). Bounding both factors of \(\widehat{u}\) by \(\rho\) and summing the two factors of \(\widehat{h}\) independently over \(\mathbb{Z}_p^2\) gives:
   \[
   \boxed{|R_{2,(2)}| \le 6\,\rho^2\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}^2,} \tag{1.4}
   \]
   and combining (1.2), (1.4), and `CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md` `(8.1)` gives:
   \[
   \boxed{|R_2| \le 12a\,\rho\,\min\bigl(\sqrt{Uv},\ \rho\|\widehat{h}\|_{\ell^1}\bigr) + 6\,\rho\,\|\widehat{h}\|_{\ell^1}\,\min\bigl(\sqrt{Uv},\ \rho\|\widehat{h}\|_{\ell^1}\bigr).} \tag{1.5}
   \]
   *(Verified in exact rational and Fourier arithmetic across 1,498 subset/factor cases on \(\mathbb{Z}_7,\mathbb{Z}_{11}\) and 12 global-law orbits on \(\mathbb{Z}_{23},\mathbb{Z}_{29}\) in `verify_cubic_resonance_20261014.py`.)*

---

## Phase 1, Phase 2, Phase 3 & Phase 4 — Exact Resonance Geometry, Dissociated-Factor ANOVA Damping, and Resonant Alternative

### 1.1 Exact Fourier Resonance Geometry on a Rank-\(d\) Quarter Factor
Let \(F\) be a rank-\(d\) quarter-arc factor on \(\mathbb{Z}_p\) with generator tuple \(\Xi = (\xi_1,\dots,\xi_d)\in(\mathbb{Z}_p\setminus\{0\})^d\) and rotations \(\theta_1,\dots,\theta_d\in\mathbb{R}/\mathbb{Z}\). Every function \(h\) measurable with respect to \(F\) is the pullback \(h(x) = G(\xi_1 x/p - \theta_1,\dots,\xi_d x/p - \theta_d)\) of a step function \(G\) on \(\mathbb{T}^d = (\mathbb{R}/\mathbb{Z})^d\) constant on the \(4^d\) quarter-cubes \(C_\omega = \prod_{j=1}^d [\omega_j/4, (\omega_j+1)/4)\), \(\omega\in\{0,1,2,3\}^d\).
On \(\mathbb{T}^d\), \(G\) has the exact Fourier series \(G(y) = \sum_{m\in\mathbb{Z}^d} \widehat{G}(m) e(m\cdot y)\), where for each \(m\in\mathbb{Z}^d\) its support set (coordinate Hamming weight) is
\[
S(m) := \{j\in\{1,\dots,d\} : m_j \ne 0\}, \qquad \operatorname{wt}(m) := |S(m)|. \tag{2.1}
\]
Under the pullback \(y_j = \xi_j x/p - \theta_j\), a torus mode \(m\in\mathbb{Z}^d\) maps to the cyclic frequency \(\lambda(m) := \sum_{j=1}^d m_j \xi_j \bmod p\). Consequently, in the cubic completion transforms \(K_{E,h}(t)\) and \(K_{M,h}(t)\), a triple of torus modes \((m^{(1)}, m^{(2)}, m^{(3)})\in(\mathbb{Z}^d)^3\) contributes to frequency \(t = \lambda(m^{(1)}+m^{(2)}+m^{(3)})\) whenever:
\[
\begin{aligned}
\text{(Endpoint } E\text{)}:\quad & \lambda\bigl(m^{(1)} + 2m^{(2)} + 3m^{(3)}\bigr) \equiv 0 \pmod p, \\
\text{(Interior } M\text{)}:\quad & \lambda\bigl(-m^{(1)} + m^{(2)} + 2m^{(3)}\bigr) \equiv 0 \pmod p.
\end{aligned} \tag{2.2}
\]
We classify solutions of (2.2) into two exact regimes:
1. **True Torus Resonances (Dissociated Regime)**:
   \(m^{(1)} + 2m^{(2)} + 3m^{(3)} = 0\) in \(\mathbb{Z}^d\) (for \(E\)), or \(-m^{(1)} + m^{(2)} + 2m^{(3)} = 0\) in \(\mathbb{Z}^d\) (for \(M\)). Here the relation holds coordinate-by-coordinate in every \(j\in\{1,\dots,d\}\).
2. **Modular Aliasing Collisions (Resonant Regime)**:
   The integer vector \(n := m^{(1)} + 2m^{(2)} + 3m^{(3)} \in \mathbb{Z}^d\) is **nonzero** in \(\mathbb{Z}^d\), but \(\sum_{j=1}^d n_j \xi_j \equiv 0 \pmod p\). If \(|m^{(i)}|_\infty \le L\), then \(0 < |n|_\infty \le 6L\).

### 2.1 Rigorous Multilinear ANOVA Decomposition and Weight-\(k\) Damping Theorem — PROVED
On the torus \(\mathbb{T}^d\) with uniform Haar measure \(\mu_{\mathbb{T}^d}\) (under which each quarter-cube \(C_\omega\) has measure \(4^{-d}\) and the \(d\) coordinates \(y_1,\dots,y_d\) are exactly independent), decompose \(G = \sum_{S\subset\{1,\dots,d\}} G_S\) into its orthogonal ANOVA components:
\[
G_S(y) := \sum_{m\in\mathbb{Z}^d:\, S(m)=S} \widehat{G}(m)\,e(m\cdot y)
= \sum_{T\subset S} (-1)^{|S\setminus T|} \mathbb{E}_{\mathbb{T}^d}\bigl[G \mid (y_j)_{j\in T}\bigr], \tag{2.3}
\]
so \(\mathbb{E}_{\mathbb{T}^d}[G_S(y)\mid (y_j)_{j\in S\setminus\{i\}}] = 0\) for every \(i\in S\), and \(\|G\|_{L^2(\mathbb{T}^d)}^2 = \sum_S \|G_S\|_{L^2(\mathbb{T}^d)}^2\).

**Theorem 2 (Exact Weight-\(k\) ANOVA Fourier Cap and Continuum \(4/27\) Walsh Constant).**
1. **(Universal weight-\(k\) Fourier cap)**: For every \(S\subset\{1,\dots,d\}\) with \(|S|=k\ge 1\) and every \(m\in\mathbb{Z}^d\) with \(S(m)=S\), the Fourier coefficient of the quarter-step ANOVA component \(G_S\) satisfies:
   \[
   |\widehat{G_S}(m)|^2 \le \|G_S\|_{L^2(\mathbb{T}^d)}^2 \prod_{j\in S} (4w(m_j)) \le \left(\frac{8}{\pi^2}\right)^k \|G_S\|_{L^2(\mathbb{T}^d)}^2, \qquad 4w(m_j) = \frac{16\sin^2(\pi m_j/4)}{\pi^2 m_j^2}. \tag{2.4}
   \]
2. **(Dissociated weight-\(k\) cubic damping on \(\mathbb{Z}_p\))**: Suppose \(\Xi = (\xi_1,\dots,\xi_d)\) is \(6L\)-dissociated modulo \(p\), meaning that \(\sum_{j=1}^d n_j \xi_j \equiv 0 \pmod p\) with \(|n|_\infty \le 6L\) implies \(n = 0\in\mathbb{Z}^d\). Let \(G_S^{(L)}(x) = \sum_{m:\, S(m)=S,\, |m|_\infty\le L} \widehat{G_S}(m)e(-m\cdot\theta)e_p(\lambda(m)x)\). Then:
   - The modes \(\{\lambda(m) : S(m)=S,\, |m|_\infty\le L\}\) are distinct modulo \(p\), so \(\|G_S^{(L)}\|_{L^2(\mathbb{Z}_p)}^2 \le \|G_S\|_{L^2(\mathbb{T}^d)}^2\).
   - Every cubic completion coefficient of \(G_S^{(L)}\) on \(\mathbb{Z}_p\) is exponentially damped in \(k = |S|\):
     \[
     \max_{t\in\mathbb{Z}_p} |K_{E,G_S^{(L)}}(t)| \le \left(\frac{8}{\pi^2}\right)^{k/2} \|G_S\|_{L^2(\mathbb{T}^d)}^3, \qquad
     \max_{t\in\mathbb{Z}_p} |K_{M,G_S^{(L)}}(t)| \le \left(\frac{8}{\pi^2}\right)^{k/2} \|G_S\|_{L^2(\mathbb{T}^d)}^3. \tag{2.5}
     \]
3. **(Exact continuum \(4/27\) constant for \(k\)-fold Walsh products)**:
   For the 1D alternating quarter-step Walsh basis mode \(b_1(\theta) = (-1)^{\lfloor 4\theta\rfloor}\) on \(\mathbb{R}/\mathbb{Z}\) (\(\|b_1\|_{L^2(\mathbb{T})}=1\)), the continuum cubic completion \(C_E(b_1,b_1,b_1)(\theta) = \int_0^1 b_1(\theta+\phi)b_1(\theta+2\phi)b_1(\theta+3\phi)\,d\phi\) has exact \(L^2\) norm squared
   \[
   \|C_E(b_1,b_1,b_1)\|_{L^2(\mathbb{T})}^2 = \frac{4}{27} = 0.148148\dots \qquad \left(\text{and }\frac{4}{27} + \frac{64}{3N^2}\text{ on a discrete }N\text{-grid, } 48\mid N\right). \tag{2.6}
   \]
   Consequently, for any \(6L\)-dissociated \(k\)-fold Walsh product \(W_S(x) = \sqrt{v}\prod_{j\in S} b_1(\xi_j x/p)\), its continuum limit satisfies \(\|C_E(W_S,W_S,W_S)\|_2^2 = (4/27)^k v^3\).
   **Crucial distinction**: For a *general* weight-\(k\) ANOVA component \(G_S\) (which is a linear combination of up to \(3^k\) Walsh tensor products on \(S\)) or for a sum of \(k=1\) coordinate modes \(\sum_{j=1}^d G_{\{j\}}(\xi_j x/p)\), the \(L^2\) norm \(\|C_E(G_S,G_S,G_S)\|_2^2\) is bounded universally by \(\|G_S\|_2^6\) (Theorem 1(1) of `CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md`), whereas its *individual* Fourier coefficients are damped by \((8/\pi^2)^{k/2}\) (`(2.5)`). We do not extrapolate \((4/27)^k\) to non-product sums.

*Proof of (2.4)–(2.5).* On \(\mathbb{T}^k\), \(G_S(y_S) = \sum_{\omega\in\{0,1,2,3\}^k} g_\omega \prod_{j\in S} \chi_{\omega_j}(y_j)\) with \(\|G_S\|_{L^2(\mathbb{T}^k)}^2 = 4^{-k}\sum_\omega g_\omega^2\). For \(S(m)=S\), \(\widehat{G_S}(m) = \sum_\omega g_\omega \prod_{j\in S} c_{\omega_j,m_j}\). Cauchy–Schwarz over \(\omega\in\{0,1,2,3\}^k\) gives \(|\widehat{G_S}(m)|^2 \le (4^{-k}\sum_\omega g_\omega^2)(4^k \sum_\omega \prod_{j\in S}|c_{\omega_j,m_j}|^2) = \|G_S\|_2^2 \prod_{j\in S}(4w(m_j)) \le (8/\pi^2)^k \|G_S\|_2^2\). Under \(6L\)-dissociation, \(\lambda(m)\) is injective on \([-L,L]^d\), so \(\max_\xi |\widehat{G_S^{(L)}}(\xi)| \le (8/\pi^2)^{k/2}\|G_S\|_2\) and \(\|G_S^{(L)}\|_{L^2(\mathbb{Z}_p)} \le \|G_S\|_2\); applying `CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md` Theorem 1(2) (`|K_{E,f}(t)|\le \rho_f \|f\|_2^2`) proves (2.5). \(\square\)

### 3.1 The Resonant Factor Alternative (Phase 3 — PROVED)
What if \(\Xi = (\xi_1,\dots,\xi_d)\) **fails** \(M\)-dissociation modulo \(p\) (for an integer threshold \(M \ge 1\))? Then there exists a nonzero integer vector \(n = (n_1,\dots,n_d)\in\mathbb{Z}^d\) with \(0 < |n|_\infty \le M\) such that
\[
\sum_{j=1}^d n_j \xi_j \equiv 0 \pmod p. \tag{3.1}
\]

**Theorem 3 (Resonant Factor Reduction and Diophantine Phase Locking).**
Suppose \(\Xi = (\xi_1,\dots,\xi_d)\) satisfies (3.1) with \(0 < |n|_\infty \le M\), and pick an index \(r\in\{1,\dots,d\}\) with \(q := |n_r| \ge 1\).
1. **(Exact frequency span collapse)**: Every integer combination \(m\in[-L,L]^d\) satisfies
   \[
   q\,\lambda(m) \equiv \sum_{j\ne r} (q m_j - m_r n_j)\xi_j \pmod p. \tag{3.2}
   \]
   Thus the entire rank-\(d\) frequency box \(\Lambda_L(\Xi)\) is contained in the \(q^{-1}\pmod p\) scaling of the **rank-\((d-1)\) box** of side \((d+1)ML\) generated by \(\Xi\setminus\{\xi_r\}\):
   \[
   \bigl|\Lambda_L(\Xi)\bigr| \le (2L+1)\,\bigl|\Lambda_{dML}(\Xi\setminus\{\xi_r\})\bigr| \le (2L+1)\bigl(2dML+1\bigr)^{d-1}. \tag{3.3}
   \]
2. **(Low-order phase locking on narrow windows)**: If \(\Omega\) is a narrow coordinate window where \(\xi_j x \bmod p\) lies in an interval of diameter \(D_j\) for \(j\in S(n)\), then for every \(x\in\Omega\) the integer \(\sum_{j=1}^d n_j \operatorname{lift}(\xi_j x)\) is a multiple of \(p\) of absolute value \(\le \sum_j |n_j| D_j\), so it takes at most \(1 + 2M\sum_{j\in S(n)} D_j/p \le 1 + \frac{2}{3}Md\) possible integer values on \(\Omega\)!

---

## Phase 5, Phase 7, Phase 8 & Phase 10 — Synthesis of the Three Branches and Exact Remaining Gap

Combining Theorem 1 (`(1.2)`–`(1.5)`) with `CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md` Theorem 1 (`(4.1)`) gives a unified \(\ell^1\)-Fourier control of **both** \(R_1\) (Branch III) and \(R_2\) (Branch II) on \(\mathbb{Z}_p\):

**Theorem 4 (Simultaneous Elimination of Branch III and \(R_2\) Error in Branch II under Factor \(\ell^1\) Control).**
On \(\mathbb{Z}_p\) (\(p>3\)), let \(A\) be 4-AP-free with \(pa^3\ge 8\), let \(g = a+h = \mathbb{E}[1_A\mid F]\) satisfy \(v = \mathbb{E}[h^2] \le \zeta a^{9/4}\), and assume `SELECT` fails (\(\rho = \max_{\xi\ne 0}|\widehat{u}(\xi)| \le \sqrt{c}a^{5/4}\sqrt{\ell(a)}\)). Then:
\[
\begin{aligned}
|R_1| &\le 4\rho v\bigl(3a + \|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}\bigr) \le 4\sqrt{c}\zeta\,a^{7/2}\sqrt{\ell(a)}\,\bigl(3a + \|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}\bigr), \\
|R_2| &\le 6\rho^2\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}\bigl(2a + \|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}\bigr) \le 6c\,a^{5/2}\ell(a)\,\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}\bigl(2a + \|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)}\bigr).
\end{aligned} \tag{5.1}
\]
Consequently:
1. If \(\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)} = o\bigl(a^{1/2}/\sqrt{\ell(a)}\bigr)\), then \(|R_1| = o(a^4)\) and **Branch III is impossible**.
2. If \(\|\widehat{h}\|_{\ell^1(\mathbb{Z}_p)} = o\bigl(a^{1/2}/\ell(a)\bigr)\) (for instance, if \(h\) is approximated on a frequency set of size \(|\Lambda| = o(a^{-5/4}/\ell(a)^2)\), since \(\|\widehat{h_\Lambda}\|_{\ell^1} \le \sqrt{|\Lambda|v} \le \sqrt{\zeta|\Lambda|}a^{9/8}\)), then **both \(|R_1| = o(a^4)\) AND \(|R_2| = o(a^4)\) hold simultaneously**!
3. Under \(|R_1| = o(a^4)\) and \(|R_2| = o(a^4)\), the three-way dichotomy on \(\mathbb{Z}_p\) collapses to the **exact two-branch positive dichotomy at every intermediate factor \(F\)**:
   - **Branch I**: \(S_E + S_M \ge \frac{1}{2}a^4 - o(a^4)\), or
   - **Branch II**: \(R_3 \le -3a^4 + o(a^4)\) and \(R_4 = \Lambda_4(u) \ge 2a^4 - o(a^4)\) (forcing \(\max_{\xi\ne 0}|\widehat{u}(\xi)|^2 \ge \frac{9}{16}a^4\) when \(h\) is small).

### Verification Summary (`verify_cubic_resonance_20261014.py`)
Run `python3 verify_cubic_resonance_20261014.py` (outputs `CUBIC_RESONANCE_VERIFICATION_20261014.json`):
- **1,498** exact rational verifications of \(R_2 = R_{2,(1)} + R_{2,(2)}\) and **1,498** verifications of the single-variable Fourier formula (1.1) and the new \(\rho^2\) bounds \(|R_{2,(1)}| \le 12a\rho^2\|\widehat{h}\|_{\ell^1}\) and \(|R_{2,(2)}| \le 6\rho^2\|\widehat{h}\|_{\ell^1}^2\);
- **100** random tensor checks of the ANOVA weight-\(k\) Fourier cap \(|\widehat{G_S}(m)|^2 \le (8/\pi^2)^k \|G_S\|_2^2\) (`k=1..4`);
- **3** exact rational continuum limit checks confirming \(\|C_E(b_1,b_1,b_1)\|_2^2 = \frac{4}{27} + \frac{64}{3N^2}\) on grids \(N=48, 96, 192\);
- **3** dissociated vs resonant generator tests on \(\mathbb{Z}_{257}\) and **12** global-law orbit checks on \(\mathbb{Z}_{23}, \mathbb{Z}_{29}\).

### Corrected Continuation Prompt

> Continue offline from `CUBIC_RESONANCE_ATTACK_20261014.md` and `CUBIC_RESONANCE_VERIFICATION_20261014.json`. Accept as proved:
> 1. **Single-Variable \(R_{2,(1)}\) Formula and \(\rho^2\)-Bounds on \(R_2\) (Theorem 1 & Theorem 4)**: Because one slot in \(R_{2,(1)}\) is the constant \(a\), \(R_{2,(1)}\) is a single-variable Fourier sum satisfying \(|R_{2,(1)}| \le 12a\rho^2\|\widehat{h}\|_{\ell^1} = O(a^{7/2}\ell(a)\|\widehat{h}\|_{\ell^1})\), and \(|R_{2,(2)}| \le 6\rho^2\|\widehat{h}\|_{\ell^1}^2 = O(a^{5/2}\ell(a)\|\widehat{h}\|_{\ell^1}^2)\). Thus under `SELECT` failure and \(v \le \zeta a^{9/4}\), \(\|\widehat{h}\|_{\ell^1} = o(a^{1/2}/\ell(a))\) makes **both \(|R_1| = o(a^4)\) and \(|R_2| = o(a^4)\) simultaneously**, eliminating Branch III and the \(R_2\) error in Branch II.
> 2. **Weight-\(k\) ANOVA Damping and Continuum \(4/27\) Constant (Theorem 2 & Theorem 3)**: On \(\mathbb{T}^d\), every weight-\(k\) ANOVA component \(G_S\) has \(|\widehat{G_S}(m)|^2 \le (8/\pi^2)^k \|G_S\|_2^2\), and the 1D Walsh basis mode has exact continuum cubic completion norm \(\|C_E(b_1,b_1,b_1)\|_2^2 = 4/27\).
>
> Attack the two remaining problems:
> - **Problem 1 (Replacing \(g = \mathbb{E}_\Omega[B\mid F]\) by a smoothed low-\(\ell^1\) factor proxy \(\tilde{g}\))**: Since sharp quarter-arc step functions have discontinuous jumps (making \(\|\widehat{h}\|_{\ell^1}\) logarithmically large on each coordinate and product-large across \(d\) coordinates), replace the sharp conditional expectation \(g\) in the multilinear expansion \(B = \tilde{g} + \tilde{u}\) by a smoothed proxy \(\tilde{g}\) with controlled \(\|\widehat{\tilde{h}}\|_{\ell^1} = o(a^{1/2}/\ell(a))\) so Theorem 4 applies directly.
> - **Problem 2 (Multi-frequency amplification from \(a^4\) to \(|\Gamma|a^{5/2}R(a)\))**: In Branches I and II, prove that 4-AP exclusion \(B q_E = B q_M = 0\) and Booleanity force a character packet \(\Gamma\) of size \(\le M(a)\) to capture regularized Gram energy \(\ge c|\Gamma|a^{5/2}\log\log(e^2/a)\).
