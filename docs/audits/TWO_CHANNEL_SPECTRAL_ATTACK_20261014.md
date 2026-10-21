# Two-channel spectral concentration, unwindowed Fourier synthesis, and binomial residual identities — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with an exact sharper remaining sublemma).
Offline. No internet was used and no literature novelty is claimed. The unconditional target \(r_4(N)=o(N/\log N)\) and `SELECT` remain unresolved.

---

## Phase 1 — Independent Proof Audit

We independently rederived and verified every identity and quantifier in `MULTI_POSITION_COMPLETION_20261014.md`, `COMPLETION_PROJECTION_20261013.md`, `SIXTH_ORDER_FOURIER_ATTACK_20261012.md`, `STRUCTURAL_HYPOTHESIS_ATTACK_20261002.md`, `SELECT_ATTACK_20261002.md`, `NEW_RESULTS_20261002.md`, `SOLUTION_LEDGER.md`, and `PROOF_DEPENDENCIES.md`.

### 1.1 Exact cell decomposition and degenerate cells — PROVED
Let \(p>3\) be prime, \(\Omega\subset\mathbb{Z}_p\) be a nonempty window of size \(n=|\Omega|=wp\), and \(A\subset\Omega\) be cyclically 4-AP-free for nonzero differences. Extend \(B=1_A\) by zero outside \(\Omega\). Define on \(\mathbb{Z}_p\):

    h_E(v) = p^-1 sum_{d in Z_p} B(v+d)B(v+2d)B(v+3d),    q_E(v) = h_E(v) - B(v)/p,
    h_M(v) = p^-1 sum_{d in Z_p} B(v-d)B(v+d)B(v+2d),    q_M(v) = h_M(v) - B(v)/p.

Because \(B(v)\in\{0,1\}\) and \(A\) has no nonzero-difference 4-AP, \(B(v)q_E(v)=0\) and \(B(v)q_M(v)=0\) hold pointwise on \(\mathbb{Z}_p\), with \(q_E(v),q_M(v)\ge 0\).

Let \(F\) be any partition of \(\Omega\) with uniform probability measure \(\mathbb{E}_\Omega\). On each nonempty cell \(C\in F\), write \(g=\mathbb{E}_C B\), \(u=B-g\), \(T_C=(T_{E,C},T_{M,C})^T=\mathbb{E}_C[(q_E,q_M)^T]\), and \(k=(k_E,k_M)^T=(q_E-T_{E,C},q_M-T_{M,C})^T\).
- **Case \(0\le g<1\)**: Define \(\alpha_C = (1-g)^{-1} T_C\) and \(z = q - (1-g)^{-1}(1-B)T_C\).
  1. Since \(q=0\) on \(A\) (where \(B=1\)) and \(1-B=0\) on \(A\), we have \(z=0\) on \(A\cap C\), so \(Bz=0\) pointwise on \(C\).
  2. Taking \(\mathbb{E}_C\) gives \(\mathbb{E}_C z = T_C - (1-g)^{-1}(1-g)T_C = 0\).
  3. Since \(u=B-g\), \(\mathbb{E}_C[uz] = \mathbb{E}_C[Bz] - g\mathbb{E}_C[z] = 0 - 0 = 0\).
  4. Adding \(-\alpha_C u + z\) gives
     \[
     -\frac{T_C}{1-g}(B-g) + q - \frac{1-B}{1-g}T_C = q - \frac{B-g+1-B}{1-g}T_C = q - T_C = k.
     \]
- **Case \(g=1\)**: Every \(x\in C\) has \(B(x)=1\), hence \(q(x)=0\), \(T_C=0\), \(u(x)=0\), \(k(x)=0\). Setting \(\alpha_C=0\) and \(z(x)=0\) satisfies \(k=-\alpha_C u+z\), \(\mathbb{E}_C z=0\), \(Bz=0\), and \(\mathbb{E}_C[uz]=0\) identically.
- **Case \(g=0\)**: Every \(x\in C\) has \(B(x)=0\), hence \(u(x)=0\), \(\alpha_C=T_C\), and \(z(x)=q(x)-T_C=k(x)\), which satisfies \(\mathbb{E}_C z=0\), \(Bz=0\), and \(\mathbb{E}_C[uz]=0\).

### 1.2 Independent derivation of the \(2\times 2\) Loewner inequality — PROVED
With relative averages on \(\Omega\), set
\[
S = \mathbb{E}_\Omega[g T_C]\in\mathbb{R}^2,\quad U = \mathbb{E}_\Omega[g(1-g)],\quad J = \mathbb{E}_\Omega[g(1-g)\alpha_C\alpha_C^T],\quad Z = \mathbb{E}_\Omega[z z^T],\quad W = \mathbb{E}_\Omega[k k^T].
\]
1. Since \(\mathbb{E}_C[uz^T]=0\) and \(\mathbb{E}_C[u^2]=g(1-g)\), on each cell \(\mathbb{E}_C[k k^T] = g(1-g)\alpha_C\alpha_C^T + \mathbb{E}_C[z z^T]\). Averaging over \(C\in F\) gives \(W = J + Z\) with \(Z\succeq 0\), hence \(UW \succeq UJ\).
2. For any vector \(\lambda\in\mathbb{R}^2\), set \(X=\sqrt{g(1-g)}\) and \(Y=\sqrt{g(1-g)}(\lambda^T\alpha_C)\) (with \(Y=0\) on \(g=1\) cells). Then \(\mathbb{E}_\Omega[XY] = \mathbb{E}_\Omega[g(\lambda^T T_C)] = \lambda^T S\), \(\mathbb{E}_\Omega[X^2]=U\), and \(\mathbb{E}_\Omega[Y^2]=\lambda^T J\lambda\). By Cauchy–Schwarz,
   \[
   (\lambda^T S)^2 = (\mathbb{E}_\Omega[XY])^2 \le \mathbb{E}_\Omega[X^2]\mathbb{E}_\Omega[Y^2] = U(\lambda^T J\lambda) \le U(\lambda^T W\lambda),
   \]
   which holds even when \(U=0\), \(J\) is singular, or \(W\) is singular. Thus \(UW \succeq UJ \succeq S S^T\) in the \(2\times 2\) Loewner order.

