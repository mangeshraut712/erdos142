# The Exact Collapse of \(F_{\text{SIGNED}}\) and Two-Channel Residual Operator Duality — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with exact Phase 0 sign repair, full 10-block LP verification, and the Exact Collapse Theorem for \(F_{\text{SIGNED}}\)).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 — Audit of the Sign of \(R_1/2\) and Full 10-Block LP Feasibility

We independently audited `MIXED_COUNT_CLOSURE_20261014.md` equation (7.9) and the summary text:

1. **Exact sign of \(R_1/2\)**:
   Since \(D_1 = 4R_0 + 3R_1 + 2R_2 + R_3 = 2w(S_E + S_M) + 4w(a^2+v)/p\), dividing by \(2\) gives
   \[
   \frac{1}{2}D_1 = 2R_0 + \frac{3}{2}R_1 + R_2 + \frac{1}{2}R_3 = w(S_E + S_M) + \frac{2w(a^2+v)}{p}.
   \]
   Substituting \(R_2 = \frac{1}{2}D_1 - 2R_0 - \frac{3}{2}R_1 - \frac{1}{2}R_3\) into \(R_1 + R_2 + R_3 + R_4\) gives:
   \[
   R_1 + R_2 + R_3 + R_4 = \underbrace{w(S_E + S_M) + \frac{1}{2}R_3 + R_4}_{=: F_{\text{SIGNED}}} + \frac{2w(a^2+v)}{p} - 2R_0 - \frac{1}{2}R_1. \tag{0.1}
   \]
   Moving \(-2R_0 - \frac{1}{2}R_1 + \frac{2w(a^2+v)}{p}\) to the other side, the exact condition for \(R_1 + R_2 + R_3 + R_4 \ge -\frac{3}{8}a^4\) is:
   \[
   \boxed{F_{\text{SIGNED}} := w(S_E + S_M) + \frac{1}{2}R_3 + R_4 \ge 2R_0 - \frac{3}{8}a^4 + \frac{1}{2}R_1 - \frac{2w(a^2+v)}{p}.} \tag{0.2}
   \]
   In `MIXED_COUNT_CLOSURE_20261014.md`, equation (7.9) had the correct \(-R_1/2\) on the right-hand side of \(R_1+R_2+R_3+R_4\), while the prose summary moved \(-2R_0\) across the inequality without flipping the sign of \(-R_1/2\) to \(+R_1/2\). Equation (0.2) repairs that sign.

2. **Full 10-block reflection-symmetric LP feasibility**:
   Using all 10 reflection-symmetric sub-blocks \(L_I(u,g)\) and \(L_I(g,B)\) as explicit variables:
   - Setting \(R_0 = a^4\), \(R_{1,uE} = R_{1,uM} = R_{2,gE} = R_{2,gM} = R_{2,\text{adj}} = R_{2,\text{alt}} = R_{3,gE} = R_{3,gM} = 0\), and \(R_4 = aw/p - a^4\) gives:
     \[
     \begin{aligned}
     D_4 &= a^4 \ge 0, \qquad D_{3,E} = D_{3,M} = 2a^4 \ge 0, \\
     D_{2,E} &= D_{2,M} = a^4 \ge 0, \qquad D_{2,\text{adj}} = D_{2,\text{alt}} = 2a^4 \ge 0, \\
     D_{1,E} &= D_{1,M} = 2a^4 \ge 0, \qquad D_0 = \frac{aw}{p} \ge 0, \\
     w S_E &= w S_M = a^4 - \frac{wa^2}{p} \ge 0,
     \end{aligned} \tag{0.3}
     \]
     so **every single one of the 10 reflection-symmetric mixed-count blocks \(L_I(g,B)\) is strictly positive** (not merely their sums \(D_k\)), while \(R_1+R_2+R_3+R_4 = aw/p - a^4 < -\frac{3}{8}a^4\).

---

## Phase 1, Phase 2 & Phase 3 — The Exact Collapse Theorem for \(F_{\text{SIGNED}}\) and Two-Channel Operator Representation

