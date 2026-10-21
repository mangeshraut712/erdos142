# Operator Block Decomposition, Cross/Complement Cancellation, and Dual Schur Certificates — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM.**
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## 1. Exact Block Decomposition of \(K = K_B + R_B\) (Phase 2 — PROVED)

Let \(p>3\) be prime, \(\Omega\subset\mathbb{Z}_p\) have size \(n=wp\), \(A\subset\Omega\) be cyclically 4-AP-free for nonzero differences, \(B=1_A\), \(F\) be a partition of \(\Omega\), \(g=\mathbb{E}_\Omega[B\mid F]\), and \(u=B-g\) (all extended by zero outside \(\Omega\)).
On \(\mathbb{Z}_p\) with normalized inner product \(\langle f_1,f_2\rangle_p = \mathbb{E}_x[\overline{f_1(x)}f_2(x)]\), recall the endpoint and interior completion operators:
\[
(K_B h)(x) = \mathbb{E}_y B\bigl((2x+y)/3\bigr)B\bigl((x+2y)/3\bigr)h(y), \qquad
(R_B h)(x) = \mathbb{E}_y B(2x-y)B(2y-x)h(y),
\]
and set \(K := K_B + R_B\). Let \(P\) be pointwise multiplication by \(1_A = B\) and \(Q\) be pointwise multiplication by \(1_{\Omega\setminus A} = 1_\Omega - B\). Decompose the residual \(u = u_A + u_C\) into its occupied and complement components:
\[
u_A := P u = (1-g)1_A, \qquad u_C := Q u = -g 1_{\Omega\setminus A}. \tag{1.1}
\]
Because \(u\) is supported on \(\Omega = A \sqcup (\Omega\setminus A)\), \(u_A\) and \(u_C\) have disjoint supports and
\[
\|u_A\|_p^2 = \frac{1}{p}\sum_{x\in A}(1-g(x))^2 = w\mathbb{E}_\Omega[g(1-g)^2] = w\bigl(U - \mathbb{E}_\Omega[g^2(1-g)]\bigr), \qquad
\|u_C\|_p^2 = w\mathbb{E}_\Omega[g^2(1-g)]. \tag{1.2}
\]

Expanding \(\langle u, K_B u\rangle_p\), \(\langle u, R_B u\rangle_p\), and \(\langle u, K u\rangle_p\) via \(u = u_A + u_C\) yields:
\[
\begin{aligned}
M_E := \langle u, K_B u\rangle_p &= \underbrace{\langle u_A, P K_B P u_A\rangle_p}_{\text{DIAG}_E} + \underbrace{2\langle u_A, P K_B Q u_C\rangle_p}_{\text{CROSS}_E} + \underbrace{\langle u_C, Q K_B Q u_C\rangle_p}_{\text{COMPLEMENT}_E}, \\
M_M := \langle u, R_B u\rangle_p &= \underbrace{\langle u_A, P R_B P u_A\rangle_p}_{\text{DIAG}_M} + \underbrace{2\langle u_A, P R_B Q u_C\rangle_p}_{\text{CROSS}_M} + \underbrace{\langle u_C, Q R_B Q u_C\rangle_p}_{\text{COMPLEMENT}_M}, \\
\langle u, K u\rangle_p &= \text{DIAG} + \text{CROSS} + \text{COMPLEMENT}.
\end{aligned} \tag{1.3}
\]

**Theorem 1 (Exact formulas and signs for DIAG, CROSS, and COMPLEMENT).**
For every cyclically 4-AP-free \(A\subset\Omega\) and every partition \(F\) of \(\Omega\):
1. **(Diagonal block `DIAG`)**: By 4-AP exclusion, \(P K_B P = \frac{1}{p}P\) and \(P R_B P = \frac{1}{p}P\), hence \(P K P = \frac{2}{p}P\) and
   \[
   \text{DIAG}_E = \text{DIAG}_M = \frac{1}{p}\|u_A\|_p^2 \ge 0, \qquad \text{DIAG} = \frac{2}{p}\|u_A\|_p^2 \ge 0. \tag{1.4}
   \]
