# Auditing and Repairing the Two-Channel Dichotomy and Closing Analysis of Branches I & II — 14 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM** (with Phase 0 repair of the \(R_1\) scale issue in the dichotomy, exact operator block cancellation in `TWO_CHANNEL_OPERATOR_BLOCKS_20261014.md`, and sharp quantitative isolation of the remaining Branch I & II sublemmas).
Offline. No internet was used and no literature novelty is claimed. `SELECT`, `WSELECT`, `SIGNED`, and the unconditional local target \(r_4(N)=o(N/\log N)\) remain unresolved.

---

## Phase 0 & Phase 1 — Audit of the October 14 Dichotomy and Repair of the \(R_1\) Scale Issue

### 0.1 Why \(|R_1| = O(a^{31/8})\) does NOT make \(T = R_0 + \frac{1}{2}R_1 + \frac{w(U-a^2-v)}{p}\) positive at scale \(a^4\)
In `SIGNED_QUARTIC_ATTACK_20261014.md` Theorem 1 & Theorem 3, we proved the exact identity:
\[
\underbrace{w(S_E + S_M)}_{=: X} + \underbrace{\left(\frac{1}{2}R_3 + R_4\right)}_{=: Y} = \underbrace{R_0 + \frac{1}{2}R_1 + \frac{w(U - a^2 - v)}{p}}_{=: T}. \tag{0.1}
\]
We now audit the scale of \(T\) as \(a \to 0\) under low factor energy \(v \le \zeta a^{9/4}\):
1. **For the trivial factor \(F=\{\Omega\}\) (\(g \equiv a\), \(v=0\))**:
   Here \(R_1 = 0\) **identically** on \(\mathbb{Z}_p\)! Thus \(T = a^4 + \frac{a(1-2a)}{p} \sim a^4\) is genuinely positive at scale \(a^4\) with zero \(R_1\) error.
2. **For a general intermediate factor \(F\) with \(0 < v \le \zeta a^{9/4}\)**:
   The generic Cauchy–Schwarz bound from `SELECT_ALGEBRA_20261002.md` (`A9`) gives
   \[
   |R_1| \le 12a\rho v + 4\sqrt{b}v^{3/2} = O(a^{9/2}\sqrt{\ell} + a^{31/8}).
   \]
   Because \(31/8 = 3.875 < 4\), \(a^{31/8} \gg a^4\) as \(a \to 0\)! Therefore, \(|R_1| = O(a^{31/8})\) **does not** imply \(R_1 = o(a^4)\), and if \(R_1\) were as negative as \(-2R_0\), \(T = R_0 + \frac{1}{2}R_1 + O(w a/p)\) could vanish or become negative (down to \(-R_0\), since \(D_3 = 4R_0 + R_1 \ge 0\) only guarantees \(R_1 \ge -4R_0\), i.e. \(T \ge -R_0 + O(w a/p)\))!

### 1.1 Repairing the Dichotomy: Three Exact Unconditional Formulations — PROVED
Using the nonnegative mixed progression counts \(D_3 = 4R_0 + R_1 \ge 0\) and \(D_2 = 6R_0 + 3R_1 + R_2 \ge 0\), we repair the dichotomy in three ways so that no false \(R_1 = o(a^4)\) assumption is ever made:

**Theorem 1 (Repaired Unconditional Two-Channel Dichotomies).**
Let \(A\subset\Omega\subset\mathbb{Z}_p\) be cyclically 4-AP-free for nonzero differences, let \(F\) be any partition of \(\Omega\), and set \(X = w(S_E + S_M) \ge 0\) and \(Y = \frac{1}{2}R_3 + R_4\). Then:
1. **(Exact \(R_1\)-free conservation law)**: Moving \(\frac{1}{2}R_1\) to the left-hand side gives an identity whose right-hand side is **strictly positive at scale \(R_0 \sim a^4 C\)** for every factor \(F\):
   \[
   \boxed{X + \left(Y - \frac{1}{2}R_1\right) = R_0 + \frac{w(U - a^2 - v)}{p}.} \tag{1.1}
   \]
   Consequently, for any \(\theta\in(0,1)\) (e.g. \(\theta=1/2\)), every 4-AP-free set satisfies either
   \[
   \text{(Branch I)}:\quad X = w(S_E + S_M) \ge \theta R_0, \qquad\text{or}\qquad
   \text{(Branch IIa)}:\quad \frac{1}{2}R_3 + R_4 - \frac{1}{2}R_1 \ge (1-\theta)R_0 + \frac{w(U - a^2 - v)}{p}. \tag{1.2}
   \]