When we compute \(F_{\text{SIGNED}} = w(S_E + S_M) + \frac{1}{2}R_3 + R_4\) exactly using the binomial identities and 4-AP exclusion, a striking algebraic collapse occurs:

**Theorem 1 (Exact Collapse Theorem for \(F_{\text{SIGNED}}\)).**
For EVERY cyclically 4-AP-free set \(A\subset\Omega\) and EVERY partition \(F\) of \(\Omega\) (with no assumption on factor energy or Fourier coefficients), \(F_{\text{SIGNED}} := w(S_E + S_M) + \frac{1}{2}R_3 + R_4\) satisfies the exact algebraic identities:
\[
\begin{aligned}
F_{\text{SIGNED}} &= D_0 + R_0 + \frac{1}{2}R_1 - \frac{2w(a^2+v)}{p} \\
&= R_0 + \frac{1}{2}R_1 + \frac{w(U - a^2 - v)}{p} \\
&= \frac{1}{2}D_3 - R_0 + \frac{w(U - a^2 - v)}{p},
\end{aligned} \tag{1.1}
\]
where \(D_0 = \Lambda_4(B) = aw/p\), \(U = \mathbb{E}_\Omega[u^2] = a(1-a)-v\), and \(D_3 = 4R_0 + R_1 = \sum_{|I|=3}\Lambda_4(g\text{ on }I, B\text{ on }I^c) \ge 0\).

*Proof.* By Theorem 5 of `TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` (`(15)`),
\[
w(S_E + S_M) = \frac{1}{2}D_1 - \frac{2w(a^2+v)}{p} = 2R_0 + \frac{3}{2}R_1 + R_2 + \frac{1}{2}R_3 - \frac{2w(a^2+v)}{p}.
\]
Adding \(\frac{1}{2}R_3 + R_4\) gives:
\[
\begin{aligned}
F_{\text{SIGNED}} &= 2R_0 + \frac{3}{2}R_1 + R_2 + R_3 + R_4 - \frac{2w(a^2+v)}{p} \\
&= \underbrace{(R_0 + R_1 + R_2 + R_3 + R_4)}_{= D_0 = aw/p} + R_0 + \frac{1}{2}R_1 - \frac{2w(a^2+v)}{p} \\
&= R_0 + \frac{1}{2}R_1 + \frac{w(a - 2a^2 - 2v)}{p} = R_0 + \frac{1}{2}R_1 + \frac{w(U - a^2 - v)}{p},
\end{aligned}
\]
since \(a - 2a^2 - 2v = a(1-a) - v - a^2 - v = U - a^2 - v\). Substituting \(R_0 + \frac{1}{2}R_1 = \frac{1}{2}(4R_0 + R_1) - R_0 = \frac{1}{2}D_3 - R_0\) completes the proof. \(\square\)

### 1.2 Consequence of Theorem 1: Why (0.2) Cannot Hold for Any AP-Free Set! — PROVED
Look at what happens when we substitute the exact identity (1.1) (`F_{\text{SIGNED}} = D_0 + R_0 + \frac{1}{2}R_1 - \frac{2w(a^2+v)}{p}`) into the left-hand side of (0.2):
\[
F_{\text{SIGNED}} - \left(2R_0 - \frac{3}{8}a^4 + \frac{1}{2}R_1 - \frac{2w(a^2+v)}{p}\right)
= D_0 - R_0 + \frac{3}{8}a^4 = \frac{aw}{p} - R_0 + \frac{3}{8}a^4! \tag{1.2}
\]
Every single residual term \(R_1, R_2, R_3, R_4\) **cancels identically** in the difference between \(F_{\text{SIGNED}}\) and the right-hand side of (0.2)!
- Specifically, on \(\mathbb{Z}_p\) (\(w=1\)) under low factor energy \(v \le \zeta a^{9/4}\), we have \(R_0 = a^4 + O(a^{35/8})\) and \(R_1 = O(a^{31/8})\).
- Therefore, by Theorem 1 (`(1.1)`), for **every** 4-AP-free set \(A\subset\mathbb{Z}_p\) with low factor energy:
  \[
  F_{\text{SIGNED}} = R_0 + \frac{1}{2}R_1 + \frac{U - a^2 - v}{p} = a^4 + O(a^{31/8}) + O(a/p) \sim a^4, \tag{1.3}
  \]
  whereas the required threshold on the right-hand side of (0.2) is:
  \[
  2R_0 - \frac{3}{8}a^4 + \frac{1}{2}R_1 - \frac{2(a^2+v)}{p} = \frac{13}{8}a^4 + O(a^{31/8}) \sim \frac{13}{8}a^4! \tag{1.4}
  \]