---

## Phase 2 & Phase 9 — Unwindowed Cubic Fourier Synthesis on \(\Omega\), Direct Regularized Gram Bridge, and Exact Spectral Budget

### 2.1 Unwindowed full-group cubic Fourier synthesis of \(k_\lambda\) on a proper window — PROVED
In earlier notes (`DEGREE_SIX_ATTACK_20261012.md` §7), restricting \(h\) or \(q\) to \(\Omega\) before Fourier inversion introduced \(\widehat{1_\Omega q}\), convolving the cubic spectrum with the window transform \(\widehat{1_\Omega}\). We prove an exact identity that **avoids multiplying \(q_\lambda\) by \(1_\Omega\)**:

**Theorem 1 (Unwindowed cubic Fourier representation on proper windows).**
Let \(B=1_A\) be zero-extended to \(\mathbb{Z}_p\), and let \(\widehat{q_E}(\xi), \widehat{q_M}(\xi)\) be the **full-group** Fourier coefficients of \(q_E,q_M\) on \(\mathbb{Z}_p\):
\[
\widehat{q_E}(\xi) = \sum_{r\in\mathbb{Z}_p} b(2\xi+r)b(-\xi-2r)b(r) - \frac{b(\xi)}{p},\qquad
\widehat{q_M}(\xi) = \sum_{r\in\mathbb{Z}_p} b\bigl((\xi+r)/2\bigr)b\bigl((\xi-3r)/2\bigr)b(r) - \frac{b(\xi)}{p}.
\]
For any partition \(F\) of \(\Omega\), let \(\psi_\xi(x) = (I-\mathbb{E}(\cdot\mid F))e_p(\xi x)\) for \(x\in\Omega\), and let \(c_\xi = \langle \psi_\xi, u\rangle_\Omega = \mathbb{E}_\Omega[u(x)e_p(-\xi x)]\) be the relative Fourier coefficient of \(u\) on \(\Omega\). Then for every \(\lambda=(\lambda_E,\lambda_M)^T\in\mathbb{R}^2\) and \(\widehat{q_\lambda}(\xi)=\lambda_E\widehat{q_E}(\xi)+\lambda_M\widehat{q_M}(\xi)\):
1. Pointwise on \(\Omega\),
   \[
   k_\lambda(x) = \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} \widehat{q_\lambda}(\xi)\,\psi_\xi(x). \tag{1}
   \]
2. The relative pairing on \(\Omega\) equals the unwindowed frequency pairing:
   \[
   -\lambda^T S = \langle u, k_\lambda\rangle_\Omega = \sum_{\xi\in\mathbb{Z}_p\setminus\{0\}} \overline{c_\xi}\,\widehat{q_\lambda}(\xi). \tag{2}
   \]

*Proof.* For every \(x\in\mathbb{Z}_p\), Fourier inversion on \(\mathbb{Z}_p\) gives \(q_\lambda(x) = \sum_{\xi\in\mathbb{Z}_p} \widehat{q_\lambda}(\xi)e_p(\xi x)\). Restricting \(x\) to \(\Omega\) and applying the linear operator \(I-\mathbb{E}(\cdot\mid F)\) kills the constant \(\xi=0\) mode and maps \(e_p(\xi x)\big|_\Omega\) to \(\psi_\xi(x)\), yielding (1). Taking the \(\Omega\)-inner product of (1) with \(u\) gives (2). \(\square\)

### 2.2 Direct bridge from two-channel spectral concentration to quarter-arc refinement gain — PROVED
On a proper window \(\Omega\), the centered relative characters \(\{\psi_\xi\}_{\xi\in\Gamma}\) are not orthogonal, and passing from subspace projection \(\|P_\Gamma u\|_2^2\) to a quarter-arc refinement gain \(\Delta E\) requires controlling the regularized relative Gram matrix \(M_\Gamma = \kappa^2 G_\Gamma + (1-\kappa^2)I_s\), where \((G_\Gamma)_{\xi,\eta} = \langle \psi_\xi,\psi_\eta\rangle_\Omega\) and \(\kappa^2 = 8/\pi^2\). We prove a direct variational bridge that includes both the subspace projection and the unwindowed cubic Fourier decomposition:

**Theorem 2 (Regularized relative Gram bridge for two-channel completions).**
Let \(\Gamma\subset\mathbb{Z}_p\setminus\{0\}\) have \(|\Gamma|=s\) characters, and let \(\Psi_\Gamma : \mathbb{C}^s \to L^2(\Omega)\) be the synthesis map \((\Psi_\Gamma v)(x) = \sum_{\xi\in\Gamma} v_\xi \psi_\xi(x)\). For any \(\lambda\in\mathbb{R}^2\) and any coefficient vector \(v(\lambda)\in\mathbb{C}^s\), let
\[
\varepsilon_\Gamma(\lambda, v) = \|k_\lambda - \Psi_\Gamma v(\lambda)\|_{L^2(\Omega)}.
\]
Then some simultaneous rotation of the \(s\) quarter-arc partitions of \(\Gamma\) produces actual factor-energy gain \(\Delta E = \operatorname{Var}_\Omega(\mathbb{E}_\Omega[B\mid F\vee P_\Gamma]) - \operatorname{Var}_\Omega(g)\) satisfying
\[
\Delta E \ge \kappa^2\, c_\Gamma^* M_\Gamma^{-1} c_\Gamma
\ge \kappa^2 \frac{\max\bigl(0,\, |\lambda^T S| - \sqrt{U}\,\varepsilon_\Gamma(\lambda, v)\bigr)^2}{\kappa^2 \|\Psi_\Gamma v(\lambda)\|_{L^2(\Omega)}^2 + (1-\kappa^2)\|v(\lambda)\|_{\ell^2(\Gamma)}^2}. \tag{3}
\]
In particular:
1. **(Unwindowed cubic coefficient choice)**: Taking \(v_\xi(\lambda) = \widehat{q_\lambda}(\xi)\) for \(\xi\in\Gamma\) gives \(\varepsilon_\Gamma(\lambda,v) \le \sum_{\xi\notin\Gamma\cup\{0\}} |\widehat{q_\lambda}(\xi)|\) (or \(\|\sum_{\xi\notin\Gamma\cup\{0\}} \widehat{q_\lambda}(\xi)\psi_\xi\|_{L^2(\Omega)}\)), and denominator at most \(\kappa^2 W_\Gamma(\lambda) + (1-\kappa^2)\sum_{\xi\in\Gamma}|\widehat{q_\lambda}(\xi)|^2\).
2. **(Minimum-norm Moore–Penrose projection choice)**: Taking \(v(\lambda) = G_\Gamma^\dagger \langle \psi_\Gamma, k_\lambda\rangle_\Omega\) makes \(\Psi_\Gamma v(\lambda) = P_\Gamma k_\lambda\), so \(\varepsilon_\Gamma(\lambda,v) = \delta(\lambda) = \|(I-P_\Gamma)k_\lambda\|_2\) and \(\|\Psi_\Gamma v(\lambda)\|_2^2 = W_\Gamma(\lambda) = \lambda^T W_\Gamma\lambda\).

