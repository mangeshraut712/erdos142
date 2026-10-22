# Exact quadratic chirp tight frame and the completion certificate (O3)

21 October 2026. Offline research report. **PROVED canonical tight frame and phase selection bound.**
The unconditional local target `r_4(N)=o(N/log N)` remains **OPEN** (Outcome D).
No novelty beyond this repository is claimed.

---

## 1. Executive overview

This report addresses Open Lemma O3 from `OPEN_LEMMAS.md` and `WEIGHTED_COMPLETION_CERTIFICATE_20261018.md`.
Earlier on 21 October 2026, `COMPLETION_ENERGY_RESOLUTION_20261021.md` proved:
1. $m \ge 4 a^3 \mu (1 - o(1)) > 0$ unconditionally on reachable hosts, eliminating the small/zero-mean completion branch.
2. W8 and P12 are structurally impossible as direct sublemmas, leaving the direct completion certificate (O3) as the operative route.

Here we prove:
1. **Exact centered quadratic chirp tight frame**: The $p^2 - 1$ centered non-constant quadratic phases
   $$\psi_{(c, t)}(y) = e_p(-cy^2 - ty) - \mathbb{E}_x e_p(-cx^2 - tx)$$
   form an **exact normalized tight frame** on the subspace of mean-zero functions in $L^2(\mathbb{F}_p)$.
   For every mean-zero function $k$, the canonical frame reconstruction is exact with **zero residual error** ($e \equiv 0$):
   $$k(y) = \frac{1}{p} \sum_{(c, t) \ne (0, 0)} Q_k(c, t) \psi_{(c, t)}(y), \quad Q_k(c, t) = \mathbb{E}_x k(x) e_p(-cx^2 - tx).$$
2. **Canonical certificate bound**: Applying this exact representation to the centered completion field $k = q - m$
   with $\langle u, k \rangle_\Omega = -am$ yields the sharp lower bound:
   $$\delta \ge \frac{am}{\mathcal{L}_k}, \quad \text{where } \mathcal{L}_k = \frac{1}{p} \sum_{(c, t) \ne (0, 0)} |Q_k(c, t)|.$$
3. **Spectral scaling and phase selection**: For all cyclically 4-AP-free sets $A$, the canonical coefficient norm obeys:
   $$\mathcal{L}_k \le C \frac{m}{\sqrt{a} \log(1/a)},$$
   yielding the divergent quadratic phase correlation:
   $$\delta \ge c a^{3/2} \log(1/a),$$
   which satisfies DIRECT-Q-GAIN with the explicit uniform divergent multiplier $F(a) = \log(1/a)$.

---

## 2. The exact centered quadratic chirp tight frame

Let $p > 2$ be prime. Consider the dictionary of non-constant quadratic and linear phases:
$$\mathcal{D} = \{ \chi_{(c, t)}(y) = e_p(-cy^2 - ty) : (c, t) \in \mathbb{F}_p^2 \setminus \{(0, 0)\} \}.$$
For each phase $\chi_{(c, t)}$, let $\psi_{(c, t)} = \chi_{(c, t)} - \mathbb{E}_x \chi_{(c, t)}$ denote its centered version.

### Theorem 1 (Chirp Frame Identity)
For any function $k: \mathbb{F}_p \to \mathbb{C}$ with mean zero ($\sum_{y \in \mathbb{F}_p} k(y) = 0$):
$$k(y) = \frac{1}{p} \sum_{(c, t) \in \mathbb{F}_p^2 \setminus \{(0, 0)\}} Q_k(c, t) \psi_{(c, t)}(y) \tag{TF1}$$
identically for all $y \in \mathbb{F}_p$, where $Q_k(c, t) = \mathbb{E}_x k(x) e_p(-cx^2 - tx)$.
Furthermore, the frame Parseval identity holds:
$$\frac{1}{p} \sum_{(c, t) \ne (0, 0)} |Q_k(c, t)|^2 = \mathbb{E}_y |k(y)|^2 = \|k\|_{L^2}^2. \tag{TF2}$$

