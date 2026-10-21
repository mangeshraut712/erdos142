# Structural sampling: relative Gram conversion and exact frequency occupancy

2 October 2026. Offline. Existing source files preserved. This note addresses attacks III, VI, and the graph/concentration part of attacks I–II of the new structural brief. No unconditional r4 theorem and no research novelty are claimed.

Read: AGENTS.md, CURRENT_STATUS_20261002.md, NEW_RESULTS_20261002.md, SOLUTION_LEDGER.md, PROOF_DEPENDENCIES.md, ROUTE_QUADRATIC_BOOLEAN_20261002.md; the conditional atom and terminal arguments were independently checked in the preceding route. Their content is not treated as authority: the elementary identities used here are derived below.

## 1. Normalization and the target statistic

Let Ω be any finite nonempty subset of Z_p, with its uniform probability measure. For any current partition F0, put

    g=E_Ω(B|F0), u=B-g, E_Ω(u|F0)=0.

For characters e_i(x)=exp(2πi ξ_i x/p), define

    m_i=E_Ω e_i, z_i=e_i-m_i,
    c_i=E_Ω[u conjugate(e_i)],
    G_ij=E_Ω[conjugate(z_i) z_j].

G is a Hermitian PSD Gram matrix. The original relative Fourier correlations are c_i, not full-group coefficients of B. In particular full-group orthogonality does NOT hold on Ω.

The exact refinement gain for quarter cells P_j is

    ΔE = sum_{V in F0, j: |V∩P_j|>0}
             |E_Ω u 1_(V∩P_j)|² / μ_Ω(V∩P_j).           (1)

It follows from orthogonal projection and E(u|F0)=0. Zero-mass cells are omitted; no division by zero occurs.

## 2. Relative quarter conversion with a stronger constant

For θ uniform on [0,1), divide the circle into arcs
[θ+j/4, θ+(j+1)/4), j=0,...,3. On arc j define the unit-modulus midpoint quantization

    Q_θ(t)=exp(2πi[θ+(j+1/2)/4]).

For fixed t, its error phase is uniform on [-π/4,π/4]. Therefore

    E_θ Q_θ(t)=κ exp(2πit), κ=2sqrt(2)/π, κ²=8/π².        (2)

The character ξ composed with Q is measurable on its quarter partition. For any θ, since E u=0,

    |E_Ω u conjugate(Q_θ(ξx/p))|²
       <= ΔE_θ · Var_Ω(Q_θ(ξx/p)) <= ΔE_θ.               (3)

Here ΔE_θ is the gain from F0 to its refinement by that quarter partition: its conditional projection contains Q, and Cauchy–Schwarz applies. Equations (2), Jensen, and (3) imply

    E_θ ΔE_θ >= κ² |c_ξ|²,
    max_θ ΔE_θ >= (8/π²)|c_ξ|².                         (4)

This holds on every Ω and every existing F0, with no equidistribution or boundary approximation. Thus the relative conversion loses NO additional density power. It is stronger than the earlier full-group constant 4/π² obtained from one arc indicator. The rotations where a residue hits a boundary are finitely many and measure zero, so the half-open convention does not change the integral.

No optimality is claimed for real residuals. A universal constant larger than 1 is impossible for arbitrary Ω: take Ω={0,(p-1)/2} and u=±1 on its two points. The coefficient at ξ=1 tends in magnitude to 1, whereas every refinement gain is at most ||u||²=1. The guaranteed constant 8/π² is below that obstruction. The example does not meet the large-window structural hypotheses and is used only to test universal conversion.

## 3. Many weak coefficients: regularized relative Gram theorem

Let Γ consist of s DISTINCT nonzero characters. Let

    M=κ²G+(1-κ²)I_s.

Since 0<κ²<1, M is positive definite even if G is singular.

**Theorem.** Some simultaneous choice of rotations of these s quarter partitions satisfies

    ΔE >= κ² c* M^-1 c.                                 (5)

Consequently

    ΔE >= κ² sum_i |c_i|² /
                   [κ² λ_max(G)+1-κ²].                 (6)

Proof. Choose all rotations independently. Write q_i=Q_(θ_i)(ξ_i x/p), and for any vector v define h=sum_i v_i(q_i-E_Ωq_i). Since h is measurable in the refined factor,

    |<u,h>|² <= ΔE ||h||².

Independent averaging and (2) imply

    E_θ |<u,h>|² >= κ² |v*c|².                          (7)

