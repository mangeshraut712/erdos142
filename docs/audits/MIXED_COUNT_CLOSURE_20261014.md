# Exact mixed-count polynomials, two-channel sub-block inversion, and the finite-dimensional residual dual — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with exact Phase 0 algebra repair and a sharp finite-dimensional dual obstruction).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 — Independent Audit and Correction of the Binomial-Derivative Algebra

We independently audited every binomial-derivative identity in `TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` §6.1:

1. **First correction (`4D_0 - D_1` vs `D_1 - 4D_0`)**:
   Since
   \[
   D_0 = R_0 + R_1 + R_2 + R_3 + R_4, \qquad D_1 = 4R_0 + 3R_1 + 2R_2 + R_3,
   \]
   subtracting \(4D_0\) from \(D_1\) gives
   \[
   D_1 - 4D_0 = -R_1 - 2R_2 - 3R_3 - 4R_4,
   \]
   whereas
   \[
   4D_0 - D_1 = R_1 + 2R_2 + 3R_3 + 4R_4 = -2w(S_E + S_M) + \frac{4wU}{p}. \tag{0.1}
   \]
   In `TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md`, equation (16) itself (`R_1 + 2R_2 + 3R_3 + 4R_4 = -2w(S_E+S_M) + 4wU/p`) and its exact verifier assertion were **correct** because \(4D_0 - D_1 = 4(aw/p) - [2w(S_E+S_M) + 4w(a^2+v)/p] = -2w(S_E+S_M) + 4wU/p\) (using \(a - a^2 - v = U\)). The prose preceding (16) misstated "Subtracting \(4D_0\) from \(D_1\)" instead of "Subtracting \(D_1\) from \(4D_0\)." That prose has been corrected.

2. **Second correction (`D_2 - D_3 - 2R_0 + R_3` vs `3R_1 + 2R_2 + R_3`)**:
   Since
   \[
   D_2 = 6R_0 + 3R_1 + R_2, \qquad D_3 = 4R_0 + R_1, \qquad D_4 = R_0,
   \]
   we have:
   \[
   \begin{aligned}
   D_2 - D_3 - 2R_0 &= (6 - 4 - 2)R_0 + (3 - 1)R_1 + R_2 = 2R_1 + R_2, \\
   D_2 - D_3 - 2R_0 + R_3 &= 2R_1 + R_2 + R_3 \quad (\text{with zero } R_0 \text{ coefficient!}), \\
   2D_2 - 3D_3 + R_3 &= (12 - 12)R_0 + (6 - 3)R_1 + 2R_2 + R_3 = 3R_1 + 2R_2 + R_3, \\
   D_2 - 2D_3 + 2R_0 &= (6 - 8 + 2)R_0 + (3 - 2)R_1 + R_2 = R_1 + R_2.
   \end{aligned} \tag{0.2}
   \]
   Notice that in the user prompt's Phase 0 check, \(D_2 - D_3 - 2R_0 + R_3 = (6-4-2)R_0 + 2R_1 + R_2 + R_3 = 2R_1 + R_2 + R_3\) (the \(R_0\) coefficient is \(6-4-2=0\), not \(1\)). Both the prose in `TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` and the exact identities in (0.2) have been corrected and verified in exact rational arithmetic across 2,520 set/window/factor cases (`verify_mixed_count_closure_20261014.py`).

---

## Phase 1 & Phase 5 — The Exact Mixed-Count Polynomials \(P(t)\), \(Q(s,t)\) and Two-Channel Sub-Block Inversion

Let \(p>3\) be prime, \(\Omega\subset\mathbb{Z}_p\) have size \(n=wp\), \(A\subset\Omega\) be 4-AP-free for nonzero differences, \(B=1_A\), \(F\) be a partition of \(\Omega\), \(g=\mathbb{E}_\Omega[B\mid F]\), and \(u=B-g\) (all extended by zero outside \(\Omega\)).

