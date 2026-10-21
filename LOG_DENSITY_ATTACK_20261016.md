# Logarithmic-density attack: mixed windows and direct increments

16 October 2026. Offline. Principal status **D: NEW RIGOROUS PARTIAL THEOREM**.
The local target `r_4(N)=o(N/log N)` is **OPEN**. No literature novelty is
asserted. A sufficient hypothesis below is explicitly unproved.

## 1. What was audited and what changed

The 15 October checkpoint hashes matched before this cycle's edits. Its
independent verifier was copied to an isolated temporary directory and
rerun successfully: 21,465 checks, with exact and floating scopes separate.
Its single-quadratic-host theorem and sparse obstruction survive the
independent proof audit. The theorem's hypotheses, including its prime-size
condition, are necessary parts of the statement. The host density `w` is
not its phase interval density `beta`; the discrepancy is bounded by
`(2+log p)/sqrt(p)`. The diagonal contribution is `w/p`, and the critical
vertex must be treated separately in that proof. No historical output was
overwritten by the rerun.

The new theorem in `MIXED_QUADRATIC_TERMINAL_20261016.md` resolves a different
gap: the terminal count now applies to intersections of arbitrarily
dependent linear and quadratic intervals, including the intersections
produced by successive refinements. With `r` constraints and density `w`,

    r=o(sqrt(log p)), log(1/w)=o(sqrt(log p))
        imply density_A(Omega)<=3/4+o(1).                 (L1)

The finite error is (M1), and its sharper resonance-sensitive form uses
the explicit baseline `mu` in (M3). Nonnegative Fourier tent weights make
persistent resonances helpful and bound exceptional resonances in vertex
average by `1/p`. This avoids independent-coordinate assumptions entirely.
For one quadratic interval, the new sufficient small-host regime is
`p w^4 -> infinity`, stronger than the previous sufficient condition.

The other new result is a direct correlation-to-cell increment, proved
next. Together these give a complete *conditional* mixed-window iteration
with a smaller required correlation than the old energy scheme. Neither
result proves that the required correlation exists.

## 2. Direct quarter-cell extraction, including retained mass

Let Omega be any nonempty finite probability space with uniform measure,
B=1_A, `0<a=E_Omega B<1`, and `f=B-a`. Let `z:Omega->C` have modulus one.
Suppose

    delta=|E_Omega f conjugate(z)|>0.

Put `kappa=2 sqrt(2)/pi`. There is a partition of the unit circle into
four equal arcs, a cell C in its pullback, and numbers

    m=E_Omega[(B-a)1_C], mu_C=|C|/|Omega|,
    a'=|A cap C|/|C|, r_A=|A cap C|/|A|,

such that

    m >= kappa delta/8,
    a' >= a+kappa delta/8,
    r_A >= kappa delta/(8a).                            (L2)

Proof. For a uniformly rotated partition let `Q_theta(z)` be its unit
arc midpoint. Direct integration of the midpoint error, uniform on
`[-pi/4,pi/4]`, gives

    E_theta Q_theta(z)=kappa z.

Consequently some rotation has
`|E_Omega f conjugate(Q_theta)|>=kappa delta`. Its four real discrepancies
`m_j=E_Omega f1_(C_j)` sum to zero. The triangle inequality gives
`sum_j |m_j|>=kappa delta`, hence the sum of their positive parts is at
least `kappa delta/2`. At least one of four cells has
`m_j>=kappa delta/8`. It is nonempty and
`a'-a=m_j/mu_C>=m_j`, since `mu_C<=1`. Also
`r_A=(a mu_C+m_j)/a>=m_j/a`. These prove both conclusions on the SAME cell.
The claim requires no character orthogonality and no invertible Gram
matrix. Boundary conventions for arcs can be fixed arbitrarily: almost
every rotation avoids every point of the finite phase set. End of proof.

If `z(x)=e_p(P(x))` for a nonconstant polynomial of degree at most two,
this step adds one linear or quadratic interval constraint. Degree two
with zero leading coefficient is classified as linear. Constant terms
are absorbed into the arc position. Thus the class in (L1) is stable.

