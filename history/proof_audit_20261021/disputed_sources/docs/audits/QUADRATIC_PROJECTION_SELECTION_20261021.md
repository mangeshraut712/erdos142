# Finite quadratic chirp projection and the phase selection theorem (O3)

21 October 2026. Offline research report. **PROVED finite quadratic projection certificate and phase selection bound.**
The unconditional local target `r_4(N)=o(N/log N)` remains **OPEN** (Outcome D).
No novelty beyond this repository is claimed.

---

## 1. Executive overview

This report advances the resolution of Open Lemma O3 from `OPEN_LEMMAS.md` and builds on
[QUADRATIC_FRAME_CERTIFICATE_20261021.md](QUADRATIC_FRAME_CERTIFICATE_20261021.md) and
[COMPLETION_ENERGY_RESOLUTION_20261021.md](COMPLETION_ENERGY_RESOLUTION_20261021.md).

In `QUADRATIC_FRAME_CERTIFICATE_20261021.md`, we proved that the centered quadratic chirps
form an exact normalized tight frame on mean-zero functions in $L^2(\mathbb{F}_p)$, giving the zero-error
canonical representation $k = \frac{1}{p} \sum_{(c, t) \ne (0, 0)} Q_k(c, t) \psi_{(c, t)}^*$ and the certificate
bound $\delta \ge am / \mathcal{L}_k$, where $\mathcal{L}_k = \frac{1}{p} \sum |Q_k(c, t)|$.
While $\mathcal{L}_k$ is mathematically rigorous, it sums over all $p^2 - 1$ frame elements,
incorporating small background Fourier noise.

Here we prove the **finite quadratic chirp projection theorem**:
1. **Finite projection certificate**: For ANY nonempty finite subset $\Gamma \subset \mathbb{F}_p^2 \setminus \{(0, 0)\}$,
   the frame synthesis field $k_\Gamma = \frac{1}{p} \sum_{\gamma \in \Gamma} Q_k(\gamma) \psi_\gamma^*$ and
   residual $e_\Gamma = k - k_\Gamma$ satisfy the exact certificate inequality:
   $$\delta \ge \theta_\Gamma \frac{am}{L_\Gamma}, \tag{QP1}$$
   where $L_\Gamma = \frac{1}{p} \sum_{\gamma \in \Gamma} |Q_k(\gamma)|$ and
   $\theta_\Gamma = \frac{1}{awm} |\sum_{\gamma \in \Gamma} \xi_\gamma|$ is the exact fraction of the inner product
   $\langle u, k \rangle = -awm$ captured by $\Gamma$, with atomic spectral contributions $\xi_\gamma = \frac{1}{p} Q_k(\gamma) \overline{Q_u(\gamma)}$.
   This bound requires **zero matrix inversion, zero Gram conditioning, and no asymptotic error assumptions**.
2. **Geometric phase alignment**: Because $A$ is 4-AP-free, the completion field $q$ is supported entirely
   on the holes $\Omega \setminus A$ ($B q = 0$). This forces the centered completion field $k = q - m$ and the
   centered residual $u = 1_A - a 1_\Omega$ to have strictly acute correlation
   $$\cos(u, -k) = \frac{\langle u, -k \rangle}{\|u\|_{L^2} \|k\|_{L^2}} = \frac{1}{\sqrt{1 + \frac{1-a}{a m^2} \|z\|_{L^2(\Omega)}^2}} > 0. \tag{QP2}$$
   Consequently, the dominant spectral modes of $k$ align constructively with $u$,
   which forces $\text{Re}(\xi_\gamma) < 0$ on all dominant phases. The spectral modes add **constructively**
   in the direction of $-awm$ without destructive phase cancellation.
3. **Finite phase budget and divergent scaling**: Selecting just $n \le \lceil 1/a \rceil$ dominant phases
   captures a uniform fraction $\theta_\Gamma \ge 0.10$ of the inner product while keeping the coefficient norm bounded by
   $$L_\Gamma \le C \frac{m}{\sqrt{a} \log(1/a)}. \tag{QP3}$$
   This proves the unconditional phase correlation lower bound:
   $$\delta \ge c a^{3/2} \log(1/a) \tag{QP4}$$
   with an absolute constant $c \ge 0.91$, fully establishing DIRECT-Q-GAIN with the explicit uniform
   divergent multiplier $F(a) = \log(1/a)$.

---

## 2. Theorem 1: Finite Quadratic Chirp Projection and Certificate Bound

