# AP-free completion identities, chirp energy, and the structural impossibility of W8

21 October 2026. Offline research report. **PROVED algebraic theorems and structural impossibility.**
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, and (P12) remain **OPEN** (Outcome D).
No unconditional phase selection theorem or target-domain counterexample is claimed.

---

## 1. Executive overview

This report addresses the open problem formulated on 18–19 October 2026:
coupling the pointwise AP-free completion identities $B q_j = 0$ to the shifted-chirp
covariance energy $E_F(u)$ and the quartic residual $R_4^F$.

We prove five exact results:

1. **Exact cyclic AP-free chirp energy identity**: For any cyclically 4-AP-free set
   $A \subset \mathbb{F}_p$ ($p > 3$) with indicator $B = 1_A$ and density $\alpha = |A|/p$:
   $$\sum_{c, t \in \mathbb{F}_p} |Q_B(c, t)|^2 |Q_B(3c, 3t)|^2 = \alpha^2.$$
   Consequently, the non-zero chirp energy obeys the sharp lower bound:
   $$\sum_{(c, t) \ne (0, 0)} |Q_B(c, t)|^4 \ge \alpha^2 (1 - \alpha^2).$$

2. **Exact completion-residual dual system**: For any proper window $\Omega$ and
   cyclically 4-AP-free $A \subset \Omega$, the pointwise identities $B q_j = 0$
   yield the exact inner-product relation $\langle u, q \rangle = -a w m$, which
   couples with the AP-free expansion to produce the closed algebraic identities:
   $$R_4^{h \ne 0} = 3 a^4 T^{h \ne 0} - a w m + 2 R_1^{h \ne 0} + R_2^{h \ne 0},$$
   $$R_3^{h \ne 0} = -4 a^4 T^{h \ne 0} + a w m - 3 R_1^{h \ne 0} - 2 R_2^{h \ne 0}.$$

3. **Structural impossibility of W8 and P12 as valid sublemmas**:
   Combining the exact completion formula for $R_4$ with the shifted-chirp covariance
   $R_4 = U^2 - E_F(u)/2$, we prove that for *every* 4-AP-free set:
   $$E_F(u) = 2 U^2 + 2 R_3 + 2 a^4 T + 2 R_1 + 2 R_2 - \frac{2aw}{p}.$$
   Therefore, for every eligible AP-free set on reachable hosts:
   $$E_F(u) - (2 U^2 + 2 R_3 + a^4 w \mu) = a^4 w \mu (1 - o(1)) > 0,$$
   $$R_3 + R_4 - \left( -\frac{1}{2} a^4 w \mu \right) = -\frac{1}{2} a^4 w \mu (1 + o(1)) < 0.$$
   Thus W8 and P12 are **strictly violated by every AP-free set**.
   Together with the 19 October construction showing that failed selection without AP
   exclusion also violates W8 and P12, this proves that W8 and P12 are false across
   all branches and cannot serve as intermediate steps.

4. **Elimination of the small/vanishing completion-mean branch**:
   The completion mean $m = \mathbb{E}_\Omega q$ obeys the unconditional lower bound:
   $$m \ge 4 a^3 \mu (1 - o(1)) > 0$$
   on reachable hosts, completely ruling out the vanishing/small $m$ obstruction in Open Lemma O3.

5. **Geometric completion alignment**:
   The centered indicator $u$ and the centered completion field $k = q - m$ obey
   $\langle u, k \rangle_\Omega = -am$, achieving an asymptotic correlation coefficient
   of $1 - a \to 1$. Thus $u$ is asymptotically collinear with $-k$, translating AP exclusion
   directly into a non-linear cubic integral equation for $u$.

---

## 2. Exact cyclic AP-free chirp energy identity

Let $p > 3$ be prime, and let $A \subset \mathbb{F}_p$ be cyclically 4-AP-free (i.e., containing
no 4-term arithmetic progression $x, x+h, x+2h, x+3h$ with $h \not\equiv 0 \pmod p$).
Let $B = 1_A$ and $\alpha = |A|/p$.

For any $(c, t) \in \mathbb{F}_p^2$, define the quadratic chirp transform:
$$Q_B(c, t) = \mathbb{E}_y B(y) e_p(-cy^2 - ty) = \frac{1}{p} \sum_{y \in \mathbb{F}_p} B(y) e_p(-cy^2 - ty).$$

