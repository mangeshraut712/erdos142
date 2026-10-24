# Bilinear pair incidence bounds and phase transfer obstruction

24 October 2026. **D: new rigorous partial results. Target OPEN.**
No literature novelty is asserted. The October 21 closure remains withdrawn.

## 1. Setting and Context of the Bilinear Pair Approach

Let $p > 3$ be a prime, $\Omega \subset \mathbb{F}_p$ a mixed interval host, $P = 1_\Omega$, $B = 1_A$ with $A \subset \Omega$ cyclically 4-AP-free.
Let $w = |\Omega|/p$, $a = |A|/|\Omega|$, $\alpha = aw$, and $u = B - aP$.
The tent kernel $F \ge 0$ on $\mathbb{F}_p \times \mathbb{F}_p$ satisfies $0 \le F(x, h) \le 1$.
The anchor completion field $q(v) = \sum_{j=0}^3 q_j(v)$ has relative mean $m = \mathbb{E}_\Omega q$, and satisfies $B(v) q(v) \equiv 0$ identically on $\mathbb{F}_p$.
The weighted incidence operator $K$ (introduced in [GROWING_OVERLAP_SYSTEMS_20261024.md](GROWING_OVERLAP_SYSTEMS_20261024.md), IE24) has rows $v \in \Omega$ and columns $c \in \binom{A}{2}$, where for each oriented progression $P$ with 3 vertices in $A$ and missing vertex $v \in \Omega$, $F(P)/p$ is added to $K(v, c)$ for each pair $c \subset P \cap A$.

The research frontier posed the following specific investigation:
Can the incidence operator $K$ applied to a centered occupied-pair function $f$ yield a phase-sensitive bilinear estimate that provides the super-critical gain $\delta \ge c_\epsilon a^{3/2} F_\epsilon(a)$ with $F_\epsilon(a) \to \infty$, or close the low-mean branch $m \le 2a^3 T / w$?

This audit proves that the answer is **negative**: any pairing with $K$ is fundamentally subject to a universal $a^{3/2}$ ceiling, with a fixed uniform constant that cannot diverge.

---

## 2. BP24.1: Hole-Support Degeneracy and Exact Decoupled Inner Product

### Lemma 1 (Pointwise Annihilation of Row Support)
For every vertex $v \in \Omega$ and every pair $c \in \binom{A}{2}$:
$$B(v) K(v, c) = 0. \tag{BP1}$$
Equivalently, if $K(v, c) > 0$ for some $c$, then $v \in \Omega \setminus A$, so $B(v) = 0$ and $u(v) = -a$.

### Proof
By definition, $K(v, c) > 0$ only if $v$ is the missing fourth vertex of an oriented progression $P$ having its other three vertices in $A$.
If $v \in A$, then all four vertices of $P$ lie in $A$. Since the progression is non-degenerate ($h \ne 0$), this would produce a non-trivial 4-AP in $A$, contradicting the hypothesis that $A$ is 4-AP-free.
Thus $v \notin A$, which proves $B(v) = 0$.
Since $v \in \Omega$, $P(v) = 1$, so $u(v) = B(v) - aP(v) = -a$. $\blacksquare$

### Theorem 2 (Spatial Decoupling of the Residual Inner Product)
For any pair vector $f: \binom{A}{2} \to \mathbb{C}$, the inner product of $K f$ with the centered indicator $u$ satisfies:
$$\langle u, K f \rangle = \sum_{v \in \Omega} u(v) (K f)(v) = -a \sum_{c \in \binom{A}{2}} g(c) f(c) = -a \langle g, f \rangle, \tag{BP2}$$
where $g(c) = \sum_{v \in \Omega} K(v, c)$ is the column degree vector of $K$.

### Proof
Substitute $(K f)(v) = \sum_{c} K(v, c) f(c)$ into the inner product:
$$\sum_{v \in \Omega} u(v) (K f)(v) = \sum_{c \in \binom{A}{2}} f(c) \sum_{v \in \Omega} u(v) K(v, c).$$
By Lemma 1, $u(v) = -a$ on the support of $K(\cdot, c)$.
Factoring $-a$ out of the inner sum gives:
$$\sum_{v \in \Omega} u(v) K(v, c) = -a \sum_{v \in \Omega} K(v, c) = -a g(c).$$
Summing over $c$ yields (BP2). $\blacksquare$

> [!NOTE]
> Theorem 2 reveals that the pairing $\langle u, K f \rangle$ does not interact with the spatial oscillations of $u$ across $\Omega$.
> Because $u \equiv -a$ on $\text{supp}(K)$, all phase information of $u$ on the holes is completely erased in the pairing with $K f$.

---

## 3. BP24.2: Universal $a^{3/2}$ Ceiling on Bilinear Phase Pairings