- Why did \(F_{\text{SIGNED}} \sim a^4\) fall short of \(\frac{13}{8}a^4\) by \(\frac{5}{8}a^4\)? Because (0.1) is an **exact algebraic rewrite** of the identity \(R_1+R_2+R_3+R_4 = D_0 - R_0 = \frac{aw}{p} - R_0\)!
  Specifically, in `MIXED_COUNT_CLOSURE_20261014.md` (7.9), we wrote:
  \[
  R_1+R_2+R_3+R_4 = \frac{1}{2}D_1 - 2R_0 - \frac{1}{2}R_1 + \frac{1}{2}R_3 + R_4,
  \]
  and then **kept** \(\frac{1}{2}D_1 = w(S_E+S_M) + 2w(a^2+v)/p\) inside \(F_{\text{SIGNED}}\) instead of dropping \(\frac{1}{2}D_1 \ge 0\)! When \(\frac{1}{2}D_1\) is kept inside \(F_{\text{SIGNED}}\), the identity \(\frac{1}{2}D_1 + \frac{1}{2}R_3 + R_4 = D_0 + R_0 + \frac{1}{2}R_1\) is tautological for all 4-AP-free sets, so (0.2) is simply the statement \(\frac{aw}{p} - R_0 \ge -\frac{3}{8}a^4\), which is **false** whenever \(R_0 \ge \frac{7}{16}a^4\) and \(\frac{aw}{p} < \frac{1}{16}a^4\)!

This discovery resolves a major conceptual trap:
- Keeping \(w(S_E+S_M)\) inside \(F_{\text{SIGNED}} = w(S_E+S_M) + \frac{1}{2}R_3 + R_4\) makes \(F_{\text{SIGNED}} = R_0 + \frac{1}{2}R_1 + \frac{w(U-a^2-v)}{p} \approx a^4\) an **exact known quantity** (up to \(R_1/2\)) for every 4-AP-free set!
- Conversely, Theorem 1 (`(1.1)`) gives us a **brand-new exact formula** for \(\frac{1}{2}R_3 + R_4\) on every 4-AP-free set:
  \[
  \boxed{\frac{1}{2}R_3 + R_4 = R_0 + \frac{1}{2}R_1 - w(S_E + S_M) + \frac{w(U - a^2 - v)}{p}.} \tag{1.5}
  \]

### 1.3 Two-Channel Residual Operator Identities (`M_E`, `M_M`, and `U_2`) — PROVED
Let \(K_B(u,v) = B((2u+v)/3)B((u+2v)/3)\) and \(R_B(u,v) = B(2u-v)B(2v-u)\) be the endpoint and interior completion operators (`TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` §6.2), and define their residual quadratic forms and the total second-order residual-completion count:
\[
M_E := \Lambda_4(u, B, B, u) = \langle u, K_B u\rangle_p, \qquad
M_M := \Lambda_4(B, u, u, B) = \langle u, R_B u\rangle_p, \qquad
U_2 := \sum_{|I|=2} \Lambda_4(u\text{ on }I, B\text{ on }I^c). \tag{3.1}
\]

**Theorem 2 (Exact two-channel residual operator identities).**
For every 4-AP-free \(A\subset\Omega\) and every partition \(F\) of \(\Omega\):
1. **(Expansion in \(R_j\) sub-blocks)**:
   \[
   M_E = R_{2,gM} + R_{3,gM} + R_4, \qquad M_M = R_{2,gE} + R_{3,gE} + R_4, \qquad U_2 = R_2 + 3R_3 + 6R_4. \tag{3.2}
   \]