For i!=j the expected centered cross-covariance of q_i,q_j is exactly κ²G_ij. For a diagonal term, |q_i|=1 and Jensen gives

    E_θ Var_Ω(q_i)
      =1-E_θ|E_Ωq_i|² <=1-κ²|m_i|²
      =κ² G_ii+(1-κ²).

Thus

    E_θ||h||² <= v*Mv.                                  (8)

If every refinement had gain smaller than κ²|v*c|²/(v*Mv), averaging the projection inequality would contradict (7)-(8). Hence some refinement attains at least this ratio. Optimize over v using v=M^-1c, or use the trivial case c=0. This proves (5). The largest-eigenvalue bound proves (6).

On the full group, distinct nonzero characters are orthonormal and G=I. Therefore

    ΔE >= (8/π²) sum_{ξ in Γ}|uhat(ξ)|².                 (9)

On Ω, Gershgorin gives the useful explicit sufficient bound

    λ_max(G) <=1+(s-1)ρ

if |G_ij|<=ρ for distinct ξ_i,ξ_j. The correct relative entries are

    G_ij=E_Ω e_(ξ_j-ξ_i)
            -conjugate(E_Ω e_ξ_i) E_Ω e_ξ_j.             (10)

Neither the window-size lower bound nor its rank bound automatically makes ρ small for all character choices. Nearby frequencies on an interval can be strongly correlated. The regularized formulation (5) remains valid regardless.

**Dimension versus count.** This theorem uses s actual quarter partitions. If Γ lies in an additive span of dimension s but has many elements, e_ξ need not be measurable in the quarter partition of the generators: multiplying/coordinating phases requires finer resolution. No such automatic compression is used here.

## 4. Exact random-sampling moments

Let q_ξ be ANY probability distribution on a finite frequency set. Sample s frequencies independently with replacement and retain the distinct sampled set Γ_s. For nonnegative weights z_ξ put

    T_s=sum_{ξ in Γ_s}z_ξ, P_ξ=1-(1-q_ξ)^s.

Then EXACTLY

    E T_s=sum_ξ z_ξ P_ξ,                                (11)
    Cov(1_{ξ sampled},1_{ζ sampled})
       =(1-q_ξ-q_ζ)^s-(1-q_ξ)^s(1-q_ζ)^s <=0, ξ!=ζ,
    Var T_s <=sum_ξ z_ξ² P_ξ <=(max z_ξ) E T_s.          (12)

These follow by computing probabilities that frequencies are absent. Consequently

    P(T_s >= (E T_s)/2)
       >= E T_s/[4(E T_s+max z_ξ)]                     (13)

when E T_s>0, by Cauchy–Schwarz/Paley–Zygmund. Also

    (1-e^-1) min(1,sq_ξ) <=P_ξ<=min(1,sq_ξ).             (14)

For the lower bound use (1-q)^s<=e^-sq and concavity of 1-e^-x on [0,1]. The upper bound is a union bound. Therefore

    E T_s >=(1-e^-1) sum_ξ z_ξ min(1,sq_ξ).              (15)

Repeated selections do not create extra Fourier energy. Their expected pair collision count is binom(s,2)sum q_ξ², but collision concentration by itself says nothing about the useful weights z_ξ.

On the full group, with z_ξ=|uhat(ξ)|², combining (9) and (11) gives a factor with at most s quarter coordinates and

    ΔE >=(8/π²) sum_ξ |uhat(ξ)|²[1-(1-q_ξ)^s].          (16)

No probability-of-success argument is needed for mere existence: some sample attains its expected T_s. Equation (13) additionally quantifies random-search success. On a relative Ω use (5), or (6) together with a uniform Gram bound for the sampled sets; replacing G by I without proof is invalid.

A sufficient and quantitatively exact sampling condition at the allowed budget s≈a^-1/2/log(2/a) is

    sum_ξ |uhat(ξ)|² min(1,sq_ξ) >=c a²                 (17)

in the full-group case. In the relative case the exact sufficient statistic is

    E_sample[ c_(Γ_s)*
        (κ²G_(Γ_s)+(1-κ²)I)^-1 c_(Γ_s)] >=c a².        (18)

The rotations then provide the required energy with an absolute constant depending on c. Neither (17) nor (18) has been proved from AP-freeness.

## 5. What the Boolean derivative graph really supplies

For the full group only, put C_d(x)=B(x)B(x+d), W_t=|Bhat(t)|². Expanding B twice gives

    C_d_hat(ξ)=sum_t Bhat(ξ-t)Bhat(t)e_p(td).