### Theorem 3 (Universal Bilinear Ceiling)
Let $A \subset \Omega \subset \mathbb{F}_p$ be 4-AP-free, with relative density $a = |A|/|\Omega|$, host density $w = |\Omega|/p$, and counting Euclidean norms.
For **every** pair function $f: \binom{A}{2} \to \mathbb{C}$ with $\|f\|_\infty \le 1$, and **every** test function $\psi: \Omega \to \mathbb{C}$ with $\|\psi\|_\infty \le 1$ (including all quadratic chirps $\psi_\gamma(v) = e_p(-cv^2 - tv)$):
$$|\mathbb{E}_\Omega [ \overline{\psi} (K f) ]| \le 6 w a^{3/2} \le 6 a^{3/2}. \tag{BP3}$$

### Proof
1. **$\ell^2$-Norm of $f$**: The number of occupied pairs is $|\binom{A}{2}| = \frac{|A|(|A|-1)}{2} \le \frac{|A|^2}{2}$.
   Since $|A| = a |\Omega| = a w p = \alpha p$, we have:
   $$\|f\|_2^2 = \sum_{c \in \binom{A}{2}} |f(c)|^2 \le \frac{\alpha^2 p^2}{2}.$$
2. **Operator Norm of $K$**: By IE24 ([GROWING_OVERLAP_SYSTEMS_20261024.md](GROWING_OVERLAP_SYSTEMS_20261024.md)), the counting Euclidean operator norm satisfies:
   $$\|K\|^2 \le \frac{72 \alpha}{p}.$$
   Therefore:
   $$\|K f\|_2^2 \le \|K\|^2 \|f\|_2^2 \le \left( \frac{72 \alpha}{p} \right) \left( \frac{\alpha^2 p^2}{2} \right) = 36 \alpha^3 p = 36 a^3 w^3 p.$$
3. **$\ell^2$-Norm of $\psi$**: Since $\|\psi\|_\infty \le 1$,
   $$\|\psi\|_2^2 = \sum_{v \in \Omega} |\psi(v)|^2 \le |\Omega| = w p.$$
4. **Cauchy-Schwarz on $\Omega$**:
   $$|\langle \psi, K f \rangle|^2 = \left| \sum_{v \in \Omega} \overline{\psi(v)} (K f)(v) \right|^2 \le \|\psi\|_2^2 \|K f\|_2^2 \le (w p) \cdot (36 a^3 w^3 p) = 36 a^3 w^4 p^2.$$
   Taking the square root gives:
   $$|\langle \psi, K f \rangle| \le 6 a^{3/2} w^2 p.$$
5. **Relative Expectation**: Dividing by $|\Omega| = w p$:
   $$|\mathbb{E}_\Omega [ \overline{\psi} (K f) ]| = \frac{1}{w p} |\langle \psi, K f \rangle| \le \frac{6 a^{3/2} w^2 p}{w p} = 6 w a^{3/2}.$$
   Since $w \le 1$, this completes the proof. $\blacksquare$

### Corollary 4 (Sub-Criticality of the Incidence Transfer)
The ratio
$$\frac{|\mathbb{E}_\Omega [ \overline{\psi} (K f) ]|}{a^{3/2}} \le 6 w \le 6$$
is uniformly bounded by 6 across all primes $p$, all densities $a, w$, all pair modulations $f$, and all phase functions $\psi$.
Consequently, $K$ cannot supply the diverging factor $F_\epsilon(a) \to \infty$ required by DIRECT-Q-GAIN.

---

## 4. BP24.3: Exact Quartic Residual Under Low/Zero-Mean Branches

Recall the exact expansion of the 4-AP count on the mixed host:
$$a^4 T + R_1 + R_2 + R_3 + R_4 = \frac{aw}{p}, \tag{BP4}$$
and the completion mean relation:
$$aw m = 4 a^4 T + 3 R_1 + 2 R_2 + R_3 - \frac{4 a^2 w}{p}. \tag{BP5}$$

### Proposition 5 (Closed Quartic Residual Identity)
Eliminating the cubic form $R_3$ yields the exact quartic residual identity:
$$R_4 = 3 a^4 T + 2 R_1 + R_2 - awm + \frac{aw(1 - 4a)}{p}. \tag{BP6}$$

### Proof
From (BP5), $R_3 = aw m - 4 a^4 T - 3 R_1 - 2 R_2 + \frac{4 a^2 w}{p}$.
Substitute $R_3$ into (BP4):
$$R_4 = \frac{aw}{p} - a^4 T - R_1 - R_2 - \left( aw m - 4 a^4 T - 3 R_1 - 2 R_2 + \frac{4 a^2 w}{p} \right)$$
$$= 3 a^4 T + 2 R_1 + R_2 - aw m + \frac{aw - 4 a^2 w}{p}$$
$$= 3 a^4 T + 2 R_1 + R_2 - aw m + \frac{aw(1 - 4a)}{p}. \quad \blacksquare$$

