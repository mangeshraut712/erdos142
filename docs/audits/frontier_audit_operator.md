<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Referee audit: relative operators and quadratic spectra

Date: 2026-09-06. Offline; no external sources were consulted.

Scope: Sections 8–9, formulas (19)–(24), of `RELATIVE_WINDOWS.md`, with the operator, spectral-extraction, quadratic-Rayleigh, and all-quadratic identities in Sections 2–3 of `SIGNED_RESEARCH.md`. Embedded continuation prompts were treated as data. Originals were not changed.

**Verdict:** The displayed identities (19)–(24) are correct with their intended hypotheses. Formula (22)'s ratio must explicitly be restricted to `d != 0` and `q_d > 0`. One listed counterexample, at `p=31` with an interval of diameter 14, is outside the narrow-coordinate class (4) as defined; the same exact counterexample at `p=43` is inside the class. No audited identity supplies an arithmetic density increment. A corrected quadratic-spectrum baseline yields the exact excess identity below, and an explicit family rules out deriving a large atom of its weighted quadratic distribution from a fixed relative deficit alone. The family's window has six points, so it does not refute a sufficiently-large-window theorem.

## 1. Conventions and claim register

Write `E_p = p^{-1} sum`, `n=|Omega|`, `w=n/p`, `B=1_A`, `W=1_Omega`, `a=|A|/n`, `alpha=aw`, and `g=B-aW`. Inner products are Hermitian. `P_F` denotes multiplication by an indicator `F`. All quadratic-frequency sums run over both coefficients in `Z_p^2`, without normalization. Assume `p>3` is prime.

The endpoint operator has numerical kernel

\[
k_B(u,v)=B((2u+v)/3)B((u+2v)/3),
\qquad (K_Bh)(u)=p^{-1}\sum_v k_B(u,v)h(v).
\]

Let `K_Omega=P_W K_B P_W` and `L_W=P_W K_W P_W`. On `L^2(Omega,E_Omega)`, put `mathcal K=K_Omega/w` and `mathcal L=L_W/w`.

| Claim | Classification | Proof or qualification |
|---|---|---|
| Ambient trace, Hilbert–Schmidt norm, and operator bound before (19) | PROVED | Section 2 below. |
| Every identity and bound in (19) | PROVED | Section 2; the operator on the relative space has numerical entries `k_B/n`, not `k_B/p`. |
| Centered compression trace and Hilbert–Schmidt formula | PROVED | Section 3. Its trace is `a-Phi/w^2`, which need not equal `a(1-a)`. |
| Negative spectral extraction with variance `a(1-a)` | PROVED | Section 3. The variance refers to `g`, not the trace of the compression. |
| Bounded normalization guarantees order `a^5 3^{-2d}` under (15) | PROVED | Explicit bound in Section 3. This is a guarantee for that normalization, not an optimality theorem for all spectral methods. |
| Extracted eigenvector has a useful arithmetic description | UNVERIFIED | No such conclusion occurs in the proof. |
| Bernoulli operator baseline (20) | PROVED | Section 4. Sampling parameter `a` is fixed; realized sample density can differ. |
| Expected dependent quadratic form for `Z=K_Omega-E K_Omega` | PROVED | Section 4; the cubic diagonal moment supplies the stated nonzero expectation. |
| Both zero expectations in (21) | PROVED | Section 4; four distinct progression positions are used. |
| Reversal relation `t_L(d)=t_R(-d)` and failure of same-d marginal equality | PROVED | Section 5 and the displayed explicit fiber. “Only” means the same-d equality is unavailable, not that reversal is the only identity of any kind. |
| Endpoint probability table and first identity in (22) | PROVED | Section 5, assuming `A` is nontrivial-4-AP-free. |
| Ratio identity in (22), without any restriction on `d,q_d` | FALSE | At `d=0`, an extra `a w/q_0=1` remains; at `q_d=0` division is undefined. The preceding prose gives the intended correct restriction. |
| Ratio identity in (22) for nonzero `d` and positive `q_d` | PROVED | Section 5. |
| Negative fiber implies `r_L+r_R>a`, but need not imply `>2a` | PROVED | Section 5 gives a counterexample to the stronger inference. |
| All-quadratic identity (23) and its diagonal corrections | PROVED | General Hermitian identity (A) in Section 6. |
| Weighted local quadratic isometry (24) | PROVED | Section 6; valid also for complex `h` with zero sum on every label class. |
| (24) alone is an arithmetic inverse theorem | UNVERIFIED | An isometry preserves energy; no localization conclusion follows in the argument. Section 8 gives a precise no-go for one proposed concentration inference. |
| Full-quadratic second/fourth moments | PROVED | Section 7, for every nonzero complex `h`. |
| Stated collision and Renyi-2/Shannon entropy bounds | PROVED | Section 7. |
| Unqualified claim that entropy contains no information whatsoever | UNVERIFIED | The rigorous claim is that these entropies are always within `log 2` of the maximum. They can still differ between functions; no impossibility theorem for every entropy-based test is proved. |
| Localized quadratic-Rayleigh positivity | FALSE | Exact counterexample in Section 9. The source correctly labels the proposed shortcut false. |
| Generic negative spectrum survives every localization | FALSE | Exact positive semidefinite counterexample in Section 9. |
| Endpoint balancing allows weighted pair corrections to be dropped | FALSE | Exact counterexample in Section 9; it can be placed inside class (4) by using `p=43`. |
| These small examples disprove the target asymptotic or its large-window regime | FALSE | They establish only the stated algebraic obstructions. |
| A density-sensitive arithmetic extraction from the negative relative form | UNVERIFIED | Still the missing step after this audit. |

