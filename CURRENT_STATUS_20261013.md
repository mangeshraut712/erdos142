# Current completion-projection status — 13 October 2026

**(D) NEW RIGOROUS PARTIAL THEOREM.** SELECT and the local target
r4(N)=o(N/log N) remain unresolved.

The diagonal-corrected identity is Bh=B/p, and for q=h-B/p it is Bq=0.
Inside each factor cell, q-E(q|F)=-[E(q|F)/(1-g)](B-g)+z with z orthogonal
to the residual. The exact residual pairing is -E[g E(q|F)]. The pairing
uncertainty depends only on between-cell variance, and its spectral
projection bound uses within-cell variance and the actual relative Gram.
These sharpen the earlier estimate without proving a small character set.
A finite spectral diagnostic confirms that the globally orthogonal
remainder can cancel part of the component at a selected frequency.

Whole-group q=0 is equivalent to 3-AP-freeness and gives
rho>=max(0,(a^2-1/p)/(1-a)); the guaranteed squared scale a^4 remains below
SELECT. Window-only q=0 need not imply 3-AP-freeness. The relative-window
zero/low-pairing branch and the character-budget lemma remain open.

Proof and precise remaining lemma: COMPLETION_PROJECTION_20261013.md.
Checks: verify_completion_projection_20261013.py and
COMPLETION_PROJECTION_VERIFICATION_20261013.json. All 743 finite set/window
cases passed, with exact rational identities and numerical spectral
checks. Earlier reports and unrelated working-tree changes are preserved.
