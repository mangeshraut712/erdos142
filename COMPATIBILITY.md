# Global regular-center compatibility and lane closure

Date: 2026-09-06. Offline continuation of `MIXED_INCREMENT.md`.
No internet. Completion-driven; both current increment lanes are closed
as architectures. The local target remains open.

STATUS: (D) NEW RIGOROUS PARTIAL THEOREM

The local target \(r_4(N)=o(N/\log N)\) is not proved or disproved.
Official Erdős #142 is not addressed.

## 1. Strongest new theorem

**Theorem A (first-moment compatibility). PROVED.**
The exact regular-center system \(r_d=\alpha\) for every \(d\neq 0\)
with \(q_d>0\) is compatible with every first-moment identity implied
by 4-AP-freeness. It produces \(\Lambda_3(B)=\alpha/p+\alpha Q_*\) and
\(M=M_{\mathrm{ctr}}\), and it does not contradict Booleanity at the
level of one-point or two-point counts.

**Theorem B (entropy non-obstruction). PROVED.**
Relative to independent Bernoulli(\(\alpha\)) endpoints, one regular-center
fiber has KL divergence \(\sim\alpha^2\). A naive sum over \(p\) fibers
is \(O(p\alpha^2)\). The Boolean entropy of a density-\(\alpha\) set is
\(\sim p\,\alpha\log(1/\alpha)\). For small \(\alpha\),
\(p\alpha^2=o\bigl(p\alpha\log(1/\alpha)\bigr)\). Local exclusions do
not overfill the entropy budget.

**Theorem C (low-\(\Sigma\) series). PROVED, checkpointed form made
terminal.**
On the hereditary window class, every low-\(\Sigma\) increment that
pays a factor \(3^{-d}\) contributes at most \(O(3^{-d})\) to
\(1/a\). The series \(\sum_d 3^{-d}\) converges, so the total
reciprocal-density gain is \(O(1)\). Starting at
\(a_0=\varepsilon/\log N\) one needs gain \(\Theta(\log N)\) in
\(1/a\). The present low-\(\Sigma\) conversion cannot close the local
target, even with infinitely many steps.

Together with `MIXED_INCREMENT.md` (negative mixed mass is not an
inverse theorem), both increment lanes of the current architecture are
closed.

## 2. Exact obstruction

After alternatives I–II, a 4-AP-free set may be pair-regular,
triple-regular, linearly uniform, and mean-fiber-regular. First moments
and entropy do not forbid that. The mixed form is then exactly the
deleted-joint baseline. The low-\(\Sigma\) alternative, if it occurs,
cannot accumulate enough density. What is missing is a **positive-density
structured increment** (quadratic or equivalent) with \(s+t<2\).

No disproof of the local target is obtained: Behrend-type sets have size
\(N\exp(-c\sqrt{\log N})=o(N/\log N)\) and do not violate the claimed
upper bound. A finite 4-AP-free set is not a disproof.

## 3. Failed approaches and counterexamples

| Approach | Verdict |
|---|---|
| Derive increment from \(M-M_{\mathrm{ctr}}\) | FALSE as an inverse. This equals \(-2\alpha Q_*\mathbb E_\mu(r_d-\alpha)\) and vanishes on the mean-regular center. |
| \(\mathbb E_\mu(r_d-\alpha)^2\ge c\alpha^C\) useful for iteration | Not proved. Falsified as a large-constant claim on small groups. |
| Entropy overflow from many fibers | FALSE at leading order (Theorem B). |
| Single-fiber or \(K\)-mode increment | Already FALSE / \(s=5\) (checkpoint). |
| Low-\(\Sigma\) with one new frequency per rank | Quantitatively closed (Theorem C). |
| Interval cubic conversion (28)–(29) | Survives only \(O(\log\log N)\) steps; needs \(\Theta(\log N)\). |

Finite witnesses, `python3 verify_compat.py`:

- \(\mathbb Z_7\), \(A=\{0,1,2,4\}\): \(r_d=1/2\) is **constant**. Variance
  of \(r\) is zero. Variance of \(r-\alpha\) is \((1/2-4/7)^2=1/196\).
  Negative \(M\) with no fiber above \(\alpha\).
- \(\mathbb Z_{11}\), \(A=\{0,1,2,4,7\}\): minimum variance among
  4-AP-free sets of size at least 3 in \(\mathbb Z_{11}\).
  \(\mathrm{Var}_\mu(r-\alpha)=\frac1{484}\),
  \(\mathrm{Var}/\alpha^2=\frac1{100}\).
- \(\mathbb Z_{13}\), \(A=\{0,1,3,9\}\): flat spectrum, \(r_d=0\),
  3-AP-free, \(M>0\). Outside Lane I.
- \(\mathbb Z_{101}\) regime set: mean \(r-\alpha=-848/19089<0\),
  \(\mathrm{Var}/\alpha^2\approx 0.161\). Not post-reduction alternative III.
- \(\mathbb Z_{11}\) wrap set \(\{6,8,9,10\}\): still forbids cyclic reuse.
- Affine-spread 3-AP-free family: \(r_d=0\), \(M>0\), outside Lane I.

## 4. Proofs

### Theorem A

Write \(q_d=\mathbb E B(x+d)B(x+2d)=\alpha^2+c_d\) and
\(t_d=\mathbb E B(x)B(x+d)B(x+2d)\). The regular-center system is
\(t_d=\alpha q_d\) for all \(d\neq 0\). Then
\(\sum_{d\neq 0}c_d=-b\) because \(\sum_d c_d=0\) and \(c_0=b\), so

