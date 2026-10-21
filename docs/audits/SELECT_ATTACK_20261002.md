# SELECT attack — 2 October 2026

**Principal result: (D) NEW RIGOROUS THEOREM.** Offline; no literature novelty claimed.
SELECT is neither proved nor refuted. The unconditional target
r4(N)=o(N/log N) remains unresolved. All prior work is preserved.

The principal new result is the exact-cardinality, degree-four moment
relaxation theorem in SELECT_CARDINALITY_RELAXATION_20261002.md. It includes
actual quartic AP equations, positive semidefiniteness for every quadratic
square, and exact cardinality through degree four. It nevertheless has
per-frequency expected Fourier squares far below SELECT at the target
density. This identifies a precise limitation of the specified dual route;
it is not an AP-free set, a probability law, or an impossibility theorem for
all degree-four proofs. The second new result settles full-group main-term
positivity, with a quantified relative-window substitute below.

## 1. Quantifiers and threshold audit

Retain the original H window class: p>3 prime, d<=sqrt(log p),
n=|Ω|>=p exp(-sqrt(log p)), and ε/(2log n)<=a<=4/5. Every intermediate
factor must stay within the original greedy budget. Set ell=log(2/a),
κ²=8/π², and

    M(a)=ceil[(ζ/(κ²c)) a^(-1/4)/ell].

At a refinement the proved relative arc conversion increases factor
energy by at least κ² times the squared residual coefficient. Thus SELECT's
gain c a^(5/2)ell reaches ζa^(9/4) within M refinements. The last refinement
can overshoot; no premise is needed after it. Empty cells and existing
factors are handled by the prior relative conversion theorem. κ² is a
proved universal constant; its optimality was not proved.

An absolute c,ζ would be sufficient. The existing conditional closure only
needs positive constants for each fixed ε, independent of p, Ω, A and the
intermediate factor. Constants deteriorating with ε do not obstruct that
little-o argument. We do not conflate these two quantifier strengths.

A STRICTLY WEAKER sufficient unproved statement keeps exactly M(a).
Let R(a)=log log(e²/a), so 0<R(a)<ell for 0<a<=4/5. Ask for

    Var_Ω(g)<ζa^(9/4) R(a)/ell
        => max_{ξ!=0}|E_Ω u e_p(-ξx)|²>=c a^(5/2)R(a),     (WSELECT)

only for factors with fewer than M added characters. Its lower stopping
energy and smaller requested coefficient make it weaker than SELECT.
Their common R factor cancels in the quotient, so the same ceiling M
suffices. This weakening is conditional, not a proved selection theorem.

Here is the complete asymptotic ledger using the already proved density
increment bookkeeping. The relative energy threshold is
η=ζ a^(1/4)R/ell; stages in a dyadic density epoch are O(η^-1).
Each costs O(M) rank and O(M+log(1/(ηa))) log-size. The non-ceiling main
cost per epoch is O(a^-1/2/R). Ceiling and logarithmic costs are bounded
by O(a^-1/4 ell²/R). Summing epochs down to density t yields

    D,S=O(t^-1/2/R(t)),

including those smaller costs. To justify slow variation, split at sqrt(t):
on [t,sqrt(t)], R(a)>=R(t)/2 for sufficiently small t, and geometric
sums of a^-1/2 are dominated by t^-1/2. Above sqrt(t), the bound
O(t^-1/4 log(1/t)^3) is negligible relative to t^-1/2/R(t).
At t=ε/log N, therefore

    D,S=O_ε(sqrt(log N)/log log log N)=o(sqrt(log N)),
    DS=o(log N),  D log D=o(log N).

Both original H geometry requirements and terminal packing survive.
There is no assertion of a weakest divergent saving. Nine scalar
trajectories were checked; the asymptotic argument is the proof of this
conditional ledger, rather than evidence that WSELECT holds.

With the original stopping energy, a gain a^(5/2)/ell^C instead yields
D,S=O(t^-1/2 ell^C); a gain a^(5/2+δ) yields
O(t^(-1/2-δ)). Neither ledger guarantees the required little-o losses.
A cloud collecting ζa^(9/4) in O(a^-γ) rank yields
O(t^(-γ-1/4)); γ<1/4 suffices, while γ=1/4 needs a divergent saving.
A direct factor increment has the same gain/energy quotient. The present
proof derives the logarithm from the rank/size budget; no spectral dyadic
identity producing that logarithm has been proved.