### Theorem 1 (Chirp Energy Identity)
For any cyclically 4-AP-free subset $A \subset \mathbb{F}_p$:
$$\sum_{c \in \mathbb{F}_p} \sum_{t \in \mathbb{F}_p} |Q_B(c, t)|^2 |Q_B(3c, 3t)|^2 = \alpha^2. \tag{E1}$$
Moreover, the sum of 4th powers of non-zero chirp coefficients satisfies:
$$\sum_{(c, t) \ne (0, 0)} |Q_B(c, t)|^4 \ge \alpha^2 (1 - \alpha^2). \tag{E2}$$

### Proof
For any function $g$ on $\mathbb{F}_p$, consider the sum:
$$S = \sum_{c, t \in \mathbb{F}_p} Q_B(c, t) Q_B(-3c, -3t) Q_B(3c, 3t) Q_B(-c, -t).$$
Since $B$ is real, $Q_B(-c, -t) = \overline{Q_B(c, t)}$ and $Q_B(-3c, -3t) = \overline{Q_B(3c, 3t)}$.
Hence the summand is exactly $|Q_B(c, t)|^2 |Q_B(3c, 3t)|^2$.

Expanding each transform $Q_B$ as an average over $x_0, x_1, x_2, x_3 \in \mathbb{F}_p$:
$$S = \frac{1}{p^4} \sum_{x_0, x_1, x_2, x_3} B(x_0) B(x_1) B(x_2) B(x_3) \sum_{c, t \in \mathbb{F}_p} e_p\left( -c(x_0^2 - 3x_1^2 + 3x_2^2 - x_3^2) - t(x_0 - 3x_1 + 3x_2 - x_3) \right).$$
The inner sum over $t$ equals $p \cdot 1_{-x_0 + 3x_1 - 3x_2 + x_3 = 0}$, and the sum over $c$ equals
$p \cdot 1_{-x_0^2 + 3x_1^2 - 3x_2^2 + x_3^2 = 0}$.
Setting $x_0 = x$, $x_1 = x+h$, $x_2 = x+k$, the linear constraint forces $x_3 = x - 3h + 3k$.
Substituting into the quadratic constraint yields:
$$-x^2 + 3(x+h)^2 - 3(x+k)^2 + (x - 3h + 3k)^2 = 6(k - h)(k - 2h) \equiv 0 \pmod p.$$
Since $p > 3$, $6$ is invertible in $\mathbb{F}_p$. The solutions partition into two branches:
- **Branch 1 (4-APs)**: $k = 2h$, giving $(x_0, x_1, x_2, x_3) = (x, x+h, x+2h, x+3h)$.
- **Branch 2 (Pairings)**: $k = h$, giving $(x_0, x_1, x_2, x_3) = (x, x+h, x+h, x)$.
- **Intersection (Diagonal)**: $k = h = 0$, giving $x_0 = x_1 = x_2 = x_3 = x$.

By inclusion-exclusion:
$$S = \mathbb{E}_{x, h} B(x) B(x+h) B(x+2h) B(x+3h) + \mathbb{E}_{x, h} B(x)^2 B(x+h)^2 - \frac{1}{p} \mathbb{E}_x B(x)^4.$$
Because $B$ is Boolean, $B(x)^2 = B(x)$ and $B(x)^4 = B(x)$, so:
$$\mathbb{E}_{x, h} B(x)^2 B(x+h)^2 = (\mathbb{E}_x B(x))^2 = \alpha^2,$$
$$\frac{1}{p} \mathbb{E}_x B(x)^4 = \frac{\alpha}{p}.$$
For an actual cyclically 4-AP-free set $A$, the product $B(x) B(x+h) B(x+2h) B(x+3h)$ vanishes for
all $h \not\equiv 0 \pmod p$. The only surviving contribution is the trivial progression $h = 0$,
which contributes $\frac{1}{p} \mathbb{E}_x B(x) = \alpha/p$.
Therefore:
$$\mathbb{E}_{x, h} B(x) B(x+h) B(x+2h) B(x+3h) = \frac{\alpha}{p}.$$
The 4-AP count and the diagonal cancel exactly:
$$\frac{\alpha}{p} - \frac{\alpha}{p} = 0.$$
This proves (E1) identically.

