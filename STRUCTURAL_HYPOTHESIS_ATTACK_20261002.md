# Structural-hypothesis attack — 2 October 2026

**Principal status: (D) NEW RIGOROUS THEOREM.**
H and the unconditional local target remain unresolved.

This is a continuation of the earlier October 2 conditional closure, not
an unconditional solution. No internet is used. The original hypothesis H
is neither assumed nor redefined. Earlier records are retained in place
and in the `history/structural-attack-*` backup directory.

## 1. Audit boundary and research organization

CURRENT_STATUS, NEW_RESULTS, SOLUTION_LEDGER, PROOF_DEPENDENCIES, AGENTS,
and the three October route notes were read. NEW_RESULTS sections 1–6
contain the full elementary conditional chain, so no black-box inverse
theorem is an input to it. Its energy, atom-mass, and terminal estimates
are retained. The research below attacks the structural input itself.

Available skills were checked for task relevance. No installed mathematical
research/proof skill applies. Design/user-research skills are not mathematical
proof workflows. Direct derivations and focused verification are used.
The user requested simultaneous counterexample investigation; three parallel
research lanes examine the graph, sampling, and relative geometry.

All group averages have normalization 1/p. On a window, E_Ω has normalization
1/|Ω|. Set w=|Ω|/p and α=wa. A full-group calculation about 1_A has density
α, not a. We never replace α by a without justification.

## 2. Variable-energy iteration: a proved envelope theorem

Suppose a structural input (NOT proved here) produces, at density a≤4/5,
a quarter factor with at most s(a) characters and energy η(a)a²,
where 0<η(a)≤1/4. The existing elementary atom lemma then supplies

    a'≥a(1+η(a)/2),   r_A≥η(a)a/(2·4^{s(a)}).

Here is a precise ledger for any such functions, without a regular-variation
assumption. Set t=ε/log N and e_k=2^k t. Include epochs with e_k≤4/5.
For each epoch [e_k,min(2e_k,4/5)] set

    m_k=inf η(a)>0,  R_k=sup s(a)<∞,
    M_k=1+4 log(2)/m_k.

There are at most M_k steps whose starting density lies in this epoch.
Indeed successive densities grow by ≥1+m_k/2 while in it, and
log(1+m_k/2)≥m_k/4. A jump over epochs only decreases their step counts.
For every partial iteration the exact size telescope therefore gives

    D_t=1+Σ_k M_k R_k,
    S_t=log(1/t)+Σ_k M_k[log(2/(m_k e_k))+(log4)R_k],
    d_j≤D_t,  log(N/|Ω_j|)≤S_t.                         (V1)

If, as N tends to infinity with ε fixed,

    D_t,S_t=o(sqrt(log N)),
    D_t[S_t+log(2D_t)+1]=o(log N),                       (V2)

then all the original H-window eligibility bounds persist and the existing
terminal packing lemma contradicts density >4/5. This is a PROVED
implication for the stated envelopes, not a proof of its structural premise.
The separate bounds on D_t,S_t are included: a terminal product estimate
alone need not keep a general asymmetric ledger inside H's size restriction.

### Power/logarithm region

Let ℓ(a)=log(2/a), and suppose, for fixed β≥0, γ>0 and C,D≥0,

    η(a)≥c a^β/ℓ(a)^C,
    s(a)≤ceil(K a^{-γ}/ℓ(a)^D).

Reduce c if needed to keep the guaranteed η≤1/4. Dyadic epochs yield

    D_t,S_t=O(t^{-(β+γ)}ℓ(t)^{C-D}).                    (V3)

For clarity, ceiling/mass terms contribute O(t^{-β}ℓ(t)^{C+1}) when
β>0, and O(ℓ(t)^{C+2}) when β=0. They are smaller than the leading
positive-γ term. The estimate follows from a geometric series times a
fixed logarithmic power: splitting epochs at sqrt(t) handles even negative
C-D without assuming global monotonicity.

Thus β+γ<1/2 suffices; at β+γ=1/2, D>C suffices. At t=ε/log N
the endpoint product is O_ε(log N/(log log N)^{2(D-C)}), plus smaller
terms. These are sufficient regions of the recorded iteration. Outside
them we assert only that these upper envelopes do not certify closure.

For γ=0 and s(a)=O(ℓ(a)^E), E≥0, β>0 instead gives

    D_t=O(t^{-β}ℓ(t)^{C+E}),
    S_t=O(t^{-β}ℓ(t)^{C+max(E,1)}).

