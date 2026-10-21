# Offline research continuation: critical-rank conditional closure

2 October 2026. Principal status: **(C) COMPLETE CONDITIONAL CLOSURE**.

The local target `r_4(N)=o(N/log N)` has NOT been proved or disproved.
The one structural hypothesis H below remains CONJECTURED. This document
proves, from elementary ingredients, that H alone implies the target.
The new quantitative point is the critical rank exponent 1/2 with a
logarithmic saving, and restricting H to the geometries actually reached.
Earlier notes required a strict exponent below 1/2 or used coarser sums.
No claim of literature novelty is made. No internet was used in this run.

Five required routes were attempted: Fourier counting/character selection;
quadratic localization; Boolean polynomial constraints; incidence/trace/
entropy constraints; and counterexample constructions. Their results and
failures are recorded below and in the three new ROUTE_*.md notes.

## 1. Definitions and the ONE unproved statement

All logarithms are natural. Let p>3 be prime. A narrow coordinate window is

    Ω = {x in Z_p : ξ_i x lies in I_i, 1<=i<=d},

where each ξ_i is nonzero, and I_i is a circular interval of residues with
a consecutive integer lift of diameter <p/3. Keep constraints separately,
including repeated characters if necessary. Rank means number of recorded
constraints, not linear independence. An initial constraint x in [N] is
retained in the eventual iteration. Write n=|Ω|, a=|A|/n. Expectations and
conditional variance on Ω use its uniform probability measure.

**H — reachable-regime critical-rank energy hypothesis (CONJECTURED).**
For every ε>0 there exist K>=1, 0<η<=1/4 and p_0, depending on ε but
independent of p,d,n,a,Ω,A, such that the following holds. Whenever

    p>=p_0,  1<=d<=floor(sqrt(log p)),
    n>=p exp(-sqrt(log p)),
    ε/(2 log n)<=a<=4/5,

and A⊂Ω has no nonzero-difference cyclic 4-AP, there is a refinement F
of Ω by at most

    s <= ceil(K/[sqrt(a) log(2/a)])                         (H1)

new nonzero characters, each partitioned into four equal rotated
half-open circular arcs, such that

    Var_Ω(E_Ω[1_A | F]) >= η a^2.                          (H2)

H is not a consequence established in this run. In particular a large U3
norm, signed negativity, the Boolean identities below, and the new entropy
bound have NOT been converted into H. A counterexample to H would not by
itself disprove the r4 target. H is one sufficient statement, not a claim
of an absolutely weakest theorem among all possible proof strategies.

The restriction d<=sqrt(log p), n>=p exp(-sqrt(log p)) deliberately avoids
demanding a theorem on all sparse, high-rank hereditary windows. The recent
symmetric window candidate has rank of order log p and tiny cyclic size;
it does not test these hypotheses. We do not accept its mixed-factor sketch
as a proved refutation of any statement.

## 2. Factor energy to an atom — PROVED elementary lemma

Let an indicator B on a finite probability space have mean a>0. Suppose
a partition has M nonempty atoms of masses μ_i and densities b_i, with

    sum_i μ_i(b_i-a)^2 >= η a^2.

Then some atom satisfies

    b_i >= a(1+η/2),
    μ_i b_i/a >= η a/(2M).                                (2.1)

Proof. Since sum μ_i b_i=a, the variance equals sum μ_i b_i(b_i-a).
Atoms with b_i-a<ηa/2 contribute at most ηa^2/2 in total; negative
contributions only lower that upper bound. Good atoms therefore contribute
at least ηa^2/2. On them b_i-a<=1, so their occupied mass sum μ_i b_i is
at least ηa^2/2. One of at most M atoms carries at least ηa^2/(2M).
Both assertions follow. No lower bound on the size of every cell is used.

For a factor with s quarter partitions, M<=4^s. Every nonempty atom is
another narrow window after retaining old constraints and adjoining the
new arcs: their integer diameters are below p/3. There is no modulus reset,
unproved smoothing, or additional radius loss hidden in this selection.