2. **(Positive-baseline dichotomy via \(D_3 = 4R_0 + R_1 \ge 0\))**: Adding \(2R_0\) to both sides of \(X + Y = T\) uses \(3R_0 + \frac{1}{2}R_1 = R_0 + \frac{1}{2}D_3 \ge R_0\) to eliminate any negative contribution from \(R_1\) unconditionally:
   \[
   \boxed{X + (Y + 2R_0) = R_0 + \frac{1}{2}D_3 + \frac{w(U - a^2 - v)}{p} \ge R_0 + \frac{w(U - a^2 - v)}{p}.} \tag{1.3}
   \]
   In this form, however, \(Y + 2R_0 = 2R_0 + \frac{1}{2}R_3 + R_4 \ge \frac{1}{2}R_0\) only forces \(\frac{1}{2}R_3 + R_4 \ge -\frac{3}{2}R_0\).
3. **(Exact three-way dichotomy isolating the \(R_1\) branch)**: For any fixed \(c_0 \in (0, 1/2)\) (e.g. \(c_0 = 1/4\)), every 4-AP-free set \(A\subset\Omega\) satisfies **at least one** of the three unconditional alternatives at scale \(R_0 \sim a^4 C\):
   - **Branch I (Large two-channel completion pairing)**:
     \[
     w(S_E + S_M) \ge c_0 R_0; \tag{1.4a}
     \]
   - **Branch II (Genuinely positive cubic-plus-quartic residual & operator form)**:
     \[
     \frac{1}{2}R_3 + R_4 \ge c_0 R_0 + \frac{w(U - a^2 - v)}{p} \quad \left(\text{and}\quad \frac{M_E + M_M}{2} \ge c_0 R_0 + \frac{R_{2,gE} + R_{2,gM}}{2} + \frac{w(U - a^2 - v)}{p}\right); \tag{1.4b}
     \]
   - **Branch III (Large negative linear-residual count \(R_1\))**:
     \[
     R_1 \le -2(1 - 2c_0)R_0 \quad \left(\text{so } |R_1| \ge 2(1 - 2c_0)R_0 \text{ and } D_3 \le 2(1 + 2c_0)R_0\right). \tag{1.4c}
     \]
   Moreover, whenever \(\operatorname{Var}_\Omega(g) = v \le c_1 a^{8/3}\) (which includes the trivial factor \(v=0\) and any factor with variance below \(O(a^{8/3})\), where \(4\sqrt{b}v^{3/2} = O(a^{1/2 + 4}) = O(a^{9/2}) = o(a^4)\)), **Branch III is impossible** under `SELECT` failure, reducing (1.4) to the strict two-way positive dichotomy (1.4a) vs (1.4b)!

*Proof.* (1.1) and (1.3) follow directly from (0.1) and \(D_3 = 4R_0 + R_1 \ge 0\). For (1.4), if (1.4a) and (1.4b) both fail, then \(X + Y < 2c_0 R_0 + \frac{w(U-a^2-v)}{p}\), so \(R_0 + \frac{1}{2}R_1 < 2c_0 R_0\), giving \(R_1 < -2(1-2c_0)R_0\). Finally, by `SELECT_ALGEBRA_20261002.md` (`A9`), \(|R_1| \le 12a\rho v + 4\sqrt{b}v^{3/2}\); when \(v = o(a^{7/3})\), \(\sqrt{b}v^{3/2} = o(a^4)\) and \(a\rho v = o(a^4)\), so \(|R_1| = o(a^4) < 2(1-2c_0)R_0\), ruling out (1.4c). \(\square\)

---

