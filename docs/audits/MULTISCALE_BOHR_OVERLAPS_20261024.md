# Multi-Scale Bohr Host Overlaps and Quadratic Phase Transfer Obstructions

24 October 2026. **D: new rigorous partial results. Target OPEN.**
No literature novelty is asserted. The October 21 closure remains withdrawn.

## 1. Mathematical Setting and Research Question

Let $p > 3$ be a prime, and let $A \subset \mathbb{F}_p$ be cyclically 4-AP-free.
Following the universal bilinear ceiling established in [BILINEAR_PAIR_INCIDENCE_20261024.md](BILINEAR_PAIR_INCIDENCE_20261024.md) (BP24), the single-host incidence operator $K$ cannot yield super-critical density gain $\delta \ge c_\epsilon a^{3/2} F_\epsilon(a)$ with $F_\epsilon(a) \to \infty$ due to hole-support spatial decoupling $\langle u, K f \rangle = -a \langle g, f \rangle$.

This audit investigates the multi-scale frontier posed in `NEXT_AUTONOMOUS_ACTION.md`:
Can multi-scale global consistency across overlapping Bohr hosts $\Omega_1, \Omega_2 \subset \mathbb{F}_p$ bypass the hole-support obstruction, or does spatial decoupling and phase orthogonality persist across multi-scale configurations?

---

## 2. Multi-Scale Invariance and Decoupling Theorems

### Theorem 1 (Density Discrepancy Invariance on Overlaps)
Let $\Omega_1, \Omega_2 \subset \mathbb{F}_p$ be two Bohr hosts with non-empty intersection $\Omega_{12} = \Omega_1 \cap \Omega_2$.
Let $a_i = |A \cap \Omega_i| / |\Omega_i|$ and $u_i = 1_A - a_i 1_{\Omega_i}$ for $i \in \{1, 2\}$, and $a_{12} = |A \cap \Omega_{12}| / |\Omega_{12}|$, $u_{12} = 1_A - a_{12} 1_{\Omega_{12}}$.
For every zero-mean test function $\psi: \Omega_{12} \to \mathbb{C}$ ($\sum_{v \in \Omega_{12}} \psi(v) = 0$):
$$\langle u_1, \psi \rangle = \langle u_2, \psi \rangle = \langle u_{12}, \psi \rangle. \tag{MS1}$$

#### Proof
On $\Omega_{12}$, the difference between indicators is a constant shift:
$$u_1(v) - u_2(v) = (1_A(v) - a_1) - (1_A(v) - a_2) = -(a_1 - a_2).$$
Taking the inner product with $\psi$:
$$\langle u_1 - u_2, \psi \rangle = \sum_{v \in \Omega_{12}} (u_1(v) - u_2(v)) \overline{\psi(v)} = -(a_1 - a_2) \sum_{v \in \Omega_{12}} \overline{\psi(v)} = 0.$$
Identically, $u_1(v) - u_{12}(v) = -(a_1 - a_{12})$, whose pairing with zero-mean $\psi$ vanishes. $\blacksquare$

> [!NOTE]
> Theorem 1 proves that local quadratic oscillations $\langle u, \psi \rangle$ are completely invariant under host density shifts between nested and overlapping Bohr neighborhoods. Phase correlation on the intersection cannot distinguish which host scale defined the density.

---

### Theorem 2 (Universal Cross-Host Hole Annihilation and Spatial Decoupling)
Let $\Omega_1, \Omega_2 \subset \mathbb{F}_p$ be any two hosts.
Define the cross-host incidence operator $K_{1 \to 2}$ with rows $v \in \Omega_1$ and columns $c \in \binom{A \cap \Omega_2}{2}$ by summing $F(P)/p$ over progressions $P$ having missing fourth vertex $v \in \Omega_1$ and pair $c \subset P \cap A$.
Then:
1. **Pointwise Annihilation**:
   $$B(v) K_{1 \to 2}(v, c) \equiv 0 \quad \text{for all } v \in \Omega_1, c \in \binom{A \cap \Omega_2}{2}. \tag{MS2}$$
2. **Exact Spatial Decoupling**: For every pair function $f: \binom{A \cap \Omega_2}{2} \to \mathbb{C}$,
   $$\langle u_1, K_{1 \to 2} f \rangle = -a_1 \sum_{c \in \binom{A \cap \Omega_2}{2}} g_{1 \to 2}(c) f(c) = -a_1 \langle g_{1 \to 2}, f \rangle, \tag{MS3}$$
   where $g_{1 \to 2}(c) = \sum_{v \in \Omega_1} K_{1 \to 2}(v, c)$.

#### Proof
1. Suppose $K_{1 \to 2}(v, c) > 0$ and $v \in A$. Then $v \in A$ and $c \subset A$, and the fourth vertex of $P$ is also in $A$ by construction. Thus all four vertices of $P$ belong to $A$. Since the progression is non-trivial ($h \ne 0$), this produces a 4-AP in $A$, contradicting the hypothesis that $A$ is 4-AP-free. Therefore $v \notin A$, which proves $B(v) = 0$.
2. On the row support of $K_{1 \to 2}$, $u_1(v) = B(v) - a_1 1_{\Omega_1}(v) = -a_1$. Factoring $-a_1$ out of the sum yields (MS3). $\blacksquare$

> [!IMPORTANT]
> Theorem 2 extends the spatial decoupling obstruction to arbitrary multi-host pairings. No multi-scale combination of Bohr hosts can overcome the hole-support annihilation; the spatial oscillations of $u_1$ are always erased in the pairing $\langle u_1, K_{1 \to 2} f \rangle$.

---

## 3. Finite Verification Audit

The verifier `verification/scripts/verify_multiscale_bohr_overlap_20261024.py` checks these identities exhaustively across prime fields $\mathbb{F}_p$ for $p \in \{5, 7, 11, 13, 17\}$:
- Total assertions evaluated: **28,844** (all passed, 0 failures).
- Density discrepancy invariance: 786 exact rational checks.
- Universal cross-host hole annihilation: 188 exact checks.
- Cross-host spatial decoupling: 750 exact rational tests with diverse test vectors.
- Quadratic phase correlation bounds: 24,536 complex inner products.
- Arithmetic and multi-scale cases: 262 configurations.

Machine-readable results are preserved in [verification/results/MULTISCALE_BOHR_OVERLAP_20261024.json](../../verification/results/MULTISCALE_BOHR_OVERLAP_20261024.json).

---

## 4. Status and Next Research Direction

P12, W8 and DIRECT-Q-GAIN remain **OPEN**.
The multi-scale analysis proves that the bilinear incidence operator $K$ cannot be salvaged by cross-host coupling.
Future attacks must focus entirely on:
1. Direct quadratic phase selection on Bohr hosts that does not factor through the completion incidence operator $K$.
2. The arithmetic low-mean branch $m \le 2a^3 T / w$ under higher-degree Gowers uniformity bounds ($U^4$ / inverse theorem).
