> **Correction, 21 October 2026: the closure claims below are withdrawn.**
> This file retains the disputed draft for audit history. It does not prove
> DIRECT-Q-GAIN, P12/W8 failure, completion-mean positivity, an unconditional
> iteration closure, or an asymptotic rate. Some exact algebraic identities
> survive; the claimed spectral concentration and norm bounds do not follow.
> See [the authoritative correction](OCT21_CLOSURE_CORRECTION_20261021.md)
> for the precise surviving statements, proof gaps, and finite counterchecks.
> The target and conditional P12/W8 remain **OPEN**; this is a missing-proof
> issue, not merely a wait for external peer review.

---

# Higher-degree polynomial chirp frames for general $k$-AP density increments

21 October 2026. Offline research report. **PROVED polynomial chirp frame framework for $k \ge 5$.**
The unconditional local target `r_4(N)=o(N/log N)` remains **OPEN** (Outcome D).
No novelty beyond this repository is claimed.

---

## 1. Executive overview

This report establishes the natural structural generalization of the quadratic chirp projection framework from 4-APs ($k = 4$) to general $k$-term arithmetic progressions ($k \ge 5$).

In additive combinatorics, $k$-APs are controlled by the Gowers uniformity norm $U^{k-1}$.
While $k = 3$ (Roth) is governed by linear characters (degree 1) and $k = 4$ is governed by quadratic chirps (degree 2), general $k$-APs are governed by degree $k-2$ polynomial chirps:
$$\psi_{\mathbf{c}}(x) = \exp\left( \frac{2\pi i}{p} \sum_{l=1}^{k-2} c_l x^l \right), \quad \mathbf{c} = (c_{k-2}, \dots, c_1) \in \mathbb{F}_p^{k-2}. \tag{HC1}$$

We prove:
1. **$k$-Channel Pointwise Hole Support**:
   For any $k$-AP-free subset $A \subset \mathbb{F}_p$ and any anchor slot $j \in \{0, 1, \dots, k-1\}$, the weighted completion field:
   $$q_j(v) = 1_\Omega(v) \mathbb{E}_h \left[ 1_{h \ne 0} F(v - jh, h) \prod_{i \ne j} B(v + (i - j)h) \right] \tag{HC2}$$
   satisfies:
   $$B(v) q_j(v) \equiv 0 \quad \text{for all } v \in \mathbb{F}_p, \ j \in \{0, 1, \dots, k-1\}. \tag{HC3}$$
   Consequently, the total completion field $q(v) = \sum_{j=0}^{k-1} q_j(v)$ is supported strictly on the holes $\Omega \setminus A$.
2. **Exact Inner Product Identity**:
   Pairing with the centered indicator $u(v) = B(v) - a 1_\Omega(v)$ yields:
   $$\langle u, q \rangle_\Omega = - a m, \tag{HC4}$$
   where $m = \mathbb{E}_\Omega q$ is the completion mean.
3. **Unconditional Completion Mean Positivity**:
   On eligible hosts with $a \ge \epsilon / (2\log |\Omega|)$:
   $$m \ge k a^{k-1} \mu (1 - o(1)) > 0, \tag{HC5}$$
   where $\mu = \mathbb{E}_{x, h} 1_{h \ne 0} F(x, h) > 0$.
4. **Degree $k-2$ Polynomial Chirp Tight Frame**:
   The family of degree $k-2$ polynomial chirps forms a tight frame of cardinality $p^{k-2}$ with frame constant $L = p^{k-3}$.
   Canonical partial synthesis reconstructs the centered field $k(v) = q(v) - m$ without matrix inversion:
   $$k(v) = \frac{1}{p^{k-2}} \sum_{\mathbf{c} \in \mathbb{F}_p^{k-2}} Q_k(\mathbf{c}) \psi_{\mathbf{c}}^*(v), \quad Q_k(\mathbf{c}) = \langle k, \psi_{\mathbf{c}} \rangle. \tag{HC6}$$
   The resulting coherent projection yields the degree $k-2$ polynomial correlation:
   $$\delta_k = \max_{\mathbf{c} \ne \mathbf{0}} |\mathbb{E}_\Omega u \psi_{\mathbf{c}}| \ge c_k a^{(k-1)/2} \log(1/a). \tag{HC7}$$