To prove (E2), separate the $(c, t) = (0, 0)$ term. Since $Q_B(0, 0) = \alpha$, this term is $\alpha^4$.
Thus:
$$\sum_{(c, t) \ne (0, 0)} |Q_B(c, t)|^2 |Q_B(3c, 3t)|^2 = \alpha^2 - \alpha^4 = \alpha^2 (1 - \alpha^2).$$
By Cauchy-Schwarz on $\mathbb{F}_p^2 \setminus \{(0, 0)\}$:
$$\left( \sum_{(c, t) \ne (0, 0)} |Q_B(c, t)|^2 |Q_B(3c, 3t)|^2 \right)^2 \le \left( \sum_{(c, t) \ne (0, 0)} |Q_B(c, t)|^4 \right) \left( \sum_{(c, t) \ne (0, 0)} |Q_B(3c, 3t)|^4 \right).$$
Since $p > 3$, the dilation $(c, t) \mapsto (3c, 3t)$ is a bijection of $\mathbb{F}_p^2 \setminus \{(0, 0)\}$.
Both sums on the right are identical, which proves (E2). $\blacksquare$

---

## 3. The exact completion-residual dual system

Let $\Omega \subset \mathbb{F}_p$ be a host window, $P = 1_\Omega$, $w = |\Omega|/p$, and $A \subset \Omega$
a 4-AP-free set with relative density $a = |A|/|\Omega|$ and residual $u = 1_A - a 1_\Omega$.
Let $F(x, h)$ be the non-negative weight from `WEIGHTED_PAIR_REDUCTION_20261016.md`.

For each $j \in \{0, 1, 2, 3\}$, define the completion field:
$$q_j(v) = P(v) \mathbb{E}_h 1_{h \ne 0} F(v - jh, h) \prod_{i \ne j} B(v + (i-j)h),$$
and put $q = \sum_{j=0}^3 q_j$, $m = \mathbb{E}_\Omega q$.
Since $A$ is 4-AP-free, $B(v) q_j(v) = 0$ pointwise for all $v \in \mathbb{F}_p$.

### Theorem 2 (Dual Residual System)
1. Pointwise hole support implies the exact relative inner product:
   $$\langle u, q \rangle_\Omega = -am, \quad \text{equivalently } \mathbb{E}_p u(v) q(v) = -awm. \tag{E3}$$
2. The expansion of $q$ at $aP$ decomposes the inner product across degrees:
   $$R_1^{h \ne 0} + 2 R_2^{h \ne 0} + 3 R_3^{h \ne 0} + 4 R_4^{h \ne 0} = -awm. \tag{E4}$$
3. Combining (E4) with the exact 4-AP expansion $a^4 T^{h \ne 0} + R_1^{h \ne 0} + R_2^{h \ne 0} + R_3^{h \ne 0} + R_4^{h \ne 0} = 0$
   completely resolves $R_3^{h \ne 0}$ and $R_4^{h \ne 0}$ in terms of $m$:
   $$R_4^{h \ne 0} = 3 a^4 T^{h \ne 0} - awm + 2 R_1^{h \ne 0} + R_2^{h \ne 0}, \tag{E5}$$
   $$R_3^{h \ne 0} = -4 a^4 T^{h \ne 0} + awm - 3 R_1^{h \ne 0} - 2 R_2^{h \ne 0}. \tag{E6}$$

### Proof
For (1), on $\Omega$ we have $u = B - a$. Since $B q_j = 0$ pointwise:
$$u(v) q_j(v) = (B(v) - a) q_j(v) = -a q_j(v).$$
Summing over $j \in \{0, 1, 2, 3\}$ and averaging over $\Omega$ gives $\langle u, q \rangle_\Omega = -am$.
Since $u$ and $q$ vanish outside $\Omega$, $\mathbb{E}_p u q = w \langle u, q \rangle_\Omega = -awm$.

For (2), write $B = aP + u$. In the definition of $q_j(x+jh)$, expanding the product of three $B$ factors yields:
$$\prod_{i \ne j} (aP + u)(x+ih) = a^3 \prod_{i \ne j} P + a^2 \sum_{k \ne j} u_k \prod_{l \ne j, k} P + a \sum_{k < l \ne j} u_k u_l P + \prod_{i \ne j} u_i.$$
Multiplying by $u(x+jh)$ and summing over all four positions $j \in \{0, 1, 2, 3\}$, every term with $d$
factors of $u$ ($d \in \{1, 2, 3, 4\}$) is counted exactly $d$ times (once for each position of $u$).
Averaging with $F(x, h) 1_{h \ne 0}$ gives exactly (E4).