## 3. Sharper cumulative-rank summation — PROVED

Fix η,K from H and set q=1+η/2>1. For small t>0 write ℓ=log(2/t).
Consider ANY partial sequence of densities satisfying

    a_0>=t,  a_j<=4/5 before each step,  a_(j+1)>=q a_j.

There are at most

    J_* = ceil(ℓ/log q)+1                                 (3.1)

steps. At each step bound s_j by ceil(K/[sqrt(a_j)log(2/a_j)]).
Put c_*=log(5/2), and define the explicit envelope

    U_* = J_* + K/(1-q^(-1/2))
                   [2t^(-1/2)/ℓ + t^(-1/4)/c_*].          (3.2)

Then sum s_j<=U_*.

Proof. Split the actual monotone sequence at a_j=sqrt(t). In its first
part log(2/a_j)>=ℓ/2 and a_j>=t q^j, so the corresponding sum of
1/[sqrt(a_j)log(2/a_j)] is at most
2t^(-1/2)/[ℓ(1-q^(-1/2))]. After the first density above sqrt(t),
all denominators log(2/a_j)>=c_* and geometric growth bounds the rest
by t^(-1/4)/[c_*(1-q^(-1/2))]. Ceiling terms add at most J_*.
This does not assume that 1/[sqrt(a)log(2/a)] is globally decreasing;
it is not. Since t^(1/4)log(2/t)->0, the second term is asymptotically
smaller than the first. Thus

    U_* = O_{η,K}(t^(-1/2)/ℓ + ℓ).                        (3.3)

The same argument, replacing ℓ by ℓ^γ in the first part, allows any fixed
γ>0 in (H1). Only γ=1 is needed for the explicit hypothesis above.

## 4. Complete conditional iteration — PROVED implication of H

Fix ε>0. Assume an integer 4-AP-free A⊂[N] has density at least
t=ε/log N. Take N sufficiently large, and a prime 3N<p<6N, whose
elementary existence is proved in section 6. Embed [N] into Z_p. Its
rank-one constraint has diameter N-1<p/3. If four embedded points form
a cyclic 4-AP, their two integer second differences have absolute values
at most 2(N-1)<p. The congruences force both second differences to be
zero as integers. Nonzero cyclic difference gives a nonconstant integer
progression. The embedded A is therefore cyclic 4-AP-free.

At a step satisfying H, select the atom from (2.1). If r_j is its retained
fraction of A, then

    a_(j+1)>=q a_j,
    r_j>=η a_j/(2·4^(s_j)).                               (4.1)

Writing n_j=|Ω_j| gives the EXACT telescope

    log(n_0/n_j)=log(a_j/a_0)+sum_{i<j}log(1/r_i).          (4.2)

For every partial iteration, set

    D_* = 1+U_*,
    S_* = ℓ + J_*[log(2/η)+ℓ] + (log 4)U_*.              (4.3)

Since a_j>=t and a_j<=1, (4.1)-(4.2) imply

    d_j<=D_*,   log(N/n_j)<=S_*.

In particular, with X=log N,

    D_* = O_{ε,η,K}(sqrt(X)/log X + log X),
    S_* = O_{ε,η,K}(sqrt(X)/log X + (log X)^2),            (4.4)
    D_*,S_* = o(sqrt(log p)),
    D_*[S_*+log(2D_*)+1] = o(log N).                     (4.5)

For example the leading product is O_ε(X/(log X)^2); all cross terms
are sqrt(X) times fixed powers of log X, or fixed powers of log X.
Every one is o(X). Constants may be large; for each fixed ε they are
fixed before N tends to infinity.

**Eligibility without circularity.** Suppose a first step failed because
its window left H's range. The estimates above apply to the preceding
partial iteration. They give

    d_j <= D_* < sqrt(log p),
    log(p/n_j) <= log 6 + S_* < sqrt(log p),
    log n_j >= (1/2)log N,
    a_j >= ε/log N >= ε/(2log n_j)