*Proof.* By `STRUCTURAL_SAMPLING_20261002.md` Theorem 3 (`P21`), \(\Delta E \ge \kappa^2 c_\Gamma^* M_\Gamma^{-1} c_\Gamma = \kappa^2 \sup_{v\ne 0} |\langle u, \Psi_\Gamma v\rangle_\Omega|^2 / (v^* M_\Gamma v)\). Now \(|\langle u, \Psi_\Gamma v\rangle_\Omega| \ge |\langle u, k_\lambda\rangle_\Omega| - |\langle u, k_\lambda - \Psi_\Gamma v\rangle_\Omega| \ge |\lambda^T S| - \sqrt{U}\,\varepsilon_\Gamma(\lambda,v)\), while \(v^* M_\Gamma v = \kappa^2 \|\Psi_\Gamma v\|_{L^2(\Omega)}^2 + (1-\kappa^2)\|v\|_{\ell^2}^2\). \(\square\)

### 2.3 Weakest quantitative spectral budget closing the October 2 iteration — PROVED
By `STRUCTURAL_HYPOTHESIS_ATTACK_20261002.md` §2 (`V1`–`V3`), if a factor refinement adds \(s(a)\le \lceil K a^{-\gamma}/\ell(a)^D\rceil\) characters (\(\ell(a)=\log(2/a)\)) to reach factor variance \(\eta(a)a^2\) with \(\eta(a)\ge c a^\beta/\ell(a)^C\), the cumulative rank and logarithmic size loss satisfy \(D_t, S_t = O(t^{-(\beta+\gamma)}\ell(t)^{C-D})\), which closes the terminal packing contradiction whenever:
\[
\beta + \gamma < \frac{1}{2}, \qquad \text{or} \qquad \beta + \gamma = \frac{1}{2} \quad\text{with}\quad D > C. \tag{4}
\]
If each multi-character step adds \(s_0(a)\) characters and captures energy \(\Delta E(a)\), reaching \(\eta(a)a^2\) in \(m(a) = \lceil \eta(a)a^2/\Delta E(a)\rceil\) stages uses \(s(a) \le m(a)s_0(a)\) characters. Thus, under the tail condition \(\varepsilon_\Gamma(\lambda,v)^2 \le (\lambda^T S)^2/(4U)\), Theorem 2 yields
\[
\Delta E(a) \ge \frac{\kappa^2 (\lambda^T S)^2}{4 D_{\text{reg}}(\lambda,v)}, \qquad D_{\text{reg}}(\lambda,v) := \kappa^2 \|\Psi_\Gamma v(\lambda)\|_2^2 + (1-\kappa^2)\|v(\lambda)\|_{\ell^2}^2,
\]
and the exact sufficient condition to close the October 2 iteration is:
\[
\frac{s_0(a)\, D_{\text{reg}}(\lambda, v)}{(\lambda^T S)^2} \lesssim \frac{a^{-(5/2 - (\beta+\gamma))}}{\ell(a)^{D-C}} \qquad (\beta+\gamma \le 1/2,\ D>C\text{ if }\beta+\gamma=1/2). \tag{5}
\]
At the critical frontier \(\beta+\gamma=1/2\) and \(D-C=1\) (or with iterated logarithm \(R(a)=\log\log(e^2/a)\) as in `WSELECT`), this requires
\[
\frac{(\lambda^T S)^2}{s_0(a)\, D_{\text{reg}}(\lambda,v)} \gtrsim a^{5/2} \ell(a) \quad (\text{or } a^{5/2} R(a)). \tag{6}
\]
When \(|\lambda^T S|\asymp a^4\) (the natural scale \(a\mathbb{E}[q]\asymp a^4\)), (6) requires \(s_0(a)\,D_{\text{reg}}(\lambda,v) \lesssim a^{11/2}/\ell(a)\). Neither `SELECT` (\(s_0=1\)) nor (6) is proved unconditionally; (5)–(6) give the exact weakest quantitative budget.

---

## Phase 4 — Exact \(2\times 2\) Matrix Pencil Optimization for the Channel Combination

For a fixed character family \(\Gamma\), let \(P_\Gamma\) be the \(\Omega\)-orthogonal projection onto \(L_\Gamma = \operatorname{span}\{\psi_\xi : \xi\in\Gamma\}\). Define the \(2\times 2\) real symmetric positive-semidefinite matrices
\[
W_\Gamma = \mathbb{E}_\Omega\bigl[(P_\Gamma k)(P_\Gamma k)^T\bigr], \qquad
W_{\text{tail}} = \mathbb{E}_\Omega\bigl[((I-P_\Gamma)k)((I-P_\Gamma)k)^T\bigr] = W - W_\Gamma.
\]
Then for every \(\lambda=(\lambda_E,\lambda_M)^T\in\mathbb{R}^2\):
\[
W_\Gamma(\lambda) = \lambda^T W_\Gamma \lambda, \qquad \delta(\lambda)^2 = \lambda^T W_{\text{tail}} \lambda. \tag{7}
\]