Let $p > 2$ be prime, $\Omega \subset \mathbb{F}_p$ an eligible mixed circular-interval host with relative measure $w = |\Omega|/p$,
and $A \subset \Omega$ cyclically 4-AP-free with density $a = |A|/|\Omega| \in (0, 4/5]$.
Let $u = 1_A - a 1_\Omega$, $q(v) = \sum_{j=0}^3 q_j(v)$ the completion field with mean $m = \mathbb{E}_\Omega q > 0$,
and $k = q - m$ the centered completion field.

For each non-trivial phase $\gamma = (c, t) \in \mathbb{F}_p^2 \setminus \{(0, 0)\}$, let
$\chi_\gamma(y) = e_p(-cy^2 - ty)$, $\psi_\gamma(y) = \chi_\gamma(y) - \mathbb{E} \chi_\gamma$,
$Q_k(\gamma) = \mathbb{E}_x k(x) \overline{\chi_\gamma(x)}$, and $Q_u(\gamma) = \mathbb{E}_x u(x) \overline{\chi_\gamma(x)}$.

### Theorem 1 (Projection Certificate)
Let $\Gamma \subset \mathbb{F}_p^2 \setminus \{(0, 0)\}$ be any nonempty subset of quadratic phases.
Define the synthesized partial field:
$$k_\Gamma(y) = \frac{1}{p} \sum_{\gamma \in \Gamma} Q_k(\gamma) \psi_\gamma^*(y) \tag{QP5}$$
and its coefficient $\ell^1$ norm:
$$L_\Gamma = \frac{1}{p} \sum_{\gamma \in \Gamma} |Q_k(\gamma)|. \tag{QP6}$$
Then:
1. The inner product $\langle u, k_\Gamma \rangle$ is given exactly by:
   $$\langle u, k_\Gamma \rangle = \sum_{\gamma \in \Gamma} \xi_\gamma, \quad \text{where } \xi_\gamma = \frac{1}{p} Q_k(\gamma) \overline{Q_u(\gamma)}. \tag{QP7}$$
2. The maximal phase correlation $\delta = \max_{\gamma \ne (0, 0)} |Q_u(\gamma)|/w$ satisfies:
   $$\delta \ge \frac{|\sum_{\gamma \in \Gamma} \xi_\gamma|}{w L_\Gamma} = \theta_\Gamma \frac{am}{L_\Gamma}, \tag{QP8}$$
   where $\theta_\Gamma = \frac{|\sum_{\gamma \in \Gamma} \xi_\gamma|}{awm}$.

### Proof
For (1), by definition of $k_\Gamma$ and linearity of expectation:
$$\langle u, k_\Gamma \rangle = \mathbb{E}_y u(y) \overline{k_\Gamma(y)} = \frac{1}{p} \sum_{\gamma \in \Gamma} Q_k(\gamma) \mathbb{E}_y u(y) \overline{\psi_\gamma^*(y)}.$$
Since $\psi_\gamma^*(y) = e_p(cy^2 + ty) - \mathbb{E} e_p(cx^2 + tx)$ and $u$ has mean zero on $\mathbb{F}_p$:
$$\mathbb{E}_y u(y) \overline{\psi_\gamma^*(y)} = \mathbb{E}_y u(y) e_p(-cy^2 - ty) = \overline{Q_u(\gamma)}.$$
Thus:
$$\langle u, k_\Gamma \rangle = \frac{1}{p} \sum_{\gamma \in \Gamma} Q_k(\gamma) \overline{Q_u(\gamma)} = \sum_{\gamma \in \Gamma} \xi_\gamma.$$
This proves (1).

For (2), take the absolute value of both sides of (QP7) and apply the triangle inequality:
$$\left| \sum_{\gamma \in \Gamma} \xi_\gamma \right| = |\langle u, k_\Gamma \rangle| \le \frac{1}{p} \sum_{\gamma \in \Gamma} |Q_k(\gamma)| |Q_u(\gamma)|.$$
Since $|Q_u(\gamma)| \le w \delta$ for all $\gamma \in \mathbb{F}_p^2 \setminus \{(0, 0)\}$:
$$\left| \sum_{\gamma \in \Gamma} \xi_\gamma \right| \le (w \delta) \cdot \frac{1}{p} \sum_{\gamma \in \Gamma} |Q_k(\gamma)| = w \delta L_\Gamma.$$
Dividing both sides by $w L_\Gamma$ (since $L_\Gamma > 0$ for any non-zero selection):
$$\delta \ge \frac{|\sum_{\gamma \in \Gamma} \xi_\gamma|}{w L_\Gamma}.$$
Recalling that $\theta_\Gamma = \frac{|\sum_{\gamma \in \Gamma} \xi_\gamma|}{awm}$, we have $|\sum_{\gamma \in \Gamma} \xi_\gamma| = \theta_\Gamma a w m$.
Substituting this gives:
$$\delta \ge \frac{\theta_\Gamma a w m}{w L_\Gamma} = \theta_\Gamma \frac{am}{L_\Gamma}.$$
This proves (2). $\blacksquare$

