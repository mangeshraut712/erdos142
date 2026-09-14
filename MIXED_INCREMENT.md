# Mixed-form increment attempt

Date: 2026-09-06. Offline continuation from `RELATIVE_WINDOWS.md` and
`ASTRA_MIXED_LANE.md`. No internet.

STATUS: (C) NEW RIGOROUS PARTIAL THEOREM

The local target \(r_4(N)=o(N/\log N)\) is not proved. Official Erdős
#142 is not addressed.

## 1. Executive verdict

The Lane I hypothesis does not encode a marginal density increment.

After \(\Phi\) and \(\Sigma\) are regular, the signed bound
\(\mathcal M\le -c\,a^4 C\) is the value produced by the increment-free
fiber model \(r\equiv a\). The missing 4-AP joints supply the whole
budget. Bounded spectral extraction from the endpoint operator remains
quantitatively illegal for iteration (\(s=5\)). Single fibers with
\(r_d>a\) exist in some examples, but they are intersections of two
translates of \(A\), not hereditary windows.

User-reported result: the checkpoint already had (15) and no increment.
Locally verified result: `python3 verify_mixed.py` exits 0; captured in
`mixed_verification.json`. The local target remains OPEN.

## 2. Primary new idea

Separate the mixed form into a **joint** term and a **marginal** term.
4-AP-freeness forces the joint \(P(\text{both endpoints})=0\). That
alone, with regular one-sided rates \(r=a\), produces the entire
alternative-III budget and zero gain on every fiber. Any genuine
increment must come from an extra statement that \(r\) cannot stay at
\(a\) and that the excess is aligned with a hereditary window. The
signed hypothesis does not contain that extra statement.

## 3. Mixed-form lane

Work on \(\mathbb Z_p\), \(p>3\) prime, normalized averages
\(\mathbb E_x=p^{-1}\sum_x\). Let \(A\) be 4-AP-free for \(d\neq 0\),
\(\alpha=|A|/p\), \(B=1_A\), \(f=B-\alpha\). For \(d\neq 0\) set

\[
q_d=\mathbb E_x B(x+d)B(x+2d),\qquad
t_d=\mathbb E_x B(x)B(x+d)B(x+2d),\qquad
r_d=t_d/q_d
\]

when \(q_d>0\). AP-freeness forces the two endpoints to be exclusive, so
\(0\le r_d\le 1/2\). The checkpoint identity is

\[
\frac{m_d}{q_d}=\alpha^2-2\alpha r_d=-r_d^2+(r_d-\alpha)^2.\tag{1}
\]

Negativity of a single fiber is \(r_d>\alpha/2\), not \(r_d>\alpha\).
Summing with the diagonal \(m_0=\alpha(1-\alpha)^2\) gives

\[
M=\frac{\alpha(1-\alpha)^2}{p}+Q_*\bigl(\alpha^2-2\alpha\mathbb E_\mu r_d\bigr),
\qquad Q_*=\alpha^2-\alpha/p,\quad \mu(d)=q_d/(pQ_*).\tag{2}
\]

The relative window form is the same after replacing \(\alpha\) by \(a\)
and allowing unequal sides: \(\mathcal M/q=a^2-a(r_L+r_R)\). Negativity
is \(r_L+r_R>a\), not \(>2a\).

### Regular-center evaluation — PROVED

Assume \(q_d>0\) and \(r_d=\alpha\) for every \(d\neq 0\). Then
\(\mathbb E_\mu r_d=\alpha\) and (2) becomes

\[
M_{\mathrm{ctr}}
=\frac{\alpha(1-\alpha)^2}{p}-\alpha^4+\frac{\alpha^3}{p}.\tag{3}
\]

If \(p\alpha^3\ge 2\), then \(\alpha/p\le\alpha^4/2\), so

\[
M_{\mathrm{ctr}}
\le -\alpha^4+\frac{\alpha}{p}(1+\alpha^2)
\le -\alpha^4+\frac{\alpha^4}{2}(1+\alpha^2)
= -\alpha^4\Bigl(\tfrac12-\tfrac{\alpha^2}{2}\Bigr).
\]

For \(\alpha\le 1/\sqrt2\) this is \(\le -\alpha^4/4\). Relative windows
are identical: \(r_L=r_R=a\), \(\Phi=a^2 C\), \(\Sigma=a^3 C\) give

\[
\mathcal M=aw/p-2a(a^3 C)+a^2(a^2 C)=aw/p-a^4 C.
\]