for sufficiently large N. Thus no such first failure can occur before
a_j>4/5. The older cutoff also persists, if desired:

    log max(256d_j3^(d_j),8·3^(d_j)a_j^(-3))
           =O(D_*+log(2D_*)+ℓ)=o(log N),

while log n_j~log N. These statements hold uniformly for all partial
iterations, not just a hypothetical final one.

By (3.1), H and (2.1) consequently produce a terminal density a_J>4/5
in at most J_* steps. If the starting density already exceeds 4/5,
take J=0. Successors remain in the same prime group, are proper windows,
and are still cyclic 4-AP-free.

## 5. Terminal contradiction — PROVED from pigeonhole

For any nonempty proper narrow window Ω of rank d, put
R=floor((p-1)^(1/d)). Partition [0,1)^d into R^d boxes. The R^d+1
points ((uξ_i mod p)/p)_i, 0<=u<=R^d, contain two in one box. Their
index difference h satisfies 1<=h<p and each centered residue δ_i of
hξ_i has |δ_i|<=floor(p/R).

For one circular interval, translation by δ_i loses at most |δ_i|
residues. Invertibility of ξ_i and a union bound therefore give

    b=|Ω \ (Ω+h)| <= d floor(p/R).

Since h!=0 and p is prime, translation by h is one p-cycle. Proper Ω
consists of b nonempty runs along this cycle. Split each run into blocks
of four and a remainder of at most three points. Each full block is a
nonzero-difference 4-AP, and has at most three occupied A-points. Thus

    |A|/n <= 3/4 + 3b/(4n)
            <= 3/4 + 3d floor(p/R)/(4n).                 (5.1)

This treats diagonal progressions and wrap correctly: the full blocks
have nonzero difference h and four distinct points, and wrap is allowed
inside the one cyclic group. No integer reembedding occurs here.

Since floor z>=z/2 for z>=1,

    3d floor(p/R)/(4n)
       <= (3/2)d(p/n) exp[-log(p-1)/d]
       <= 9D_* exp[S_*-log(p-1)/D_*].                    (5.2)

By (4.5) this tends to zero. More explicitly, eventually
log(p-1)/D_*>S_*+log(180D_*), so the error is below 1/20.
Formula (5.1) then bounds the terminal density by 4/5, contradicting
a_J>4/5. H therefore implies that for each ε>0 and all sufficiently
large N, r_4(N)<εN/log N. This is the local target, conditionally on H.

## 6. Elementary comparable-prime existence — PROVED

Here is a self-contained asymptotic Bertrand argument, also present in
SIGNED_RESEARCH.md section 13. Write P(m)=product of primes <=m. Induction
gives P(m)<=4^m. For odd m=2k+1, primes in (k+1,2k+1] divide
binomial(2k+1,k). This binomial coefficient is at most 2^(2k), since the
two central coefficients are equal and their sum is part of 2^(2k+1).
Multiply by P(k+1)<=4^(k+1) to get P(2k+1)<=4^(2k+1).
For even m>2, m is composite and P(m)=P(m-1); the small bases are immediate.

If (u,2u) has no prime for an integer u>=2, then

    4^u/(2u+1) <= binomial(2u,u)
                 <= (2u)^sqrt(2u) · 4^(2u/3).            (6.1)

For the upper bound, each prime <=sqrt(2u) contributes a factorial
valuation power at most 2u: each summand in the valuation is 0 or 1.
There are at most sqrt(2u) such primes. Larger primes occur at most once;
those in (2u/3,u] have valuation zero. The remaining ones contribute at
most P(floor(2u/3)). The absence of primes in (u,2u), and composite 2u,
remove the final range. The lower bound is the maximal central binomial
coefficient exceeding the average of all 2u+1 coefficients.
Taking logarithms of (6.1) would force

    (u/3)log4 <= sqrt(2u)log(2u)+log(2u+1),

which fails for sufficiently large u. Apply this to u=3N. No prime
distribution theorem or online source is needed for the transfer.

## 7. Fourier structure-versus-counting attempt