2. **(Cross block `CROSS` — strictly nonpositive)**: Since \(u_A \ge 0\), \(u_C \le 0\), and \(K_B, R_B \ge 0\) entrywise, \(\text{CROSS}_E \le 0\) and \(\text{CROSS}_M \le 0\). Moreover, writing \(g_A := g 1_A\) so \(u_A = B - g_A\), and using \((Q K_B P 1_A)(y) = q_E(y)\) and \((Q R_B P 1_A)(y) = q_M(y)\) for every \(y\in\Omega\setminus A\) (because \(y\notin A\) eliminates the \(x=y\) diagonal automatically), we have
   \[
   \langle 1_A, K_B u_C\rangle_p = -\frac{1}{p}\sum_{y\in\Omega\setminus A} g(y)q_E(y) = -w S_E, \qquad
   \langle 1_A, R_B u_C\rangle_p = -\frac{1}{p}\sum_{y\in\Omega\setminus A} g(y)q_M(y) = -w S_M. \tag{1.5}
   \]
   Therefore:
   \[
   \begin{aligned}
   \text{CROSS}_E &= -2w S_E - 2\langle g_A, K_B u_C\rangle_p \le 0, \\
   \text{CROSS}_M &= -2w S_M - 2\langle g_A, R_B u_C\rangle_p \le 0, \\
   \text{CROSS} &= -2w(S_E + S_M) - 2\langle g_A, K u_C\rangle_p \le 0,
   \end{aligned} \tag{1.6}
   \]
   with \(0 \le -2\langle g_A, K_B u_C\rangle_p \le 2(\max_\Omega g)w S_E \le 2w S_E\) and \(0 \le -\text{CROSS} \le 2w(S_E + S_M)\).
3. **(Complement block `COMPLEMENT` — strictly nonnegative)**: Since \(u_C = -g 1_{\Omega\setminus A} = g - g_A\) and \(K_B, R_B \ge 0\) entrywise, \(\text{COMPLEMENT}_E = \langle u_C, K_B u_C\rangle_p \ge 0\) and \(\text{COMPLEMENT}_M = \langle u_C, R_B u_C\rangle_p \ge 0\). Expanding \(u_C = g - g_A\) and using \(\langle g, K_B g\rangle_p = D_{2,E}\), \(\langle g, R_B g\rangle_p = D_{2,M}\), and \(\langle g_A, K_B g_A\rangle_p = \langle g_A, R_B g_A\rangle_p = \frac{1}{p}\|g_A\|_p^2\) (by \(P K_B P = P R_B P = \frac{1}{p}P\)) gives:
   \[
   \begin{aligned}
   \text{COMPLEMENT}_E &= D_{2,E} + 2\langle g_A, K_B u_C\rangle_p - \frac{1}{p}\|g_A\|_p^2 \ge 0, \\
   \text{COMPLEMENT}_M &= D_{2,M} + 2\langle g_A, R_B u_C\rangle_p - \frac{1}{p}\|g_A\|_p^2 \ge 0, \\
   \text{COMPLEMENT} &= D_{2,E} + D_{2,M} + 2\langle g_A, K u_C\rangle_p - \frac{2}{p}\|g_A\|_p^2 \ge 0.
   \end{aligned} \tag{1.7}
   \]
4. **(Exact cancellation of `\langle g_A, K u_C\rangle_p` in `CROSS + COMPLEMENT`)**:
   Adding (1.6) and (1.7) cancels the unknown cross term \(2\langle g_A, K u_C\rangle_p\) **identically**:
   \[
   \boxed{\text{CROSS} + \text{COMPLEMENT} = D_{2,E} + D_{2,M} - 2w(S_E + S_M) - \frac{2}{p}\|g_A\|_p^2.} \tag{1.8}
   \]
   Since \(\|u_A\|_p^2 - \|g_A\|_p^2 = \frac{1}{p}\sum_{x\in A}[(1-g(x))^2 - g(x)^2] = \frac{1}{p}\sum_{x\in A}(1-2g(x)) = w(a - 2a^2 - 2v) = w(U - a^2 - v)\), adding \(\text{DIAG} = \frac{2}{p}\|u_A\|_p^2\) recovers the exact total:
   \[
   \langle u, K u\rangle_p = \text{DIAG} + \text{CROSS} + \text{COMPLEMENT} = D_{2,E} + D_{2,M} - 2w(S_E + S_M) + \frac{2w(U - a^2 - v)}{p}. \tag{1.9}
   \]

