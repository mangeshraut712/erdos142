# Boolean AP-free sets with uniformly small chirps: the full alteration range

18 October 2026. Offline. **PROVED domain-separation partial theorem.**
The local target, DIRECT-Q-GAIN on its stated domain, and P12 remain OPEN.
This extends `BOOLEAN_ALTERATION_CHIRP_20261018.md` from
`2/5<theta<1/2` to `1/3<theta<1/2`. No claim of novelty outside this
repository is made. The construction is outside the logarithmic-density
and small-diagonal hypotheses of the target argument.

## 1. Statement and exact construction

Fix `1/3<theta<1/2`. For every sufficiently large prime p, there is an
actual Boolean set A in F_p containing no four-term progression with
nonzero difference, such that

    a=|A|/p=(1+o(1))p^(-theta),
    delta=max_(c,b)!=(0,0)|E_y(1_A(y)-a)e_p(-cy^2-by)|,
    delta/a^(3/2)
      =O_theta(p^(theta-1/2)sqrt(log p)
                  +p^(3theta/2-1)log p+p^(3theta/2-10))=o(1).   (TA1)

All averages are normalized by p. The constants and threshold may depend
on the fixed theta. This is not uniform as theta approaches 1/3 or 1/2.
Take independent Bernoulli(t) variables X_y with `t=p^(-theta)`, and let
R be their support. Define A(R) to consist of precisely those vertices
of R that belong to **no** nonzero-difference 4-AP contained in R.
Deleting every vertex of every such progression makes A(R) AP-free for
every realization. This rule commutes with translations of F_p.

The proof controls the final set directly, avoiding the entire deletion
mass as an error in each Fourier coefficient.

## 2. A good family with bounded local AP counts

For each v let H_v be the family of distinct three-element sets

    E minus {v}, where E is a distinct four-element cyclic 4-AP set
    containing v.

For p>3 all four progression vertices are distinct. Let

    D_v(R)=number of T in H_v with T subset R.                  (TA2)

This definition does not require v in R; in particular D_v is independent
of X_v. Any other vertex w belongs to at most 12 triples of H_v. Indeed,
place v and w in distinct slots i,j of an ordered 4-AP: the 12 choices
determine `h=(w-v)/(j-i)` and `x=v-ih`. Counting distinct sets only reduces
this upper bound. Also `|H_v|<=4(p-1)` by choosing the slot of v and h.

The intersection graph of H_v has degree at most `3(12-1)=33`, hence a
greedy coloring partitions it into at most 34 classes of disjoint triples.
In a fixed class the indicators `1_(T subset R)` are independent Bernoulli
variables of parameter t^3. Its size is at most p, and its mean at most
`pt^3`. For integer k, the elementary binomial union bound gives

    Prob(class count >=k)<=binom(n,k)t^(3k)
                            <=(ept^3/k)^k.                   (TA3)

If k>n the event is empty, so the same upper bound remains valid. Set

    eta=3theta-1, k=ceil(12/eta), K=34k,
    G={R: D_v(R)<K for every v}.

If D_v>=34k, at least one color class has count >=k. Thus, since
`eta k>=12` and k>=24,

    Prob(R not in G)<=34p(e/k)^k p^(-eta k)
                       <=34p^(-11)<=p^(-10) for p>=37.        (TA4)

The family G is nonempty: it contains the empty set.

## 3. Global Lipschitz control between good endpoints