**Theorem 3 (Exact \(2\times 2\) matrix pencil optimization).**
1. **(Maximum signal-to-tail ratio)**: The concentration condition \(\delta(\lambda)^2 \le (\lambda^T S)^2/(4U)\) holds for some nonzero \(\lambda\in\mathbb{R}^2\) if and only if the generalized Rayleigh quotient of the rank-one matrix \(S S^T\) against \(W_{\text{tail}}\) satisfies
   \[
   \rho_{\text{tail}}(\Gamma) := \sup_{\lambda\ne 0} \frac{(\lambda^T S)^2}{U (\lambda^T W_{\text{tail}} \lambda)} = U^{-1} S^T W_{\text{tail}}^\dagger S \ge 4 \tag{8}
   \]
   (or \(S\notin \operatorname{range}(W_{\text{tail}})\), in which case choosing \(\lambda\in\ker(W_{\text{tail}})\) with \(\lambda^T S\ne 0\) gives \(\delta(\lambda)=0\) and \(\rho_{\text{tail}}(\Gamma)=+\infty\)). When \(W_{\text{tail}}\succ 0\), the unique maximizer up to scale is the generalized eigenvector \(\lambda_{\text{tail}}^* = W_{\text{tail}}^{-1} S\).
2. **(Exact variational maximum of the spectral lower bound)**: Define
   \[
   B_\Gamma(\lambda) := \frac{\max\bigl(0,\, |\lambda^T S| - \sqrt{U(\lambda^T W_{\text{tail}}\lambda)}\bigr)^2}{\lambda^T W_\Gamma \lambda}.
   \]
   Whenever \(\rho_{\text{tail}}(\Gamma) > 1\), the supremum \(\sup_{\lambda\in\mathbb{R}^2} B_\Gamma(\lambda)\) is attained by solving the \(1\)-parameter family of \(2\times 2\) linear systems: for any \(\lambda\) with \(\lambda^T S = 1\), setting the gradient of \(\lambda^T W_{\text{tail}}\lambda\) and \(\lambda^T W_\Gamma\lambda\) proportional gives the matrix-pencil line
   \[
   \lambda(\mu) \propto \bigl((1-\mu)W_\Gamma + \mu W_{\text{tail}}\bigr)^\dagger S, \qquad \mu\in[0,1]. \tag{9}
   \]
3. **(Channel-vanishing resilience)**: By optimizing over \(\lambda\in\mathbb{R}^2\), the bound automatically satisfies
   \[
   \sup_{\lambda\in\mathbb{R}^2} B_\Gamma(\lambda) \ge \max\bigl(B_\Gamma(e_1),\, B_\Gamma(e_2)\bigr)
   = \max\!\left(
     \frac{\max(0, S_E - \sqrt{U W_{\text{tail},EE}})^2}{W_{\Gamma,EE}},\,
     \frac{\max(0, S_M - \sqrt{U W_{\text{tail},MM}})^2}{W_{\Gamma,MM}}
   \right), \tag{10}
   \]
   which remains strictly positive when \(S_E=0\) and \(S_M > \sqrt{U W_{\text{tail},MM}}\) (or vice versa), without assuming \(S_E+S_M\) is generically positive.

**Verification on `ternary_cube` and `three_point`**:
- For `ternary_cube` (\(p=59, n=14, A=\text{cube}\)), \(q_E\equiv 0\) on \(\Omega\), so \(S_E=0\) and \(B_\Gamma(e_1)=0\) for every \(\Gamma\). However, \(S_M = 0.006918 > 0\) with \(S_M^2/(U W_{MM}) = 0.8772\), and already at \(s=3\) symmetric frequency pairs \(\Gamma=\{\pm 1,\pm 2,\pm 3\}\), \(B_\Gamma(e_2) = 0.01160 > 0\) (and \(0.10396\) at \(s=4\)).
- For `three_point` (\(p=101, n=25, A=\{0,1,3\}\)), \(S_E=0\) while \(S_M = 4.752\times 10^{-5} > 0\); for \(s=12\) frequency pairs, \(B_\Gamma(e_2) = 3.736\times 10^{-4} > 0\) while \(B_\Gamma(e_1)=0\).

---

## Phase 5 — Exact Cross-Channel Sixth-Order Spectrum and Affine Classification

Let \(p>7\) be prime, \(m=p-1\), and \(B=1_A\) on \(\mathbb{Z}_p\) be 4-AP-free. Set \(H_E(v)=p q_E(v)\) and \(H_M(v)=p q_M(v)\). Expanding \(\mathbb{E}_v[H_E(v)^2]\), \(\mathbb{E}_v[H_M(v)^2]\), and the cross-correlation \(\mathbb{E}_v[H_E(v)H_M(v)]\) in both physical and Fourier space gives:

**Theorem 4 (Complete \(2\times 2\) sixth-order completion spectrum).**
1. **(Fourier second-moment matrix)**: For any 4-AP-free \(B\) on \(\mathbb{Z}_p\) (\(\Lambda_4(B)=a/p\)),
   \[
   \begin{aligned}
   \mathbb{E}_v[H_E(v)^2] &= p^2 \sum_{t\in\mathbb{Z}_p} |K_E(t)|^2 - a, \\
   \mathbb{E}_v[H_M(v)^2] &= p^2 \sum_{t\in\mathbb{Z}_p} |K_M(t)|^2 - a, \\
   \mathbb{E}_v[H_E(v)H_M(v)] &= p^2 \sum_{t\in\mathbb{Z}_p} \operatorname{Re}\bigl(K_E(t)\overline{K_M(t)}\bigr) - a.
   \end{aligned} \tag{11}
   \]