## 2. Full-group algebra: positivity is settled, cancellation is not

SELECT_ALGEBRA_20261002.md expands all sixteen AP terms with normalized
Fourier conventions, proves exact conditional Bernoulli moments, and
bounds each residual group. Write h=g-a, v=E h² and b=E u²=a(1-a)-v.
On Z_p, pairwise independence of progression coordinates gives

    |Λ4(g)-a^4|<=4a v^(3/2)+v².

In particular v<=ζa^(9/4), ζ<=1/4 gives Λ4(g)>=7a^4/16.
This is unconditional for every real g with mean a and that variance.
With residual groups R1,...,R4, the verified bounds are

    |R1|<=12aρv+4sqrt(b)v^(3/2),
    |R2|<=12aρsqrt(bv)+6bv,
    |R3|<=4aρb+4sqrt(v)b^(3/2),  |R4|<=b²,

where ρ=max nonzero |u-hat|. Inserting SELECT failure does not make these
o(a^4). Conditional identities u²=(1-2g)u+g(1-g) and the exact third/fourth
moments do not supply joint independence at distinct AP positions.

A precise remaining sufficient full-group inequality is

    R1+R2+R3+R4>=-3a^4/8                              (SIGNED)

under AP-freeness, low variance and failure of the coefficient threshold.
It would contradict Λ4(B)=a/p once pa³>16. SIGNED is unproved.
An absolute o(a^4) perturbation estimate from Booleanity, low variance and
small coefficients alone is false: the existing genuine quadratic Boolean
host meets those three conditions but has Λ4(B) of order a³. That host
contains APs and is not a refutation of SELECT.

## 3. Relative-window main term: exact marginal theorem

Let W=1_Ω, C=Λ4(W)>0, w=n/p, T=p²C, and let D_i(x) count differences whose
four AP coordinates lie in Ω, with coordinate i equal to x. Define

    r_i(x)=n D_i(x)/T, R_i=E_Ω r_i², K=w²/C.

Then E_Ω r_i=1 and 1<=R_i<=K: indeed D_i(x)<=n, hence r_i<=K.
For every 0<=g<=1 of relative mean a, v=E_Ω(g-a)², one has

    Λ4(Wg)>=a^4 C [1 - sqrt(v)/(2a)
                         Σ_i(sqrt(R_i)+sqrt(R_i-1))].    (RELMAIN)

Proof: writing h=g-a, truncate each g above at a. The elementary product
inequality gives product_j g(x+jd)>=a^4-a³Σ_i h_-(x+id).
The AP marginal average of h_- is E_Ω r_i h_-. Since E_Ωh=0,

    E_Ω r_i h_-=(E_Ω r_i|h|-E_Ω(r_i-1)h)/2
               <=sqrt(v)(sqrt(R_i)+sqrt(R_i-1))/2.

Sum the four slots to prove RELMAIN. In particular its relative error is
at most 4sqrt(Kv)/a. For H windows the prior counting lower bound gives
C>=w²/3^d, hence K<=3^d. At the SELECT energy scale, this crude guarantee
is useful when K a^(1/4) is small; the full H rank ceiling alone does not
ensure it. For example d log3<=(1/4-δ)log(1/a) gives an error
O(sqrt(ζ)a^(δ/2)). This is a sufficient regime, not a necessary restriction.

Chebyshev gives relative bad-cell mass <=v/(λ²a²). The probability a
uniform Ω-contained progression hits a bad cell is at most
Σ_i sqrt(R_i v)/(λa), not four times the uniform bad-cell mass.
This marginal correction prevents an invalid transfer of full-group
orthogonality to Ω. The direct inequality RELMAIN avoids an arbitrary
choice of λ; the usual bad-cell balancing chooses
λ of order (Kv/a²)^(1/4) when that quantity is small.