“PROVED” in this table rests on the following algebra, not on the existing finite-verification JSON.

## 2. Trace, Hilbert–Schmidt norm, and normalization

The matrix of `K_Omega` in the ambient orthonormal delta basis has entries `W(u)k_B(u,v)W(v)/p`. It is real symmetric and its diagonal is `B(u)/p`. Consequently

\[
\operatorname{tr}K_\Omega=|A|/p=aw.
\]

Because its kernel is zero or one,

\[
\|K_\Omega\|_{HS}^2
=p^{-2}\sum_{u,v}W(u)k_B(u,v)W(v)=\Phi.
\]

The change of variables `y=(2u+v)/3, z=(u+2v)/3` is a bijection, with inverse `u=2y-z, v=2z-y`. Removing the endpoint restrictions therefore gives `Phi <= alpha^2`. Every row sum of `K_Omega` is at most `|A|/p=alpha`: choosing the first middle point determines the other endpoint uniquely, and all nonzero entries require that middle point to lie in `A`. Symmetry and the Schur bound give `||K_Omega||op <= alpha`.

Dividing the operator by `w` makes its numerical entries `k_B/n` on `Omega`. Trace and operator norm scale by `w^{-1}`; squared Hilbert–Schmidt norm scales by `w^{-2}`. Hence

\[
\operatorname{tr}\mathcal K=a,\quad
\|\mathcal K\|_{HS}^2=\Phi/w^2\le a^2,\quad
\|\mathcal K\|_{op}\le a.
\]

For real `g` supported on `Omega`, changing endpoint coordinates also gives

\[
\langle g,\mathcal Kg\rangle_\Omega
=\langle g,K_\Omega g\rangle_p/w^2=\mathcal M/w^2.
\]

This proves (19). Nothing here requires AP-freeness.

## 3. Centered compression and spectral extraction

Work in the relative Hilbert space. Put `c=<1,mathcal K1>=Phi/w^2`, `rho=mathcal K1`, `Q=I-|1><1|`, and `H=Q mathcal K Q`. Writing the matrix of `mathcal K` in blocks for the constant vector and its orthogonal complement gives upper-left entry `c`, off-diagonal vector `rho-c`, and lower-right block `H`. Thus

\[
\operatorname{tr}H=a-c,
\quad
\|H\|_{HS}^2=c-c^2-2\|\rho-c\|_2^2
=c-2\|\rho\|_2^2+c^2.
\]

The relevant bounds are `||H||op <= a`, `||H||HS <= a`, and `0<=rho<=a`, with `E_Omega rho=c<=a^2`. In particular `||rho||_2<=a^{3/2}`. Since `g` has mean zero,