For arbitrary R,R' in G put S=R symmetric-difference R'. Then

    |A(R) symmetric-difference A(R')| <= L |S|,
    L=1+3K.                                                   (TA5)

Proof: at most |S| changed vertices themselves can change membership in
A. Consider an unchanged vertex y whose membership in A changes. On the
side where y is removed from A, it lies in a 4-AP E contained in that
side's R. On the other side y is retained, so E cannot be contained in
that side's R. Hence E contains a changed vertex v that is present only
on the first side. Charge y to one such v and E. For each changed v,
only the endpoint containing v matters. That endpoint is good, and it
has fewer than K incident completed triples. Their union contains at most
3K possible unchanged vertices y. Summing proves (TA5).

This proves a bound between any two good endpoints; it does not assume
that a coordinate-by-coordinate path between them stays in G.
Consequently, for any real coefficients |z_y|<=1,

    f_z(R)=sum_y 1_(A(R))(y) z_y

is L-Lipschitz on G in Hamming distance.

## 4. Extension and Bernoulli martingale concentration

Extend f_z from G to the whole Boolean cube by

    ftilde_z(R)=clip_[-p,p] inf_(S in G){f_z(S)+L d(R,S)}.       (TA6)

The triangle inequality proves that the infimum is L-Lipschitz. On G,
its value equals f_z: the lower bound follows from (TA5), and choosing
S=R gives equality. Clipping preserves both this equality and the
Lipschitz constant. Since the true and extended functions lie in [-p,p],

    |E ftilde_z-E f_z|<=2p Prob(G complement)<=2p^(-9).         (TA7)

Here is a self-contained concentration bound for the extension. Reveal
the independent Bernoulli variables in any fixed order and take the
Doob martingale for ftilde_z. Conditional on the earlier coordinates,
let Delta_i be the difference of the expected final value with X_i=1
versus X_i=0. Coupling the remaining coordinates identically gives
`|Delta_i|<=L`. Its martingale difference is

    Y_i=(X_i-t)Delta_i,
    |Y_i|<=L, E[Y_i|past]=0,
    E[Y_i^2|past]=t(1-t)Delta_i^2<=tL^2.                       (TA8)

For any mean-zero conditional variable Y with |Y|<=L, expanding the
exponential and using `j!>=2*3^(j-2)` for j>=2 proves

    E[e^(lambda Y)|past]
      <=exp(lambda^2 E[Y^2|past]/(2(1-lambda L/3)))

for `0<lambda<3/L`. Iterating conditional expectations, the deterministic
variance bound `v=ptL^2` gives

    Prob(|ftilde_z-E ftilde_z|>=s)
      <=2exp(-s^2/[2(v+Ls/3)]).                              (TA9)

Use Markov's inequality with `lambda=s/(v+Ls/3)`; the case v=0 is
deterministic. In particular the choice

    s=L(2sqrt(pt x)+2x)

has `s^2>=2x(v+Ls/3)`, so its failure probability is at most `2e^-x`.
No independence between the martingale differences is asserted or needed.

## 5. All quadratic phases, actual centering, and density

Translation invariance of the deletion rule gives the same expectation
`bar a=E 1_A(v)` at every v. Independence of X_v and D_v gives

    bar a=t Prob(D_v=0),
    t(1-4pt^3)<=bar a<=t.                                    (TA10)

The lower bound is the union bound over at most 4(p-1) triples of
probability t^3. Since theta>1/3, `bar a/t->1`.

Apply (TA9) to real and imaginary parts of every phase
`chi_(c,b)(y)=e_p(-cy^2-by)`, including the constant phase, using the
extensions (TA6) separately for these real functions. Take `x=8log p`.
A union bound over 2p^2 functions has exceptional probability at most
`4p^2 e^-x=4p^-6`. Intersect with G. The resulting event has probability
at least `1-p^-10-4p^-6`, positive for p>=37. On this event the extensions
equal the true sums and (TA7), with the sum of real and imaginary error
bounds, yields simultaneously

    |sum_y(1_A(y)-bar a)chi_(c,b)(y)|<=B_p,
    B_p=4Lsqrt(pt x)+4Lx+4p^(-9).                            (TA11)

Here `E sum 1_A chi=bar a sum chi` exactly; no estimate for the mean of
a nonconstant quadratic phase is substituted. Taking the constant phase
shows `|a-bar a|<=B_p/p`. Since B_p/(pt)->0, (TA10) gives `a/t->1`.
Finally, centering by the **actual** density a gives

    |E(1_A-a)chi|<=B_p/p+|a-bar a||E chi|<=2B_p/p.            (TA12)

Dividing by a^(3/2) gives (TA1). The three powers are strictly negative
in the asserted range. All samples on this event are actual AP-free
Boolean sets; no pseudo-moment or signed-function surrogate is used.

## 6. Why this does not refute the open claim

The exact negation of DIRECT-Q-GAIN demands examples satisfying its
logarithmic density range. For every fixed epsilon>0, the sets here have

    a log p->0,
    a < epsilon/(2log|Omega|), with Omega=F_p, eventually.     (TA13)

Their rank-one full-linear-interval presentation eventually satisfies
the geometric product condition T5. For the original prescribed weight,

    tau=a^2/log p, H=floor(pa^2/(48log p)),
    F(x,h)=f(h), mu=(H+1)/p,
    H->infinity, mu~a^2/(48log p), T=mu.

Nevertheless the exact AP-free count is entirely its diagonal a/p and

    (a/p)/(a^4mu)~48log p/(pa^5)->infinity.                   (TA14)

Thus the diagonal is larger than the intended main scale, not negligible.
In fact this obstruction persists for every baseline `0<mu<=1`, since
`pa^3mu<=pa^3=(1+o(1))p^(1-3theta)->0`. Changing the tent cannot restore
diagonal negligibility for these examples.
Neither the P11 contradiction nor P12's original package applies. This
proves that Booleanity and AP exclusion alone cannot supply the requested
global quadratic correlation on an enlarged all-density domain. It
leaves the logarithmic-density structural problem open.

The Parseval lower bound in the elementary alteration note also shows
that a~p^-theta with theta>=1/2 cannot satisfy delta/a^(3/2)->0. The
present statement covers the full interval between that obstruction and
the vanishing mean incident-AP threshold theta>1/3. No conclusion at
theta=1/3 is asserted.

## 7. Verification and audit

`verify_boolean_typical_alteration_20261018.py` checks distinct arithmetic
hyperedges, the codegree/color bounds, the deletion rule and global
good-endpoint Lipschitz inequality on exhaustive finite cubes, and the
extension/martingale identities on small cubes. It also checks actual
modular AP-free altered sets and all quadratic phases numerically. Its
JSON separates exact checks from floating ones. These finite examples
are diagnostics, not evidence that the asymptotic target domain holds.
The saved run passed 525,186 checks and evaluated 707,238 chirp coefficients;
the largest FFT/direct-sum discrepancy was 2.09e-17. All six sampled
outputs were AP-free. Their prescribed H was zero, so none is an eligible
finite P12 test. The asymptotic conclusion does not come from their ratios.

Two independent mathematical audits checked the coloring, global endpoint
argument, extension, conditional variance, simultaneous concentration,
and actual centering. Computational checks support the proof; they do
not replace the asymptotic probability estimates above.