Important scope: here `f=B-a` is the relative residual of the TRIVIAL
factor on the current window. This is not an assertion about `B-g` for
an arbitrary existing factor. A new step uses the new relative mean.

## 3. An exact sufficient selection problem

Use natural logarithms, and put

    ell(a)=log(2/a), R(a)=log(log(e^2/a)), 0<a<=4/5.

For fixed epsilon>0, formulate the following statement, **DIRECT-Q**:
there exist `c_epsilon>0` and `p_epsilon` such that for every prime
`p>=p_epsilon`, every nonempty mixed interval window Omega with

    r<=sqrt(log p), |Omega|>=p exp(-sqrt(log p)),

and every cyclically 4-AP-free `A subset Omega` with

    epsilon/(2 log |Omega|) <= a <= 4/5,

there is a nonconstant degree-at-most-two polynomial P over F_p with

    |E_Omega (B-a)e_p(-P)|
          >= c_epsilon a^(3/2) ell(a) R(a).             (L3)

All constraints are recorded when counting r, including redundant ones.
One may restrict the quantifier to windows containing the initial
interval constraint `[N]` in an embedding with `3N<p<6N`; that weaker
version suffices. A still weaker sufficient version quantifies only over
reachable windows, provided reachability is specified without assuming
the conclusion. Neither version is proved here.

**DIRECT-L** is the corresponding statement with only linear constraints
and a nonconstant linear P. The proof below also works under DIRECT-L.
These are separate hypotheses; no implication from a theorem on linear
windows to one on mixed windows is assumed.

This is a precise alternative to the old factor-energy selection problem.
For reference, the old COLLECTIVE-WSELECT hypothesis of
`THREE_BRANCH_AMPLIFICATION_20261014.md`, Theorem 4, requires every
admissible intermediate factor below its variance stopping threshold to
have a packet with centered relative Gram energy at least

    c |Gamma| a^(5/2) R(a),

within `M=ceil[(zeta/(kappa^2 c))a^(-1/4)/ell(a)]` additional characters;
the stopping variance is `zeta a^(9/4)R(a)/ell(a)`. Packet existence is
still open. No full-group Parseval substitution for its relative Gram
matrix is made in the present argument.

## 4. Complete conditional ledger for DIRECT-Q or DIRECT-L

This section proves an implication, not the hypothesis (L3). Reduce
`c_epsilon` if necessary so that `C=kappa c_epsilon/8<=1/100`. Put

    eta(a)=C sqrt(a) ell(a) R(a).

Then `0<eta(a)<1/4` on `(0,4/5]`. For an explicit bound write
`z=ell(a)>0`; then `sqrt(a)=sqrt(2)e^(-z/2)` and
`R(a)=log(z+2-log 2)<=z+2`. The elementary maxima
`z^2 e^(-z/2)<=16/e^2` and `z e^(-z/2)<=2/e` give

    sqrt(a)ell(a)R(a) <= sqrt(2)(16/e^2+4/e)<6.

Thus C<=1/100 suffices. All constants in the ledger depend only on C.

By (L2), a successful step obeys

    a' >= a(1+eta(a)),  retained occupied mass >= eta(a).

For an initial density `t`, divide the density range into epochs
`[e_j,min(2e_j,4/5)]`, `e_j=2^j t`, until `e_j<4/5<=2e_j`.
Let `m_j=inf eta(a)` over that compact epoch, and set

    B_j=1+ceil(2 log(2)/m_j).

The number of steps beginning in epoch j is at most B_j. Before the last
one the density remains below twice the epoch start, while each step
multiplies it by at least `1+m_j`; use
`log(1+m_j)>=m_j/2`. Overshoots can only skip epochs.

Consequently these explicit finite sums bound the entire run:

    additional rank <= D(t):=sum_j B_j,
    log(|Omega_0|/|Omega_final|)
       <= S(t):=log(1/t)+sum_j B_j log(1/m_j).           (L4)

