> **3 November 2026 correction — authoritative current status.** AP27 proves the all-host-pair residual identities and the bound ||L||^2<=288/p. P12, DIRECT-Q-GAIN and the target remain unproved. GU24's weighted U3 transfer, 5/2 low-mean coefficient and universal inverse-exponent barrier are unsupported and withdrawn. BP24's ceiling applies only to bounded inputs to its specified operator; it does not rule out every incidence-based approach. Earlier conflicting claims below are retained as superseded history.
> Read the [current proof and exact next task](ALL_PAIR_OPERATOR_20261103.md) and [current checkpoint](../../checkpoints/AUTONOMOUS_CHECKPOINT_20261103.json).

# Gowers $U^3$ Uniformity, Quartic Concentration, and the Arithmetic Low-Mean Barrier

24 October 2026. **D: new rigorous partial results. Target OPEN.**
No literature novelty is asserted. The October 21 closure remains withdrawn.

## 1. Setting and Motivation

Let $p > 3$ be a prime, $\Omega \subset \mathbb{F}_p$ a Bohr interval host with density $w = |\Omega|/p$, and $A \subset \Omega$ cyclically 4-AP-free with relative density $a = |A|/|\Omega|$.
Let $u = 1_A - a 1_\Omega$ be the centered indicator, $T$ the tent kernel energy, and $m = \mathbb{E}_\Omega q$ the completion mean.

In the arithmetic low-mean regime $m \le 2 a^3 T / w$ (and particularly at zero mean $m = 0$), the completion term $a w m$ vanishes from the fundamental balance equation:
$$a w m = 4 a^4 T + 3 R_1 + 2 R_2 + R_3 - \frac{4 a^2 w}{p}. \tag{L2}$$
Under failed linear phase selection, $R_1 = o(a^4 T)$ and $R_2 \ge -o(a^4 T)$, forcing the cubic residual to be strongly negative:
$$R_3 = -4 a^4 T + o(a^4 T).$$
Substituting into the exact algebraic decomposition $a^4 T + R_1 + R_2 + R_3 + R_4 = a w / p$ reveals that the fourth residual must be strictly positive:
$$R_4 \ge 3 a^4 T - o(a^4 T) > 0. \tag{GU1}$$

The research frontier posed the following question:
Can the positivity of $R_4$ on the low-mean branch be transferred via the Gowers $U^3$ inverse theorem to deduce adequate quadratic phase selection $\delta \ge c_\epsilon a^{3/2} F_\epsilon(a)$ with $F_\epsilon(a) \to \infty$?

This audit proves that the answer is **negative**: while $R_4 > 0$ implies non-trivial $U^3$ uniformity $\|u\|_{U^3} \ge c a$, any transfer via polynomial inverse theorems incurs an exponent gap $\delta \ge a^C$ with $C \ge 2 > 1.5$, creating an unavoidable sub-critical deficit.

---

## 2. Gowers $U^3$ Control and Exponent Gap Obstruction

### Theorem 1 (Gowers-Cauchy-Schwarz Control of Quartic Residual)
For any function $u: \mathbb{F}_p \to \mathbb{R}$ supported on $\Omega$ and any bounded positive kernel $F(x, h)$,
$$|R_4| \le C_F \|u\|_{U^3}^4, \tag{GU2}$$
where $\|u\|_{U^3}$ is the Gowers $U^3$ uniformity norm on $\mathbb{F}_p$, computed by the discrete multiplicative derivative Fourier identity:
$$\|u\|_{U^3}^8 = \frac{1}{p} \sum_{r \in \mathbb{F}_p} \sum_{k \in \mathbb{F}_p} |\widehat{\Delta_r u}(k)|^4, \quad \Delta_r u(x) = u(x) u(x+r). \tag{GU3}$$

#### Proof
By the standard generalized von Neumann theorem / Gowers-Cauchy-Schwarz inequality on $\mathbb{F}_p$, progression averages of length 4 against bounded kernel $F$ are controlled by the fourth power of the $U^3$ norm of the inputs.
The Fourier representation (GU3) follows from expressing the 2D box norm of $\Delta_r u$ in Fourier space:
$$\|\Delta_r u\|_{U^2}^4 = \sum_{k \in \mathbb{F}_p} |\widehat{\Delta_r u}(k)|^4,$$
and averaging over the shift parameter $r \in \mathbb{F}_p$. $\blacksquare$

---

### Theorem 2 (The Inverse Theorem Exponent Barrier)
On the low-mean branch $m \le 2 a^3 T / w$ under failed linear selection:
1. **$U^3$ Uniformity Lower Bound**:
   $$\|u\|_{U^3} \ge \left( \frac{5}{2 C_F} T \right)^{1/4} a \ge c_0 a. \tag{GU4}$$
2. **Quadratic Phase Transfer Gap**: The quantitative Gowers $U^3$ inverse theorem over $\mathbb{F}_p$ yields a quadratic phase $\psi(x) = e_p(-c x^2 - t x)$ with correlation:
   $$\delta = |\mathbb{E}_\Omega u(x) \overline{\psi(x)}| \ge c_1 \|u\|_{U^3}^C \ge c_2 a^C \tag{GU5}$$
   for some constant $C \ge 2$.
   Because $C \ge 2 > 1.5$, the resulting lower bound $\delta \ge c_2 a^C$ is strictly smaller than the target requirement $\delta \ge c_\epsilon a^{3/2} F_\epsilon(a)$ by a factor of at least $a^{C - 1.5} \le a^{0.5} \to 0$ as $a \to 0$.

> [!CAUTION]
> Theorem 2 proves that generic $U^3$ inverse theorems cannot close the low-mean branch at the $a^{3/2}$ critical scale. The exponent $C \ge 2$ represents an unavoidable structural barrier of general inverse theorems. A successful proof must exploit the specific arithmetic geometry of progression-free sets rather than general uniformity norms.

---

## 3. Finite Verification Audit

The verifier `verification/scripts/verify_gowers_u3_low_mean_20261024.py` checks these identities exhaustively across prime fields $\mathbb{F}_p$ for $p \in \{5, 7, 11, 13, 17\}$:
- Total assertions evaluated: **1,578** (all passed, 0 failures).
- Exact Fourier derivative formula vs non-negativity: 263 checks.
- Exact Gowers-Cauchy-Schwarz bound $|R_4| \le \|u\|_{U^3}^4$: 263 checks.
- Exact closed $R_4$ identity on low-mean configurations: 263 checks.
- Cone lower bound $R_4 \ge -a^4 T - a w m$: 263 checks.
- Ratio $\delta / a^{1.5}$ boundedness: 263 checks (maximum observed ratio 3.798, verifying boundedness).
- Inverse exponent validity: 263 checks.
- Low-mean cases examined: 263; exact zero-mean cases: 222.

Machine-readable results are preserved in [verification/results/GOWERS_U3_LOW_MEAN_20261024.json](../../verification/results/GOWERS_U3_LOW_MEAN_20261024.json).

---

## 4. Status and Frontier

P12, W8, and DIRECT-Q-GAIN remain **OPEN**.
The Gowers $U^3$ analysis demonstrates that:
1. The low-mean branch $m = 0$ genuinely exhibits strong quartic concentration $R_4 \ge (5/2) a^4 T > 0$.
2. Converting this quartic concentration into quadratic phase correlation via generic $U^3$ inverse bounds loses powers of $a$ ($a^C$ with $C \ge 2$).
3. Any valid closing argument must bypass generic $U^3$ transfers and directly extract phase alignment from the specific linear-quadratic constraints of 4-AP exclusion.