For normalized Fourier transform Bhat(ξ)=E_x B(x)e_p(-ξx), expand all
four factors and average x,d. The frequency constraints are

    ξ_0+ξ_1+ξ_2+ξ_3=0,
    ξ_1+2ξ_2+3ξ_3=0.

Writing ξ_2=u, ξ_3=v gives ξ_0=u+2v, ξ_1=-2u-3v, hence

    Λ4(B)=sum_(u,v) Bhat(u+2v)Bhat(-2u-3v)Bhat(u)Bhat(v).

Put f=B-a, b=a(1-a), ρ=max_(ξ!=0)|fhat(ξ)|. Separating the four
one-zero-coordinate lines (which meet only at the origin) gives

    Λ4(B)=a^4+2a(T+S)+Q,
    T=sum_(t!=0) fhat(t)^2 fhat(-2t),
    S=sum_(t!=0) fhat(t)fhat(2t)fhat(-3t),
    Q=sum_(u,v) fhat(u+2v)fhat(-2u-3v)fhat(u)fhat(v).

Parseval and Cauchy-Schwarz give |T|,|S|<=bρ. Therefore a sufficient
COUNTING condition, proved directly, is

    ρ<=a^2/16 and Q>=-a^4/2  ==>  Λ4(B)>=a^4/4.          (7.1)

If pa^3>=8, (7.1) contradicts the AP-free diagonal Λ4(B)=a/p.
Equivalently every AP-free set in this regime has either

    ρ>a^2/16, or Q<=-5a^4/8.                              (7.2)

The first branch only supplies an endpoint Fourier signal of order a^2;
the second is a genuinely signed quartic cancellation. We did not prove
its exclusion from low factor energy. (7.2) is not a new inverse theorem.

**Large spectrum check.** If D is dissociated, subset sums are distinct,
so |D|<=log_2 p, not log_3 p. For a dissociated subset of
Spec_τ(f), a positive Riesz product and Jensen yield

    |D| <= 4(a/τ)^2 log(1/a).

Proof: choose phases with E_A cos>=τ/a, take
P=product_(ξ in D)(1+t cos), E P=1 by dissociation, and use
log(1+z)>=z-z^2 for |z|<=1/2. Then
log(1/a)>=|D|(tτ/a-t^2). Choose t=τ/(2a).
A maximal D spans the spectrum with coefficients {-1,0,1}.
At τ=a^2/16 this allows O(a^-2 log(1/a)) generators, too large for H.
Even hypothetical constant-relative increments at that rank give a
terminal rank/loss product of order a^-4 up to logarithms, far beyond
log N at the target scale. No improvement using AP exclusion was proved.

## 8. Iterative character selection attempt

In this subsection the ambient probability space is the full Z_p; the U2
conclusion is not asserted for a relative window without another argument.

For a current partition F, put g=E(B|F), u=B-g. Refinement by quarter
cells P_j has the exact orthogonal gain

    ΔE=sum_(V in F,j:μ(V∩P_j)>0)
                  |E u1_(V∩P_j)|^2/μ(V∩P_j).             (8.1)

The circle indicator I_θ(t)=1_[θ,θ+1/4)(t) has coefficients

    c_0=1/4,
    c_m=e(-mθ)[1-e(-m/4)]/(2π i m), m!=0.               (8.2)

Rotation integration and Parseval in θ retain the ±1 terms, giving a
rotation with |E u I_θ(ξx/p)|^2>=|uhat(ξ)|^2/π^2.
Grouping F-cells by this arc and using mean-zero u gives from (8.1)

    ΔE >= |E u I_θ|^2/[μ(I_θ)(1-μ(I_θ))]
        >= (4/π^2)|uhat(ξ)|^2.                           (8.3)

Finite grid endpoint changes occur at finitely many θ; they do not affect
the rotation integral. The derivation does not assume arc masses exactly
1/4. Conditional Booleanity is exactly

    u^2=(1-2g)u+g(1-g),   E(u^2|F)=g(1-g).