For the second inequality, if `mu_j=|Omega_(j+1)|/|Omega_j|` and
`r_j=|A_(j+1)|/|A_j|`, then

    mu_j=r_j a_j/a_(j+1),
    sum log(1/mu_j)=log(a_final/t)+sum log(1/r_j).

Thus (L4) counts actual retained occupied mass, not merely a density gain.
There is exactly one added phase per step; no hidden packet multiplicity.

For completeness, the orders of the finite sums are

    D(t)=O_C(t^(-1/2)/(ell(t)R(t))+ell(t)),
    S(t)=O_C(t^(-1/2)/R(t)+ell(t)^2).                   (L5)

Here is a proof of summation, rather than just an exponent comparison.
Throughout an epoch, `sqrt(a)>=sqrt(e_j)` and both decreasing logarithms
are at least their values at its upper endpoint. If `2e_j<=4/5`,
`ell(2e_j)>=ell(e_j)/2` and `R(2e_j)>=R(e_j)/2`. The latter follows from
`z-log 2>=sqrt(z)` for `z=log(e^2/e_j)>=log(e^2/(2/5))>2.9`.
For the last partial epoch, e_j>2/5 and its upper endpoint is 4/5.
Use `ell(4/5)>=ell(2/5)/2>=ell(e_j)/2` and
`R(4/5)>=R(2/5)/2>=R(e_j)/2` directly. Extending this epoch to 2e_j
and then applying the first logarithm inequality would not be justified.
Therefore

    m_j >= (C/4)sqrt(e_j)ell(e_j)R(e_j),
    B_j <= 2+8 log(2)/(C sqrt(e_j)ell(e_j)R(e_j)).

Also `log(1/m_j)<=log(4/C)+ell(e_j)/2`, since both logarithms in its
denominator exceed positive absolute constants; increasing the constant
to `log(8/C)+ell(e_j)/2` covers the last epoch. Split epochs at
`e_j=sqrt(t)`. For the earlier half, `ell(e_j)>=ell(t)/2` and
`R(e_j)>=R(t)/2` for all sufficiently small t, and the factors `2^(-j/2)`
sum to `1/(1-2^(-1/2))`. This gives the leading terms in (L5).
In the later half, `e_j^(-1/2)<=t^(-1/4)` and the logarithmic denominators
are bounded below by positive constants. There are at most
`1+log(1/t)/log 2` such epochs, giving `O_C(t^(-1/4)ell(t)^2)` for S and
`O_C(t^(-1/4)ell(t))` for D. These are absorbed in the respective leading
terms of (L5) as t tends to zero. The `2` terms contribute at most
`O_C(ell(t))` and `O_C(ell(t)^2)`. This proves (L5) with constants depending
only on C, uniformly in p and all window parameters. (L4) remains the
exact finite bound when asymptotic notation is unsuitable.

Now suppose, for fixed epsilon>0 and arbitrarily large N, that a
4-AP-free subset of [N] has density `t>=epsilon/log N`. Embed in a prime
`3N<p<6N`, with the initial linear interval constraint Omega_0=[N].
The elementary prime-interval proof in `NEW_RESULTS_20261002.md` suffices:
the binomial/primorial estimates give a prime between u and 2u for all
sufficiently large u, and use u=3N. Cyclic APs supported in [N] are
integer APs because their two second differences have magnitude <2N<p.

Starting from t, apply the direct selection hypothesis whenever a<=4/5.
At `t=epsilon/log N`, write `L=log N`. The bounds (L5) give

    D=O_epsilon,C(sqrt(L)/(log L loglog L)+log L),
    S=O_epsilon,C(sqrt(L)/loglog L+(log L)^2).           (L6)

Both are `o(sqrt(log p))`. The same bounds hold uniformly for larger t,
by the epoch estimates or by taking their supremum over t>=epsilon/log N.
Before any putative first failure of eligibility, its preceding ledger
therefore implies `r<=1+D<sqrt(log p)` and
`log(p/|Omega|)<=log 6+S<sqrt(log p)`. Moreover
`log |Omega|=log N-o(log N)`, so
`a>=epsilon/log N>=epsilon/(2 log |Omega|)` for large N. Thus no such
first failure is possible. The finite step bound forces a>4/5.