For a general window a sufficient signed residual bound would be
Σ_{I nonempty}Λ4(W times u on I, g elsewhere)>=-a^4 C/4,
together with Λ4(Wg)>=a^4 C/2 and Λ4(WB)=aw/p.
These would contradict AP-freeness when a^4 C/4>aw/p. Neither that signed
bound nor a uniform positive relative main term at the full H rank has
been proved. This specifies arithmetic cancellation and marginal geometry
separately rather than merely renaming SELECT.

## 4. Duality: actual quartic constraints and exact cardinality

The principal theorem is proved in SELECT_CARDINALITY_RELAXATION_20261002.md.
For arbitrary Ω of n>=200 points, 4<=k<=n-2, a=k/n, set B_n=800+16log n.
If (n-k)(n-k-1)>=B_n(k-2)(k-3), there is a degree-four Boolean moment
functional L with uniform fixed-k moments through degree three,
L(X_e)=0 for every AP four-set e, L(q²)>=0 for every quadratic q, and
L[(ΣX_i-k)X_T]=0 for |T|<=3. Its expected Fourier squares are

    L|E_Ω(X_i-a)e_p(-ξi)|²
        =a(1-a)/(n-1)(1-|E_Ωe_p(ξi)|²)<=a/(n-1).

At a~ε/log p and the H size floor this is o(a^(5/2)ell), while the PSD
condition holds. The proof uses independently chosen eight-vertex signed
trades, balanced at every triple, to kill each AP moment. A uniform pair
load controls the perturbation norm on the harmonic pair subspace.

This strengthens the simpler degree-two and unbalanced degree-four
certificates: cardinality is exact and true quartic AP moments vanish.
It still has negative non-AP fourth moments, does not establish a
representing law, and does not enforce all pointwise Fourier-cap
localizers. Max of expected squares is not expectation of a maximum.
Thus it diagnoses this explicitly specified relaxation only.

## 5. Other mandatory attacks and what they established

SELECT_DISCOVERY_20261002.md records 174,538 genuine AP-free set/factor
cases. The smallest recorded proper-window normalized ratio for ζ=1/8 is
about .047398. Finite minima neither prove a uniform asymptotic lower
bound nor refute one. The exact residual Parseval lower bound is only
p/[n(p-1)] times [a(1-a)-Var(g)]. First-moment LP and second-moment
certificates remain feasible; the quartic theorem above is stronger.

Summing over differences before selecting frequencies gives exactly
E_d|E_x u(x)u(x+d)|²=Σ|u-hat|^4<=ρ²b. At SELECT failure its bound is
O(a^(7/2)ell), larger than a^4. Higher difference moments give the
existing eight-factor/codegree expression, without a favorable sign.
The original shared spectrum, Boolean convolution identities and support
cocycle constrain genuine derivative graphs; the old abstract diffuse
graph is not reused as a counterexample after imposing these constraints.
No signed concentration estimate follows from the verified identities.

SELECT_DELETION_20261002.md proves an exact AP hitting certificate for
arbitrary hosts and a quadratic-bias-or-quarter-deletion alternative for
the genuine quadratic interval host. Deleting less than a quarter by a
fixed margin forces a quadratic Fourier bias of order its density.
That is a quadratic coefficient, not SELECT's linear coefficient.
Deletion of a quarter or more and conversion to a linear bias remain
unresolved. Existing thinning/product/block candidates supply no actual
sequence satisfying every SELECT hypothesis; no refutation is claimed.

## 6. Verification and status

Symbolic proofs accompany every theorem. Separate finite checks cover
7,465 balanced trades, 51,744 cardinality triple identities, eight PSD row
certificates, 400 harmonic quadratic forms, and nine slow-threshold
trajectories. Algebra checks cover 480 cases and all 7,680 expanded terms;
delete-host checks cover 36 hosts and 2,721 hole certificates. The relative
main-term checker tests actual progression marginals in proper windows.
All 11 scripts in the combined rerun passed; the record is
select_reverification_20261002.json. The relative-window checker passed
5,844 actual set/factor cases. An independent audit confirmed WSELECT
logical weakening, its unchanged ceiling, the slow-logarithm epoch sums,
and RELMAIN. The relative AP-free diagonal is exactly aw/p.

The proved new theorems improve the algebra and the diagnosis of dual
relaxations. They do not prove SELECT, WSELECT, SIGNED, or the local target.
No complete-proof draft is produced because its missing selection step
would be unsupported.