2. **(Exact overlap decomposition of \(\mathbb{E}[H_M^2]\) and \(\mathbb{E}[H_E H_M]\))**:
   With \(R_E = \{1,2,3,1/2,3/2,1/3,2/3\}\), \(R_M = \{1,-1,2,1/2,-2,-1/2\}\), and \(R_{EM} = \{1,2,3,-1,-2,-3,1/2,3/2\}\):
   \[
   \begin{aligned}
   \mathbb{E}_v[H_E(v)^2] &= m F_{3,E} + m \sum_{r\in\{3,1/3,3/2,2/3\}} F_{5,EE,r} + m(m-7) A_{6,EE}, \\
   \mathbb{E}_v[H_M(v)^2] &= m F_{3,M} + m F_{4,MM,-1} + m \sum_{r\in\{2,1/2,-2,-1/2\}} F_{5,MM,r} + m(m-6) A_{6,MM}, \\
   \mathbb{E}_v[H_E(v)H_M(v)] &= m F_{4,EM,1} + m \sum_{r\in\{3,-1,-2,-3,1/2,3/2\}} F_{5,EM,r} + m(m-8) A_{6,EM},
   \end{aligned} \tag{12}
   \]
   where \(F_{5,EE,2}=F_{5,EE,1/2}=0\) and \(F_{5,EM,2}=0\) identically by 4-AP exclusion!
3. **(Affine collapse of the 5-term overlap patterns)**:
   - All four 5-term unions in \(\mathbb{E}[H_M^2]\) (\(r\in\{2,1/2,-2,-1/2\}\)) lie in **one single affine equivalence class** \(\{-2,-1,1,2,4\}\sim \{0,1,3,4,6\}\), so \(F_{5,MM,2}=F_{5,MM,1/2}=F_{5,MM,-2}=F_{5,MM,-1/2}\) identically on \(\mathbb{Z}_p\)!
   - The four surviving 5-term unions in \(\mathbb{E}[H_E^2]\) collapse into **two** affine classes: \(F_{5,EE,3}=F_{5,EE,1/3}\) (\(\sim\{0,1,2,5,8\}\)) and \(F_{5,EE,3/2}=F_{5,EE,2/3}\) (\(\sim\{0,1,2,4,7\}\)).
   - The 4-term cross-union at \(r=1\) in \(\mathbb{E}[H_E H_M]\) is \(E_d\cup M_d = \{v-d,v+d,v+2d,v+3d\}\), which contains the 3-AP \(\{v+d,v+2d,v+3d\}\); thus \(F_{4,EM,1}=0\) whenever \(A\) is 3-AP-free.
4. **(Localized cross-channel sixth-moment enhancement)**:
   At any vertex \(v\in\Omega\) with \(m_{E,v}a^4\ge 20\) and \(m_{M,v}a^4\ge 20\), the \(2\times 2\) degree-six SOS inequality (`MULTI_POSITION_COMPLETION_20261014.md` Theorem 3) and cubic PSD bound \(|M(U)|\le \rho_3\) on the at most \(5m_{E,v}\) (for \(EE\)), \(6m_{M,v}\) (for \(MM\)), and \(7\sqrt{m_{E,v}m_{M,v}}\) (for \(EM\), since \(r=2\) vanishes) overlapping pairs force average disjoint sixth-moment enhancements \(\ge \rho_6 + a^7/8\) in both channels simultaneously.

---

## Phase 6 & Phase 10 — Contrapositive Counting, Exact Binomial-Derivative Identities for \(R_0,\dots,R_4\), and Operator Duality

### 6.1 Exact binomial-derivative identities connecting \(R_0,\dots,R_4\) to \(S_E+S_M\) — PROVED
In `SELECT_ALGEBRA_20261002.md`, \(\Lambda_4(B)\) was expanded via \(B=g+u\) into the five residual groups \(R_0,R_1,R_2,R_3,R_4\), where \(R_j = \sum_{|I|=j} \Lambda_4(v^{(I)})\) has \(u\) in \(j\) slots and \(g\) in \(4-j\) slots, and the missing step (`SIGNED`) was to lower-bound \(R_1+R_2+R_3+R_4\).

We prove an exact system of identities that holds **on every window \(\Omega\subset\mathbb{Z}_p\) with zero boundary error** (where \(B,g,u\) are extended by zero outside \(\Omega\) and \(w=|\Omega|/p\)):

**Theorem 5 (Binomial-derivative residual identities and two-channel pairing).**
For \(k\in\{0,1,2,3,4\}\), define the nonnegative \(k\)-th directional completion functional
\[
D_k := \sum_{\substack{I\subset\{0,1,2,3\}\\|I|=k}} \Lambda_4\bigl(g\text{ on }I,\ B\text{ on }I^c\bigr) \ge 0. \tag{13}
\]
Because \(B = g+u\), substituting \(B=g+u\) into \(D_k\) gives the exact upper-triangular binomial transform and its inverse:
\[
D_k = \sum_{j=0}^{4-k} \binom{4-j}{k} R_j, \qquad R_j = \sum_{k=0}^{4-j} (-1)^k \binom{4-j}{k} D_k. \tag{14}
\]
Now assume \(A\subset\Omega\) is 4-AP-free for nonzero differences. Then:
1. **(Zeroth derivative)**: \(D_0 = \Lambda_4(B) = R_0 + R_1 + R_2 + R_3 + R_4 = \frac{aw}{p}\).
2. **(First derivative = two-channel pairing!)**: Because \(\sum_{i=0}^3 \prod_{j\ne i} B(x+jd)\) sums the two endpoint completions \(h_E(x), h_E(x+3d)\) and the two interior completions \(h_M(x+d), h_M(x+2d)\), and \(\mathbb{E}_C[u]=0\), we have \(D_1 = \mathbb{E}_x[g(x)(2h_E(x)+2h_M(x))] = \mathbb{E}_x[g(x)(2q_E(x)+2q_M(x) + 4B(x)/p)]\). Since \(\Omega\) supports \(g\), this gives the **exact boundary-free identity**:
   \[
   D_1 = 4R_0 + 3R_1 + 2R_2 + R_3 = 2w(S_E + S_M) + \frac{4w(a^2+v)}{p}, \tag{15}
   \]
   where \(v = \operatorname{Var}_\Omega(g)\) and \(U = \mathbb{E}_\Omega[u^2] = a(1-a)-v\).