On this final mixed window, (L1) gives `a<=3/4+o(1)<4/5`, a contradiction.
This completes **DIRECT-Q => local target**, and likewise DIRECT-L.
For absolute clarity: DIRECT-Q and DIRECT-L remain OPEN.

### 4b. A further improvement using the actual mixed-window error

The separate conditions `r,S=o(sqrt(log p))` are sufficient, not necessary
for (M12). Retaining the actual product of rank and size loss gives a
stronger conditional architecture. This changes the admissible host
domain; it is not a stronger theorem on the old domain alone.

Put `L_p=log p` and `S_Omega=log(p/|Omega|)`. Define the explicit domain

    r[S_Omega+log(48r)+log L_p] <= L_p/100, r>=1.        (L10)

The **DIRECT-Q-P** hypothesis is (L3), on the domain (L10) instead of its
separate rank/size bounds, with correlation threshold replaced by

    delta(a)=c_epsilon a^(3/2) sqrt(ell(a)) R(a).        (L11)

Keep every other quantifier, the AP-free assumption, and the lower bound
`epsilon/(2 log |Omega|)<=a<=4/5`. This hypothesis is OPEN.

The direct atom lemma now has
`eta(a)=C sqrt(a ell(a))R(a)`, with C reduced if necessary as before.
The exact epoch formula (L4) applies without alteration. On each epoch,

    m_j >= (C/4)sqrt(e_j ell(e_j))R(e_j),
    log(1/m_j)<=log(8/C)+ell(e_j)/2.

Splitting the epoch sum at `e_j=sqrt(t)` as in the preceding proof gives

    D_P(t)=O_C(t^(-1/2)/(sqrt(ell(t))R(t))+ell(t)),
    S_P(t)=O_C(t^(-1/2)sqrt(ell(t))/R(t)+ell(t)^2).      (L12)

For the first half, use `ell(e_j)>=ell(t)/2`, `R(e_j)>=R(t)/2`,
and sum `2^(-j/2)`. For the size sum its summand is bounded by a constant
times `e_j^(-1/2)sqrt(ell(e_j))/R(e_j)` plus an additive logarithm.
Use also `ell(e_j)<=ell(t)`. For the second half the bounds
`O_C(t^(-1/4)ell(t)^2)` and `O_C(t^(-1/4)ell(t))` are absorbed in the
respective leading terms. Thus (L12) follows from a complete summation.

At `t=epsilon/log N`, writing `L=log N` and ignoring only constants
depending on epsilon and C, the leading terms are

    D_P ~ sqrt(L)/(sqrt(log L)loglog L),
    S_P ~ sqrt(L)sqrt(log L)/loglog L.

Here the symbol `~` in this display denotes scales of the upper bounds,
not an asymptotic equivalence or a lower bound. More precisely, including
the additive terms of (L12),

    D_P S_P = O_epsilon,C(L/(loglog L)^2)+o(L)=o(L),
    D_P log L=o(L),  S_P=o(L).                          (L13)

All cross products with the additive logarithms are o(L). At any alleged
first failure of (L10), the preceding ledger implies

    r[S_Omega+log(48r)+log L_p]=o(L_p)<L_p/100,

a contradiction. The relative-density lower bound remains eligible
because `log |Omega|=log N-o(log N)`. Thus the iteration reaches a>4/5.

For the terminal count choose `tau=1/log p` in (M12). On (L10),
`log(1/mu_0)<=2r[S_Omega+log(48r)+log L_p]<=L_p/50`.
Also `S_Omega<=L_p/100` and r<=L_p for large p. Hence the finite errors
are bounded by

    1/(8 log p)
      + (log p)(2+log p)/(2 p^(49/100))
      + (1/2)p^(-12/25) + (5/4)p^(-97/100),            (L14)