\[
\Lambda_3(B)=\frac\alpha p+\alpha Q_*,\qquad
Q_*=\alpha^2-\alpha/p.
\]

The mixed identity
\(M=\alpha/p-2\alpha\Lambda_3(B)+\alpha^4\) then becomes exactly
\(M_{\mathrm{ctr}}\) from `MIXED_INCREMENT.md` (3). The same calculation
in a window gives \(\mathcal M=aw/p-a^4 C\) at \(\Phi=a^2 C\),
\(\Sigma=a^3 C\).

Let \(N(x)=\sum_d B(x+d)B(x+2d)\). Regular center forces
\(\sum_{x\in A}N(x)=p\alpha+p^2\alpha^3-p\alpha^2\), which is consistent
with \(\mathbb E f N=b\). No first-moment contradiction.

### Theorem B

The regular-center endpoint law is
\(P(1,1)=0\), \(P(1,0)=P(0,1)=\alpha\), \(P(0,0)=1-2\alpha\)
(requiring \(\alpha\le 1/2\)). Independent Bernoulli(\(\alpha\)) pairs
have masses \(\alpha^2\), \(\alpha(1-\alpha)\), \((1-\alpha)^2\). The KL
divergence expands as

\[
2\alpha\log\frac1{1-\alpha}+(1-2\alpha)\log\frac{1-2\alpha}{(1-\alpha)^2}
=\alpha^2+O(\alpha^3).
\]

Summing \(p\) fibers counts each Boolean coordinate in \(O(p)\) fibers.
Even without Shearer discounting, the total is \(O(p\alpha^2)\). Binary
entropy of \(B\) is \(p\,h(\alpha)\sim p\alpha\log(1/\alpha)\). The ratio
is \(O\bigl(\alpha/\log(1/\alpha)\bigr)\to 0\).

### Theorem C

From `RELATIVE_WINDOWS.md` (14) and the ledger after (31): a low-\(\Sigma\)
step at rank \(d\) satisfies
\(\Delta a\ge c a^2/(3^d\mathcal A(W))\) and, in the optimistic
mass-retaining model,
\(1/a_{d+1}=1/a_d-O(3^{-d})\). Therefore

\[
\frac1{a_0}-\frac1{a_\infty}\le O(1)\sum_{d\ge 0}3^{-d}=O(1).
\]

At \(a_0=\varepsilon/\log N\) one needs \(1/a\) to drop by
\(\Theta(\log N)\). The mechanism cannot do that.

The same boundary appears for a single global Roth step
\(\eta\asymp\alpha^2\) converted through a rank-one semicircle atom:
\(\Delta\alpha\asymp\alpha^2\), \(s=2\), \(t=0\), so \(s+t=2\), which is
not sufficient without an extra saving. Subsequent ranks make the gain
worse, not better.

## 5. Exponent ledger at \(\alpha=\varepsilon/\log N\)

| Route | \(s\) | \(t\) | total log-loss | Status |
|---|---|---|---|---|
| Regular-center mixed form | n/a | n/a | no \(\Delta a\) | closed |
| \(M-M_{\mathrm{ctr}}\) mean bias | n/a | n/a | may vanish | closed |
| Bounded \(K\)-mode | 5 | \(\ge 0\) | \((\log N)^{4}\) | fail Test C |
| One fiber \(S_d\) | \(0\) if \(r=1/2\) | illegal | n/a | fail Tests A,B |
| High linear / \(\Phi\)-cell | 1 | 0 | \(O(\log\log N)\) | works; not the remaining case |
| Low-\(\Sigma\), rank \(d\) | 2 | grows | \(\sum 3^{-d}=O(1)\) in \(1/a\) | closed |
| Interval cubic (28) | 2 | \(\sim 1\) | half \(\log N\) per step | closed |
| Quadratic atom, \(\mu\ge 1/8\), \(\Delta a\ge c a^{2-\delta}\) | \(2-\delta\) | 0 | \((\log N)^{1-\delta}\) | **not proved** |

## 6. One sharpest remaining lemma

After \(\Phi\)-stability and removal of every linear coefficient larger
than \(O(a^2)\), on a 4-AP-free set with \(p a^3\ge 2\), prove that
there exist a quadratic polynomial \(q\) on \(\mathbb Z_p\) and an
interval \(I\subset\mathbb R/\mathbb Z\) of length at least \(1/4\) such
that

\[
\Omega'=\{x: q(x)/p\in I\}
\quad\text{satisfies}\quad
|\Omega'|\ge p/8
\quad\text{and}\quad
\frac{|A\cap\Omega'|}{|\Omega'|}\ge a+c a^{2-\delta}
\]

for some fixed \(c>0\) and \(\delta>0\).

This is \(s=2-\delta\), \(t=0\), hence \(s+t<2\). The first-moment
regular-center model does not imply it, and it is not a uniform
actual-\(U^3\) inverse with exponent \(C<2\). It is a density-sensitive
quadratic increment on a **positive-density** atom.

If the lemma is true, the local target follows by the already-proved
transfer \([N]\to\mathbb Z_p\), the high-signal / \(\Phi\) reductions,
and \(O(a_0^{\delta-1})\) quadratic steps with total logarithmic loss
\(o(\log N)\). If it is false, the current density-increment architecture
does not prove the local target, and a genuinely different proof is
required.

Do not claim official Erdős #142 from this lemma even if proved.