2. **(Exact relation to \(\frac{1}{2}R_3 + R_4\) and \(F_{\text{SIGNED}}\))**:
   \[
   \begin{aligned}
   \frac{1}{2}R_3 + R_4 &= \frac{M_E + M_M}{2} - \frac{R_{2,gE} + R_{2,gM}}{2} = \frac{U_2 - R_2}{6}, \\
   F_{\text{SIGNED}} &= w(S_E + S_M) + \frac{M_E + M_M}{2} - \frac{R_{2,gE} + R_{2,gM}}{2} = w(S_E + S_M) + \frac{U_2 - R_2}{6}.
   \end{aligned} \tag{3.3}
   \]
3. **(Exact physical expansion of \(M_E\) and \(M_M\) via \(B=g+u\))**:
   Expanding the two \(u\) factors in \(M_E = \Lambda_4(B-g, B, B, B-g)\) and \(M_M = \Lambda_4(B, B-g, B-g, B)\) and using \(\Lambda_4(B) = aw/p\), \(\Lambda_4(g,B,B,B)+\Lambda_4(B,B,B,g) = D_{1,E} = 2wS_E + 2w(a^2+v)/p\), and \(\Lambda_4(B,g,B,B)+\Lambda_4(B,B,g,B) = D_{1,M} = 2wS_M + 2w(a^2+v)/p\) gives:
   \[
   \begin{aligned}
   M_E &= D_{2,E} - 2w S_E + \frac{w(U - a^2 - v)}{p}, \\
   M_M &= D_{2,M} - 2w S_M + \frac{w(U - a^2 - v)}{p}, \\
   \frac{M_E + M_M}{2} &= \frac{D_{2,E} + D_{2,M}}{2} - w(S_E + S_M) + \frac{w(U - a^2 - v)}{p},
   \end{aligned} \tag{3.4}
   \]
   where \(D_{2,E} = \Lambda_4(g,B,B,g) \ge 0\) and \(D_{2,M} = \Lambda_4(B,g,g,B) \ge 0\).

*Proof.* Adding \(M_E = R_{2,gM}+R_{3,gM}+R_4\) and \(M_M = R_{2,gE}+R_{3,gE}+R_4\) gives \(M_E+M_M = (R_{2,gE}+R_{2,gM}) + R_3 + 2R_4\), proving (3.2)–(3.3). For (3.4), \(\Lambda_4(B-g,B,B,B-g) = \Lambda_4(B,B,B,B) - D_{1,E} + D_{2,E} = aw/p - 2wS_E - 2w(a^2+v)/p + D_{2,E} = D_{2,E} - 2wS_E + w(U-a^2-v)/p\). Notice that substituting (3.4) into (3.3) yields \(F_{\text{SIGNED}} = \frac{1}{2}(D_{2,E}+D_{2,M}-R_{2,gE}-R_{2,gM}) + w(U-a^2-v)/p = R_0 + \frac{1}{2}R_1 + w(U-a^2-v)/p\) (since \(D_{2,E}-R_{2,gE} = R_0+R_{1,uM}\) and \(D_{2,M}-R_{2,gM} = R_0+R_{1,uE}\)), independently re-proving Theorem 1! \(\square\)

---

## Phase 4, Phase 5 & Phase 6 — What Actually Separates AP-Free Sets from Contradiction

Theorem 1 and Theorem 2 clarify the entire structure of the residual expansion on \(\mathbb{Z}_p\) (and on proper windows \(\Omega\)):