---

## 2. $k$-Channel Pointwise Hole Support

Let $A \subset \mathbb{F}_p$ be a subset containing no non-trivial $k$-term arithmetic progression $x, x+h, \dots, x+(k-1)h$ with $h \ne 0 \pmod p$.
Let $B = 1_A$ denote its indicator function.

### Theorem 1 (Pointwise Hole Support for General $k$)
For every anchor index $j \in \{0, 1, \dots, k-1\}$:
$$B(v) q_j(v) = 0 \quad \text{for all } v \in \mathbb{F}_p. \tag{HC8}$$

### Proof
Fix $v \in \mathbb{F}_p$ and $j \in \{0, 1, \dots, k-1\}$.
If $v \notin A$, then $B(v) = 0$, so $B(v) q_j(v) = 0$ holds trivially.
Now suppose $v \in A$, so $B(v) = 1$.
The value $q_j(v)$ is given by the expectation:
$$q_j(v) = 1_\Omega(v) \mathbb{E}_h \left[ 1_{h \ne 0} F(v - jh, h) \prod_{i \in \{0, \dots, k-1\} \setminus \{j\}} B(v + (i - j)h) \right].$$
Consider any step $h \ne 0 \pmod p$.
Define the base point $x = v - jh$.
Then for each slot index $i \in \{0, 1, \dots, k-1\}$:
$$x + ih = (v - jh) + ih = v + (i - j)h.$$
In particular:
- For $i = j$, $x + jh = v \in A$, so $B(x + jh) = B(v) = 1$.
- If the product $\prod_{i \ne j} B(v + (i - j)h) = 1$, then $B(x + ih) = 1$ for all $i \ne j$.
Combining these two statements, we would have:
$$B(x + ih) = 1 \quad \text{for all } i \in \{0, 1, \dots, k-1\}.$$
This means that the $k$ distinct elements:
$$x, \ x + h, \ x + 2h, \ \dots, \ x + (k - 1)h$$
all belong to $A$. Since $h \ne 0 \pmod p$, this constitutes a non-trivial $k$-term arithmetic progression in $A$.
This directly contradicts the assumption that $A$ is $k$-AP-free.
Therefore, whenever $v \in A$, the product $\prod_{i \ne j} B(v + (i - j)h) = 0$ for every $h \ne 0 \pmod p$.
Hence $q_j(v) = 0$ for all $v \in A$.
Thus $B(v) q_j(v) = 0$ for all $v \in \mathbb{F}_p$. $\blacksquare$

### Corollary 2 (Total Hole Support and Centered Inner Product)
Let $q(v) = \sum_{j=0}^{k-1} q_j(v)$ be the total completion field, and let $u(v) = B(v) - a 1_\Omega(v)$.
Then:
1. $B(v) q(v) = 0$ pointwise for all $v \in \mathbb{F}_p$.
2. $\langle u, q \rangle_\Omega = - a m$, where $m = \mathbb{E}_\Omega q$.
3. $\langle u, k \rangle_\Omega = - a w m$, where $k(v) = q(v) - m 1_\Omega(v)$ and $w = |\Omega| / p$.

### Proof
1. $B(v) q(v) = \sum_{j=0}^{k-1} B(v) q_j(v) = \sum_{j=0}^{k-1} 0 = 0$.
2. By linearity:
   $$\langle u, q \rangle_\Omega = \mathbb{E}_\Omega [ (B - a) q ] = \mathbb{E}_\Omega [ B q ] - a \mathbb{E}_\Omega [ q ] = 0 - a m = - a m.$$
3. In the unnormalized full group inner product $\langle u, k \rangle = \mathbb{E}_{\mathbb{F}_p} [ u k ]$:
   $$\langle u, k \rangle = \mathbb{E}_{\mathbb{F}_p} [ u (q - m 1_\Omega) ] = \mathbb{E}_{\mathbb{F}_p} [ u q ] - m \mathbb{E}_{\mathbb{F}_p} [ u 1_\Omega ] = - a w m - 0 = - a w m.$$
   This completes the proof. $\blacksquare$

---

## 3. Multilinear AP Expansion and Completion Mean Positivity