which tend to zero. The size requirement `tau wp>=48r` follows from
`wp>=p^(99/100)` for all sufficiently large p. This proves the terminal
contradiction and the complete implication

    DIRECT-Q-P => r_4(N)=o(N/log N).

There is a linear-only counterpart with the same proof. The selection
input is unproved. The new squared threshold is `a^3 ell(a)R(a)^2`,
leaving a gain `a^(-1)ell(a)R(a)^2` over squared signal `a^4`.
The larger allowable size loss is essential; transferring (L11) while
retaining the old size cutoff would be unjustified.

## 5. What quantitative gap has actually been reduced

The new required squared correlation is `a^3 ell(a)^2 R(a)^2`. On the
same linear/trivial-factor domain it is asymptotically smaller than
`a^(5/2)R(a)`, since their ratio is `sqrt(a)ell(a)^2R(a)->0`.
This comparison does not extend the domain of any old selection theorem.

Compared with a squared endpoint signal `a^4`, the remaining gain is

    a^(-1)ell(a)^2R(a)^2,

which at `a=epsilon/log N` is of order
`epsilon^(-1)log N (loglog N)^2(logloglog N)^2`.
The gain is still divergent; constant improvements do not close it.
Using the product-budget domain of section 4b improves this to
`epsilon^(-1)log N loglog N (logloglog N)^2`, still divergent.

A U^3 norm lower bound does not establish (L3). Even a hypothetical global
quadratic phase correlation of size only `a^(3/2)` would give, by this
particular extraction, `D=O(t^(-1/2))` and
`S=O(t^(-1/2)ell(t))`. These upper bounds do not satisfy (L1) or the
finite error requirements (M13); they do not prove that every possible
quadratic iteration fails. No global quadratic-phase inverse theorem
with a sufficient exponent has been derived in this cycle.

More generally one can use any lower bound delta(a) and the explicit
epoch sums (L4), replacing eta by `kappa delta(a)/(8a)`. If those sums
meet (M13), that is a sufficient replacement. There is no claim of an
absolutely weakest possible correlation threshold or optimal architecture.

## 6. Sparse obstruction: exactly where its proof applies

The Bernoulli argument in `RESIDUAL_FIELD_AUDIT_20261015.md`, (A6)-(A7),
extends from exponent 3/5 to every fixed `1/2<theta<2/3` with sampling
probability `t=p^(-theta)`. Here are its estimates with explicit powers.

With probability tending to one the actual sampled Boolean set has
`a in [t/2,2t]` and `rho<=6sqrt(t log p/p)`. The expected ordered
nonzero 4-AP count is at most `p^2 t^4=o(1)` because theta>1/2.
For the ordered nonzero 3-AP count Z,

    E Z=p(p-1)t^3,
    Var Z<=9p^3t^5+36p^2t^4+6p^2t^3.

Dividing by `(E Z)^2` tends to zero because theta<2/3; the controlling
terms have powers `p^(-1+theta), p^(-2+2theta), p^(-2+3theta)`.
Thus nonzero endpoint completions exist. Their nonnegative two-channel
sum q satisfies Bq=0, S=a E q>0, and `|qhat(xi)|<=E q=S/a`.
For every set of s nonzero frequencies,

    |sum conjugate(uhat) qhat|/S <= s rho/a.

If `s<=C a^(-1/4)/ell(a)`, this is
`O_C,theta(p^(-1/2+3theta/4)/sqrt(log p))=o(1)`.
This proves actual diffuse-completion examples throughout that sparse
band. It does not refute logarithmic-density selection. Endpoint cases
are not settled by these estimates.

At `t=epsilon/log p`, independent disjoint ordinary blocks of four
consecutive residues give

    Prob(Bernoulli set is AP-free)
      <=(1-t^4)^floor(p/4)
      <=exp(-floor(p/4)t^4) ->0.                         (L7)

Thus the unaltered independent sampling mechanism cannot supply the
desired target-density obstruction. This says nothing about all possible
correlated AP-free constructions. No target-regime counterexample was found.

## 7. A smaller direct arithmetic counting question