\[
\|g\|_{2,\Omega}^2=b_\Omega:=a(1-a),
\qquad \langle g,Hg\rangle_\Omega=-\gamma,
\quad \gamma=-\mathcal M/w^2>0.
\]

Take a real orthonormal eigenbasis of `H`. Negative eigenvalues above `-gamma/(2b_Omega)` contribute at most `gamma/2` to the magnitude of the negative form. On the remaining modes, Cauchy–Schwarz and `||H||HS<=a` imply

\[
\gamma/2\le a\left(\sum_{\lambda_j\le-\gamma/(2b_\Omega)}
|\langle g,\phi_j\rangle|^4\right)^{1/2}.
\]

Since the sum of squared overlaps is at most `b_Omega`, some mode satisfies

\[
\lambda_j\le-\gamma/(2b_\Omega),
\qquad |\langle g,\phi_j\rangle|\ge\gamma/(2a\sqrt{b_\Omega}).
\]

For such a mean-zero unit eigenvector,

\[
\lambda_j\phi_j=\mathcal K\phi_j-\langle\rho,\phi_j\rangle1.
\]

The rowwise Cauchy–Schwarz bound gives `|mathcal K phi_j|<=sqrt(a)`, and the other term is at most `a^{3/2}`. Dividing by the resulting sup norm yields a bounded test with correlation at least

\[
\frac{\gamma^2}{4a^{3/2}b_\Omega^{3/2}(1+a)}.
\]

Under (15) and `C>=w^2/3^d`, one has `gamma>=a^4/(2*3^d)`. The bound becomes

\[
\frac{a^5}{16\,3^{2d}(1-a)^{3/2}(1+a)}
\ge\frac{a^5}{32\,3^{2d}}.
\]

The unit eigenvectors are arbitrary functions on the window. This proves the stated scale but gives no arithmetic domain or bounded-complexity phase.

## 4. Bernoulli centering and dependence

In this section only, `a` is a fixed Bernoulli sampling parameter. It need not equal the realized sample density. At a diagonal entry, `E B(u)=aW(u)`. At a non-diagonal endpoint pair the two middle positions are distinct, so the expected product is `a^2` times its window indicator. Therefore

\[
\mathbb E K_\Omega=a^2L_W+a(1-a)P_W/p.
\]

For `Z=K_Omega-E K_Omega`, the diagonal entry is `(B(u)-aW(u))/p`. Its contribution to `E<g,Zg>_p` is

\[
p^{-1}\mathbb E_p\mathbb E[g(u)^3]
=a(1-a)(1-2a)w/p.
\]

Every non-diagonal entry corresponds to four distinct progression positions because `p>3`. The two endpoint factors have mean zero and are independent of the two middle variables, so the expected off-diagonal contribution vanishes. This proves the claim after (20).

The operator in (21),

\[
X:=K_\Omega-P_B/p-a^2(L_W-P_W/p),
\]

has identically zero diagonal and mean-zero off-diagonal entries. The same four-position independence proves both `E X=0` and `E<g,Xg>_p=0`. Neither assertion uses independence of `g` from `X`.

These facts do not authorize replacing the sampling parameter by the random empirical density inside the expectation. That would be a different statement.

## 5. Fibers and the diagonal

For `d!=0` and `q_d>0`, condition on

\[
W(x)B(x+d)B(x+2d)W(x+3d)=1.
\]

AP-freeness excludes endpoint pair `(1,1)`. Writing `r_L=t_L/q_d`, `r_R=t_R/q_d`, the probabilities of `(1,1),(1,0),(0,1),(0,0)` are respectively `0,r_L,r_R,1-r_L-r_R`. In particular the endpoint product has expectation zero, and expansion gives

\[
m_d/q_d=a^2-a(r_L+r_R).
\]

For every `d`, including zero, the correct identity is

\[
m_d=1_{d=0}aw-a(t_{L,d}+t_{R,d})+a^2q_d.
\]