## Phase 5, Phase 6 & Phase 7 — Analysis of Branch I and Branch II Closure

### 5.1 What happens in Branch II (\(\frac{1}{2}R_3 + R_4 \ge c_0 R_0\)) using the Operator Block Decomposition
Suppose Branch II holds: \(Y = \frac{1}{2}R_3 + R_4 \ge c_0 R_0 + \frac{w(U-a^2-v)}{p}\), and \(X = w(S_E + S_M) < c_0 R_0\).
By `TWO_CHANNEL_OPERATOR_BLOCKS_20261014.md` Theorem 1 (`(1.8)`–`(1.9)`), the operator quadratic form \(\langle u, K u\rangle_p = M_E + M_M\) satisfies two simultaneous equations:
1. From the \(R_j\) expansion (`SIGNED_QUARTIC_ATTACK_20261014.md` Theorem 2):
   \[
   \frac{1}{2}\langle u, K u\rangle_p = Y + \frac{R_{2,gE} + R_{2,gM}}{2}. \tag{5.1}
   \]
2. From the operator block decomposition (`TWO_CHANNEL_OPERATOR_BLOCKS_20261014.md` `(1.6)`–`(1.9)`):
   \[
   \begin{aligned}
   \frac{1}{2}\langle u, K u\rangle_p &= \frac{1}{2}\text{DIAG} + \frac{1}{2}\text{CROSS} + \frac{1}{2}\text{COMPLEMENT} \\
   &= \frac{D_{2,E} + D_{2,M}}{2} - X + \frac{w(U - a^2 - v)}{p},
   \end{aligned} \tag{5.2}
   \]
   with \(\text{DIAG} = \frac{2}{p}\|u_A\|_p^2 \ge 0\), \(-2X \le \text{CROSS} \le 0\), and \(\text{COMPLEMENT} \ge 0\).

**What (5.1)–(5.2) prove and what they do NOT prove**:
- Combining \(\text{CROSS} \le 0\) with (5.2) gives an **exact lower bound on the complement block `COMPLEMENT`**:
  \[
  \frac{1}{2}\text{COMPLEMENT} \ge \frac{1}{2}\langle u, K u\rangle_p - \frac{1}{p}\|u_A\|_p^2 = Y + \frac{R_{2,gE} + R_{2,gM}}{2} - \frac{1}{p}\|u_A\|_p^2. \tag{5.3}
  \]
  In particular, for the trivial factor \(g \equiv a\) on \(\mathbb{Z}_p\) (where \(R_2 = 0\), \(\text{CROSS} = -2(1-a)X\), and \(\text{COMPLEMENT} = D_{2,E}+D_{2,M} - 2aX - 2a^3/p\)), Branch II (\(Y \ge c_0 a^4\) and \(X < c_0 a^4\)) forces **both**:
  \[
  \frac{1}{2}\langle u, K u\rangle_p = Y \ge c_0 a^4 > 0 \qquad\text{and}\qquad
  \frac{1}{2}\text{COMPLEMENT} = Y + (1-a)X - \frac{a(1-a)^2}{p} \ge c_0 a^4 - \frac{a}{p} > 0! \tag{5.4}
  \]
- **Why operator block compression alone does NOT refute Branch II**:
  In `SIGNED_RESEARCH.md` §3 (`(5)`), \(P K_B P = \frac{1}{p}P\) was used when \(\langle f, K_B f\rangle_p = M < 0\) was *negative*. Here in Branch II, \(\frac{1}{2}\langle u, K u\rangle_p = \frac{1}{2}\text{DIAG} + \frac{1}{2}\text{CROSS} + \frac{1}{2}\text{COMPLEMENT} \ge c_0 a^4 > 0\) is **positive**, and that positivity comes entirely from \(\frac{1}{2}\text{COMPLEMENT} = \frac{1}{2}\langle u_C, Q K Q u_C\rangle_p \ge c_0 a^4 + (1-a)X - a/p > 0\) (completions of pairs in \(A^2\) whose endpoints both lie in the complement \(\Omega\setminus A\), which are **not** 4-APs in \(A\) because neither endpoint is in \(A\)!).