---

## 2. Exact Incidence & Fourier Structure of `PKQ` and `QKQ` (Phases 3 & 4 — PROVED)

### 2.1 Row and column degrees of the cross operators \(P K_B Q\) and \(P R_B Q\)
Write the unnormalized zero-diagonal matrices \(J_E(x,y) = 1_{x\ne y} B((2x+y)/3)B((x+2y)/3)\) and \(J_M(x,y) = 1_{x\ne y} B(2x-y)B(2y-x)\), so \(K_B = \frac{1}{p}(\operatorname{diag}(B) + J_E)\) and \(R_B = \frac{1}{p}(\operatorname{diag}(B) + J_M)\).
Because \(P \operatorname{diag}(B) Q = 0\) and \(P J_E P = P J_M P = 0\) (by 4-AP exclusion):
1. **Column sums on \(\Omega\setminus A\)**: For every \(y\in\Omega\setminus A\),
   \[
   \sum_{x\in A} J_E(x,y) = \sum_{x\in\mathbb{Z}_p} J_E(x,y)B(x) = H_E(y) = p\, q_E(y), \qquad
   \sum_{x\in A} J_M(x,y) = \sum_{x\in\mathbb{Z}_p} J_M(x,y)B(x) = H_M(y) = p\, q_M(y). \tag{2.1}
   \]
   That is why \((Q K_B P 1_A)(y) = q_E(y)\) and \((Q R_B P 1_A)(y) = q_M(y)\) hold pointwise on \(\Omega\setminus A\)!