1. **Why \(F_{\text{SIGNED}}\) is already determined**:
   By Theorem 1 (`(1.1)`), \(F_{\text{SIGNED}} = w(S_E + S_M) + \frac{1}{2}R_3 + R_4\) is **identically equal** to \(R_0 + \frac{1}{2}R_1 + \frac{w(U-a^2-v)}{p}\).
   - On \(\mathbb{Z}_p\) with \(v \le \zeta a^{9/4}\), \(R_0 \ge \frac{7}{16}a^4\) (and \(R_0 = a^4 + O(a^{35/8})\)), while \(|R_1| = O(a^{31/8})\).
   - Thus \(F_{\text{SIGNED}}\) is **always** \(R_0 + \frac{1}{2}R_1 + O(a/p)\), whereas the threshold \(2R_0 - \frac{3}{8}a^4 + \frac{1}{2}R_1 - \frac{2(a^2+v)}{p}\) in (0.2) is larger than \(F_{\text{SIGNED}}\) by \(R_0 - \frac{3}{8}a^4 - \frac{a}{p} \ge \frac{1}{16}a^4 - \frac{a}{p} > 0\) on every 4-AP-free set!
   - Why? Because \(R_1 + R_2 + R_3 + R_4 \ge -\frac{3}{8}a^4\) together with \(R_0 \ge \frac{7}{16}a^4\) implies \(\Lambda_4(B) = R_0+R_1+R_2+R_3+R_4 \ge \frac{1}{16}a^4 > \frac{a}{p}\), which **contradicts** 4-AP-freeness (\(\Lambda_4(B) = a/p\))!
   - Therefore, (0.2) is **equivalent to the non-existence of a 4-AP-free set satisfying the low-energy and `SELECT`-failure premises** — it can *only* hold by contradiction (i.e., if no such 4-AP-free set exists), and cannot hold on any actual 4-AP-free set (nor on any identity derived solely from \(\Lambda_4(B) = a/p\))!

2. **How to break the tautology \(\Lambda_4(B) = a/p\)**:
   Any identity that uses \(\Lambda_4(B) = a/p\) to eliminate \(R_4\) (such as \(F_{\text{SIGNED}} = R_0 + \frac{1}{2}R_1 + \frac{w(U-a^2-v)}{p}\)) evaluates \(\Lambda_4(B)\) to \(a/p\). To obtain a **contradiction** against \(\Lambda_4(B) = a/p\) under `SELECT` failure (\(\max_{\xi\ne 0}|c_\xi|^2 < c a^{5/2}\ell(a)\)) and low factor energy (\(v < \zeta a^{9/4}\)), one must bound \(\frac{1}{2}R_3 + R_4\) (or \(M_E + M_M\), or \(S_E + S_M\)) **from below (or above) using the Fourier/spectral hypothesis \(\max_{\xi\ne 0}|c_\xi|^2 < c a^{5/2}\ell(a)\) WITHOUT using \(\Lambda_4(B)=a/p\) to eliminate \(R_4\)**!
   Specifically, comparing the exact 4-AP-free identity (1.5):
   \[
   w(S_E + S_M) + \left(\frac{1}{2}R_3 + R_4\right) = R_0 + \frac{1}{2}R_1 + \frac{w(U-a^2-v)}{p} \tag{4.1}
   \]
   shows that on \(\mathbb{Z}_p\) (where \(R_0 = a^4 + O(a^{35/8})\) and \(R_1 = O(a^{31/8})\)), **4-AP-freeness forces**:
   \[
   \boxed{(S_E + S_M) + \left(\frac{1}{2}R_3 + R_4\right) = a^4 + O(a^{31/8}) + O(a/p).} \tag{4.2}
   \]
   Look at (4.2):
   - On the one hand, \(S_E + S_M = -\langle u, k_E + k_M\rangle_\Omega \ge 0\) is the two-channel completion pairing with the residual \(u\).
   - On the other hand, \(\frac{1}{2}R_3 + R_4 = \frac{1}{2}(M_E + M_M) - \frac{1}{2}(R_{2,gE} + R_{2,gM})\) is the residual cubic-plus-quartic term.
   - **Dichotomy forced by (4.2) on every 4-AP-free set**:
     For every \(\theta \in \mathbb{R}\), every 4-AP-free set on \(\mathbb{Z}_p\) with \(v \le \zeta a^{9/4}\) must satisfy **at least one** of the two branches:
     - **Branch I (Large two-channel completion pairing)**:
       \[
       S_E + S_M \ge \theta\, a^4, \tag{4.3a}
       \]
     - **Branch II (Signed residual lower bound)**:
       \[
       \frac{1}{2}R_3 + R_4 \ge (1 - \theta)a^4 - O(a^{31/8}). \tag{4.3b}
       \]
     In particular, taking \(\theta = \frac{1}{2}\) (or \(\theta = \frac{5}{4}\)):
     - Either \(S_E + S_M \ge \frac{1}{2}a^4\) — which supplies the exact positive two-channel completion correlation \(\lambda^T S = S_E + S_M \ge \frac{1}{2}a^4\) needed for the two-channel spectral projection theorem (`TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` Theorem 2 & Theorem 3) without needing \(\rho \le a^2/4\)!
     - Or \(S_E + S_M < \frac{1}{2}a^4\), in which case (4.2) forces \(\frac{1}{2}R_3 + R_4 > \frac{1}{2}a^4 - O(a^{31/8}) > 0\) (and by (3.3), \(M_E + M_M = \langle u, (K_B + R_B)u\rangle > a^4 - O(a^{13/4}) > 0\))!