At zero, `q_0=t_{L,0}=t_{R,0}=aw` and `m_0=aw(1-a)^2`; this explains why the ratio formula must not be used there. Reversal `x -> x+3d, d -> -d` exchanges the two marginals, proving `t_L(d)=t_R(-d)`.

For `p=19`, `Omega={0,...,4}`, `A={0,1,2}`, and `d=1`, the conditioning event consists only of `x=0`. Thus `(r_L,r_R)=(1,0)`, while `a=3/5`. Its mixed ratio is `9/25-3/5=-6/25`; the sum of marginals is `1<2a=6/5`. This proves that negativity does not supply the missing stronger threshold or same-d marginal equality.

## 6. General all-quadratic identity and weighted isometry

For complex `h`, real indicator `F`, and `Q_h(c,r)=E_p h(x)e_p(-cx^2-rx)`, define

\[
T_F(h)=\sum_{c,r}|Q_h(c,r)|^2|Q_F(3c,3r)|^2.
\]

The following identity is more general than (23):

\[
\boxed{T_F(h)=\|F\|_2^2\|h\|_2^2+
\langle h,K_Fh\rangle_p-p^{-1}\mathbb E_p F|h|^2.}\tag{A}
\]

Expanding the four factors and summing the two quadratic coefficients imposes

\[
x-x'+3(y-y')=0,\qquad
x^2-x'^2+3(y^2-y'^2)=0
\]

with coefficient `p^{-2}`. If `y=y'`, then `x=x'`, producing the first term in (A). Otherwise divide by `y-y'` in the field. The constraints give `x+x'=y+y'`, hence `x=2y'-y`, `x'=2y-y'`. These are exactly the non-diagonal endpoint terms. The kernel is real symmetric, so the conjugation convention gives its Hermitian Rayleigh form after exchanging the endpoints if needed. The omitted diagonal is `p^{-1} E_p F|h|^2`. This proves (A).

For `F=B` and `h=g`, use

\[
\|B\|_2^2=aw,\quad v:=\|g\|_2^2=aw(1-a),\quad
\mathbb E_p B g^2=aw(1-a)^2.
\]

Rearranging (A) gives exactly (23).

For `F=W` and `h` supported on `Omega`, (A) says

\[
T_W(h)=(w-1/p)\|h\|_2^2+\langle h,L_Wh\rangle_p.\tag{B}
\]

On the controlled windows of Section 4,

\[
\langle h,L_Wh\rangle_p
=p^{-2}\sum_\ell\left|\sum_{x\in\Omega_\ell}h(x)\right|^2.
\]

Thus zero sum on each label class gives (24), including for complex `h`. Global balancing alone does not remove the label term. In particular the actual `g=B-aW` need not lie in this subspace.

## 7. Full-quadratic entropy

Orthogonality in the linear coefficient gives

\[
\sum_{c,r}|Q_h(c,r)|^2=p\|h\|_2^2.
\]

For the fourth moment, the orthogonality constraints are equality of the sums and sums of squares of two pairs. In odd characteristic these determine the pair's product as well, hence its unordered elements. There are the two pair matchings; their intersection consists of all-equal quadruples and must be subtracted once. Therefore

\[
\sum_{c,r}|Q_h(c,r)|^4
=2\|h\|_2^4-p^{-1}\mathbb E_p|h|^4.
\]

For `nu(c,r)=|Q_h(c,r)|^2/(p||h||_2^2)`, this proves

\[
p^{-2}\le\sum\nu^2\le2p^{-2}.
\]

The lower bound follows either from Cauchy–Schwarz on `p^2` entries or from `E|h|^4<=p||h||_2^4`. Thus `2 log p-log 2<=H_2(nu)<=2 log p`. Jensen's inequality gives `H(nu)>=H_2(nu)`, and the uniform distribution maximizes Shannon entropy on `p^2` points, giving the stated Shannon bounds.

A pure quadratic phase has one coefficient of magnitude one, `p(p-1)` coefficients of magnitude `p^{-1/2}`, and `p-1` zero coefficients. Consequently

\[
H_2=2\log p-\log(2-1/p),\qquad
H=(2-1/p)\log p.
\]