- In fact, **actual 4-AP-free sets can lie in Branch II**:
  In `verify_two_channel_dichotomy_20261014.py` (`TWO_CHANNEL_DICHOTOMY_VERIFICATION_20261014.json`), the proper-window 4-AP-free diagnostic `three_point_window` (\(p=101, n=25, A=\{0,1,3\}\)) has:
  \[
  X = 1.176\times 10^{-5},\qquad Y = 2.133\times 10^{-4} \gg R_0 = 4.248\times 10^{-6},\qquad \langle u, K u\rangle_p = 4.348\times 10^{-4} > 0,
  \]
  and on \(\mathbb{Z}_p\), any Sidon / 3-AP-free set with \(S_E = S_M = 0\) has \(X = 0\) and \(Y = a^4 + \frac{a(1-2a)}{p} \sim a^4 > 0\)!
  Wait — look at that example: **for ANY 3-AP-free set on \(\mathbb{Z}_p\) with \(S_E = S_M = 0\) (such as a Sidon set or a set where both \(q_E \equiv 0\) and \(q_M \equiv 0\)), \(X = w(S_E+S_M) = 0\) and \(Y = \frac{1}{2}R_3 + R_4 = a^4 + O(a/p)\) lies 100% in Branch II!**
  Let us double-check that!
  On \(\mathbb{Z}_p\) with trivial factor \(g \equiv a\):
  - If \(q_E \equiv 0\) and \(q_M \equiv 0\) on \(\mathbb{Z}_p\), then \(S_E = S_M = 0\), so \(X = 0\)!
  - And by (0.1), \(X + Y = a^4 + \frac{a(1-2a)}{p}\), so \(Y = \frac{1}{2}R_3 + R_4 = a^4 + \frac{a(1-2a)}{p} \sim a^4\)!
  - And what are \(\text{CROSS}\) and \(\text{COMPLEMENT}\) when \(q_E \equiv 0\) and \(q_M \equiv 0\)?!
    Since \((Q K_B P 1_A)(y) = q_E(y) = 0\) and \((Q R_B P 1_A)(y) = q_M(y) = 0\), \(K_B = \frac{1}{p}\operatorname{diag}(B)\) and \(R_B = \frac{1}{p}\operatorname{diag}(B)\) have **zero off-diagonal entries** (\(J_E = J_M = 0\))! Thus \(\text{CROSS} = 0\), \(\text{COMPLEMENT} = 0\), and \(\frac{1}{2}\langle u, K u\rangle_p = \frac{1}{2}\text{DIAG} = \frac{a(1-a)^2}{p}\), while \(R_{2,gE} = R_{2,gM} = -a^4 + \frac{a^3}{p}\), so \(Y = \frac{1}{2}\langle u, K u\rangle_p - \frac{1}{2}(R_{2,gE}+R_{2,gM}) = a^4 + \frac{a(1-2a)}{p}\)!
  - Why does a set on \(\mathbb{Z}_p\) with \(q_E \equiv 0\) and \(q_M \equiv 0\) still have a large Fourier coefficient? Because as proved in `MULTI_POSITION_COMPLETION_20261014.md` §5 (`(12)`), \(0 = \mathbb{E}[q_E] = a^3 - a/p + T_f\) forces \(T_f = -a^3 + a/p\), which by Parseval forces \(\rho = \max_{\xi\ne 0}|\widehat{f}(\xi)| \ge \frac{a^2 - 1/p}{1-a} \sim a^2\) (at scale \(\rho^2 \sim a^4\), still below `SELECT`'s \(a^{5/2}\ell(a)\))!

This proves a crucial structural fact:
**Branch II is NOT vacuously impossible for 4-AP-free sets!** Every 3-AP-free set on \(\mathbb{Z}_p\) with \(q_M \equiv 0\) (and more generally every 4-AP-free set with \(S_E + S_M \ll a^4\), where \(T_f + S_f \approx -2a^3\)) lies in Branch II!
Specifically, for the trivial factor \(g \equiv a\) on \(\mathbb{Z}_p\):
\[
X = S_E + S_M = a\bigl(\mathbb{E}[q_E] + \mathbb{E}[q_M]\bigr) = 2a^4 + a(T_f + S_f) - \frac{2a^2}{p},
\]
and since \(X + Y = a^4 + \frac{a(1-2a)}{p}\), we have:
\[
Y = \frac{1}{2}R_3 + R_4 = -a^4 - a(T_f + S_f) + \frac{a}{p}. \tag{5.5}
\]
Look at (5.5):
- In **Branch I** (\(X \ge \frac{1}{2}a^4\)), we have \(T_f + S_f \ge -\frac{3}{2}a^3 + \frac{2a}{p}\), so the completion fields \(q_E, q_M\) have large global mean \(\mathbb{E}[q_E + q_M] \ge \frac{1}{2}a^3\) and large residual pairing \(S_E + S_M \ge \frac{1}{2}a^4\).
- In **Branch II** (\(Y \ge \frac{1}{2}a^4\), i.e. \(X < \frac{1}{2}a^4\)), (5.5) forces:
  \[
  \boxed{a(T_f + S_f) = \frac{1}{2}R_3 < -\frac{3}{2}a^4 + \frac{2a^2}{p} \iff T_f + S_f < -\frac{3}{2}a^3 + \frac{2a}{p}!} \tag{5.6}
  \]
  And since \(Y = \frac{1}{2}R_3 + R_4 \ge \frac{1}{2}a^4\) while \(\frac{1}{2}R_3 = a(T_f + S_f) < -\frac{3}{2}a^4 + \frac{2a^2}{p}\), Branch II simultaneously forces:
  \[
  \boxed{R_4 = \Lambda_4(f) = Y - \frac{1}{2}R_3 > 2a^4 - \frac{2a^2}{p} > 0!} \tag{5.7}
  \]

Let us pause and admire (5.6) and (5.7)!
On \(\mathbb{Z}_p\) (and more generally when \(|R_1|, |R_2| \ll a^4\)):
- **Branch II (\(X < \frac{1}{2}R_0\)) is literally the Negative Cubic / Positive Quartic Residual Branch**:
  Because \(D_1 = 4R_0 + 3R_1 + 2R_2 + R_3 = 2w(S_E+S_M) + 4w(a^2+v)/p = 2X + 4w(a^2+v)/p\), having \(X < \frac{1}{2}R_0\) forces:
  \[
  \boxed{R_3 = 2X + \frac{4w(a^2+v)}{p} - 4R_0 - 3R_1 - 2R_2 < -2R_0 - 3R_1 - 2R_2 + \frac{4w(a^2+v)}{p},} \tag{5.8}
  \]
  and since \(R_0 + R_1 + R_2 + R_3 + R_4 = \frac{aw}{p}\), substituting (5.8) forces the pure quartic residual \(R_4 = \Lambda_4(u)\) to be **strictly positive**:
  \[
  \boxed{R_4 = 3R_0 + 2R_1 + R_2 - 2X + \frac{w(a - 4a^2 - 4v)}{p} > 2R_0 + 2R_1 + R_2 + \frac{w(a - 4a^2 - 4v)}{p}!} \tag{5.9}
  \]

**Theorem 3 (Exact Identification of Branch II: Negative Cubic \(R_3\) and Positive Quartic \(R_4 = \Lambda_4(u)\)).**
For every cyclically 4-AP-free \(A\subset\Omega\) and partition \(F\) of \(\Omega\), if \(X = w(S_E + S_M) \le \theta R_0\), then:
1. The cubic residual sum \(R_3\) is forced to be negative (modulo \(3R_1+2R_2\)):
   \[
   R_3 \le -2(2 - \theta)R_0 - 3R_1 - 2R_2 + \frac{4w(a^2+v)}{p}. \tag{5.10}
   \]
2. The pure quartic residual \(R_4 = \Lambda_4(u)\) is forced to be positive (modulo \(2R_1+R_2\)):
   \[
   R_4 \ge (3 - 2\theta)R_0 + 2R_1 + R_2 + \frac{w(a - 4a^2 - 4v)}{p}
   = (1 - 2\theta)R_0 + \frac{1}{3}D_2 + R_1 + \frac{2}{3}R_2 + \frac{w(a - 4a^2 - 4v)}{p}. \tag{5.11}
   \]
3. In particular, on \(\mathbb{Z}_p\) with the trivial factor \(g \equiv a\) and \(\theta = \frac{1}{2}\) (assuming \(pa^3 \ge 8\)):
   - **Branch I (\(S_E + S_M \ge \frac{1}{2}a^4\))**: The two-channel completion pairing with \(u\) is at least \(\frac{1}{2}a^4\).
   - **Branch II (\(S_E + S_M < \frac{1}{2}a^4\))**: We have **both** a strongly negative cubic Fourier sum and a strongly positive quartic Fourier sum:
     \[
     T_f + S_f = \sum_{\xi\ne 0} \widehat{f}(\xi)\widehat{f}(-\xi)\bigl[\widehat{f}(-2\xi)\dots\bigr] < -\frac{5}{4}a^3 \qquad\text{and}\qquad
     R_4 = \Lambda_4(f) > \frac{7}{4}a^4. \tag{5.12}
     \]
     Specifically, by Parseval on \(T_f = \sum_{\xi\ne 0}\widehat{f}(\xi)^2\widehat{f}(-2\xi)\) and \(S_f = \sum_{\xi\ne 0}\widehat{f}(\xi)\widehat{f}(2\xi)\widehat{f}(-3\xi)\), Branch II immediately forces an unconditional linear Fourier coefficient
     \[
     \max_{\xi\ne 0}|\widehat{f}(\xi)| \ge \frac{|T_f + S_f|}{2a(1-a)} > \frac{5a^2}{8(1-a)}, \tag{5.13}
     \]
     which is at the endpoint scale \(\rho \gtrsim a^2\) (\(\rho^2 \gtrsim a^4\)), still \(a^{3/2}/\ell(a)\) below `SELECT` (\(\rho^2 \gtrsim a^{5/2}\ell(a)\)).

---

## Phase 10 — Quantitative Closure Ledger at \(a = \epsilon/\log N\) and Exact Remaining Sublemma

| Branch / Quantity | Exact Proved Formula / Bound | Scale at \(a = \epsilon/\log N\) | Required Scale for October 2 Closure | Exact Remaining Gap |
| --- | --- | --- | --- | --- |
| Conservation Law | \(X + (Y - R_1/2) = R_0 + w(U-a^2-v)/p\) | \(R_0 \sim a^4 C\) | Holds with zero error | PROVED (Theorem 1) |
| Intermediate \(R_1\) error | \(|R_1| \le 12a\rho v + 4\sqrt{b}v^{3/2}\) (`A9`); \(R_1 \ge -4R_0\) (`D_3\ge 0`) | Upper bound \(O(a^{31/8})\) at \(v\sim a^{9/4}\); \(0\) at \(v=0\) | Need \(|R_1| \le c_0 R_0 \sim a^4 C\) at \(v\sim a^{9/4}\) | Factor \(a^{1/8}\) in upper bound of \(|R_1|\) when \(v\sim a^{9/4}\) |
| Branch I (\(X \ge \frac{1}{2}R_0\)) | \(\Delta E \ge \kappa^2 \frac{(|\lambda^T S| - \sqrt{U}\varepsilon_\Gamma)^2}{D_{\text{reg}}(\lambda,v)}\) | \(\Delta E \gtrsim a^4\) (from \(W\lesssim a^4\)) | \(\Delta E / s_0(a) \gtrsim a^{5/2}\ell(a)\) | Needs \(s_0(a) D_{\text{reg}}(\lambda,v) \lesssim a^{11/2}/\ell(a)\) (factor \(a^{3/2}\ell(a)\)) |
| Branch II (\(X < \frac{1}{2}R_0\)) | \(R_3 < -2R_0 - 3R_1 - 2R_2 + 4w(a^2+v)/p\) and \(R_4 > 2R_0 + 2R_1 + R_2\) | At \(v=0\): \(\rho > \frac{5}{8}a^2\) (\(\rho^2 \gtrsim a^4\)) and \(\Lambda_4(f) > \frac{7}{4}a^4\) | \(\max_{\xi\ne 0}|c_\xi|^2 \gtrsim a^{5/2}\ell(a)\) (or multi-character gain) | Same \(a^4\) vs \(a^{5/2}\ell(a)\) gap: needs \(a^{-3/2}\ell(a)\) coherent frequencies |

### Corrected Continuation Prompt

> Continue offline from `TWO_CHANNEL_DICHOTOMY_CLOSURE_20261014.md`, `TWO_CHANNEL_OPERATOR_BLOCKS_20261014.md`, and `TWO_CHANNEL_DICHOTOMY_VERIFICATION_20261014.json`. Accept as proved:
> 1. **Repaired Unconditional Two-Channel Dichotomies (Theorem 1)**: Because \(|R_1| = O(a^{31/8})\) does not imply \(R_1 = o(a^4)\) at \(v \sim a^{9/4}\), the exact \(R_1\)-free conservation law is \(X + (Y - \frac{1}{2}R_1) = R_0 + \frac{w(U-a^2-v)}{p}\), and every 4-AP-free set satisfies at least one of: **Branch I** (\(w(S_E+S_M) \ge c_0 R_0\)), **Branch II** (\(\frac{1}{2}R_3+R_4 \ge c_0 R_0 + \frac{w(U-a^2-v)}{p}\)), or **Branch III** (\(R_1 \le -2(1-2c_0)R_0\), which vanishes whenever \(v = o(a^{8/3})\)).
> 2. **Exact Operator Block Decomposition and Cancellation (`TWO_CHANNEL_OPERATOR_BLOCKS_20261014.md` Theorem 1 & Theorem 2)**: For \(K = K_B + R_B\) and \(u = u_A + u_C\), \(\text{DIAG} = \frac{2}{p}\|u_A\|_p^2 \ge 0\), \(\text{CROSS} = -2w(S_E+S_M) - 2\langle g_A, K u_C\rangle_p \le 0\), and \(\text{COMPLEMENT} = D_{2,E}+D_{2,M} + 2\langle g_A, K u_C\rangle_p - \frac{2}{p}\|g_A\|_p^2 \ge 0\), so \(\text{CROSS} + \text{COMPLEMENT} = D_{2,E}+D_{2,M} - 2w(S_E+S_M) - \frac{2}{p}\|g_A\|_p^2\) cancels \(2\langle g_A, K u_C\rangle_p\) identically, and \(\text{COMPLEMENT}\) satisfies the dual Schur complement inequalities on \(A^c\).
> 3. **Exact Identification of Branch II (Theorem 3)**: Branch II (\(X \le \theta R_0\)) is not vacuous (3-AP-free sets with \(q_M\equiv 0\) lie in it), and is identically the **Negative Cubic / Positive Quartic Residual Branch**: \(R_3 \le -2(2-\theta)R_0 - 3R_1 - 2R_2 + \frac{4w(a^2+v)}{p}\) and \(R_4 = \Lambda_4(u) \ge (3-2\theta)R_0 + 2R_1 + R_2 + \frac{w(a-4a^2-4v)}{p}\).
>
> Both Branch I (via two-channel completion pairing \(X \ge \frac{1}{2}R_0\)) and Branch II (via negative cubic \(R_3 \le -2R_0\) and positive quartic \(R_4 \ge 2R_0\)) unconditionally supply squared Fourier signal at the endpoint scale \(a^4\), leaving the exact factor \(a^{3/2}\ell(a)\) gap to `SELECT`'s \(a^{5/2}\ell(a)\). Attack the coherent multi-frequency capture problem in either branch: prove that under 4-AP exclusion and Booleanity, either the completion spectrum of \(k_E+k_M\) (in Branch I) or the cubic/quartic residual spectrum of \(R_3, R_4\) and \(\text{COMPLEMENT} = \langle u_C, Q K Q u_C\rangle_p\) (in Branch II) concentrates a positive fraction of its pairing on a character set \(\Gamma\) of size \(s_0(a) = O(a^{-1/4}/\ell(a))\).