Parseval IN THE DIFFERENCE VARIABLE, with normalized E_d, gives the exact right-degree identity

    E_d |C_d_hat(ξ)|² =sum_t W_t W_(ξ-t)=(W*W)(ξ).       (19)

This is valid for every Boolean B, with no AP-free assumption. Summing ξ yields a², since sum W=a.

For an AP-free B use the accepted negative angular edge weights

    h(d,ξ)=1_{d!=0}1_{cos(4πξd/p)<0}|C_d_hat(ξ)|²,
    r_ξ=E_d h(d,ξ), M=sum_ξ r_ξ,
    q_ξ=r_ξ/M when M>0.

The independently derived angular identity forces

    M >=(a²-a/p)²/(1-1/p),
    0<=r_ξ<=(W*W)(ξ), r_0=0.                            (20)

Thus there is a precisely defined sampling distribution. However its right-degree is a convolution of original Fourier magnitudes, not those magnitudes themselves. For ξ!=0,

    (W*W)(ξ)=2a²W_ξ+
               sum_{t!=0,ξ}W_t W_(ξ-t).                 (21)

The second term can dominate. No legitimate deduction replaces r_ξ by W_ξ or transfers derivative angular mass directly to original energy.

In particular the AP-free Z_13 difference set A={0,1,3,9} has every nonzero derivative C_d a singleton. Therefore all derivative magnitudes are equal, the angular right-degree distribution is uniform on the 12 nonzero frequencies, and the original squared magnitudes are also flat there (3/169). This directly tests the lack of a distinguished preferred frequency. It does not refute (17) at the asymptotic target scale.

For a diffuse hypothetical q_ξ≈1/p and total original energy sum_{ξ!=0}W_ξ≈a, (11) gives only

    E T_s≈s a/p,
    E T_s/a²≈s/(ap)
        ≈(log p)^(3/2)/(epsilon^(3/2)p log log p) ->0.   (22)

The graph's total angular mass M≈a⁴ does not rule this out by itself. This is a conditional calculation explaining what exact concentration/overlap statistic is missing, not a globally AP-free counterexample.

Entropy or dependent random choice based only on q is likewise insufficient: one needs overlap with z_ξ or the regularized relative Gram signal in (18). A high collision probability can be concentrated on frequencies with negligible original correlation. Conversely a diffuse q can retain signal if the original weights are sufficiently large across its support; formulas (11)-(18) handle both possibilities without guessing.

## 6. Quantitative significance and remaining attack

The new conversion theorem requires only many original residual coefficients at the available rank, and loses no extra density power:

    s≈a^-1/2/log(2/a), total squared correlation≈a²
        =>quarter-factor energy≈a²

when the relative Gram covariance is controlled, or when (18) holds directly. At a≈epsilon/log p the available rank is sqrt(log p)/log log p. Coefficients of typical squared size a²/s are therefore

    a^(5/2)log(2/a).

The exact derivative marginal (19) now expresses the compression problem as an overlap between the selected convolution mass r and the original residual analysis vector c, corrected by the window Gram matrix. The sufficient statistic (18) is more precise than a statement that frequencies must be coherent. It is NOT claimed necessary for H, and H might hold by characters chosen by another mechanism.

A next attack should prove a lower bound for (18), or a comparable greedy residual variant, USING the labeled exclusions rather than just M or unlabeled right-degree moments. The present theorem removes the conversion uncertainty; it does not establish this compression inequality or remove H.

## 7. Verification

`python3 verify_structural_sampling_20261002.py` passed and saved `structural_sampling_verification_20261002.json`:

- 2,208 Boolean subsets, p=5,7,11: the exact-in-form difference Parseval convolution identity (19), floating tolerance 1e-10;
- 15 exact rational sampling distributions/lengths: (11)-(12), enumerating all sample tuples;
- 886 relative rotation integrals over all nonempty Ω in Z_5,Z_7: (2) and the diagonal covariance bound, analytic integration between every quarter-boundary event;
- 2,658 residual refinement checks on arbitrary nonempty Ω and three existing partitions: average gain in (4), including empty-cell handling;
- 36 simultaneous two-character regularized-Gram checks with existing partitions: exhaustive quarter-rotation cells compared against the exact 2-by-2 inverse in (5).

The proofs are symbolic. Finite checks provide normalization/error diagnostics, not asymptotic proof or a proof of the unestablished compression conditions.

Classification: (1)-(16), (19)-(21) PROVED; (17)-(18) CONDITIONAL sufficient compression statements, unproved under AP-free hypotheses; numerical checks COMPUTATIONALLY CHECKED ONLY; the local r4 target remains unresolved.