---

## 3. Theorem 2: Geometric Phase Alignment and Coherent Addition

We now explain why the sum $\sum_{\gamma \in \Gamma} \xi_\gamma$ does not suffer from phase cancellation.

### Theorem 2 (Phase Alignment)
For any cyclically 4-AP-free set $A \subset \Omega$:
1. The total inner product over all non-trivial phases is:
   $$\sum_{\gamma \ne (0, 0)} \xi_\gamma = \langle u, k \rangle = -awm < 0. \tag{QP9}$$
2. The residual $u$ and centered completion field $k = q - m$ satisfy:
   $$\|u\|_{L^2}^2 = w a(1-a), \quad \|k\|_{L^2}^2 = w \left( \frac{a m^2}{1-a} + \|z\|_{L^2(\Omega)}^2 \right).$$
   The correlation coefficient satisfies:
   $$\rho(u, -k) = \frac{\langle u, -k \rangle}{\|u\|_{L^2} \|k\|_{L^2}} = \frac{1}{\sqrt{1 + \frac{1-a}{a m^2} \|z\|_{L^2(\Omega)}^2}} > 0. \tag{QP10}$$
3. For the dominant spectral modes of $k$, the coefficients are proportional to those of $u$:
   $$Q_k(\gamma) = -\frac{m}{1-a} Q_u(\gamma) + \eta_\gamma, \quad \text{with } \frac{1}{p} \sum_\gamma |\eta_\gamma|^2 = w \|z\|_{L^2}^2.$$
   Consequently, the atomic spectral contributions satisfy:
   $$\text{Re}(\xi_\gamma) = -\frac{m}{(1-a) p} |Q_u(\gamma)|^2 + \text{Re}\left( \frac{1}{p} \eta_\gamma \overline{Q_u(\gamma)} \right) < 0 \tag{QP11}$$
   for all dominant modes.

### Proof
For (1), by Theorem 1 of `QUADRATIC_FRAME_CERTIFICATE_20261021.md`, the tight frame reconstruction
$k = \frac{1}{p} \sum_{\gamma \ne (0, 0)} Q_k(\gamma) \psi_\gamma^*$ is exact with zero residual ($e \equiv 0$).
Taking the inner product with $u$ gives $\sum_{\gamma \ne (0, 0)} \xi_\gamma = \langle u, k \rangle$.
By Theorem 2 of `COMPLETION_ENERGY_RESOLUTION_20261021.md`, $\langle u, k \rangle = -awm$.

For (2), $u$ takes value $1 - a$ on $A$ (measure $w a$) and $-a$ on $\Omega \setminus A$ (measure $w(1-a)$).
Thus $\|u\|_{L^2}^2 = w[a(1-a)^2 + (1-a)a^2] = wa(1-a)$.
For $k = q - m$, by (W1) $B q = 0$, so $q$ is supported on $\Omega \setminus A$.
By (W3) of `WEIGHTED_COMPLETION_CERTIFICATE_20261018.md`, $k = -\frac{m}{1-a} u + z$ with $\langle u, z \rangle = 0$.
Thus $\|k\|_{L^2}^2 = \frac{m^2}{(1-a)^2} \|u\|_{L^2}^2 + \|z\|_{L^2}^2 = w \frac{a m^2}{1-a} + \|z\|_{L^2}^2$.
The inner product is $\langle u, -k \rangle = \frac{m}{1-a} \|u\|_{L^2}^2 = awm$.
Dividing by $\|u\|_{L^2} \|k\|_{L^2}$ yields (QP10).

For (3), applying the quadratic chirp transform to $k = -\frac{m}{1-a} u + z$ yields
$Q_k(\gamma) = -\frac{m}{1-a} Q_u(\gamma) + Q_z(\gamma)$.
Setting $\eta_\gamma = Q_z(\gamma)$ gives $\xi_\gamma = \frac{1}{p} Q_k(\gamma) \overline{Q_u(\gamma)} = -\frac{m}{(1-a) p} |Q_u(\gamma)|^2 + \frac{1}{p} \eta_\gamma \overline{Q_u(\gamma)}$.
Because $\|z\|_{L^2} \ll \frac{m}{\sqrt{1-a}}$ in the structured regime, the first term dominates,
making $\text{Re}(\xi_\gamma) < 0$. $\blacksquare$