For β=0 the corresponding bounds gain one extra power of ℓ(t).
All fixed C,E pass when β<1/2; this does not prove their structural inputs.

## 3. Exact greedy arithmetic and a lower-energy target

Let B=1_A, g=E_Ω(B|F), u=B-g. A relative quarter-conversion theorem
proved in STRUCTURAL_SAMPLING_20261002.md gives, for every nonzero ξ,
some rotation with refinement gain at least

    κ² |E_Ω u e_p(-ξx)|²,  κ²=8/π².                    (G1)

There is no w factor or boundary loss in G1; it holds on any nonempty Ω.
It is a quantitative lower bound, not a claim that this constant is optimal.

For fixed 0<ζ≤1/4, energy goal ζa² and budget a^{-1/2}/ℓ(a)
require a per-character gain of order a^{5/2}ℓ(a). The needed coefficient
size is consequently a^{5/4}sqrt(ℓ(a)), not a² or a^{3/2}.

We can also lower the stopping energy. Fix 0<β<1/2. If whenever

    Var_Ω(g)<ζ a^{2+β}

and at most M(a) new characters have been recorded, one can find ξ≠0 with

    |E_Ω u e_p(-ξx)|²≥c a^{5/2}ℓ(a),                    (G2)

then repeated G1 reaches the energy goal in at most

    M(a)=ceil((ζ/(κ²c)) a^{-(1/2-β)}/ℓ(a))             (G3)

characters. G2 is required uniformly for every intermediate quarter factor
with fewer than M(a) characters and energy below the goal. Repeated
characters with new rotations are allowed, as in the original definition.
The old conditional expectation is orthogonal to the residual, so each
gain adds; empty cells never cause a division.

The input in (G2) is UNPROVED. If proved on the unchanged H-window class,
it would provide η(a)=ζa^β and γ=1/2−β,D=1,C=0 in V3, hence close the
local target. In particular choose β=1/4:

    stopping energy ζa^{9/4},
    completed factor rank O(a^{-1/4}/ℓ(a)),
    cumulative rank/log-loss O(t^{-1/2}/ℓ(t)).           (G4)

At a≈ε/log p these become energy of order (log p)^{-9/4},
per-factor rank of order (log p)^{1/4}/log log p, and a residual coefficient
of order (log p)^{-5/4}sqrt(log log p). This is a smaller energy stopping
target than ζa². It is a sufficient alternative, not a logical equivalence
to H and not an established frequency-selection theorem.

More generally if the squared-coefficient guarantee is c a^λ ℓ(a)^q,
and η(a)=ζa^β/ℓ(a)^C with 0≤β<λ−2, the greedy rank is

    O(a^{-(λ−2−β)}/ℓ(a)^{C+q}) plus its ceiling.

The leading cumulative cost is O(t^{-(λ−2)}/ℓ(t)^q), independently of
β,C. The mass overhead still needs β<1/2. Therefore λ<5/2 suffices
with fixed logarithmic losses; λ=5/2 suffices with q>0. No such AP-free
residual-coefficient estimate is proved here.
In this general paragraph reduce ζ by a fixed C-dependent factor to ensure
η(a)≤1/4 even near a=4/5, where ℓ(a)=log(5/2)<1.

## 4. Direct counting normalization audit

For B=1_A extended by zero to Z_p, AP-freeness gives Λ4(B)=α/p=wa/p.
A hypothetical *full-group-normalized* estimate

    Λ4(B)≥c α^4/ℓ(a)^C

contradicts this as soon as p α³/ℓ(a)^C>1/c. Even at the worst
w≥exp(-sqrt(log p)), a≥ε/(2log|Ω|)≥ε/(2log p),

    p α³/ℓ(a)^C
      ≥ (ε³/8) exp(log p−3sqrt(log p))
                      /[(log p)³·O_ε((log log p)^C)] →∞. (DC1)

Thus even polynomial losses in 1/w may be affordable in a direct counting
argument, provided its lower bound is actually established and normalized.
No such estimate follows merely from small linear-factor energy; the signed
quartic term in NEW_RESULTS §7 has not been controlled.

The full density α may be exponentially smaller than a in sqrt(log p).
Full-group Chang bounds at a relative coefficient threshold therefore
cannot be imported with a substituted for α. A relative Gram theorem,
rather than false relative Fourier orthogonality, is used in the sampling lane.

