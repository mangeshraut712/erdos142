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