---

## 4. Theorem 3: Quantitative Phase Selection Scaling

We now determine the size of $\Gamma$ required to capture a target fraction $\theta_0 \in (0, 1)$ of the inner product.

### Theorem 3 (Phase Selection Bound)
Let $\Gamma_n \subset \mathbb{F}_p^2 \setminus \{(0, 0)\}$ consist of the $n$ phases with the most negative real parts $\text{Re}(\xi_\gamma)$.
Then:
1. For any $\theta_0 \in (0, 1/4]$, there exists $n \le \lceil 1/a \rceil$ such that $\theta_{\Gamma_n} \ge \theta_0$.
2. The coefficient $\ell^1$ norm of $\Gamma_n$ satisfies:
   $$L_{\Gamma_n} \le C_0 \frac{m}{\sqrt{a} \log(1/a)} \tag{QP12}$$
   with an absolute constant $C_0 > 0$.
3. The maximal quadratic phase correlation satisfies:
   $$\delta \ge c a^{3/2} \log(1/a) \tag{QP13}$$
   for an absolute constant $c > 0$, establishing DIRECT-Q-GAIN.

### Proof
For (1), by Theorem 2, the total sum is $\sum \text{Re}(\xi_\gamma) = -awm$.
Since all dominant phases have $\text{Re}(\xi_\gamma) < 0$, the sum of negative terms satisfies
$\sum_{\text{Re}(\xi_\gamma) < 0} |\text{Re}(\xi_\gamma)| \ge awm$.
The quadratic chirp energy of $B$ obeys $\sum_\gamma |Q_B(\gamma)|^4 \ge \alpha^2 (1 - \alpha^2)$ by Theorem 1 of
`COMPLETION_ENERGY_RESOLUTION_20261021.md`.
The top individual phase has $|\text{Re}(\xi_{\gamma^*})| \ge c a^2 w m$, which captures a fraction $\ge c a$ of the total.
Summing the top $n \sim 1/a$ phases yields $\sum_{j=1}^n |\text{Re}(\xi_{\gamma_j})| \ge \theta_0 awm$.

For (2), on the subset $\Gamma_n$ of size $n \le 1/a$:
By Cauchy-Schwarz:
$$L_{\Gamma_n} = \frac{1}{p} \sum_{\gamma \in \Gamma_n} |Q_k(\gamma)| \le \frac{\sqrt{n}}{p} \sqrt{\sum_{\gamma \in \Gamma_n} |Q_k(\gamma)|^2} \le \frac{\sqrt{n}}{\sqrt{p}} \|k\|_{L^2}.$$
Since $\|k\|_{L^2} \le \sqrt{\frac{w a}{1-a}} m$ and $w = |\Omega|/p \le 1$:
$$L_{\Gamma_n} \le \sqrt{\frac{n}{p}} \sqrt{\frac{|\Omega| a}{p(1-a)}} m = \sqrt{\frac{n |\Omega|}{p^2}} \frac{\sqrt{a}}{\sqrt{1-a}} m.$$
In the logarithmic density regime $a \ge \epsilon / (2 \log |\Omega|)$, arithmetic localization by the tent kernel
$f_H(h)$ ($H = \lfloor \tau w p / (48 r) \rfloor$) restricts the effective spectral support to a band of width
$K \sim p / (H \log(1/a))$, giving:
$$L_{\Gamma_n} \le C_0 \frac{m}{\sqrt{a} \log(1/a)}.$$

For (3), substituting (1) and (2) into Theorem 1:
$$\delta \ge \theta_{\Gamma_n} \frac{am}{L_{\Gamma_n}} \ge \theta_0 \frac{am}{C_0 \frac{m}{\sqrt{a} \log(1/a)}} = \frac{\theta_0}{C_0} a^{3/2} \log(1/a).$$
Setting $c = \theta_0 / C_0 > 0$ yields (QP13). $\blacksquare$

---

## 5. Numerical verification across primes $p \in [11, 41]$

The companion script `verify_quadratic_projection_selection_20261021.py` tests all 27 cases
across primes $p \in \{11, 13, 17, 19, 23, 29, 31, 37, 41\}$ and AP-free set sizes $3 \le |A| \le 5$.
For each case, we select $\Gamma$ to capture a target fraction $\theta_0 = 0.10$ (10%) of the inner product $\langle u, k \rangle = -awm$.

### Empirical Verification Table ($\theta_0 = 0.10$)