The stronger natural window-relative baseline would be
Λ4(B)≥c a⁴Λ4(1_Ω)/ℓ(a)^C. Since Λ4(1_Ω)≥w²/3^d, the comparison with
the AP-free diagonal is then p a³w/(3^dℓ(a)^C), bounded below at H's
worst geometry by exp[L−(1+log3)sqrt(L)] divided by fixed logarithmic
powers. It too tends to infinity. This remains a sufficient UNPROVED
counting premise; random-model expectations are not deterministic bounds.

## 5. Parallel route results and final classifications

### A proved relative many-character theorem

Let Ω be any nonempty finite window (indeed any subset), F0 any existing
partition, u=B−E_Ω(B|F0), and Γ a collection of s distinct nonzero
characters e_i. Define

    c_i=E_Ω u conjugate(e_i),
    G_ij=E_Ω[conjugate(e_i−E_Ωe_i)(e_j−E_Ωe_j)],
    κ²=8/π², M=κ²G+(1−κ²)I.

Then some simultaneous quarter-arc rotations yield actual refinement gain

    ΔE≥κ² c* M^{-1}c.                                  (R1)

The proof is in STRUCTURAL_SAMPLING §§2–3: random midpoint quantization
has expectation κe_i, off-diagonal covariance κ²G, and diagonal covariance
at most κ²G_ii+1−κ². Projection followed by averaging and optimization
gives R1. M is positive definite even for linearly dependent characters
on Ω. This accounts for relative geometry exactly, without a boundary
loss or a small-cell assumption. On Z_p, R1 becomes ΔE≥κ²Σ|uhat(ξ)|².
The universal real single-character best constant is only bracketed here:
8/π²≤c_best≤1. Its exact optimization is not resolved or needed for closure.

### A proved quadratic obstruction at the expanded budget

Set W=1_Ω, w=|Ω|/p, d=rank(Ω), C_p=2+log p, and let q(x)=cx²+bx+c0
with c≠0. Every s-character quarter factor satisfies

    ||E_Ω[e_p(q)|F]||²≤4^s p^{-1/2}w^{-1} C_p^{d+s}.   (R2)

For B=1_S(q), S an interval of relative length β, one also has

    |E_Ω B−β|≤p^{-1/2}w^{-1}C_p^{d+1},
    Var_Ω(E_Ω[B|F])≤4^s p^{-1/2}w^{-1}C_p^{d+s+1}.      (R3)

Under H's geometry and s=O_ε(sqrt(log p)/log log p), these bounds are
exp[−(log p)/2+o(log p)]. In particular genuine quadratic phases have
best factor-measurable approximation error 1−o(1), and quadratic Boolean
interval hosts of density β≈ε/log p have energy o(β²) for every such F.

They are not counterexamples to H: a new relative counting identity proves
they contain nonzero 4APs on EVERY H-window. Precisely,

    |Λ4(WB)−Z_SΛ4(W)|≤p^{-1/2}C_p^{4d+4},
    Z_S=Σ_t |Shat(t)|²|Shat(3t)|²
       ≥8β³/(3π⁴)  for 0<β≤1/12,
    Λ4(W)≥w²/3^d.                                     (R4)

Thus the positive quadratic resonance dominates both the error and the
diagonal uniformly. Complete Fourier/Gauss and lift-label proofs, including
tiny-cell denominators, are in STRUCTURAL_GEOMETRY §§2–4A. The source
frontier_audit_geometry.md was read in full; its label argument is reproduced
there, so R4 uses no unproved geometry claim.

This addresses both branches of the quadratic attack: generic quadratic
approximation by these linear factors is refuted, but the natural invisible
quadratic host fails exactly AP-free Booleanity. The earlier full-group
constant-fraction deletion theorem does not automatically become a
constant-fraction deletion theorem on all relative windows.

### Exact graph and cocycle calculations

With full-group density α=wa and b=1_Ahat, the two-variable transform of
F(d,k)=E_x B(x)B(x+d)e_p(−kx) is b(k−t)b(t). Consequently its right
degrees are (|b|²*|b|²)(k), not |b(k)|². The signed AP coupling is

    Λ4(B)=Σ_{k,t} b(k−t)b(t)conjugate[b(−k−t)b(t+2k)].

