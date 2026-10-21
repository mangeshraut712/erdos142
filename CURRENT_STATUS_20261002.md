# Current SELECT attack status — 2 October 2026

**Principal result: (D) NEW RIGOROUS THEOREM.**

SELECT is neither proved nor refuted. The unconditional local target
r4(N)=o(N/log N) remains unresolved.

The principal new theorem constructs a degree-four Boolean PSD moment
functional with exact cardinality and vanishing actual quartic AP moments,
while per-frequency expected Fourier squares are below the SELECT scale.
It is NOT a representing probability law or an AP-free counterexample;
pointwise Fourier-cap localizers and nonnegative fourth cylinder moments
are not established. See SELECT_CARDINALITY_RELAXATION_20261002.md.

Full-group main-term positivity is also proved:
|Λ4(g)-a^4|<=4a Var(g)^(3/2)+Var(g)^2. A relative-window marginal bound
is proved in SELECT_ATTACK_20261002.md. Neither supplies the missing signed
residual cancellation at all allowed window ranks.

The exact budget also permits a strictly weaker, still UNPROVED selection
input: lower the stopping energy and Fourier gain by the matched factors
R(a)/log(2/a) and R(a), where R(a)=log log(e²/a). The greedy ceiling stays
unchanged and the resulting conditional ledger closes. This is not an
unconditional sufficient theorem.

All current proofs, limitations, experiments and dependencies are in
SELECT_ATTACK_20261002.md and the five SELECT route notes. Earlier status
is retained below without alteration.

---

# Current structural attack status — 2 October 2026

**Principal status: (D) NEW RIGOROUS THEOREM.**

The remaining hypothesis H was neither proved nor refuted. The unconditional
local target r4(N)=o(N/log N) remains unresolved. The earlier complete
conditional closure is preserved below as a historical checkpoint.

The strongest new theorem is relative many-character variance capture:
for a residual u=B−E_Ω(B|F0), correlation vector c and centered relative
character Gram matrix G, some simultaneous quarter rotations yield

    ΔE >= κ² c* [κ²G+(1−κ²)I]^{-1}c,  κ²=8/π².

This holds for every nonempty Ω, every existing F0, and includes singular
Gram matrices and tiny/empty cells. It removes the relative arc-conversion
loss; the AP-free selection of useful coefficients is still unproved.

A second theorem shows that every genuine quadratic phase stays invisible
to s=O(sqrt(log p)/log log p) linear quarter factors throughout H's window
class. Boolean quadratic interval hosts at density about ε/log p inherit
this invisibility, but a new relative counting identity proves they contain
nonzero 4APs on EVERY H-window. Hence they refute a generic approximation
mechanism, not H.

The derivative graph was transformed in both variables: right degrees are
a convolution of original squared Fourier magnitudes. Abstract angular
constraints admit diffuse graphs, and an actual AP-free finite example
refutes saturation-only additive frequency selection. The repaired cocycle
criterion explicitly needs control of the shared triangle support.

The weaker-energy iteration was quantified. In particular, a sufficient
UNPROVED residual selection statement SG asks for

    max_{ξ≠0}|E_Ω[(B−E_Ω(B|F))e_p(−ξx)]|²
           >= c a^{5/2}log(2/a)

only while factor energy is below ζa^{9/4}, for every intermediate factor
with fewer than ceil((ζ/(κ²c))a^{-1/4}/log(2/a)) added characters. If SG
held uniformly on the unchanged H-window class, its implication to the
local target is proved. SG is sufficient, not necessary or equivalent to H.

See STRUCTURAL_HYPOTHESIS_ATTACK_20261002.md for all quantifiers, the
variable-energy ledger, coverage of all fourteen attacks, and exact gaps.
Full route proofs are in STRUCTURAL_SAMPLING_20261002.md,
STRUCTURAL_GRAPH_20261002.md, and STRUCTURAL_GEOMETRY_20261002.md.

New checks passed: 324 scalar variable-energy trajectories, 225 exact
window-label identities, 17,667 quadratic-kernel tuples, eight adversarial
families with all characters/rotation states checked in Z_257; and the
route-specific rotation/Gram, graph/cocycle, and geometry/Gauss checks.
Independent mathematical audits found no substantive gap in the proved
conversion, variable-energy implication, or relative quadratic counting.
Finite/floating checks do not prove SG or H. No internet was used and
no literature-novelty or current official-problem-status claim is made.

Final independent reruns of all four new structural checkers and the four
existing core/localization/target-scale/hostile checkers exited successfully.
Full outputs are saved in structural_reverification_20261002.json.

---

## Preserved earlier October 2 checkpoint (historical)