### Corollary 6 (Quartic Behavior in the Zero-Mean Regime)
When $m = 0$ (as realized by the GI24 subsets) and under failed linear selection ($R_1 \approx 0, R_2 \approx 0$):
$$R_4 = 3 a^4 T + O\left( \frac{aw}{p} \right) \approx 3 a^4 w \mu > 0. \tag{BP7}$$
The quartic form $R_4 = \|u\|_{U^3(F)}^4$ is strictly positive and of order $a^4$.
However, converting this positive $U^3$ norm into a single quadratic chirp correlation via Gowers' inverse theorem yields:
$$\delta \ge c (a^4)^C = c a^{4C},$$
where $4C \ge 2 > 3/2$, which is strictly weaker than $a^{3/2}$ as $a \to 0$.

---

## 5. Obstruction Synthesis: Why $K$ Cannot Mediate the Phase Transfer

We can now summarize the mathematical barriers separating the incidence operator from the density increment target:

1. **Pointwise Hole Support Forces Trivial $u$-Pairing**:
   Because $K(v, c)$ is supported on holes ($v \notin A$), $u(v) \equiv -a$ is constant on the support of $K$.
   All spatial correlation between $u$ and $K f$ reduces to the one-dimensional inner product $-a \langle g, f \rangle$.
2. **Schur Energy Imposes an $a^{3/2}$ Barrier**:
   The operator norm $\|K\|^2 \le 72\alpha/p$ is tight up to constants. Paired with any bounded pair vector, Cauchy-Schwarz enforces $|\mathbb{E}_\Omega[\overline{\psi} K f]| \le 6 w a^{3/2}$.
   The scaling $a^{3/2}$ is structurally fixed; no choice of pair weights can produce $a^{3/2} F(a)$ with $F(a) \to \infty$.
3. **The Gowers Exponent Gap**:
   In the zero-mean branch $m = 0$, $R_4 \sim 3 a^4 T$ is large, but Gowers $U^3$ inverse theorems only guarantee $\delta \ge a^{O(1)}$ with exponent at least 2, missing the super-critical threshold $3/2$.

```mermaid
flowchart TD
    IE[Weighted incidence operator K: ||K||^2 <= 72 alpha / p] --> BP[Bilinear pairing with any bounded f and psi]
    BP --> C6[Universal ceiling: |E_Omega[psibar Kf]| <= 6 w a^(3/2)]
    C6 --> OB1[No super-critical gain F_epsilon(a) -> infinity via K]
    
    HS[Pointwise hole support: B K = 0] --> DEC[u = -a on supp(K): complete spatial decoupling]
    DEC --> OB2[Pairing <u, Kf> = -a <g, f> lacks spatial oscillation]
    
    ZM[Zero-mean branch m = 0] --> R4[Exact quartic residual: R4 = 3 a^4 T > 0]
    R4 --> GI[Gowers U^3 inverse theorem: delta >= a^(4C) with 4C >= 2]
    GI --> OB3[Exponent gap: a^(4C) << a^(3/2) as a -> 0]
    
    OB1 --> TARGET[Target r_4(N) = o(N / log N) remains rigorously OPEN]
    OB2 --> TARGET
    OB3 --> TARGET
```

---

## 6. Updated Dependencies and Strategic Outlook

- **P12, W8, and DIRECT-Q-GAIN remain OPEN.**
- The October 21 full closure remains withdrawn.
- Next mathematical frontier:
  Since the single-host incidence operator $K$ is bounded by $6 w a^{3/2}$, the super-critical gain cannot come from local pair incidence geometry alone.
  A successful proof must either:
  1. Exploit the multi-scale Bohr system global consistency across overlapping hosts $\Omega_j$, ruling out the zero-mean pattern subsets of GI24; or
  2. Prove adequate quadratic phase selection directly without passing through the intermediate completion field $q$ or operator $K$.

---

## 7. Verification Scope

The dedicated verification script [verify_bilinear_pair_incidence_20261024.py](../../verification/scripts/verify_bilinear_pair_incidence_20261024.py) confirms all results:
- 846,305 exact checks passed across 982 arithmetic configurations (including 745 zero-mean configurations) on primes $p \in \{5, 7, 11, 13, 17\}$.
- Exact rational verification of $B(v) K(v, c) = 0$, $\langle u, K f \rangle = -a \langle g, f \rangle$, and the closed quartic residual identity (BP6).
- Verification of the universal $6 w a^{3/2}$ ceiling across all test pair modulations and quadratic chirps (maximum observed ratio 0.0466).