3. **(Weighted residual sum identity)**: Subtracting \(D_1\) from \(4D_0\) (i.e. \(4D_0 - D_1\)) eliminates \(R_0\) completely and proves:
   \[
   \boxed{4D_0 - D_1 = R_1 + 2R_2 + 3R_3 + 4R_4 = -2w(S_E + S_M) + \frac{4wU}{p}.} \tag{16}
   \]
   Equivalently, eliminating \(R_3\) via \(D_1 - D_0\) gives:
   \[
   \boxed{D_1 - D_0 = 3R_0 + 2R_1 + R_2 - R_4 = 2w(S_E + S_M) + \frac{w(3a - 4U)}{p}.} \tag{17}
   \]
4. **(Higher nonnegative derivatives)**:
   \[
   \begin{aligned}
   D_2 &= 6R_0 + 3R_1 + R_2 \ge 0, \\
   D_3 &= 4R_0 + R_1 \ge 0 \implies R_1 \ge -4R_0, \\
   D_4 &= R_0 \ge 0,
   \end{aligned} \tag{18}
   \]
   and the exact alternating reconstruction of \(R_4 = \Lambda_4(u)\) is:
   \[
   R_4 = D_0 - D_1 + D_2 - D_3 + D_4 = \frac{aw}{p} - 2w(S_E + S_M) - \frac{4w(a^2+v)}{p} + D_2 - D_3 + R_0. \tag{19}
   \]

**Consequence for Phase 6 & Phase 10**:
- Equation (16) reveals the exact relationship between the two-channel completion pairing \(S_E+S_M\) and the sixteen-term residual expansion \(R_1,\dots,R_4\): the linear combination \(R_1 + 2R_2 + 3R_3 + 4R_4 = 4D_0 - D_1\) is **determined purely by \(S_E+S_M\)**!
- Moreover, by Theorem 2, if every small character family \(\Gamma\) fails to capture energy \(\Delta E\), then \(S_E\) and \(S_M\) are upper-bounded by \(\sqrt{U\,\delta_E^2} + \sqrt{W_{\Gamma,EE}\Delta E/\kappa^2}\), forcing \(S_E+S_M\) to be small if the completion tails are small, which by (16) forces \(R_1+2R_2+3R_3+4R_4 \approx 0\).
- However, knowing \(R_1+2R_2+3R_3+4R_4 \approx -2w(S_E+S_M)\) and \(D_2,D_3\ge 0\) does not by itself imply `SIGNED` (\(R_1+R_2+R_3+R_4 \ge -3a^4/8\) on \(\mathbb{Z}_p\)), because \(R_2, R_3, R_4\) appear with weights \((1,2,3,4)\) in (16) versus \((1,1,1,1)\) in `SIGNED`: specifically, \((R_1+R_2+R_3+R_4) = \frac{1}{4}(R_1+2R_2+3R_3+4R_4) + \frac{1}{4}(3R_1+2R_2+R_3)\), and \(3R_1+2R_2+R_3 = 2D_2 - 3D_3 + R_3\) (while \(D_2 - D_3 - 2R_0 + R_3 = 2R_1 + R_2 + R_3\)).

