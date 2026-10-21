# Quantitative solution ledger

2 October 2026. Offline. Principal status **(C) COMPLETE CONDITIONAL CLOSURE**;
the local target remains unproved. The only missing node in the completed
conditional chain is H in NEW_RESULTS_20261002.md section 1.

## 1. Budget before choosing an inverse theorem

Let t=ε/log N, ℓ=log(2/t), X=log N. Fix ε before taking N to infinity.
For a step with additive density gain at least Δ(a), added rank at most
R(a), and logarithmic domain loss at most L(a), dyadic density epochs give
the envelopes

    J ≲ 1+integral_t^(a*) 1/Δ(a) da,
    D ≲ d_0+sum_epochs [1+a/Δ(a)] sup_epoch R(a),
    S ≲ sum_epochs [1+a/Δ(a)] sup_epoch L(a).

For regular power/logarithmic functions these sums have the same dominant
orders as integrals of R/Δ and L/Δ. They are guaranteed upper envelopes;
failure of an envelope to be small does not prove a faster actual iteration
impossible. Claims of Θ require gains/costs bounded on both sides.

For persistent coordinate windows in one prime group, small size loss alone
is insufficient. The proved terminal estimate needs

    log(p-1)/D - S - log(2D) -> +infinity.                 (T)

A convenient sufficient condition is D[S+log(2D)+1]=o(log p). This also
preserves the old full cutoff. A domain class with a separately proved
rank-independent terminal criterion may have a different budget; none is
silently substituted here.

## 2. Mandatory weak gains and complexity tests

Assume for this table a usual geometric cost envelope
L(a)=O(R(a)+log(2/a)), and persistent added rank R. All exponents C,D,δ
are fixed and nonnegative, with δ>0 where stated. Set C'=max(C,1).