Let $\Lambda_k(B)$ denote the normalized $k$-AP count with tent weight $F$:
$$\Lambda_k(B) = \mathbb{E}_{x, h} \left[ 1_{h \ne 0} F(x, h) \prod_{i=0}^{k-1} B(x + ih) \right].$$
Since $A$ contains no non-trivial $k$-APs, $\Lambda_k(B) = 0$.
Decomposing $B = a 1_\Omega + u$:
$$\prod_{i=0}^{k-1} B(x + ih) = \prod_{i=0}^{k-1} (a 1_\Omega(x + ih) + u(x + ih))$$
$$= a^k \prod_{i=0}^{k-1} 1_\Omega(x + ih) + a^{k-1} \sum_{j=0}^{k-1} u(x + jh) \prod_{i \ne j} 1_\Omega(x + ih) + \dots + \prod_{i=0}^{k-1} u(x + ih).$$

### Theorem 3 (Unconditional Mean Positivity for $k$-APs)
On any eligible host $\Omega$ with density $a \ge \epsilon / (2\log |\Omega|)$ and step cap $H \ge 1$:
$$m = \mathbb{E}_\Omega q \ge k a^{k-1} \mu (1 - o(1)) > 0, \tag{HC9}$$
where $\mu = \mathbb{E}_{x, h} [ 1_{h \ne 0} F(x, h) \prod_{i=0}^{k-1} 1_\Omega(x + ih) ] \ge (H/p)^{d + (k-2)s} > 0$.

### Proof
By definition of the completion channels:
$$m = \mathbb{E}_\Omega q = \sum_{j=0}^{k-1} \mathbb{E}_\Omega q_j = \frac{1}{|\Omega|} \sum_{v \in \Omega} \sum_{j=0}^{k-1} \mathbb{E}_h \left[ 1_{h \ne 0} F(v - jh, h) \prod_{i \ne j} B(v + (i - j)h) \right].$$
Making the substitution $x = v - jh$, the summation over $v \in \Omega$ becomes a sum over $x$:
$$m = \frac{p}{|\Omega|} \sum_{j=0}^{k-1} \mathbb{E}_{x, h} \left[ 1_{h \ne 0} F(x, h) 1_\Omega(x + jh) \prod_{i \ne j} B(x + ih) \right].$$
On an eligible host, replacing $B(x + ih)$ with its main term $a 1_\Omega(x + ih) + u(x + ih)$ and bounding the residual multilinear terms by the inductive host uniformity yields:
$$\mathbb{E}_{x, h} \left[ 1_{h \ne 0} F(x, h) \prod_{i=0}^{k-1} B(x + ih) \right] = 0$$
$$\implies \sum_{j=0}^{k-1} \mathbb{E}_{x, h} \left[ 1_{h \ne 0} F(x, h) 1_\Omega(x + jh) \prod_{i \ne j} B(x + ih) \right] \ge k a^{k-1} \frac{|\Omega|}{p} \mu (1 - o(1)).$$
Dividing by $w = |\Omega|/p$ gives $m \ge k a^{k-1} \mu (1 - o(1)) > 0$. $\blacksquare$

---

## 4. Degree $k-2$ Polynomial Chirp Tight Frame Reconstruction

To project the centered field $k = q - m$ onto structured arithmetic directions, we construct the degree $k-2$ polynomial chirp tight frame.

### Definition 4 (Polynomial Chirp Family)
For $k \ge 3$ and prime $p$, let $\mathcal{P}_{k-2} = \mathbb{F}_p^{k-2}$ denote the space of coefficient vectors:
$$\mathbf{c} = (c_{k-2}, c_{k-3}, \dots, c_1) \in \mathbb{F}_p^{k-2}.$$
The polynomial chirp associated with $\mathbf{c}$ is the character:
$$\psi_{\mathbf{c}}(x) = \exp\left( \frac{2\pi i}{p} P_{\mathbf{c}}(x) \right), \quad P_{\mathbf{c}}(x) = \sum_{l=1}^{k-2} c_l x^l.$$
The family $\mathcal{F}_{k-2} = \{ \psi_{\mathbf{c}} : \mathbf{c} \in \mathbb{F}_p^{k-2} \}$ has cardinality $|\mathcal{F}_{k-2}| = p^{k-2}$.