### 6.2 Exact operator duality between \(K_B\) and \(R_B\) — PROVED
On \(\mathbb{Z}_p\), alongside the endpoint operator \(K_B(u,v) = B((2u+v)/3)B((u+2v)/3)\) (`SIGNED_RESEARCH.md` §3), define the middle-point completion operator (`RELATIVE_WINDOWS.md` §5):
\[
R_B(u,v) = B(2u-v)B(2v-u), \qquad (R_B g)(u) = \mathbb{E}_v R_B(u,v)g(v).
\]
Then:
1. **Action on \(B\)**: Pointwise on \(\mathbb{Z}_p\),
   \[
   (K_B B)(v) = h_E(v), \qquad (R_B B)(v) = h_M(v). \tag{20}
   \]
   (Indeed, setting \(v'=v+d\) in \(h_M(v)=\mathbb{E}_d B(v-d)B(v+d)B(v+2d)\) gives \(v-d=2v-v'\) and \(v+2d=2v'-v\).)
2. **Simultaneous AP-free compression**: With \(P_A = \operatorname{diag}(B)\), 4-AP-freeness is equivalent to either of the two exact matrix identities:
   \[
   P_A K_B P_A = \frac{1}{p} P_A, \qquad P_A R_B P_A = \frac{1}{p} P_A. \tag{21}
   \]
3. **Exact Fourier matrix relation**: In the orthonormal character basis \(e_r(x)=e_p(rx)\),
   \[
   \langle e_r, K_B e_s\rangle = b(2r+s)b(-r-2s), \qquad
   \langle e_r, R_B e_s\rangle = b\bigl((2r-s)/3\bigr)b\bigl((r-2s)/3\bigr). \tag{22}
   \]
   Thus \(R_B\) is conjugate to \(K_B\) in frequency space via \((r,s)\mapsto (r/3, -s/3)\).

---

## Phase 7 & Phase 8 — Quadratic Resonance Analysis and Anti-Phase Separation

We tested the two-channel construction against the weighted quadratic family \(f_p(x) = a F(x^2/p)/M_p\) (`SIXTH_ORDER_FOURIER_ATTACK_20261012.md` §6, where \(F(\theta) = 1 + 2\beta\cos(2\pi\theta) + 2\beta\cos(6\pi\theta)\)) and the Boolean quadratic interval host \(B(x) = 1_S(q(x))\) (`SELECT_DELETION_20261002.md` §2).

### 7.1 Interior quadratic resonance is also present — PROVED
In \(h_{M,f}(v) = \mathbb{E}_d f_p(v-d)f_p(v+d)f_p(v+2d)\), a mode triple \((\ell_1,\ell_2,\ell_3)\in\{0,\pm 1,\pm 3\}^3\) has quadratic phase
\[
(\ell_1+\ell_2+\ell_3)v^2 + 2(-\ell_1+\ell_2+2\ell_3)vd + (\ell_1+\ell_2+4\ell_3)d^2.
\]
The resonant kernel \(\ell_1+\ell_2+4\ell_3 = 0\) and \(-\ell_1+\ell_2+2\ell_3 = 0\) has exact solutions \((\ell_1,\ell_2,\ell_3) = t(1,3,-1)\), giving total \(v^2\)-frequency \(\ell_1+\ell_2+\ell_3 = 3t\) (whereas \(h_{E,f}\) had kernel \(t(3,-3,1)\) with \(v^2\)-frequency \(t\)). Thus for large \(p\):
\[
\begin{aligned}
h_{E,f}(v) &= \left(\frac{a}{M_p}\right)^3 \bigl[1 + 2\beta^3 \cos(2\pi v^2/p)\bigr] + O(a^3 p^{-1/2}), \\
h_{M,f}(v) &= \left(\frac{a}{M_p}\right)^3 \bigl[1 + 2\beta^3 \cos(6\pi v^2/p)\bigr] + O(a^3 p^{-1/2}).
\end{aligned} \tag{23}
\]
Similarly, for any Boolean quadratic host \(B(x) = 1_S(q(x))\), `SELECT_DELETION_20261002.md` §2 shows that \(h_E(v) = \Phi_E(q(v)) + O(K^3/\sqrt{p})\) and \(h_M(v) = \Phi_M(q(v)) + O(K^3/\sqrt{p})\) with \(\widehat{\Phi_E}(t) = c_t |c_{3t}|^2\) and \(\widehat{\Phi_M}(3t) = c_{3t}|c_t|^2\). Because \(\Phi_E\) is supported on all \(t\) and \(\Phi_M\) is supported on multiples of \(3\), **no fixed linear combination \(\lambda_E h_E + \lambda_M h_M\) cancels quadratic resonance across all frequencies**.

### 7.2 Why AP exclusion defeats quadratic resonance: In-Phase Positivity vs. Anti-Phase Orthogonality — PROVED
What separates every quadratic-resonant family from an AP-free Boolean set is the **sign of the covariance between the function and its completion fields**:
1. **(Quadratic resonance = strictly POSITIVE in-phase covariance)**:
   For the weighted quadratic family \(f_p\), pairing \(f_p - a\) with \(h_{E,f}\) and \(h_{M,f}\) picks out the \(\cos(2\pi v^2/p)\) and \(\cos(6\pi v^2/p)\) modes, giving
   \[
   \operatorname{Cov}(f_p, h_{E,f}) = \operatorname{Cov}(f_p, h_{M,f}) = 2\beta^4 a^4 + O(a^4 p^{-1/2}) > 0. \tag{24}
   \]
   More generally, for any Boolean quadratic host \(B(x) = 1_S(q(x))\),
   \[
   \mathbb{E}_v\bigl[(B(v)-a)h_E(v)\bigr] = \mathbb{E}_v\bigl[(B(v)-a)h_M(v)\bigr] = \sum_{t\ne 0} |c_t|^2 |c_{3t}|^2 + O(K^4 p^{-1/2}) = Z_S - a^4 + O(K^4 p^{-1/2}) > 0. \tag{25}
   \]
2. **(4-AP exclusion = strictly NEGATIVE anti-phase covariance)**:
   For any 4-AP-free Boolean set \(B=1_A\), \(B q_E = B q_M = 0\) forces \(q_E\) and \(q_M\) to be supported exclusively on the complement \(A^c\), so
   \[
   \operatorname{Cov}(B, q_E) = -a\,\mathbb{E}[q_E] \le 0, \qquad \operatorname{Cov}(B, q_M) = -a\,\mathbb{E}[q_M] \le 0. \tag{26}
   \]
   Equivalently, any quadratic-resonant modes in \(B\) produce **positive** overlap \(\Lambda_4(B) \approx a^4 + Z_S > a^4\), moving \(\Lambda_4(B)\) *away* from zero rather than cancelling \(a^4\).

---

## Phase 11 & Phase 12 — Computational Discovery and Quantitative Closure Ledger

### 11.1 Finite Global Laws (\(p=23, k=5\) and \(p=29, k=6\))
Evaluating the exact rational global laws from `degree_six_finite_extension_20261012.json` and `sixth_order_p29_k6_extension_20261012.json` (`verify_two_channel_spectral_20261014.py`):
- At \(p=23, k=5\): \(L(H_E^2) = 0.133695\), \(L(H_M^2) = 0.142160\), \(L(H_E H_M) = 0.015509\), against the rank-one SOS baseline \((m\rho_3)^2/(1-a) = 0.019718\). The \(2\times 2\) matrix SOS excess has trace \(0.236419\) and determinant \(1.3938\times 10^{-2} > 0\). Across the 19 support orbits, the two-channel overlap \(U^{-1}S^T W^\dagger S\) strictly beats the endpoint-only bound on **15/19** orbits.
- At \(p=29, k=6\): \(L(H_E^2) = 0.159418\), \(L(H_M^2) = 0.184155\), \(L(H_E H_M) = 0.033267\), against baseline \(0.029615\). The \(2\times 2\) matrix SOS excess has trace \(0.284344\) and determinant \(2.0047\times 10^{-2} > 0\). Across the 32 support orbits, the two-channel overlap strictly beats the endpoint-only bound on **28/32** orbits.

### 12.1 Quantitative Closure Evaluation at \(a = \epsilon/\log N\)
Let \(a \asymp \epsilon/\log N\) and \(\ell = \log(2/a) \asymp \log\log N\). Assume the non-degenerate completion pairing regime \(|\lambda^T S| \asymp a^4\) and \(U \asymp a\).

| Quantity | Proved Bound / Scale | Required Scale to Close October 2 Ledger | Status / Exact Remaining Gap |
| --- | --- | --- | --- |
| Completion pairing \(|\lambda^T S|\) | \(\mathbb{E}_\Omega[g(\lambda_E T_{E,C} + \lambda_M T_{M,C})]\) (scale \(a^4\) when \(\mathbb{E}[q_\lambda]\asymp a^3\)) | \(\gtrsim a^4\) | Vanishing of both \(q_E,q_M\) on \(\mathbb{Z}_p\) gives \(\rho \ge a^2\); relative-window low-\(S\) branch open |
| Required tail \(\varepsilon_\Gamma(\lambda,v)^2\) | \(\lambda^T W_{\text{tail}} \lambda \le \lambda^T W \lambda \lesssim a^4\) | \(\le (\lambda^T S)^2/(4U) \asymp a^7\) | Needs spectral concentration of \(k_\lambda\) to tail \(\le a^7\) on \(|\Gamma|=s_0\) characters |
| Regularized denominator \(D_{\text{reg}}(\lambda,v)\) | \(\le \lambda^T W \lambda \lesssim a^4\) (elementary bound \(0\le q_\lambda\le a\)) | \(s_0(a)\, D_{\text{reg}}(\lambda,v) \lesssim a^{11/2}/\ell(a)\) (at \(\beta+\gamma=1/2, D-C=1\)) | Elementary bound \(W\lesssim a^4\) gives \(\Delta E \gtrsim a^4\), leaving a factor \(a^{3/2}\ell(a)\) gap |
| Captured energy \(\Delta E\) from \(W\lesssim a^4\) | \(\Delta E \ge \kappa^2 (\lambda^T S)^2 / (4\lambda^T W\lambda) \gtrsim a^4\) | \(\Delta E / s_0(a) \gtrsim a^{5/2}\ell(a)\) (to reach \(\zeta a^{9/4}\) in \(O(a^{-1/4}/\ell)\) rank) | Exponent gap is \(a^4\) vs \(a^{5/2}\ell(a)\): needs \(11/2 - 4 = 3/2\) powers of \(a\) in \(s_0 D_{\text{reg}}\) |
| Cumulative rank \(D_t\) & log-loss \(S_t\) | If \(\Delta E/s_0 \sim a^\lambda \ell^q\): \(O(t^{-(\lambda-2)}/\ell(t)^q)\) | \(o(\sqrt{\log N})\) and \(D_t S_t = o(\log N)\) (\(\lambda=5/2, q>0\)) | Conditional closure (`I1`/`P29`) is proved; premise (5)/(6) remains open |

---

## Phase 13 — Adversarial Verification Summary and Exact Remaining Sublemma

Run `python3 verify_two_channel_spectral_20261014.py` (outputs `TWO_CHANNEL_VERIFICATION_20261014.json`):
- **5,610** exact cell decompositions and **2,481** exact \(2\times 2\) Loewner matrix inequalities across \(\mathbb{Z}_7,\mathbb{Z}_{11}\) and proper windows \((11,5),(13,6)\) and diagnostics;
- **321** exact rational binomial-derivative identities (\(D_0,\dots,D_4\) and \(R_0,\dots,R_4\));
- **2,481** unwindowed full-group cubic Fourier synthesis checks on proper windows and **7,443** regularized relative Gram bridge checks;
- **50** operator duality and cross-channel moment equivalence checks across \(p=11,13,17,23,29\);
- **4** quadratic resonance in-phase positivity checks (\(p=101, 257\)) and **51** exact orbit evaluations on the \(p=23,k=5\) and \(p=29,k=6\) global laws.

### Corrected Next Research Prompt

> Continue offline from `TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` and `TWO_CHANNEL_VERIFICATION_20261014.json`. Accept as proved: (i) the unwindowed cubic Fourier synthesis \(k_\lambda(x) = \sum_{\xi\ne 0} \widehat{q_\lambda}(\xi)\psi_\xi(x)\) on every proper window \(\Omega\) and the direct regularized relative Gram bridge (Theorem 1 & Theorem 2); (ii) the exact \(2\times 2\) matrix pencil optimization for \(\lambda\in\mathbb{R}^2\) (Theorem 3); (iii) the complete cross-channel sixth-order overlap decomposition and affine collapse of the 14 five-term unions (Theorem 4); (iv) the boundary-free binomial-derivative identities \(D_1 = 4R_0+3R_1+2R_2+R_3 = 2w(S_E+S_M)+4w(a^2+v)/p\) and \(R_1+2R_2+3R_3+4R_4 = -2w(S_E+S_M)+4wU/p\) (Theorem 5); and (v) the covariance sign separation between quadratic-resonant hosts (\(\operatorname{Cov}(B,q_\lambda)>0\)) and 4-AP-free sets (\(\operatorname{Cov}(B,q_\lambda)=-a\mathbb{E}[q_\lambda]\le 0\)).
>
> Attack one of two sharp remaining problems:
> 1. **Direct Binomial Residual Closure**: Combine the exact identity \(R_1+2R_2+3R_3+4R_4 = -2w(S_E+S_M)+4wU/p\) and the nonnegativity of \(D_2 = 6R_0+3R_1+R_2 \ge 0\) and \(D_3 = 4R_0+R_1 \ge 0\) with a new bound on \(3R_1+2R_2+R_3 = D_2 - D_3 - 2R_0 + R_3\) under low factor energy and small residual Fourier coefficients to prove \(R_1+R_2+R_3+R_4 \ge -a^4\Lambda_4(1_\Omega)/4\).
> 2. **Spectral Concentration via Operator Duality**: Use the simultaneous compression identities \(P_A K_B P_A = P_A R_B P_A = p^{-1}P_A\) and the unwindowed cubic transforms \(\widehat{q_E},\widehat{q_M}\) to bound \(s_0(a)\,D_{\text{reg}}(\lambda,v)/(\lambda^T S)^2 \lesssim a^{-2}/\ell(a)\) on a character set \(\Gamma\) of size \(s_0(a)\).