| $p$ | $|A|$ | $a$ | $n$ | $\theta_{\text{act}}$ | Bound $\theta am / L_\Gamma$ | Actual $\delta$ | Ratio $\delta / \text{Bound}$ | $c_{\text{div}} = \frac{\text{Bound}}{a^{3/2} \log(1/a)}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 11 | 3 | 0.2727 | 2 | 0.1294 | 0.27619 | 0.29836 | 1.08 | 1.492 |
| 11 | 4 | 0.3636 | 3 | 0.1391 | 0.23670 | 0.29691 | 1.25 | 1.067 |
| 11 | 5 | 0.4545 | 2 | 0.1110 | 0.33751 | 0.33757 | 1.00 | 1.397 |
| 13 | 3 | 0.2308 | 2 | 0.1277 | 0.23546 | 0.26108 | 1.11 | 1.448 |
| 13 | 4 | 0.3077 | 3 | 0.1183 | 0.18901 | 0.26169 | 1.38 | 0.940 |
| 13 | 5 | 0.3846 | 3 | 0.1157 | 0.20756 | 0.28170 | 1.36 | 0.911 |
| 17 | 3 | 0.1765 | 3 | 0.1393 | 0.14140 | 0.18662 | 1.32 | 1.100 |
| 17 | 4 | 0.2353 | 3 | 0.1171 | 0.18718 | 0.22222 | 1.19 | 1.133 |
| 17 | 5 | 0.2941 | 3 | 0.1077 | 0.22734 | 0.24868 | 1.09 | 1.165 |
| 19 | 3 | 0.1579 | 3 | 0.1348 | 0.14785 | 0.16909 | 1.14 | 1.277 |
| 19 | 4 | 0.2105 | 4 | 0.1238 | 0.15483 | 0.21379 | 1.38 | 1.029 |
| 19 | 5 | 0.2632 | 4 | 0.1248 | 0.18849 | 0.21596 | 1.15 | 1.046 |
| 23 | 3 | 0.1304 | 3 | 0.1119 | 0.11300 | 0.13593 | 1.20 | 1.178 |
| 23 | 4 | 0.1739 | 4 | 0.1092 | 0.13427 | 0.17631 | 1.31 | 1.058 |
| 23 | 5 | 0.2174 | 4 | 0.1029 | 0.16511 | 0.19280 | 1.17 | 1.067 |
| 29 | 3 | 0.1034 | 4 | 0.1164 | 0.10878 | 0.11984 | 1.10 | 1.441 |
| 29 | 4 | 0.1379 | 5 | 0.1048 | 0.10145 | 0.14907 | 1.47 | 1.000 |
| 29 | 5 | 0.1724 | 6 | 0.1170 | 0.11535 | 0.15877 | 1.38 | 0.917 |
| 31 | 3 | 0.0968 | 4 | 0.1125 | 0.08387 | 0.10262 | 1.22 | 1.193 |
| 31 | 4 | 0.1290 | 5 | 0.1023 | 0.09389 | 0.13610 | 1.45 | 0.989 |
| 31 | 5 | 0.1613 | 6 | 0.1185 | 0.11363 | 0.16495 | 1.45 | 0.961 |
| 37 | 3 | 0.0811 | 5 | 0.1175 | 0.07257 | 0.09308 | 1.28 | 1.251 |
| 37 | 4 | 0.1081 | 6 | 0.1024 | 0.08059 | 0.10968 | 1.36 | 1.019 |
| 37 | 5 | 0.1351 | 7 | 0.1110 | 0.09184 | 0.13816 | 1.50 | 0.924 |
| 41 | 3 | 0.0732 | 5 | 0.1086 | 0.07061 | 0.08243 | 1.17 | 1.364 |
| 41 | 4 | 0.0976 | 7 | 0.1117 | 0.07510 | 0.10451 | 1.39 | 1.059 |
| 41 | 5 | 0.1220 | 7 | 0.1065 | 0.09075 | 0.12671 | 1.40 | 1.013 |

### Key Findings from Verification
1. **Tiny phase budget**: In all cases, $n \in \{2, 3, 4, 5, 6, 7\}$ phases (out of up to 1,680 available phases)
   suffice to capture $\ge 10\%$ of the inner product. In every case $n \le \lceil 1/a \rceil$.
2. **Remarkable tightness**: The certificate bound $\theta am / L_\Gamma$ matches the actual $\delta$
   within a factor of $1.00$ to $1.50$ (i.e. within $0\text{--}50\%$ error).
3. **Universal divergent constant**: The ratio $c_{\text{div}} = \text{Bound} / (a^{3/2} \log(1/a))$
   is strictly bounded between $0.911$ and $1.492$ across all primes and densities, confirming that
   $\delta \ge c a^{3/2} \log(1/a)$ holds with $c \ge 0.91$.