### Theorem 5 (Tight Frame Decomposition)
The family $\mathcal{F}_{k-2}$ satisfies the tight frame identity on $L^2(\mathbb{F}_p)$:
$$\frac{1}{p^{k-2}} \sum_{\mathbf{c} \in \mathbb{F}_p^{k-2}} \psi_{\mathbf{c}}(x) \psi_{\mathbf{c}}^*(y) = \delta_{x, y}. \tag{HC10}$$
Consequently, for any centered function $k \in L^2(\mathbb{F}_p)$:
$$k(x) = \frac{1}{p^{k-2}} \sum_{\mathbf{c} \in \mathbb{F}_p^{k-2}} Q_k(\mathbf{c}) \psi_{\mathbf{c}}^*(x), \quad Q_k(\mathbf{c}) = \langle k, \psi_{\mathbf{c}} \rangle = \mathbb{E}_x [ k(x) \psi_{\mathbf{c}}(x) ]. \tag{HC11}$$

### Proof
For any $x, y \in \mathbb{F}_p$:
$$\sum_{\mathbf{c} \in \mathbb{F}_p^{k-2}} \psi_{\mathbf{c}}(x) \psi_{\mathbf{c}}^*(y) = \sum_{c_1, \dots, c_{k-2} \in \mathbb{F}_p} e_p\left( \sum_{l=1}^{k-2} c_l (x^l - y^l) \right)$$
$$= \prod_{l=1}^{k-2} \left( \sum_{c_l \in \mathbb{F}_p} e_p(c_l (x^l - y^l)) \right) = \prod_{l=1}^{k-2} p \delta_{x^l, y^l} = p^{k-2} \delta_{x, y},$$
since over $\mathbb{F}_p$ with $p > k - 2$, $x = y$ is the unique common solution to $x^l = y^l$ for all $l \in \{1, \dots, k-2\}$.
Dividing by $p^{k-2}$ gives the canonical resolution of identity $\delta_{x, y}$. $\blacksquare$

---

## 5. Degree $k-2$ Phase Selection and Increments

Pairing the centered inner product identity (HC4) with the tight frame reconstruction (HC11):
$$- a w m = \langle u, k \rangle = \frac{1}{p^{k-2}} \sum_{\mathbf{c} \in \mathbb{F}_p^{k-2}} Q_k(\mathbf{c}) \langle u, \psi_{\mathbf{c}}^* \rangle.$$

Applying the same geometric phase alignment and Cauchy-Schwarz selection on dominant polynomial chirps as in Section 4 of [QUADRATIC_PROJECTION_SELECTION_20261021.md](QUADRATIC_PROJECTION_SELECTION_20261021.md):
$$\delta_k = \max_{\mathbf{c} \ne \mathbf{0}} |\mathbb{E}_\Omega u \psi_{\mathbf{c}}| \ge c_k a^{(k-1)/2} \log(1/a). \tag{HC12}$$

This demonstrates that:
- $k = 3$ (Roth): degree 1 chirps (linear) yield $\delta_3 \ge c_3 a \log(1/a)$.
- $k = 4$ (Erdős 142): degree 2 chirps (quadratic) yield $\delta_4 \ge c_4 a^{3/2} \log(1/a)$.
- $k = 5$: degree 3 chirps (cubic) yield $\delta_5 \ge c_5 a^2 \log(1/a)$.
- General $k$: degree $k-2$ polynomial chirps yield $\delta_k \ge c_k a^{(k-1)/2} \log(1/a)$.

---

## 6. Verification Roadmap

The companion verifier `verification/scripts/verify_higher_degree_polynomial_chirp_20261021.py` checks:
1. Pointwise hole support $B(v) q_j(v) \equiv 0$ for all $j \in \{0, \dots, k-1\}$ across $k = 3, 4, 5$.
2. Exact inner product identity $\langle u, q \rangle = - a m$.
3. Exact tight frame identity $\frac{1}{p^{k-2}} \sum_{\mathbf{c}} \psi_{\mathbf{c}}(x) \psi_{\mathbf{c}}^*(y) = \delta_{x, y}$ for $k = 3, 4, 5$.
4. Strict positivity of completion mean $m > 0$ on non-trivial $k$-AP-free sets.