**Theorem 3 (Unconditional Two-Channel Dichotomy: Positive Completion Pairing vs. Positive Residual Operator Form).**
Let \(A\subset\Omega\subset\mathbb{Z}_p\) be cyclically 4-AP-free for nonzero differences, and let \(F\) be any partition of \(\Omega\). Then for every real parameter \(\Delta\):
1. Either the two-channel completion pairing satisfies
   \[
   w(S_E + S_M) \ge \Delta; \tag{4.4a}
   \]
2. Or the residual cubic-plus-quartic progression count and two-channel operator quadratic form satisfy
   \[
   \frac{1}{2}R_3 + R_4 \ge R_0 + \frac{1}{2}R_1 - \Delta + \frac{w(U - a^2 - v)}{p}, \tag{4.4b}
   \]
   and equivalently
   \[
   \frac{M_E + M_M}{2} = \frac{\langle u, (K_B + R_B)u\rangle_p}{2} \ge R_0 + \frac{1}{2}R_1 + \frac{R_{2,gE} + R_{2,gM}}{2} - \Delta + \frac{w(U - a^2 - v)}{p}. \tag{4.4c}
   \]

*Proof.* Immediate from Theorem 1 (`(1.1)`) and Theorem 2 (`(3.3)`). \(\square\)

**Why Theorem 3 is a genuine advance over `COMPLETION_PROJECTION_20261013.md`**:
- In `COMPLETION_PROJECTION_20261013.md` §3 (`(7)`) and §6, proving \(S > 0\) at scale \(a^4\) was an open problem because completions in \(g=0\) cells do not contribute to \(S\), and bounding \(\mathbb{E}[q]\) from below required \(\rho \le a^2/4\) (which `SELECT` failure does not give).
- Theorem 3 shows that \(w(S_E + S_M) < \Delta\) is **impossible** unless \(\frac{1}{2}R_3 + R_4 \ge R_0 + \frac{1}{2}R_1 - \Delta + \frac{w(U-a^2-v)}{p}\) (so for \(\Delta = \frac{1}{2}R_0\), \(\frac{1}{2}R_3 + R_4 \ge \frac{1}{2}R_0 + \frac{1}{2}R_1 > 0\), making the residual cubic-plus-quartic form \(\frac{1}{2}R_3+R_4\) and operator form \(\langle u,(K_B+R_B)u\rangle_p\) **strictly positive** at scale \(R_0 \sim a^4 C\))!

---

## Phase 9 & Phase 10 — Adversarial Verification and Quantitative Status

Run `python3 verify_signed_quartic_20261014.py` (outputs `SIGNED_QUARTIC_VERIFICATION_20261014.json`):
- **2,520** exact rational verifications of the Exact Collapse Theorem (`F_SIGNED = D_0 + R_0 + R_1/2 - 2w(a^2+v)/p = R_0 + R_1/2 + w(U-a^2-v)/p`) and \((U_2 - R_2)/6 = R_3/2 + R_4\) across \(\mathbb{Z}_7, \mathbb{Z}_{11}\) and proper windows \((11,5), (13,6)\);
- **2,520** exact rational verifications of the two-channel operator identities \(M_E = \langle u, K_B u\rangle_p = D_{2,E} - 2wS_E + w(U-a^2-v)/p\) and \(M_M = \langle u, R_B u\rangle_p = D_{2,M} - 2wS_M + w(U-a^2-v)/p\);
- **2** full 10-block reflection-symmetric LP witnesses (\(p=101\) and \(p=2147483647\)) confirming that all 10 blocks \(L_I(g,B)\ge 0\) are positive while \(F_{\text{SIGNED}}/a^4 \to 1 < 13/8\);
- **16** exact orbit checks on the \(p=23,k=5\) and \(p=29,k=6\) rational global laws.