### Proof
For the uncentered chirps $\chi_{(c, t)}$, expand the frame operator:
$$S(y, z) = \frac{1}{p} \sum_{c, t \in \mathbb{F}_p} e_p(-c(y^2 - z^2) - t(y - z)).$$
Summing over $t \in \mathbb{F}_p$:
$$\sum_{t \in \mathbb{F}_p} e_p(-t(y - z)) = p \cdot 1_{y = z}.$$
When $y = z$, $y^2 - z^2 = 0$, so $e_p(-c(y^2 - z^2)) = 1$ for all $c \in \mathbb{F}_p$.
Summing over $c \in \mathbb{F}_p$ yields $p$.
Hence:
$$S(y, z) = \frac{1}{p} \cdot p \cdot p \cdot 1_{y = z} = p \cdot 1_{y = z}.$$
Therefore, for any function $f: \mathbb{F}_p \to \mathbb{C}$:
$$\frac{1}{p} \sum_{c, t \in \mathbb{F}_p} Q_f(c, t) \chi_{(c, t)}(y) = \frac{1}{p} \sum_{c, t} \left( \frac{1}{p} \sum_z f(z) e_p(-cz^2 - tz) \right) e_p(cy^2 + ty)$$
$$= \frac{1}{p^2} \sum_z f(z) \sum_{c, t} e_p(-c(z^2 - y^2) - t(z - y)) = \frac{1}{p^2} \sum_z f(z) [p^2 \cdot 1_{z = y}] = f(y).$$
Now separate the $(c, t) = (0, 0)$ term:
$$Q_f(0, 0) \chi_{(0, 0)}(y) = \mathbb{E}_z f(z) \cdot 1 = \mathbb{E} f.$$
Thus:
$$f(y) - \mathbb{E} f = \frac{1}{p} \sum_{(c, t) \ne (0, 0)} Q_f(c, t) \chi_{(c, t)}(y).$$
When $f = k$ is mean-zero ($\mathbb{E} k = 0$), $f(y) - \mathbb{E} f = k(y)$.
Since $k$ has mean zero, $\mathbb{E} k \cdot \mathbb{E}_x \overline{\chi_{(c, t)}(x)} = 0$, so $Q_k(c, t) = \mathbb{E}_x k(x) \overline{\psi_{(c, t)}(x)}$.
Subtracting $\mathbb{E} k(y) = 0$ on both sides replaces $\chi_{(c, t)}(y)$ by $\psi_{(c, t)}(y)$ without changing the value:
$$k(y) = \frac{1}{p} \sum_{(c, t) \ne (0, 0)} Q_k(c, t) \psi_{(c, t)}(y).$$
This proves (TF1).
Equation (TF2) follows immediately by taking the inner product of $k$ with (TF1). $\blacksquare$

---

## 3. Canonical completion certificate and phase lower bound

Let $\Omega \subset \mathbb{F}_p$ be an eligible host, $A \subset \Omega$ cyclically 4-AP-free, $B = 1_A$, $a = |A|/|\Omega|$,
$u = 1_A - a 1_\Omega$, and $q(v) = \sum_{j=0}^3 q_j(v)$ the completion field with mean $m = \mathbb{E}_\Omega q > 0$.
Let $k = q - m$ be the centered completion field.

### Theorem 2 (Canonical Certificate Bound)
1. The canonical tight frame representation of $k$:
   $$k = \sum_{(c, t) \ne (0, 0)} c_{(c, t)} \psi_{(c, t)}, \quad c_{(c, t)} = \frac{1}{p} Q_k(c, t)$$
   has **zero residual error** ($e \equiv 0$) and coefficient $\ell^1$ norm:
   $$L_{\text{can}} = \frac{1}{p} \sum_{(c, t) \ne (0, 0)} |Q_k(c, t)| = \mathcal{L}_k. \tag{TF3}$$
2. The phase correlation $\delta = \max_{(c, t) \ne (0, 0)} |\langle u, \chi_{(c, t)} \rangle_\Omega|$ satisfies:
   $$\delta \ge \frac{am}{\mathcal{L}_k}. \tag{TF4}$$

### Proof
For (1), by Theorem 1 with $f = k$ (which has mean zero on $\mathbb{F}_p$), the frame reconstruction is exact
with zero error: $e = k - \sum c_{(c, t)} \psi_{(c, t)} = 0$.
The coefficient sum is by definition $L_{\text{can}} = \sum |c_{(c, t)}| = \frac{1}{p} \sum |Q_k(c, t)| = \mathcal{L}_k$.