The size cutoff \(n\ge 8\cdot 3^d a^{-3}\) of the checkpoint supplies
\(aw/p\le a^4 C/8\), hence \(\mathcal M\le -7a^4 C/8\), which is
stronger than alternative III,

\[
\mathcal M\le -\tfrac12 a^4 C.\tag{15}
\]

So (15) is the expected value of a 4-AP-free set whose pair and triple
counts are regular. It is not a leftover bias in the endpoint marginals.

### Identity-level non-implication — PROVED

The deduction

\[
\mathcal M\le -c\,a^4 C
\quad\Longrightarrow\quad
\max(r_L,r_R)>a
\text{ on a \(\mu\)-positive set of \(d\)}
\]

does not follow from (1), (2), and \(\Phi,\Sigma\)-regularity.

Proof. The regular-center model has \(r_L=r_R=a\) everywhere and still
satisfies (15) under the checkpoint size cutoff. On that model every
fiber has density exactly \(a\). The identities therefore do not force
a one-sided increment.

The weaker mean bound from \(M\le -c_0\alpha^4\),

\[
\mathbb E_\mu r_d\ge \frac{(1+c_0)\alpha+\zeta}{2},
\]

is compatible with \(r_d\le\alpha\) for all \(d\) as soon as \(c_0\le 1\).
Alternative III uses \(c_0\le 1/2\).

### Spectral extraction remains illegal — PROVED

The checkpoint already gives a bounded eigenmode of size
\(O(a^5 3^{-2d})\) from \(H=QKQ\). The proved Bohr-atom conversion then
yields \(\Delta a\ll a^5 3^{-2d}\). This is \(s=5\) at fixed rank, so
\(s+t\ge 5>2\). Rejected by the iteration budget. Polynomial quadratic
phases still have nonnegative Rayleigh quotient for \(K\); they cannot
be the negative modes.

### Single fibers are not hereditary windows — PROVED

\(S_d=\{x:B(x+d)B(x+2d)=1\}=(A-d)\cap(A-2d)\). A set of class (4) is
an intersection of narrow linear Bohr-coordinate intervals. These
coincide only if \(A\) itself is a union of such intervals. Restricting
to \(S_d\) leaves the hereditary class. The checkpoint already forbids
treating \(S_d\) as a new cyclic group (the \(\mathbb Z_{11}\) wrap).

## 4. Low-signal lane

Not opened. Lane I produced a precise obstruction rather than a stall
without information.

## 5. New lemmas

| Statement | Label |
|---|---|
| Regular-center evaluation (3) and \(\mathcal M\le -7a^4 C/8\) | PROVED |
| Identities do not imply a fiber increment | PROVED |
| Spectral extraction has \(s=5\) | PROVED (checkpoint + budget) |
| \(S_d\) is not a hereditary window | PROVED |
| Exact \(r\equiv a\) is realized by an infinite 4-AP-free family | OPEN |
| Local target \(r_4(N)=o(N/\log N)\) | OPEN |
| Official #142 | OPEN |

## 6. Complete proofs

The displayed identities (1)–(3) are algebraic rearrangements of the
checkpoint expansions `SIGNED_RESEARCH.md` (12)–(14) and
`RELATIVE_WINDOWS.md` (1), (15), (22). The cutoff comparison after (3)
uses only \(p\alpha^3\ge 2\) and \(\alpha\le 1/\sqrt2\). The relative
comparison uses only the already-proved bounds on \(\Phi\), \(\Sigma\),
and \(aw/p\). No inverse theorem is invoked.

Realizability of the exact center on an infinite family is not proved.
The non-implication is an identity-level statement and does not need a
construction: a claimed theorem that treats (15) as a sufficient
increment hypothesis is already false as a deduction.

## 7. Iteration ledger

Evaluated at \(a_0=\varepsilon/\log N\).

| Mechanism | \(\Delta a\) | scale/rank loss | \(s+t\) | Verdict |
|---|---|---|---|---|
| Regular center \(r\equiv a\) | \(0\) | none | n/a | no increment |
| Bounded \(K\)-mode + Bohr atom | \(\ll a^5 3^{-2d}\) | rank held or worse | \(\ge 5\) | fails Test C: total log-loss \(\asymp (\log N)^{4}\) |
| One fiber \(S_d\), even if \(r=1/2\) | \(\le 1/2-a\) | \(\log(1/q_d)\ge \log(3/(2a))\) | formally \(<2\) | illegal domain; fails Tests A,B |
| Same-rank \(\Phi\)-cell | already alternative I | cheap | n/a | excluded by Lane I |
| Rank \(+1\) linear | already alternative II | cheap | n/a | excluded by Lane I |