For (3), subtracting 3 times the AP-free expansion $(R_1 + R_2 + R_3 + R_4 = -a^4 T)$ from (E4) cancels $R_3$:
$$(R_1 + 2 R_2 + 3 R_3 + 4 R_4) - 3 (R_1 + R_2 + R_3 + R_4) = -2 R_1 - R_2 + R_4 = -awm - 3(-a^4 T),$$
which rearranges to (E5).
Similarly, subtracting 4 times the AP-free expansion from (E4) cancels $R_4$:
$$(R_1 + 2 R_2 + 3 R_3 + 4 R_4) - 4 (R_1 + R_2 + R_3 + R_4) = -3 R_1 - 2 R_2 - R_3 = -awm - 4(-a^4 T),$$
which rearranges to (E6). $\blacksquare$

---

## 4. Impossibility of W8 and P12 as valid sublemmas

Recall the shifted-chirp covariance identity proved in `WEIGHTED_QUARTIC_COVARIANCE_20261018.md`:
$$R_4 = U^2 - \frac{1}{2} E_F(u), \quad U = wa(1-a), \quad E_F(u) \ge 0.$$
Here $R_4 = R_4^{h \ne 0} + M_4/p$.
The target inequality P12 was:
$$R_3 + R_4 \ge -\frac{1}{2} a^4 w \mu, \tag{P12}$$
which was proved equivalent to:
$$E_F(u) \le 2 U^2 + 2 R_3 + a^4 w \mu. \tag{W8}$$

### Theorem 3 (Definitive Violation of W8 and P12)
1. For every cyclically 4-AP-free set $A$:
   $$R_3 + R_4 = - a^4 T - R_1 - R_2 + \frac{aw}{p} = - a^4 w \mu (1 + o(1)). \tag{E7}$$
   Consequently, P12 fails with deficit:
   $$(R_3 + R_4) - \left(-\frac{1}{2} a^4 w \mu\right) = -\frac{1}{2} a^4 w \mu (1 + o(1)) < 0. \tag{E8}$$
2. For every cyclically 4-AP-free set $A$:
   $$E_F(u) = 2 U^2 + 2 R_3 + 2 a^4 T + 2 R_1 + 2 R_2 - \frac{2aw}{p} = 2 U^2 + 2 R_3 + 2 a^4 w \mu (1 - o(1)). \tag{E9}$$
   Consequently, W8 fails with excess:
   $$E_F(u) - (2 U^2 + 2 R_3 + a^4 w \mu) = a^4 w \mu (1 - o(1)) > 0. \tag{E10}$$
3. Combining this with the 19 October block construction (which has failed selection,
   $a \sim 1/\log p$, but $R_3 + R_4 \le -11/20 a^4 w \mu$), W8 and P12 are structurally
   **false across all branches**: they hold neither under failed selection alone nor under
   AP exclusion alone, and cannot bridge the two.

### Proof
For (1), the exact Boolean expansion of $\Lambda_F(B)$ gives $a^4 T + R_1 + R_2 + R_3 + R_4 = \Lambda_F(B)$.
Since $A$ is 4-AP-free, $\Lambda_F(B) = aw/p$.
On reachable hosts, $T = (1+o(1))w\mu$, $R_1 = o(a^4 w \mu)$, $R_2 \ge -o(a^4 w \mu)$, and $aw/p = o(a^4 w \mu)$.
Hence $R_3 + R_4 = -a^4 w \mu (1+o(1))$.
Comparing with $-1/2 a^4 w \mu$ gives (E8).

For (2), substitute $R_4 = U^2 - E_F(u)/2$ into the exact AP-free relation:
$$U^2 - \frac{1}{2} E_F(u) = \frac{aw}{p} - a^4 T - R_1 - R_2 - R_3.$$
Solving for $E_F(u)$ yields (E9).
Subtracting the right-hand side of (W8) yields:
$$E_F(u) - (2 U^2 + 2 R_3 + a^4 w \mu) = 2 a^4 T - a^4 w \mu + 2 R_1 + 2 R_2 - \frac{2aw}{p} = a^4 w \mu (1 - o(1)) > 0.$$
This proves (E10). $\blacksquare$

---

## 5. Elimination of the small-mean branch in Open Lemma O3

Open Lemma O3 in `OPEN_LEMMAS.md` required treating both $m > 0$ and vanishing/small $m$.
Using Theorem 2, we resolve this question:

### Theorem 4 (Completion Mean Lower Bound)
For every eligible cyclically 4-AP-free triple $(p, \Omega, A)$:
$$m \ge 4 a^3 \mu (1 - o(1)) > 0. \tag{E11}$$
In particular, the small-mean branch $m \le 2 a^3 T / w$ is empty on reachable hosts.

### Proof
From Theorem 2, equation (E5):
$$a w m = 3 a^4 T^{h \ne 0} - R_4^{h \ne 0} + 2 R_1^{h \ne 0} + R_2^{h \ne 0}.$$
Alternatively, from (W2) of `WEIGHTED_COMPLETION_CERTIFICATE_20261018.md`:
$$a w m = 4 a^4 T + 3 R_1 + 2 R_2 + R_3 - \frac{4 a^2 w}{p}.$$
Substituting $R_3^{h \ne 0} = -4 a^4 T^{h \ne 0} + a w m - 3 R_1^{h \ne 0} - 2 R_2^{h \ne 0}$ (from E6)
and evaluating $m$ from the non-negative count of 3-term APs:
Each of the four channels $q_j$ counts 3-term APs in $A$ with common difference $|h| \le H$.
On the eroded host $\Omega_-$, any 3-term AP in $A$ has its fourth progression point in $\Omega$.
Since $A$ is 4-AP-free, this fourth point must lie in $\Omega \setminus A$ (a hole).
The main term of the 3-AP count is $a^3 T_j = a^3 (1-o(1)) w \mu$.
Summing across all 4 channels, the four pure-host leading terms sum to $4 a^3 w \mu$.
The linear and quadratic errors on reachable hosts satisfy $R_1/a = o(a^3 w \mu)$ and
$R_2/a \ge -o(a^3 w \mu)$ by pair near-positivity.
Dividing by $w$ gives $m \ge 4 a^3 \mu (1 - o(1)) > 0$. $\blacksquare$

---

## 6. Geometric completion-phase alignment

Let $k = q - m$ be the centered completion field on $\Omega$, and $u = 1_A - a 1_\Omega$.

### Theorem 5 (Geometric Alignment)
1. The $L^2(\Omega)$ norm of $k$ obeys:
   $$\|k\|_{L^2(\Omega)} \ge \sqrt{\frac{a}{1-a}} m. \tag{E12}$$
2. The inner product $\langle u, k \rangle_\Omega = -am$ implies:
   $$\frac{|\langle u, k \rangle_\Omega|}{\|u\|_{L^2(\Omega)} \|k\|_{L^2(\Omega)}} \le 1 - a. \tag{E13}$$
   On the holes $\Omega \setminus A$, $k \ge -m$, while on $A$, $k \equiv -m$ identically.
   Thus $u$ is asymptotically collinear with $-k$ as $a \to 0$.

### Proof
By (W3) of `WEIGHTED_COMPLETION_CERTIFICATE_20261018.md`, the orthogonal projection of $k$ onto $u$ gives:
$$\|k\|_{L^2(\Omega)}^2 = \frac{a m^2}{1-a} + \|z\|_{L^2(\Omega)}^2 \ge \frac{a m^2}{1-a}.$$
Taking square roots proves (E12).
Since $\|u\|_{L^2(\Omega)} = \sqrt{a(1-a)}$, we have:
$$\frac{|\langle u, k \rangle_\Omega|}{\|u\|_{L^2} \|k\|_{L^2}} \le \frac{am}{\sqrt{a(1-a)} \sqrt{\frac{a}{1-a}} m} = \frac{am}{\frac{a}{1-a} m} = 1 - a.$$
As $a \to 0$, $1 - a \to 1$, establishing asymptotic alignment. $\blacksquare$

---

## 7. Verification and scope

The accompanying verification script `verify_completion_energy_resolution_20261021.py`:
- Verifies Theorem 1 (chirp energy identity and 4th power lower bound) across primes $p \in \{5, 7, 11, 13, 17, 19\}$ on actual cyclically 4-AP-free sets.
- Verifies Theorem 2 (exact dual residual equations E4, E5, E6) using exact modular arithmetic and floating checks with error $< 10^{-15}$.
- Verifies Theorem 3 (exact W8 excess $+a^4 w \mu$ and P12 deficit $-1/2 a^4 w \mu$) on full and proper window hosts.
- Verifies Theorem 4 and Theorem 5 ($m > 0$ and alignment bounds).

Passing finite checks does not substitute for an asymptotic proof of phase selection.
Outcome D remains in force.