Thus small gains for all characters control U2, not the quartic count:
if every gain is <=δ, then max|uhat|<=πsqrt(δ)/2 and
||u||U2^4<=π^2δa/4. The AP-free implication supplying a large gain,
or coherence of many smaller gains at rank (H1), was not proved.
An energy upper bound or Fourier cutoff was never reversed.

## 9. New auxiliary results from the other routes

The following have symbolic proofs in the new notes. They are NOT proofs
of H and are not being inserted as conjectured edges into the target proof.

1. ROUTE_QUADRATIC_BOOLEAN_20261002.md: if B(x)=1_S(q(x)) is a genuine
   quadratic host, β=|S|/p, K_S=||1hat_S||_1 and
   Z_S=sum_t|1hat_S(t)|^2|1hat_S(3t)|^2, any AP-free A has host-hole
   density δ satisfying

       Z_S-K_S^4/sqrt(p)-5/p <=4δ[β^2+K_S^3/sqrt(p)].

   For an interval S with β~ε/log p, eventually δ>=β/(12π^4).
   The host cannot be repaired by negligible deletion. The proof uses
   vertexwise completion bounds, retaining the quadratic critical point
   and d=0. It does not supply an inverse theorem for arbitrary A.

2. The same note derives, for C_d=B(x)B(x+d), θ_d=E C_d and d!=0,

       sum_k |Chat_d(k)|^2 cos(4πkd/p)=0,
       sum_(cos<0)|Chat_d(k)|^2>=θ_d^2,
       sum_(cos<=-θ_d/2)|Chat_d(k)|^2>=θ_d^2/(2-θ_d).

   Averaged negative mass is at least (a^2-a/p)^2/(1-1/p).
   The unresolved step is coherently assembling d-dependent derivative
   frequencies into a localized quadratic or other reusable structure.

3. ROUTE_INCIDENCE_MOMENTS_20261002.md: exact third/fourth endpoint
   traces, the global residual Gram/Schur PSD inequality, and a rigorous
   obstruction to extracting character structure from unlabeled spectral
   summaries. Relabeling preserves all such summaries while allowing
   distinguished sets with uniformly tiny low-rank factor energy. The
   relabeled graph is generally not the arithmetic endpoint graph: this
   is not an arithmetic counterexample.

4. The same note proves for every law Q supported on AP-free subsets,
   relative to P_a=Bernoulli(a)^p,

       D(Q||P_a)>=-(p/4)log(1-a^4)>=pa^4/4.

   Uniform AP-edge overlap is accounted for by the entropy chain rule.
   At a=ε/log p the per-coordinate deficit is only of order log^-4 p;
   no arithmetic localization of that deficit was established.

5. ROUTE_CONSTRUCTIONS_20261002.md: for full-product Freiman-2
   embeddings of a union of k positive-definite quadratic shells,

       |A|/p <=2k exp[-min(log(p)/2,sqrt(2log(3/2)log(p)))].

   Polylogarithmically many such shells cannot reach c/log p. Ternary
   product embeddings and CRT products of polylog-size AP-free seeds
   also have rigorous sub-logarithmic density bounds. Embeddings defined
   only on selected shells and general random embeddings are not covered.

## 10. What has and has not been completed

PROVED: the entire implication H => r4(N)=o(N/log N), including retained
mass, critical rank summation, restricted eligibility, all cutoffs, terminal
contradiction, comparable-prime existence, and integer/cyclic transfer.
The dependency graph uses no other conjecture for this implication.

NOT PROVED: H, an alternative general density-sensitive inverse theorem,
a disproof of the target, or the official Erdős problem. H may be false.
The route experiments did not justify discarding the arithmetic labels,
turning derivative angular mass into original Fourier mass, or ignoring
the number of iterations of a weak increment.

The next focused attack is the exact restricted statement H: use the
labeled Boolean derivative/endpoint constraints to obtain constant-relative
energy at rank K/[sqrt(a)log(2/a)] only on its stated near-full-size,
sub-square-root-rank windows. This is a substantially more limited demand
than an assertion on every high-rank hereditary window, but still unproved.