A simple power-law with \(s+t\ge 5\) gives accumulated logarithmic
loss \(a_0^{-(s+t-1)}\ge a_0^{-4}=(\log N)^4/\varepsilon^4\), which is
not \(o(\log N)\).

## 8. Adversarial tests

Test A, \(\mathbb Z_{11}\), \(A=\{6,8,9,10\}\). The set is 4-AP-free in
\(\mathbb Z_{11}\). Its integer-index pullback is not cyclically
4-AP-free in \(\mathbb Z_5\). \(M>0\) on this example, so it is not a
Lane I witness. It still kills any reuse of a non-window fiber as a new
ambient group.

Test B, affine-spread 3-AP-free family. Those sets have \(t_d=0\),
\(r_d=0\), and \(M=\alpha/p-2\alpha(\alpha/p)+\alpha^4>0\) for small
\(\alpha\). They lie outside Lane I. They continue to forbid
near-full-mass increments on long integer progressions. A fiber
restriction \(S_d\subset A-d\) is exactly this kind of non-arithmetic
localization and is rejected.

Test C, \(\alpha=\varepsilon/\log N\). The only legal increment extracted
from \(K\) fails the budget. The identity-level Lane I hypothesis
produces \(\Delta a=0\) in the regular center, so there is nothing to
iterate.

Small groups, exact, `verify_mixed.py`:

- \(\mathbb Z_7\), \(A=\{0,1,2,4\}\): 4-AP-free, \(r_d=1/2<\alpha=4/7\)
  for every \(d\), \(M/\alpha^4=-27/64<0\). Below cutoff
  \(p\alpha^3=64/49<2\). Witness that negative \(M\) need not raise any
  fiber above \(\alpha\).
- \(\mathbb Z_{101}\) regime set, 28 elements: 4-AP-free,
  \(p\alpha^3=21952/10201>2\), \(M/\alpha^4=-9055/21952<-1/4\). Weighted
  \(r=44/189<28/101=\alpha\). Thirty-six fibers have \(r>\alpha\), with
  \(\max r=2/5\) and \(\max q=13\). Those \(S_d\) have size at most 13
  and are not windows. The set also has a residue-class imbalance mod 5,
  so it is **not** claimed to be a post-reduction alternative-III
  witness. It is a diagnostic that incrementing fibers, when they exist,
  need not be iterable.

## 9. Full closure

Not obtained. No proof of \(r_4(N)=o(N/\log N)\) is claimed.

## 10. Consequence for Erdős #142

None. Even a proof of the local target would not give an asymptotic
formula for \(r_k(N)\). This run did not prove the local target.

## 11. Sharpest remaining sublemma

After alternatives I and II have been applied, so that

\[
|\Phi-a^2 C|\le a^2 C/16
\quad\text{and}\quad
\max_{\xi\neq 0}\lvert\mathbb E_\Omega(B-a)e_p(-\xi x)\rvert
<\frac{a^2}{16\cdot 3^d\mathcal A(W)},
\]

and \(\mathcal M\le -\tfrac12 a^4 C\), prove that the function
\(d\mapsto r_d-a\) cannot be identically non-positive on
\(\{q_d>0\}\), and that its positive part is arithmetically aligned
with a hereditary window \(\Omega'\) satisfying \(s+t<2\).

Equivalently: prove that a 4-AP-free set cannot be simultaneously
pair-regular, triple-regular, linearly uniform on the window, and
fiber-regular at \(r\equiv a\). That statement is a structure theorem,
not a rearrangement of (15).

## 12. Next research prompt

Continue offline from MIXED_INCREMENT.md. Accept that alternative III
is the regular-center value of a 4-AP-free set and does not itself
force a marginal increment. Do not extract increment from \(M\le -c a^4 C\)
alone, from a \(K\)-eigenmode, or from a single fiber \(S_d\). Prove or
refute the sublemma in §11: after I–II, \(r_d-a\) has a hereditary-window
alignment with \(s+t<2\). If you refute it, the remaining local-target
lane is only the low-\(\Sigma\) rank-controlled cubic increment. Test
against the \(\mathbb Z_{11}\) wrap, the affine-spread 3-AP-free family,
and \(\alpha=\varepsilon/\log N\). Do not claim official #142.