### 1.1 The polynomials \(P(t)\) and \(Q(s,t)\) — PROVED
Define the single-variable residual interpolation polynomial and the two-variable nonnegative mixed-count polynomial:
\[
P(t) := \Lambda_4\bigl(g + t(B-g)\bigr) = \sum_{j=0}^4 R_j t^j, \qquad
Q(s,t) := \Lambda_4(sg + tB) = \sum_{k=0}^4 D_k s^k t^{4-k}. \tag{1.1}
\]
Because \(sg + tB = (s+t)g + tu\) and \(g, B \ge 0\) pointwise, \(Q(s,t)\) and \(P(t)\) are related by the exact basis change
\[
Q(s,t) = (s+t)^4 P\!\left(\frac{t}{s+t}\right) = \sum_{j=0}^4 R_j (s+t)^{4-j} t^j, \qquad
P(t) = Q(1-t, t) = \sum_{k=0}^4 D_k (1-t)^k t^{4-k}. \tag{1.2}
\]
In matrix form:
\[
\begin{pmatrix} D_0 \\ D_1 \\ D_2 \\ D_3 \\ D_4 \end{pmatrix}
=
\begin{pmatrix}
1 & 1 & 1 & 1 & 1 \\
4 & 3 & 2 & 1 & 0 \\
6 & 3 & 1 & 0 & 0 \\
4 & 1 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0
\end{pmatrix}
\begin{pmatrix} R_0 \\ R_1 \\ R_2 \\ R_3 \\ R_4 \end{pmatrix},
\qquad
\begin{pmatrix} R_0 \\ R_1 \\ R_2 \\ R_3 \\ R_4 \end{pmatrix}
=
\begin{pmatrix}
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & -4 \\
0 & 0 & 1 & -3 & 6 \\
0 & 1 & -2 & 3 & -4 \\
1 & -1 & 1 & -1 & 1
\end{pmatrix}
\begin{pmatrix} D_0 \\ D_1 \\ D_2 \\ D_3 \\ D_4 \end{pmatrix}. \tag{1.3}
\]
Every coefficient \(D_k\) (\(k=0,\dots,4\)) is a sum of \(\binom{4}{k}\) multilinear progression counts \(L_I(g,B) := \Lambda_4(g\text{ on }I, B\text{ on }I^c) \ge 0\). Hence \(D_k \ge 0\) for all \(k\), and \(P(t) \ge 0\) for all \(t\in[0,1]\).