2. **Row sums on \(A\)**: For every \(x\in A\), since \(J_E(x,y)=0\) and \(J_M(x,y)=0\) for all \(y\in A\), all nonzero entries in row \(x\in A\) lie in columns \(y\notin A\):
   \[
   d_E(x) := \sum_{y\notin A} J_E(x,y) = \sum_{y\in\mathbb{Z}_p} J_E(x,y), \qquad
   d_M(x) := \sum_{y\notin A} J_M(x,y) = \sum_{y\in\mathbb{Z}_p} J_M(x,y), \tag{2.2}
   \]
   where \(d_E(x) = \#\{d\ne 0: x+d, x+2d\in A\}\) is the number of 3-APs in \(A\) starting at \(x\), and \(d_M(x) = \#\{d\ne 0: x-d\in A,\ x+2d\in A\}\) is the number of \((1,3)\)-gapped triples in \(A\) with interior point \(x\).
3. **Exact trivial-factor specialization (`F` trivial on \(\mathbb{Z}_p\))**:
   When \(g \equiv a\) is constant on \(\mathbb{Z}_p\), \(g_A = a 1_A\) and \(u_A = (1-a)1_A\), so \(\langle g_A, K_B u_C\rangle_p = -a S_E\) and \(\langle g_A, R_B u_C\rangle_p = -a S_M\). Thus (1.6) and (1.7) simplify to the exact closed-form formulas:
   \[
   \begin{aligned}
   \text{CROSS}_E &= -2(1-a)S_E, \qquad \text{CROSS}_M = -2(1-a)S_M, \\
   \text{COMPLEMENT}_E &= D_{2,E} - 2a S_E - \frac{a^3}{p}, \qquad \text{COMPLEMENT}_M = D_{2,M} - 2a S_M - \frac{a^3}{p}.
   \end{aligned} \tag{2.3}
   \]
   In particular, eliminating \(S_E + S_M\) between \(\text{CROSS}\) and \(\text{COMPLEMENT}\) for the trivial factor gives the exact positive-combination identity:
   \[
   \boxed{(1-a)\text{COMPLEMENT} - a\,\text{CROSS} = (1-a)\left(D_{2,E} + D_{2,M} - \frac{2a^3}{p}\right).} \tag{2.4}
   \]

### 2.2 Exact Fourier formulas for `CROSS` and `COMPLEMENT`
Using the Fourier matrices \(\langle e_r, K_B e_s\rangle_p = b(2r+s)b(-r-2s)\) and \(\langle e_r, R_B e_s\rangle_p = b((2r-s)/3)b((r-2s)/3)\) (`TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` `(22)`), with \(\widehat{u_A}(r) = \mathbb{E}_x[u_A(x)e_p(-rx)]\) and \(\widehat{u_C}(s) = \mathbb{E}_x[u_C(x)e_p(-sx)]\):
\[
\begin{aligned}
\text{CROSS} &= 2\sum_{r,s\in\mathbb{Z}_p} \overline{\widehat{u_A}(r)}\,\widehat{u_C}(s) \Bigl[b(2r+s)b(-r-2s) + b\bigl((2r-s)/3\bigr)b\bigl((r-2s)/3\bigr)\Bigr], \\
\text{COMPLEMENT} &= \sum_{r,s\in\mathbb{Z}_p} \overline{\widehat{u_C}(r)}\,\widehat{u_C}(s) \Bigl[b(2r+s)b(-r-2s) + b\bigl((2r-s)/3\bigr)b\bigl((r-2s)/3\bigr)\Bigr].
\end{aligned} \tag{2.5}
\]

---

## 3. Exact Dual Schur Complement Inequalities on \(A^c\) (Phase 8 — PROVED)

Following `ENDPOINT_INCIDENCE_AUDIT.md` §3 (`(4)`) and `ROUTE_INCIDENCE_MOMENTS_20261002.md` §2 (`(3)`–`(4)`), both \(J_E\) and \(J_M\) arise from edge-vertex incidence matrices whose columns have support size \(2\):
- For \(J_E\): each ordered pair \((y_1,y_2)\in A^2\) (\(y_1\ne y_2\)) defines a column with \(1\)s at its two endpoints \(2y_1-y_2\) and \(2y_2-y_1\). Its Gram matrix is \(G_E = R_E R_E^T = \operatorname{diag}(2d_E(x)) + 2J_E\).
- For \(J_M\): each ordered pair \((y_0,y_3)\in A^2\) (\(y_0\ne y_3\)) defines a column with \(1\)s at its two interior trisection points \((2y_0+y_3)/3\) and \((y_0+2y_3)/3\). Its Gram matrix is \(G_M = R_M R_M^T = \operatorname{diag}(2d_M(x)) + 2J_M\).

Because \(A\) is 4-AP-free, **both** \(G_E[A,A] = \operatorname{diag}(2d_E(x) : x\in A)\) and \(G_M[A,A] = \operatorname{diag}(2d_M(x) : x\in A)\) are purely diagonal! Taking the Schur complement of the \(A\times A\) block onto \(A^c = \mathbb{Z}_p\setminus A\) and evaluating on \(u_C = -g 1_{\Omega\setminus A}\) yields:

**Theorem 2 (Dual Two-Channel Schur Complement Inequalities on \(A^c\)).**
For every cyclically 4-AP-free \(A\subset\Omega\) and every partition \(F\) of \(\Omega\):
\[
\begin{aligned}
\frac{1}{p^2}\sum_{\substack{x\in A\\d_E(x)>0}} \frac{1}{2d_E(x)}\left(\sum_{y\in\Omega\setminus A} J_E(x,y)g(y)\right)^2
&\le \frac{1}{p^2}\sum_{y\in\Omega\setminus A} d_E(y)g(y)^2 + \text{COMPLEMENT}_E, \\
\frac{1}{p^2}\sum_{\substack{x\in A\\d_M(x)>0}} \frac{1}{2d_M(x)}\left(\sum_{y\in\Omega\setminus A} J_M(x,y)g(y)\right)^2
&\le \frac{1}{p^2}\sum_{y\in\Omega\setminus A} d_M(y)g(y)^2 + \text{COMPLEMENT}_M.
\end{aligned} \tag{3.1}
\]
Furthermore, by Cauchy–Schwarz over \(x\in A\), the left-hand sides of (3.1) are bounded below by \(\frac{w^2 S_E^2}{2\mathbb{E}_p[1_A d_E/p]}\) and \(\frac{w^2 S_M^2}{2\mathbb{E}_p[1_A d_M/p]}\) respectively.
*(Verified in exact rational arithmetic across all 2,508 subset/window/factor cases in `verify_two_channel_dichotomy_20261014.py`.)*