# Current research status — 2 October 2026

**Principal status: (C) COMPLETE CONDITIONAL CLOSURE.**

The target r4(N)=o(N/log N) is NOT proved or disproved. The run obtained a
self-contained conditional closure from one explicit new sufficient
hypothesis H, and auxiliary rigorous results from multiple distinct routes.
This is not a solution of the local target or the full official problem.

## What changed mathematically

The critical rank scale a^-1/2 is now allowed with a logarithmic saving:

    rank <=ceil(K/[sqrt(a)log(2/a)]),
    relative factor energy >=ηa².

Only near-full-size, sub-square-root-rank windows need satisfy this input:

    d<=sqrt(log p),  |Ω|>=p exp(-sqrt(log p)),
    ε/(2log|Ω|)<=a<=4/5.

The full implication to the target is proved in NEW_RESULTS_20261002.md
sections 1-6, including exact retained-mass bookkeeping, every partial
iteration's eligibility, the original cutoffs, terminal contradiction,
elementary comparable-prime existence, and one-time integer/cyclic transfer.
Two independent parallel passes checked the iteration and restricted
quantifiers. H remains CONJECTURED; it is one sufficient bottleneck, not
a theorem or an assertion of necessity.

The crucial new summation is

    Σ rank(a_j)=O(a_0^-1/2/log(2/a_0)+log(2/a_0)),

which avoids multiplying the maximum rank by the whole step count. At
a_0=ε/log N, cumulative rank D and log-loss S satisfy

    D(S+log D+1)=o(log N).

The older bound with exponent c<1/2 did not capture this endpoint saving.

## Other proved results from the required routes

- Fourier/counting and character selection were pursued explicitly. The
  exact cubic/quartic dichotomy and quarter-arc series were derived, but
  generic large-spectrum rank and U2 control do not supply H.
- A robust quadratic-host deletion theorem shows that an AP-free set must
  omit a fixed positive fraction of a quadratic interval host at density
  ε/log p. Negligible deletion is not a repair of that proposed example.
- Boolean AP exclusion forces a quantified negative-angular portion of
  each pair-derivative spectrum, with an exact diagonal-aware average.
  Coherent assembly of difference-dependent frequencies is unresolved.
- Higher incidence traces, a global residual Gram PSD constraint, and a
  correctly overlap-accounted AP-exclusion entropy deficit were proved.
  A relabeling theorem shows that unlabeled spectral summaries alone cannot
  extract arithmetic factor structure.
- Full-product Freiman shell constructions and several tensor/coding
  families were excluded at logarithmic density by rigorous upper bounds.
  No actual target-density counterexample was constructed.

All of these have symbolic proofs. Finite computations provide supporting
checks and counterexample diagnostics, not proofs of asymptotic statements.
No claim of literature novelty or current official-problem status is made.

## Files and evidence

- NEW_RESULTS_20261002.md: self-contained conditional closure and route deductions.
- SOLUTION_LEDGER.md: mandatory gain/rank/loss substitutions and terminal budget.
- PROOF_DEPENDENCIES.md: every statement assigned one of the five requested classes.
- ROUTE_QUADRATIC_BOOLEAN_20261002.md: quadratic stability and Boolean angular mass.
- ROUTE_INCIDENCE_MOMENTS_20261002.md: higher traces, PSD, relabeling and entropy.
- ROUTE_CONSTRUCTIONS_20261002.md: quantified failed construction families.
- research_program_verification_20261002.json and route-specific JSON files:
  fresh verification outputs; earlier audit files were preserved.

## Verification completed

The root checker passed 6,606 exact rational energy-atom instances,
4,530 exact terminal packing instances on 130 coordinate windows, and
180 scalar iteration trajectories. Fourier identities were checked on
2,208 subsets with floating tolerance 1e-10 (largest observed error
1.17e-15). Prime-step checks covered 1,000 primorial bounds and 5,193
valuation instances. The scalar asymptotic samples are numerical
diagnostics; the limiting claims rely on the symbolic estimates above.

All three route checkers were independently rerun and exited successfully;
their outputs are collected in research_route_reverification_20261002.json.
The four existing core/localization/target-scale/hostile checkers also
passed fresh runs, recorded in research_checkpoint_verification_20261002.json.
These checks do not prove H or certify the unconditional target.

## Exact next mathematical attack

Prove or refute H exactly as stated, on its restricted geometry, rather
than a factor theorem on every high-rank window. The promising new input
is the labeled Boolean derivative and endpoint constraints. The missing
task is a density-sensitive arithmetic coherence/localization theorem
with the explicit rank and energy above. This run does not establish that
implication, and the local target remains unresolved.