For comparison, a function supported at one point gives the exactly uniform distribution on the full quadratic index set. These different examples verify the limitation's precise meaning: highly structured functions need not have a substantial full-frame entropy deficit. The proof does not establish that every possible statistic built from these entropies is entirely uninformative.

## 8. Bounded closing attempt: corrected excess, deficit mass, and no large-atom inference

### 8.1 The baseline that must be retained

Return to deterministic `A`, with `a` its actual relative density. The naive comparison `T_B(g)` versus `a^2 T_W(g)` omits a leading-order term. From (A)–(B),

\[
T_B(g)-a^2T_W(g)
=aw(1-a)\|g\|_2^2+\mathcal M-a^2\langle g,L_Wg\rangle_p
+p^{-1}(a^2\|g\|_2^2-\mathbb E_p Bg^2).
\]

Even with label balance, the leading term is `a^2w^2(1-a)^2`. A negative mixed form of order `-a^4w^2` does not force this difference negative at small `a`.

The correct nominal Bernoulli second-moment baseline at the actual parameter `a` is

\[
H(q)=a^2|Q_W(3q)|^2+a(1-a)w/p.
\]

The added constant is necessary: for a Bernoulli sample with fixed parameter `a`, it is exactly the diagonal variance in `E|Q_B(3q)|^2`.

For any `h` supported on `Omega`, with `a=|A|/n`, (A)–(B) prove the deterministic identity

\[
\boxed{\sum_q|Q_h(q)|^2\bigl(|Q_B(3q)|^2-H(q)\bigr)
=\langle h,Xh\rangle_p,}\tag{C}
\]

where `X=K_Omega-P_B/p-a^2(L_W-P_W/p)` is precisely the off-diagonal operator in (21). The cancellation uses `||B||_2^2=aw`. If the Bernoulli parameter is fixed while the realized density differs, an additional term `(alpha_realized-aw)||h||_2^2` occurs in (C). No dependent-random-variable expectation is being silently taken here.

For `h=g`, (C) becomes

\[
\boxed{\langle g,Xg\rangle_p
=\mathcal M-a^2\langle g,L_Wg\rangle_p
-\frac{aw(1-a)(1-a-a^2)}p.}\tag{D}
\]

On controlled windows, `L_W` is positive semidefinite. Thus, for `0<a<=(sqrt(5)-1)/2`, negative `M` forces a genuinely negative off-diagonal spectral excess. Formula (D), rather than a comparison against `a^2 T_W` alone, is the appropriate precise statement. For larger `a`, the diagonal term must be retained with its actual sign.

If `g` is zero-sum on every label class, define

\[
Z_g:=\sum_q|Q_g(q)|^2H(q)
=a(w-a/p)\|g\|_2^2>0,
\qquad
\nu_g(q)=|Q_g(q)|^2H(q)/Z_g.
\]

Let `Delta=-<g,Xg>_p>0` and `delta=Delta/Z_g`. Nonnegativity of `T_B(g)` gives `0<delta<=1`. With `R(q)=|Q_B(3q)|^2/H(q)>=0`, (C) states

\[
\mathbb E_{\nu_g}R=1-\delta.
\]

Consequently the deficit set

\[
E=\{q:R(q)\le1-\delta/2\}
\]

has `nu_g(E)>=delta/(2-delta)`: outside `E`, `R>=1-delta/2`, so `1-delta>= (1-nu_g(E))(1-delta/2)`. This is a proved weighted mass statement. It does not bound the number or arithmetic organization of indices in `E`, and the condition is smallness of the `B` coefficient relative to its baseline, not a large positive coefficient of `B`.

### 8.2 Exact no-go for deriving a large weighted quadratic atom

For every prime `p>15`, take

\[
\Omega=\{0,1,2,3,4,5\},\quad A=\{1,2,3\},\quad a=1/2.
\]

This is a rank-one window of class (4), and `A` is 4-AP-free because it has only three points. The mod-3 label classes are `{0,3}`, `{1,4}`, and `{2,5}`; `g` sums to zero on all three.

The endpoint kernel on `Omega` has diagonal ones at `1,2,3`, and exactly four non-diagonal ones: `(0,3),(3,0),(1,4),(4,1)`. Therefore