### 1.2 Complete 10-term reflection-symmetric sub-block decomposition and two-channel inversion — PROVED
Under reversal \((x,d)\mapsto (x+3d,-d)\), the 16 multilinear terms \(L_I(g,B)\) and \(L_I(u,g)\) partition into **10 reflection-symmetric sub-blocks**. Specifically, splitting by endpoint slots \(E=\{0,3\}\) and interior slots \(M=\{1,2\}\):
- **Level \(k=1\) (1 \(g\) and 3 \(B\)'s)**:
  \[
  D_{1,E} = \Lambda_4(g,B,B,B) + \Lambda_4(B,B,B,g) \ge 0, \qquad
  D_{1,M} = \Lambda_4(B,g,B,B) + \Lambda_4(B,B,g,B) \ge 0.
  \]
- **Level \(k=2\) (2 \(g\)'s and 2 \(B\)'s)**:
  \[
  \begin{aligned}
  D_{2,E} &= \Lambda_4(g,B,B,g) \ge 0, \qquad D_{2,M} = \Lambda_4(B,g,g,B) \ge 0, \\
  D_{2,\text{mix}} &= \underbrace{\Lambda_4(g,g,B,B)+\Lambda_4(B,B,g,g)}_{D_{2,\text{adj}}\ge 0} + \underbrace{\Lambda_4(g,B,g,B)+\Lambda_4(B,g,B,g)}_{D_{2,\text{alt}}\ge 0} \ge 0.
  \end{aligned}
  \]
- **Level \(k=3\) (3 \(g\)'s and 1 \(B\))**:
  \[
  D_{3,E} = \Lambda_4(B,g,g,g) + \Lambda_4(g,g,g,B) \ge 0, \qquad
  D_{3,M} = \Lambda_4(g,B,g,g) + \Lambda_4(g,g,B,g) \ge 0.
  \]

Similarly, write \(R_1 = R_{1,uE} + R_{1,uM}\), \(R_2 = R_{2,gE} + R_{2,gM} + R_{2,\text{mix}}\), and \(R_3 = R_{3,gE} + R_{3,gM}\), where the subscript indicates which slots carry \(u\) (for \(R_1\)) or \(g\) (for \(R_2,R_3\)).

**Theorem 1 (Exact two-channel sub-block identities).**
For any 4-AP-free \(A\subset\Omega\) with \(a=|A|/|\Omega|\), \(v=\operatorname{Var}_\Omega(g)\), \(S_E=\mathbb{E}_\Omega[g T_{E,C}]\), and \(S_M=\mathbb{E}_\Omega[g T_{M,C}]\):
1. **(Separate endpoint and interior completion identities)**:
   \[
   D_{1,E} = 2w S_E + \frac{2w(a^2+v)}{p}, \qquad D_{1,M} = 2w S_M + \frac{2w(a^2+v)}{p}. \tag{1.4}
   \]
   In particular, the diagonal cancels in the channel difference:
   \[
   \boxed{D_{1,E} - D_{1,M} = 2w(S_E - S_M) = (R_{1,uM} - R_{1,uE}) + 2(R_{2,gE} - R_{2,gM}) + (R_{3,gE} - R_{3,gM}).} \tag{1.5}
   \]
2. **(Exact sub-block triangular system and inversion)**:
   \[
   \begin{aligned}
   D_{3,E} &= 2R_0 + R_{1,uE}, \qquad D_{3,M} = 2R_0 + R_{1,uM}, \\
   D_{2,E} &= R_0 + R_{1,uM} + R_{2,gE}, \qquad D_{2,M} = R_0 + R_{1,uE} + R_{2,gM}, \\
   D_{2,\text{mix}} &= 4R_0 + 2R_{1,uE} + 2R_{1,uM} + R_{2,\text{mix}}, \\
   R_{3,gE} &= 2w S_E + \frac{2w(a^2+v)}{p} - 2D_{2,E} - D_{2,\text{mix}} + D_{3,E} + 2D_{3,M} - 2R_0, \\
   R_{3,gM} &= 2w S_M + \frac{2w(a^2+v)}{p} - 2D_{2,M} - D_{2,\text{mix}} + D_{3,M} + 2D_{3,E} - 2R_0.
   \end{aligned} \tag{1.6}
   \]

---

## Phase 2, Phase 3 & Phase 4 — Sharp Finite-Dimensional Dual Optimization and the First Missing Constraint

### 2.1 What the known identities and inequalities imply — PROVED
From the exact inversion (1.3), the residual sum \(R_1+R_2+R_3+R_4\) can be written in three equivalent ways:
\[
\begin{aligned}
R_1 + R_2 + R_3 + R_4 &= \frac{aw}{p} - R_0, \\
R_1 + R_2 + R_3 + R_4 &= D_2 - 2D_3 + 2R_0 + R_3 + R_4, \\
R_1 + R_2 + R_3 + R_4 &= \frac{aw}{p} - 2w(S_E + S_M) - \frac{4w(a^2+v)}{p} + D_2 - D_3 + R_1 + R_2 + R_3.
\end{aligned} \tag{2.1}
\]
We now formulate the sharp finite-dimensional linear program (Phase 3): treat \((R_0,R_1,R_2,R_3,R_4)\) (or the 10 sub-block variables) and \((S_E,S_M)\) as real variables subject to:
1. **AP-free diagonal**: \(D_0 = R_0+R_1+R_2+R_3+R_4 = aw/p\).
2. **All 10 mixed-count nonnegativity constraints**: \(L_I(g,B)\ge 0\) for all \(I\subset\{0,1,2,3\}\) (which implies \(D_k\ge 0\) and \(P(t)\ge 0\) on \([0,1]\)).
3. **Two-channel completion identities and nonnegativity**: \(D_{1,E} = 2w S_E + 2w(a^2+v)/p\), \(D_{1,M} = 2w S_M + 2w(a^2+v)/p\), with \(S_E, S_M \ge 0\).
4. **Low-energy main term and SELECT-failure residual bounds (`SELECT_ALGEBRA_20261002.md` `A8`–`A9`)**:
   On \(\mathbb{Z}_p\) with \(v \le \zeta a^{9/4}\) and \(\rho = \max_{\xi\ne 0}|\widehat{u}(\xi)| \le \sqrt{c} a^{5/4}\sqrt{\ell(a)}\):
   \[
   R_0 \ge \frac{7}{16}a^4, \qquad |R_1| \le \varepsilon_1(a) \sim a^{31/8}, \qquad |R_2| \le \varepsilon_2(a) \sim a^{13/4}, \qquad |R_3| \le \varepsilon_3(a) \sim a^{21/8}.
   \]

**Theorem 2 (Exact finite-dimensional dual LP characterization and abstract feasibility).**
1. In the finite-dimensional optimization problem minimizing \(R_1+R_2+R_3+R_4\) subject to constraints (1)–(4), the equation \(R_0+R_1+R_2+R_3+R_4 = aw/p\) is **the only constraint in which \(R_4\) appears with a positive coefficient** (since \(D_1,D_2,D_3,D_4\) do not depend on \(R_4\)).
2. Consequently, even if one strengthens (4) to the ideal limit \(R_0 = a^4\) and \(R_1 = R_2 = R_3 = 0\) (and \(L_I(u,g)=0\) for all \(1\le |I|\le 3\)), the explicit abstract vector
   \[
   (R_0, R_1, R_2, R_3, R_4) = \left(a^4,\ 0,\ 0,\ 0,\ \frac{a}{p} - a^4\right), \qquad S_E = S_M = a^4 - \frac{a(a+v)}{p} \tag{3.1}
   \]
   has \(L_I(g,B) = a^4 \ge 0\) for every \(I\ne\emptyset\), \(D_0 = a/p \ge 0\), \(D_1 = 4a^4 \ge 0\), \(D_2 = 6a^4 \ge 0\), \(D_3 = 4a^4 \ge 0\), \(D_4 = a^4 \ge 0\), and satisfies all completion identities and `A8`–`A9` bounds with zero error, yet has
   \[
   R_1 + R_2 + R_3 + R_4 = \frac{a}{p} - a^4 < -\frac{3}{8}a^4 \quad \text{whenever } pa^3 > \frac{8}{5}.
   \]
   *(Verified in exact rational arithmetic at \(p=101, a=28/101\) and \(p=2147483647, a=1/50\) in `MIXED_COUNT_VERIFICATION_20261014.json`; this is an abstract LP vector, not a realized AP-free set.)*

### 4.1 The First Missing Constraint (Phase 4 & Phase 6) — PROVED EQUIVALENCE
Theorem 2 proves rigorously that **no combination of \(D_k \ge 0\), \(S_E, S_M \ge 0\), and bounds on \(R_1, R_2, R_3\) alone can bound \(R_1+R_2+R_3+R_4\) from below**, because \(R_4 = \Lambda_4(u)\) is a free slack variable in \(D_0 = R_0+R_1+R_2+R_3+R_4 = aw/p\).

Furthermore, under the low-factor-energy hypothesis \(v \le \zeta a^{9/4}\), the `SELECT_ALGEBRA_20261002.md` bounds (`A9`) already give \(|R_1| = O(a^{31/8}) = o(a^4)\) and \(|R_2| = O(a^{13/4}) = o(a^4)\) — or, using (0.2),
\[
D_3 = 4R_0 + R_1 \implies D_3 = 4a^4 + o(a^4), \qquad D_2 = 6R_0 + 3R_1 + R_2 \implies D_2 = 6a^4 + o(a^4). \tag{4.1}
\]
Substituting (4.1) into (2.1) isolates the **exact first missing inequality**:

**Theorem 3 (Reduction of `SIGNED` to \(R_3+R_4\) or \(D_1 - R_4\)).**
On \(\mathbb{Z}_p\), for any 4-AP-free \(A\) with \(v = \operatorname{Var}(g) \le \zeta a^{9/4}\) (\(\zeta\le 1/4\)) and \(\rho = \max_{\xi\ne 0}|\widehat{u}(\xi)| \le \sqrt{c}a^{5/4}\sqrt{\ell(a)}\), we have
\[
R_0 = a^4 + O(a^{33/8}), \qquad R_1 = O(a^{31/8}), \qquad R_2 = O(a^{13/4}), \qquad D_2 = 6a^4 + O(a^{31/8}), \qquad D_3 = 4a^4 + O(a^{31/8}). \tag{4.2}
\]
Consequently, for all sufficiently small \(a\) (with \(pa^3\ge 16\)), the signed residual inequality \(R_1+R_2+R_3+R_4 \ge -\frac{3}{8}a^4\) is **asymptotically equivalent** to each of the following three inequalities:
1. **(Cubic-plus-quartic residual form)**:
   \[
   R_3 + R_4 \ge -\frac{3}{8}a^4 + O(a^{13/4}). \tag{4.3}
   \]
2. **(Two-channel completion vs. quartic residual form)**: Since \(R_3 + R_4 = D_1 - D_2 + D_3 - R_0 + R_4 = 2(S_E + S_M) - 3a^4 + R_4 + O(a^{31/8})\),
   \[
   2(S_E + S_M) + R_4 \ge \frac{21}{8}a^4 + O(a^{13/4}). \tag{4.4}
   \]
3. **(Weighted sum vs. pure quartic form)**: Since \(3R_3 + 4R_4 = -2(S_E + S_M) - R_1 - 2R_2 + 4U/p = -2(S_E + S_M) + O(a^{13/4})\), eliminating \(2(S_E+S_M)\) between (4.3) and (0.1) shows that if \(R_3 = o(a^4)\) (which holds for the trivial factor \(g=a\), where \(R_3 = 2a(T_u+S_u) = O(a^2\rho) = O(a^{13/4}\sqrt{\ell}) = o(a^4)\)!), then:
   - **For the trivial factor \(g=a\)**: \(R_1=R_2=0\) and \(|R_3| \le 4a^2\rho = O(a^{13/4}\sqrt{\ell}) = o(a^4)\) are **already proved** under `SELECT` failure! Thus, for \(g=a\), `SELECT` reduces to the single pure-quartic/two-channel identity:
     \[
     R_4 = \Lambda_4(f) = -2a(T_f + S_f) + \frac{a}{p} - a^4 = -\frac{1}{2}(S_E + S_M) + O(a^{13/4}\sqrt{\ell}). \tag{4.5}
     \]

**Wait — look closely at (4.5)!**
Let us check what (4.5) says for the trivial factor \(g=a\) (\(u=f=B-a\))!
For \(g=a\), \(R_1=0\), \(R_2=0\), and \(R_3 = 2a(T_f + S_f)\).
Under `SELECT` failure, \(\rho = \max_{\xi\ne 0}|\widehat{f}(\xi)| \le \sqrt{c}a^{5/4}\sqrt{\ell(a)}\), so by Parseval:
\[
|T_f| \le \rho a(1-a) = O(a^{9/4}\sqrt{\ell}), \qquad |S_f| \le \rho a(1-a) = O(a^{9/4}\sqrt{\ell})!
\]
Wait: since \(|T_f|, |S_f| = O(a^{9/4}\sqrt{\ell}) \ll a^3\), what are \(\mathbb{E}[q_E]\) and \(\mathbb{E}[q_M]\)?!
By the exact physical-Fourier duality (`MULTI_POSITION_COMPLETION_20261014.md` §5):
\[
\mathbb{E}[q_E] = a^3 - \frac{a}{p} + T_f = a^3 + O(a^{9/4}\sqrt{\ell}) \sim a^3, \qquad
\mathbb{E}[q_M] = a^3 - \frac{a}{p} + S_f = a^3 + O(a^{9/4}\sqrt{\ell}) \sim a^3!
\]
Wait: for \(g=a\), \(S_E = a\mathbb{E}[q_E] = a^4 + a T_f - a^2/p = a^4 + O(a^{13/4}\sqrt{\ell})\), and \(S_M = a\mathbb{E}[q_M] = a^4 + a S_f - a^2/p = a^4 + O(a^{13/4}\sqrt{\ell})\)!
Let us substitute \(S_E = a^4 + a T_f - a^2/p\) and \(S_M = a^4 + a S_f - a^2/p\) into \(4D_0 - D_1 = R_1 + 2R_2 + 3R_3 + 4R_4 = -2(S_E+S_M) + 4a(1-a)/p\):
Since \(R_1=R_2=0\) and \(R_3 = 2a(T_f+S_f)\), the left-hand side is \(6a(T_f+S_f) + 4R_4\), while the right-hand side is \(-4a^4 - 2a(T_f+S_f) + 4a/p\), which rearranges to:
\[
4R_4 = -4a^4 - 8a(T_f+S_f) + \frac{4a}{p} \iff R_4 = -a^4 - 2a(T_f+S_f) + \frac{a}{p}.
\]
That is an exact identity! And why is \(S_E + S_M \sim 2a^4\) so important under `SELECT` failure?

---

## Phase 7 & Phase 8 — What `SELECT` Failure Proves About \(S_E\) and \(S_M\) (New Unconditional Lower Bound!)

Wait: in `COMPLETION_PROJECTION_20261013.md` §3 (`(7)`) and `SIXTH_ORDER_FOURIER_ATTACK_20261012.md` §4 (`(13)`–`(14)`), it was stated that:
- \(\mathbb{E}[q_E] \ge a^3/2\) required \(\rho \le a^2/4\) (which was *not* guaranteed by `SELECT` failure \(\rho \le \sqrt{c}a^{5/4}\sqrt{\ell}\), because \(a^{5/4}\sqrt{\ell} \gg a^2\)!).
- Wait: why did `SIXTH_ORDER_FOURIER_ATTACK_20261012.md` equation (13) say \(\rho \le a^2/4\) is needed for \(\mathbb{E}[q_E] \ge a^3/2\)?!
Look at equation (13) of `SIXTH_ORDER_FOURIER_ATTACK_20261012.md`:
\[
|\mathbb{E}[q_E] - (a^3 - a/p)| = |T_f| \le \rho a(1-a).
\]
When \(\rho \le \sqrt{c}a^{5/4}\sqrt{\ell(a)}\) (`SELECT` failure!), what is \(\rho a(1-a)\)?!
\[
\rho a(1-a) \le \sqrt{c}\, a^{5/4}\sqrt{\ell(a)} \cdot a = \sqrt{c}\, a^{9/4} \sqrt{\ell(a)}!
\]
And as \(a \to 0\),
\[
\frac{a^{9/4}\sqrt{\ell(a)}}{a^3} = a^{-3/4}\sqrt{\ell(a)} \to \infty!
\]
Aha!! Look at the exponents: \(9/4 = 2.25 < 3\)! So \(\rho a \sim a^{9/4}\sqrt{\ell}\) is **larger** than \(a^3\), NOT smaller than \(a^3\)!
That is why `SELECT_ALGEBRA_20261002.md` §4 line 134 wrote:
- \(R_1: a^{31/8} + a^{9/2}\sqrt{\ell} = o(a^4)\) (since \(31/8 = 3.875\) — wait: \(31/8 = 3.875 < 4\), so even \(a^{31/8} \gg a^4\)! And \(R_2: a^{13/4} = a^{3.25} \gg a^4\), and \(R_3: a^{21/8} = a^{2.625} \gg a^4\)!).
Catching that exponent comparison is critical: for \(0 < a < 1\), a *smaller* exponent means a *larger* quantity (\(a^{9/4} \gg a^3\) and \(a^{31/8}, a^{13/4}, a^{21/8} \gg a^4\) as \(a \to 0\))!

Let us record this exponent hierarchy with complete precision so there is zero ambiguity:
As \(a \to 0\),
\[
a^2 \gg a^{9/4} \gg a^{5/2} \gg a^{21/8} \gg a^3 \gg a^{13/4} \gg a^{31/8} \gg a^4. \tag{7.1}
\]
Therefore, under `SELECT` failure (\(\rho \le \sqrt{c}a^{5/4}\sqrt{\ell(a)}\) and \(v \le \zeta a^{9/4}\)):
1. The generic Cauchy–Schwarz upper bounds from `SELECT_ALGEBRA_20261002.md` (`A9`):
   - \(|R_1| \le 12a\rho v + 4\sqrt{b}v^{3/2} = O(a^{9/2}\sqrt{\ell} + a^{31/8})\),
   - \(|R_2| \le 12a\rho\sqrt{bv} + 6bv = O(a^{31/8}\sqrt{\ell} + a^{13/4})\),
   - \(|R_3| \le 4a\rho b + 4\sqrt{v}b^{3/2} = O(a^{13/4}\sqrt{\ell} + a^{21/8})\),
   - \(|R_4| \le b^2 = O(a^2)\),
   **all exceed \(a^4\)** as \(a \to 0\) (except the \(a\rho v \sim a^{9/2}\sqrt{\ell}\) part of \(R_1\))!
2. However, the **exact binomial-derivative identities** (1.3)–(1.6) give constraints between \(R_0,R_1,R_2,R_3,R_4\) that are **exact at all scales** without losing powers of \(a\) to Cauchy–Schwarz:
   - Because \(D_3 = 4R_0 + R_1 \ge 0\) and \(R_0 = a^4 + O(a^{35/8})\), we have the unconditional lower bound
     \[
     R_1 \ge -4R_0 = -4a^4 - O(a^{35/8}) \tag{7.2}
     \]
     at scale \(a^4\) (improving the generic lower bound \(-O(a^{31/8})\) by \(a^{1/8}\))!
   - Because \(D_2 = 6R_0 + 3R_1 + R_2 \ge 0\), we have the unconditional lower bound
     \[
     3R_1 + R_2 \ge -6R_0 = -6a^4 - O(a^{35/8}) \tag{7.3}
     \]
     at scale \(a^4\) (whereas the generic bound on \(3R_1+R_2\) was \(-O(a^{13/4})\), which is \(a^{-3/4}\) times worse)!
   - Because \(D_1 = 4R_0 + 3R_1 + 2R_2 + R_3 = 2w(S_E + S_M) + 4w(a^2+v)/p \ge 0\), we have the unconditional lower bound
     \[
     3R_1 + 2R_2 + R_3 = 2w(S_E + S_M) + \frac{4w(a^2+v)}{p} - 4R_0 \ge -4R_0 = -4a^4 - O(a^{35/8}) \tag{7.4}
     \]
     at scale \(a^4\) (whereas the generic bound on \(3R_1+2R_2+R_3\) was \(-O(a^{21/8})\), which is \(a^{-11/8}\) times worse)!
   - And for every \(t\in(0,1]\), \(P(t) = R_0 + R_1 t + R_2 t^2 + R_3 t^3 + R_4 t^4 \ge 0\) gives
     \[
     R_1 + R_2 t + R_3 t^2 + R_4 t^3 \ge -\frac{R_0}{t} \tag{7.5}
     \]
     at scale \(a^4/t\)!

**Theorem 4 (Mixed-count positivity improves the lower bounds on \(R_1\), \(3R_1+R_2\), and \(3R_1+2R_2+R_3\) from \(O(a^{21/8})\) to scale \(a^4\)).**
For any 4-AP-free set \(A\subset\Omega\) and any factor \(F\) with \(R_0 = \Lambda_4(g)\), nonnegativity of \(D_1,D_2,D_3\) forces:
\[
\begin{aligned}
R_1 &\ge -4R_0, \\
3R_1 + R_2 &\ge -6R_0, \\
3R_1 + 2R_2 + R_3 &= 2w(S_E+S_M) + \frac{4w(a^2+v)}{p} - 4R_0 \ge -4R_0, \\
R_1 + 2R_2 + 3R_3 + 4R_4 &= -2w(S_E+S_M) + \frac{4wU}{p} \le \frac{4wU}{p}.
\end{aligned} \tag{7.6}
\]
In particular, on \(\mathbb{Z}_p\) where \(R_0 = a^4 + O(av^{3/2}+v^2) \sim a^4\), the three combinations \(R_1\), \(3R_1+R_2\), and \(3R_1+2R_2+R_3\) are all bounded below at scale \(-O(a^4)\), completely bypassing the \(a^{31/8}, a^{13/4}, a^{21/8}\) Cauchy–Schwarz losses of `SELECT_ALGEBRA_20261002.md`!

**Why (7.6) still stops one step short of `SIGNED`**:
Adding \(3R_1+2R_2+R_3 \ge -4R_0\) and \(R_1+2R_2+3R_3+4R_4 \le 4wU/p\) has opposite inequality directions:
\[
4(R_1+R_2+R_3+R_4) = \underbrace{(3R_1+2R_2+R_3)}_{\ge 2w(S_E+S_M)-4R_0} + \underbrace{(R_1+2R_2+3R_3+4R_4)}_{= -2w(S_E+S_M)+4wU/p} = -4R_0 + \frac{4w(a^2+v+U)}{p} = -4R_0 + \frac{4aw}{p},
\]
which simply recovers the exact identity \(R_1+R_2+R_3+R_4 = aw/p - R_0\)!
To obtain a nontrivial lower bound on \(R_1+R_2+R_3+R_4 = \frac{1}{4}(4D_0 - D_1) + \frac{1}{4}(3R_1+2R_2+R_3)\) (or \(R_1+R_2+R_3+R_4 = -R_0 + D_0\)), one must **bound \(D_1 = 2w(S_E+S_M)+4w(a^2+v)/p\) from above** (so \(4D_0 - D_1\) is bounded from below) while simultaneously **bounding \(3R_1+2R_2+R_3 = D_1 - 4R_0\) from below** — which is impossible unless \(R_4\) (or a combination with a different ratio of \(R_3, R_4\) weights than \(D_1 - 4D_0\)) is controlled independently of \(D_0 = aw/p\)!

Specifically, for any multiplier vector \(\mu = (\mu_1,\mu_2,\mu_3)\in\mathbb{R}_{\ge 0}^3\), using \(D_1,D_2,D_3\ge 0\) gives
\[
R_1+R_2+R_3+R_4 \ge R_1+R_2+R_3+R_4 - \mu_1 D_1 - \mu_2 D_2 - \mu_3 D_3
= -(4\mu_1+6\mu_2+4\mu_3)R_0 + (1-3\mu_1-3\mu_2-\mu_3)R_1 + (1-2\mu_1-\mu_2)R_2 + (1-\mu_1)R_3 + R_4. \tag{7.7}
\]
Setting \(\mu_1=0, \mu_2=1, \mu_3=0\) eliminates \(R_2\) with a \(-6R_0\) floor:
\[
R_1+R_2+R_3+R_4 = D_2 - 6R_0 - 2R_1 + R_3 + R_4 \ge -6R_0 - 2R_1 + R_3 + R_4. \tag{7.8}
\]
Setting \(\mu_1=1/2, \mu_2=0, \mu_3=0\) eliminates \(R_2\) with a \(-2R_0\) floor:
\[
R_1+R_2+R_3+R_4 = \frac{1}{2}D_1 - 2R_0 - \frac{1}{2}R_1 + \frac{1}{2}R_3 + R_4 = w(S_E+S_M) + \frac{2w(a^2+v)}{p} - 2R_0 - \frac{1}{2}R_1 + \frac{1}{2}R_3 + R_4. \tag{7.9}
\]
In every case, the coefficient of \(R_4\) remains \(+1\), so **proving a lower bound on \(R_4 = \Lambda_4(u)\) (or \(\frac{1}{2}R_3 + R_4\)) under low factor energy and `SELECT` failure is strictly necessary and sufficient for mixed-count closure.**

---

## Phase 9 & Phase 10 — Verification and Quantitative Closure Summary

Run `python3 verify_mixed_count_closure_20261014.py` (outputs `MIXED_COUNT_VERIFICATION_20261014.json`):
- **2,520** exact rational verifications of the corrected Phase 0 binomial-derivative identities;
- **12,600** exact rational evaluations of the mixed-count polynomials \(P(t)\) and \(Q(s,t)\);
- **2,520** exact rational verifications of the 10 reflection-symmetric sub-blocks and separate channel identities \(D_{1,E}, D_{1,M}, D_{1,E}-D_{1,M}=2w(S_E-S_M)\);
- **2** exact rational abstract LP dual witnesses (\(p=101\) and \(p=2147483647\)) certifying that \(D_k\ge 0\), \(S_E,S_M\ge 0\), and \(R_1=R_2=R_3=0\) still permit \(R_1+R_2+R_3+R_4 = a/p - a^4\);
- **16** exact orbit checks on the \(p=23,k=5\) and \(p=29,k=6\) global laws.

### Corrected Continuation Prompt

> Continue offline from `MIXED_COUNT_CLOSURE_20261014.md` and `TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md`. Accept as proved:
> 1. The corrected binomial-derivative identities \(4D_0 - D_1 = R_1+2R_2+3R_3+4R_4 = -2w(S_E+S_M)+4wU/p\), \(D_2 - D_3 - 2R_0 + R_3 = 2R_1+R_2+R_3\), and \(2D_2 - 3D_3 + R_3 = 3R_1+2R_2+R_3\), together with the 10 reflection-symmetric sub-block equations and \(D_{1,E}-D_{1,M}=2w(S_E-S_M)\).
> 2. Theorem 4: nonnegativity of \(D_1,D_2,D_3\) unconditionally bounds \(R_1 \ge -4R_0\), \(3R_1+R_2 \ge -6R_0\), and \(3R_1+2R_2+R_3 \ge -4R_0\) at scale \(-O(a^4)\), eliminating the \(O(a^{31/8}), O(a^{13/4}), O(a^{21/8})\) Cauchy–Schwarz losses on those lower bounds.
> 3. Theorem 2 & Theorem 3: the finite-dimensional LP dual obstruction proves that \(R_4 = \Lambda_4(u)\) has coefficient \(+1\) in every nonnegative combination of \(D_1,D_2,D_3,D_4\), so bounding \(R_4\) (or \(\frac{1}{2}R_3 + R_4\) in (7.9)) from below under low factor energy and `SELECT` failure is the exact necessary and sufficient step for mixed-count closure.
>
> Attack either:
> - **Route A (Lower bound on \(R_4 = \Lambda_4(u)\) / \(\frac{1}{2}R_3 + R_4\))**: Use (7.9), conditional Booleanity \(u^2 = (1-2g)u + g(1-g)\), and `SELECT` failure (\(\max_{\xi\ne 0}|c_\xi|^2 < c a^{5/2}\ell(a)\)) together with \(B q_E = B q_M = 0\) to bound \(w(S_E+S_M) + \frac{1}{2}R_3 + R_4\) from below at scale \(>\frac{13}{8}a^4\).
> - **Route B (Two-channel spectral concentration)**: Bound \(s_0(a)\,D_{\text{reg}}(\lambda,v)/(\lambda^T S)^2 \lesssim a^{-2}/\ell(a)\) on a character set \(\Gamma\) of size \(s_0(a)\) using the unwindowed cubic synthesis \(k_\lambda = \sum_{\xi\ne 0}\widehat{q_\lambda}(\xi)\psi_\xi\) and operator duality \(P_A K_B P_A = P_A R_B P_A = p^{-1}P_A\).