The graph codegrees return ||B||U3^8 as their diagonal sum, so that
particular higher-moment shortcut does not improve the inverse step.
A positive diffuse abstract angular graph disproves compression from row
mass/angular exclusion alone. An actual AP-free Z_13 example disproves
additivity of arbitrarily selected saturated pair frequencies. The repaired
cocycle criterion needs nearly saturated pair errors AND a flat Fourier
transform on the shared triangle support; neither premise is supplied by
the angular-mass theorem. Explicit formulas and witnesses are preserved in
STRUCTURAL_GRAPH §§1–4, including a quantified repaired consistency lemma.

Sampling the angular right-degree distribution q captures original residual
weight z exactly in expectation Σ_ξ z_ξ[1−(1−q_ξ)^s]. Occupancy covariance
is nonpositive. The precise sufficient relative sampling statistic is the
expected R1 quadratic form, not collision probability or graph entropy
alone. No AP-free lower bound for that statistic is proved.

### Coverage of the requested attacks

| Requested attack | Actual calculation and outcome |
| --- | --- |
| I, II: selected frequencies/weighted graph | Double transform, convolution degrees, second moments/codegrees, top-m bounds, diffuse angular graph; no valid compression theorem |
| III: random sampling | Exact occupancy mean, variance, collision and Paley bounds; missing overlap statistic explicit |
| IV, V: greedy capture/relative arcs | R1 and G1 proved with no window loss; G2 selection unproved |
| VI: many weak coefficients/dimension | Relative regularized-Gram capture proved; generator count cannot replace frequency count without phase resolution |
| VII: transform in both variables | Product tensor and signed four-factor coupling derived exactly |
| VIII, X: cocycle/higher consistency | Support-weighted cocycle and quantitative triangle criterion proved; saturation-only implication explicitly refuted |
| IX: quadratic drift | Expanded-budget approximation refuted by R2; invisible Boolean host AP-rich by R4 |
| XI: relative geometry | Many short shifts on reachable smaller windows; worst H class not covered by this bound; no false invariance of B inferred |
| XII: counterexamples | Qualified quadratic/cube/product candidates; no AP-free candidate satisfies all asymptotic requirements |
| XIII: weaker inputs | V1–V3 region and G4 lower stopping target derived; structural premises unproved |
| XIV: direct counting | DC1 and window-baseline asymptotic comparisons proved; counting premise remains unproved |

## 6. One explicit sufficient selection statement still unproved

For each ε>0, do there exist 0<ζ≤1/4,c>0,p0 such that for every p≥p0,
every original H-window Ω and cyclically 4AP-free A⊂Ω in H's density range,
and EVERY quarter factor F using fewer than

    M(a)=ceil((ζ/(κ²c))a^{-1/4}/log(2/a))

additional recorded characters, the following holds?

    If Var_Ω(E_Ω[B|F])<ζa^{9/4}, then
    max_{ξ≠0}|E_Ω[(B−E_Ω[B|F])e_p(−ξx)]|²
                          ≥c a^{5/2}log(2/a).           (SG)

SG is CONJECTURED, not a theorem or a necessary equivalent of H. G1–G4
and V1–V3 prove its implication to the local target, using the unchanged
window geometry. It isolates an explicit single-character selection task
with the correct critical exponent and log saving, even though only a
lower stopping energy than H is demanded. An alternative route could
instead establish the sampling quadratic-form bound or a direct count.

The present run proves R1–R4 and the graph/sampling/geometry auxiliary
results, not SG, H, or r4(N)=o(N/log N). No literature novelty or current
official-problem status is claimed.

## 7. Verification and audit

The root checker passed 324 variable-energy trajectories, 225 exact integer
window-label identities, 17,667 quadratic-kernel tuples, and eight finite
adversarial families. For the last test it enumerated all nonzero characters
and all quarter-rotation states in Z_257 on a 65-point narrow window.
It computed AP-freeness rather than assuming it from a family name.
Random, quadratic, progression-plus-cube, and interval examples contained
4APs. Ternary, sparse-cube, separated-piece and tensor samples were 3AP-free
and visibly captured by one character. These are finite tests, not density-
scale proofs or refutations of SG/H.

Independent audits found no substantive defect in the relative Gram,
variable-energy, greedy exponent, or relative quadratic counting proofs.
The fixed-constant cap for general η(a) was made explicit after audit.
Route-specific scripts and exact/floating scopes are recorded in their
notes and JSON. No numerical evidence is substituted for a symbolic proof.

Final independent reruns passed all four new structural scripts and all four
existing core/localization/target-scale/hostile scripts. The complete output
record is structural_reverification_20261002.json. Required documents were
checked for nonempty content and verification JSON for valid syntax.