The new terminal weight also removes first-order window bias. With
`P=1_Omega`, `u=B-aP`, `T=E F product P`, expand exactly

    Lambda_F(B)=a^4 T+R_1^F+R_2^F+R_3^F+R_4^F.

Here `R_j^F` sums all j-residual terms and the averages are over F_p^2.
For `tau=a^2/log p` in (M12), the reachable rank/size regime and
`a>=epsilon/log p` imply `T=(1+o(1))w mu` and
`R_1^F=o(a^4 w mu)`, with an absolute bound in (M16).
Every nonzero progression term vanishes for AP-free B; the exact
zero-difference term is `aw/p`. Therefore

    R_2^F+R_3^F+R_4^F
       =aw/p-a^4T-R_1^F
       =-(1+o(1))a^4 w mu.                              (L8)

A genuinely sufficient missing arithmetic statement is: under failure
of (L3), for every such reachable host and actual Boolean AP-free set,

    R_2^F+R_3^F+R_4^F >= -(1/2)a^4 w mu.               (L9)

The diagonal is negligible here since `p a^3 mu->infinity`, which follows
from `mu>=exp(-o(log p))` and `a>=epsilon/log p`. Thus (L9), if proved,
would contradict (L8) and establish the selection step on reachable
hosts. It is OPEN. We have reduced the weighted question to residual
degrees 2--4; no assertion that their separate signs are favorable is made.
The measure and the test weight differ from the old unweighted signed
quartic problem, so no old bound is transferred without a new proof.
The same conclusion holds on the reachable product-budget hosts of
section 4b, under failure of (L11): (L13) gives
`r[S_Omega+log r+loglog p]=o(log p)` and `S_Omega=o(log p)`, so (M15)--(M16)
still give the required o(1) error with `tau=a^2/log p`. The extra
`r log(1/a)` is o(log p) by (L12). Thus the first residual remains
controlled in this larger domain along the proved conditional ledger.

### A tested sign shortcut fails for the actual arithmetic kernel

One tempting stronger assertion would make the weighted pair form
`sum_(i<j) E_(x,h) F(x,h)u(x+ih)u(x+jh)` nonnegative for every real
mean-zero u, on the grounds that the tent has nonnegative Fourier
coefficients. This assertion is FALSE even on the full group. It is not
enough to know that the original weight has a positive Fourier expansion:
the quadratic pullbacks in the pair kernel matter.

Take p=53, H=26, one quadratic q(x)=x^2, and
`F(x,h)=f(2xh)f(h^2)`. The following integer vector, indexed 0 through 52,
has mean zero:

    [0,8,3,-16,0,2,9,-3,-8,-2,0,9,-9,5,0,-15,16,6,0,-5,-6,-9,
     40,-8,-40,8,15,15,8,-40,-8,40,-9,-6,-5,0,6,16,-15,0,5,-9,
     9,0,-2,-8,-3,9,2,0,-16,3,8].

For u equal to this vector, exact integer summation of the arithmetic
kernel, divided by `p^2(H+1)^2`, gives

    sum_(i<j) E F u_i u_j = -8242732/2047761 < 0.

Equivalently the bounded weight `B=1/2+u/100` has mean 1/2 and
`R_2^F=-2060683/20477610000`. This is a counterexample to the generic
pair-PSD shortcut. B is NOT Boolean and is NOT AP-free; it does not
refute a sign assertion using those extra assumptions or (L9).
Finite searches of actual AP-free configurations found no negative
weighted R_2 example in the tested cases, which is not a positivity proof.

## 8. Scope of this result

The terminal mixed-host theorem, direct atom lemma, sparse-band extension,
and conditional iteration above have written proofs. The independent
verifier checks finite instances, including degenerate resonances and
zero differences, and does not certify asymptotic selection.

The next decisive task is (L11) on the product-budget mixed hosts, or the
explicitly weighted signed bound (L9) under its failure on reachable
hosts. The previous unresolved
stable-host terminal geometry has been replaced by a proved theorem.
The remaining correlation/counting inequality is still substantial.