| Additive gain Δ | Added rank R | Steps J | Cumulative rank envelope | Cumulative log-loss envelope | Target test |
| --- | --- | --- | --- | --- | --- |
| ca² | log^C(2/a) | O(t^-1) | O(t^-1ℓ^C) | O(t^-1ℓ^C') | Does not guarantee S=o(X), or (T) |
| ca²/log^D(2/a) | log^C(2/a) | O(t^-1ℓ^D) | O(t^-1ℓ^(C+D)) | O(t^-1ℓ^(C'+D)) | Same failure, with additional logarithms |
| ca^(2+δ) | log^C(2/a) | O(t^(-1-δ)) | O(t^(-1-δ)ℓ^C) | O(t^(-1-δ)ℓ^C') | Envelope grows faster than X |
| ca² | a^-δ | O(t^-1) | O(t^(-1-δ)) | O(t^(-1-δ)) | Envelope grows faster than X |
| ca²/log^D(2/a) | a^-δ | O(t^-1ℓ^D) | O(t^(-1-δ)ℓ^D) | O(t^(-1-δ)ℓ^D) | No guaranteed closure |
| ca^(2+δ) | a^-θ, θ>=0 | O(t^(-1-δ)) | O(t^(-1-δ-θ)) | Same power, with possible log factor when θ=0 | No guaranteed closure |
| ca² | exp(Csqrt(log(2/a))) | O(t^-1) | t^-1 exp(Csqrt(ℓ)) times bounded factors | Same dominant order | At t=ε/X this is X^(1+o(1)), not o(X) |
| ca²/log^D(2/a) | exp(Csqrt(log(2/a))) | O(t^-1ℓ^D) | t^-1ℓ^D exp(Csqrt(ℓ)) | Same dominant order | No guaranteed closure |
| ca^(2+δ) | exp(Csqrt(log(2/a))) | O(t^(-1-δ)) | t^(-1-δ) exp(Csqrt(ℓ)) | Same dominant order | X^(1+δ+o(1)) |

These tests explain the distinction in the brief: exp(O(ℓ^C)) may describe
a harmless ONE-TIME complexity, while multiplying it by order 1/t steps
may destroy the required budget. In the exp(Csqrt(ℓ)) cases, each factor is
indeed X^o(1); the number of steps is still material.

For a gain ca^(2-σ), 0<σ<1, and R,L=exp(Csqrt(log(2/a))) times fixed
logarithms, the SIZE envelope is X^(1-σ+o(1))=o(X). For the present
persistent-window terminal bound, D and S have that same power, so the
sufficient PRODUCT test requires σ>1/2. Passing a size-only ledger must
not be reported as a complete quadratic localization theorem.

## 3. Constant-relative energy and the improved endpoint

For quarter-factor energy η(a)a², the proved atom lemma gives

    Δ(a)>=η(a)a/2,
    r_A>=η(a)a/(2·4^R(a)),
    log(n/n')=log(a'/a)-log r_A.

For fixed η>0, J=O(ℓ). The old worst-density bound J max R loses a
logarithm. The new density-sensitive sum with

    R(a)<=ceil(K/[sqrt(a)log(2/a)])

instead gives

    U=ΣR(a_j)=O(t^-1/2/ℓ+ℓ),
    D=O(t^-1/2/ℓ+ℓ),
    S=O(t^-1/2/ℓ+ℓ²),
    D(S+log(2D)+1)=O_ε(X/(log X)²+sqrt(X)(log X)^C)
                    =o(X)                               (fixed C).

The proof and explicit constants are in NEW_RESULTS sections 3-5. Any
fixed positive logarithmic saving log^-γ(2/a), γ>0, in the critical rank
a^-1/2 also passes after the same sharpened summation. We state just γ=1
in the single remaining hypothesis H.

For another useful parameterization, take energy η(a)≳a^β/log^D(2/a)
and added rank R(a)≲a^-δ/log^C(2/a), δ>0. Rank dominates the logarithmic
mass-retention terms. Dyadic sums give D,S=O(t^(-(β+δ))ℓ^(D-C)).
Hence β+δ<1/2 suffices for (T). At β+δ=1/2 a logarithmic saving C>D
also suffices. This endpoint statement refers to the recorded geometric
conversion, not a proof of the underlying energy theorem.

## 4. Quadratic inverse substitutions actually performed

The accepted ||f||U3>=ca^(3/2) gives no localization by itself.
If a hypothetical inverse theorem yielded correlation ρ>=c||f||U3^C
and localization loss a^-t, then the naive gain exponent would be
s=3C/2 and size loss envelope a_0^(-(s+t-1)). Even t=0 needs C<4/3
for the strict size test. PHASE2's actual-norm obstruction rules out the
overstrong C<2 formulation already; it does not rule out density-sensitive
inverse statements of a different form.

If the only guaranteed gain is ρ(a)=exp(-Ca^-k), k>0, the initial epoch
step bound involves exp(C_ε X^k) times powers of X. For every fixed k>0,
exp(C_ε X^k)/X grows faster than X. This GUARANTEE cannot close a ledger
with a positive constant per-step cost. It is not a lower bound on the
actual steps of an unknown improved inverse theorem.

No unproved known-style inverse theorem or unspecified constant was used
as an input to the completed conditional chain.

## 5. Ledger for the completed conditional chain

| Item | Explicit value or proved bound |
| --- | --- |
| Starting density | a_0>=t=ε/log N |
| Starting domain | Ω_0=[N] in a single prime 3N<p<6N; rank one |
| Structural signal | H alone: Var_Ω(E(B|F))>=ηa² |
| Density gain | a'>=a(1+η/2) |
| Per-step added rank | ceil(K/[sqrt(a)log(2/a)]) |
| Retained occupied fraction | >=ηa/(2·4^R) |
| Exact per-step size loss | log(a'/a)-log r_A |
| Step count | <=ceil(log(2/t)/log(1+η/2))+1 |
| Total rank | <=1+U_* from NEW_RESULTS (3.2) |
| Cumulative logarithmic size loss | <=S_* from NEW_RESULTS (4.3) |
| Restricted rank eligibility | D_*=o(sqrt(log p)) |
| Restricted size eligibility | log(p/n)<=log6+S_*=o(sqrt(log p)) |
| Lower density eligibility | a>=ε/(2log n) since log n>=log N/2 |
| Old full cutoff | log threshold=O(D_*+log D_*+ℓ)=o(log N) |
| Terminal density | >4/5 |
| Terminal contradiction | density<=3/4+9D_*exp(S_*-log(p-1)/D_*)<=4/5 eventually |
| Integer/cyclic transfer | two integer second differences bounded by 2(N-1)<p |
| Remaining unproved statement | H, and only H, in this conditional chain |

## 6. Failed route ledger

Fourier: cubic cancellation is bounded by 4abρ, but generic dissociation at
ρ of order a² allows O(a^-2log(1/a)) generators. No acceptable quartic
lower bound follows from this. Character selection produces U2 control
only; it does not supply the AP-free selection gain.

Quadratic: the new constant-fraction hole theorem excludes negligible
deletion of a pure quadratic interval host. Arbitrary localized quadratic
inverse/localization remains unproved.

Boolean: forced derivative angular mass is ~a⁴ at a=ε/log p, only an
order-a² fraction of total derivative energy, and the selected frequencies
depend on the difference. Coherent assembly remains unproved.

Incidence: higher traces and the global Schur PSD constraint were derived.
An unlabeled-spectrum-to-character implication is ruled out by relabeling;
the actual arithmetically labeled endpoint matrix is still essential.

Entropy: the global deficit is >=pa⁴/4, but no theorem locates it in the
admissible arithmetic factors. Overlapping star costs cannot be freely added.

Construction: full-product quadratic shells, ternary coding hosts and CRT
products of polylog-size seeds do not reach c/log p. No disproof was obtained.