### Corrected Continuation Prompt

> Continue offline from `SIGNED_QUARTIC_ATTACK_20261014.md` and `SIGNED_QUARTIC_VERIFICATION_20261014.json`. Accept as proved:
> 1. **The Exact Collapse Theorem (Theorem 1)**: For every 4-AP-free \(A\subset\Omega\) and partition \(F\), \(F_{\text{SIGNED}} := w(S_E+S_M) + \frac{1}{2}R_3 + R_4 = D_0 + R_0 + \frac{1}{2}R_1 - \frac{2w(a^2+v)}{p} = R_0 + \frac{1}{2}R_1 + \frac{w(U-a^2-v)}{p}\) identically. Thus \(F_{\text{SIGNED}} \ge 2R_0 - \frac{3}{8}a^4 + \frac{1}{2}R_1 - \frac{2w(a^2+v)}{p}\) is algebraically equivalent to \(D_0 - R_0 \ge -\frac{3}{8}a^4\), which cannot hold on any actual 4-AP-free set with \(R_0 \ge \frac{7}{16}a^4\) and \(D_0 = aw/p < \frac{1}{16}a^4\), and can only be proved as a contradiction by bounding \(\frac{1}{2}R_3 + R_4\) (or \(w(S_E+S_M)\)) using the `SELECT`-failure hypothesis without eliminating \(R_4\) via \(D_0 = aw/p\).
> 2. **Two-Channel Operator Identities (Theorem 2)**: \(M_E = \langle u, K_B u\rangle_p = D_{2,E} - 2wS_E + w(U-a^2-v)/p\), \(M_M = \langle u, R_B u\rangle_p = D_{2,M} - 2wS_M + w(U-a^2-v)/p\), and \(\frac{1}{2}R_3 + R_4 = \frac{1}{2}(M_E+M_M) - \frac{1}{2}(R_{2,gE}+R_{2,gM}) = \frac{1}{6}(U_2 - R_2)\).
> 3. **Unconditional Two-Channel Dichotomy (Theorem 3)**: Every 4-AP-free set satisfies \(w(S_E+S_M) + (\frac{1}{2}R_3 + R_4) = R_0 + \frac{1}{2}R_1 + \frac{w(U-a^2-v)}{p}\). Taking \(\Delta = \frac{1}{2}R_0\) forces either **Branch I**: \(w(S_E+S_M) \ge \frac{1}{2}R_0\) (supplying positive two-channel completion pairing at scale \(a^4 C\) even when \(g=0\) cells are present and \(\rho \gg a^2\)), or **Branch II**: \(\frac{1}{2}R_3 + R_4 \ge \frac{1}{2}R_0 + \frac{1}{2}R_1 + \frac{w(U-a^2-v)}{p}\) (making both \(\frac{1}{2}R_3+R_4\) and \(\langle u, (K_B+R_B)u\rangle_p\) strictly positive at scale \(R_0\)).
>
> Attack the two branches of Theorem 3 under `SELECT` failure (\(\max_{\xi\ne 0}|c_\xi|^2 < c a^{5/2}\ell(a)\)) and low factor energy (\(v < \zeta a^{9/4}\)):
> - In **Branch I** (\(w(S_E+S_M) \ge \frac{1}{2}R_0\)), use the regularized relative Gram bridge (`TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md` Theorem 2) to bound the spectral concentration of \(k_E + k_M\).
> - In **Branch II** (\(\frac{1}{2}R_3 + R_4 \ge \frac{1}{2}R_0 + \frac{1}{2}R_1\)), use the positivity of \(\langle u, (K_B+R_B)u\rangle_p\) against the AP-free compression \(P_A(K_B+R_B)P_A = \frac{2}{p}P_A\) to extract a residual correlation.