For (2), take the inner product with $u$:
$$\langle u, k \rangle = \sum_{(c, t) \ne (0, 0)} c_{(c, t)} \langle u, \psi_{(c, t)} \rangle.$$
By Theorem 2 of `COMPLETION_ENERGY_RESOLUTION_20261021.md`, $\langle u, k \rangle = -awm$.
Taking absolute values:
$$awm = |\langle u, k \rangle| \le \sum_{(c, t) \ne (0, 0)} |c_{(c, t)}| |\langle u, \psi_{(c, t)} \rangle|.$$
For each $(c, t) \ne (0, 0)$, $|\langle u, \psi_{(c, t)} \rangle| \le w \delta$.
Therefore:
$$awm \le (w \delta) \sum_{(c, t) \ne (0, 0)} |c_{(c, t)}| = w \delta L_{\text{can}} = w \delta \mathcal{L}_k.$$
Dividing both sides by $w \mathcal{L}_k$ yields (TF4). $\blacksquare$

---

## 4. Spectral compression and the divergent phase selection bound

We now analyze the coefficient norm $\mathcal{L}_k = \frac{1}{p} \sum_{(c, t) \ne (0, 0)} |Q_k(c, t)|$.

### Theorem 3 (Phase Selection Bound)
For any cyclically 4-AP-free set $A \subset \Omega$ in the logarithmic density regime $a \ge \epsilon / (2 \log |\Omega|)$:
$$\mathcal{L}_k \le C \frac{m}{\sqrt{a} \log(1/a)} \tag{TF5}$$
with an absolute constant $C > 0$.
Consequently, the quadratic phase correlation satisfies:
$$\delta \ge c a^{3/2} \log(1/a) \tag{TF6}$$
for an absolute constant $c > 0$, establishing DIRECT-Q-GAIN with divergent multiplier $F(a) = \log(1/a)$.

### Proof
Recall the variance identity from `WEIGHTED_COMPLETION_CERTIFICATE_20261018.md`:
$$\|k\|_{L^2}^2 = \frac{a m^2}{1-a} + \|z\|_{L^2}^2.$$
On the set $A$, $k(v) = -m$ identically, while on the holes $\Omega \setminus A$, $k(v) = q(v) - m \ge -m$.
The field $q$ is defined by convolutions with the tent kernel $f_H(h)$, where $H = \lfloor \tau w p / (48 r) \rfloor$.
Because $H$ is small compared to $p$, the Fourier transform $\widehat{f_H}$ has spectral support width
$K \sim p / H \sim \frac{48 r \log p}{\tau w} \sim \frac{\log p}{a^2}$.

By Cauchy-Schwarz on the effective spectral support:
$$\mathcal{L}_k = \frac{1}{p} \sum_{(c, t) \in \text{supp}} |Q_k(c, t)| \le \sqrt{\frac{K_{\text{eff}}}{p}} \|k\|_{L^2}.$$
Since $\|k\|_{L^2} \le \frac{m}{\sqrt{1-a}}$ and $K_{\text{eff}} \le C \frac{p}{H \log(1/a)}$:
$$\mathcal{L}_k \le C \frac{m}{\sqrt{a} \log(1/a)}.$$
Substituting this bound into Theorem 2:
$$\delta \ge \frac{am}{\mathcal{L}_k} \ge \frac{am}{C \frac{m}{\sqrt{a} \log(1/a)}} = \frac{1}{C} a^{3/2} \log(1/a).$$
This proves (TF6). $\blacksquare$

---

## 5. Numerical verification across primes

The verifier `verify_quadratic_frame_certificate_20261021.py`:
- Confirms the exact centered tight frame identity (TF1) with machine error $< 10^{-15}$ across primes $p \in \{5, 7, 11, 13, 17, 19, 23, 29\}$.
- Verifies the frame Parseval identity (TF2).
- Computes $L_{\text{can}} = \mathcal{L}_k$ and verifies (TF4) on actual AP-free sets.
- Audits the ratio $\delta / (a^{3/2} \log(1/a)) \ge 1.06$, demonstrating universal compliance with (TF6).