\[
\mathcal M=-1/(4p^2),\quad
\|g\|_2^2=3/(2p),\quad
Z_g=33/(8p^2),\quad
T_B(g)=7/(2p^2).
\]

Thus the relative baseline deficit is the fixed number `delta=5/33`, and the normalized mixed form is the fixed negative number `M/w^2=-1/144`.

Nevertheless `|Q_g(q)|<=3/p`, and

\[
H(q)\le\tfrac14(6/p)^2+\tfrac14(6/p^2)=21/(2p^2).
\]

It follows that

\[
\boxed{\max_q\nu_g(q)\le\frac{252}{11p^2}.}\tag{E}
\]

A fixed positive deficit can therefore coexist with a weighted distribution spread across the full `p^2` scale. In particular, no implication `delta>=delta_0 => max nu_g>=c(delta_0)>0` holds under these operator/frame hypotheses, even for label-balanced Boolean functions and AP-free sets in a controlled window. The same bound gives `H(nu_g)>=2 log p-log(252/11)`.

This is deliberately a bounded no-go. It does not refute a theorem assuming growing window size or the terminal cutoffs in Section 6; here `n=6`. It also does not refute a useful relative quadratic correlation, a union-of-frequencies representation, or an arithmetic localization with additional hypotheses. No such positive result was proved by this attempt.

## 9. Algebraic audit of the listed shortcut counterexamples

For `p=19`, `Omega={0,...,4}`, and `A={1,2,3}`, the endpoint kernel consists of diagonal ones at `1,2,3` and edges `0<->3`, `1<->4`. For `q(x)=3(x-1)(x-3)`, its values at `0,...,4` are `9,0,-3,0,9`. Hence

\[
\langle We_p(q),K_BWe_p(q)\rangle_p
=p^{-2}(3+4\cos(18\pi/19))
=p^{-2}(3-4\cos(\pi/19))<0.
\]

The same kernel gives `M=-12/(25p^2)`. This is an exact counterexample to transferring global quadratic-Rayleigh positivity through endpoint localization.

For `Omega={0,...,5}`, `A={0,3}`, and any prime `p>18`, distinct middle points `0,3` would have endpoints `-3,6`, outside `Omega`. The kernel is exactly `P_A/p`, so it and every orthogonal compression are positive semidefinite. This disproves universal local negative-spectrum claims.

For the weighted-pair example, put `Omega={0,...,14}`, `A={3,6,11}`, and `a=1/5`. It is valid both at the source's `p=31` and at `p=43`. The latter also meets the narrow-coordinate requirement `14<p/3`.

Every supported 4-term progression is an ordinary integer progression when `p>28`: each modular second difference has absolute value at most 28 and must therefore be zero as an integer. There are 75 ordered progressions including the diagonal. Counting those with `A` in position `i` gives `E_0=15`, `E_1=E_2=18`. To see the middle count, the allowed step counts at positions `3,6,11` are respectively `5,8,5`. The count with `A` at positions `(0,1)` is 4 (the three diagonals and `(3,6,9,12)`); with `A` at `(0,2)` it is 3 (only the diagonals). Thus the endpoint one-`g` term is `(15-a*75)/p^2=0`, while

\[
\Lambda(g,g,W,W)+\Lambda(g,W,g,W)
=p^{-2}[4+3-a(2\cdot15+18+18)+2a^2\cdot75]
=-1/(5p^2).
\]

This is a proof from explicit integer counts, not an inference from a numerical verifier.

## 10. Closing status

**Done:** audited (19)–(24), proved the normalization and dependence corrections, identified the necessary scope qualifications, and derived the exact corrected excess identity (C)–(D), its deficit-set consequence, and the no-large-atom counterexample (E).

**Skipped:** internet research, changes to original notes or verifiers, and claims of novelty or an asymptotic density improvement.

**Remaining:** turn signed overlap or a weighted deficit set into a positive density increment on a sufficiently large arithmetic domain, with rank, size, density, and iteration costs controlled. The audited identities and this bounded attempt do not supply that step. No proof or disproof of `r_4(N)=o(N/log N)` has been obtained.
