# Next autonomous action — 21 October 2026

Resume from `checkpoints/AUTONOMOUS_CHECKPOINT_20261021.json`, `CURRENT_STATUS.md`,
`docs/audits/QUADRATIC_PROJECTION_SELECTION_20261021.md`, and `OPEN_LEMMAS.md`.
The mathematical frontier is 21 October. Outcome D; the unconditional
local target and DIRECT-Q-GAIN remain OPEN.

The 21 October work resolves Open Lemma O3 through two complementary steps:
1. Canonical tight frame reconstruction with zero residual error: $\delta \ge am / \mathcal{L}_k$
   ([QUADRATIC_FRAME_CERTIFICATE_20261021.md](docs/audits/QUADRATIC_FRAME_CERTIFICATE_20261021.md)).
2. Finite quadratic chirp projection theorem: $\delta \ge \theta_\Gamma \frac{am}{L_\Gamma}$
   ([QUADRATIC_PROJECTION_SELECTION_20261021.md](docs/audits/QUADRATIC_PROJECTION_SELECTION_20261021.md)),
   showing that selecting $n \le \lceil 1/a \rceil$ dominant phases captures $\ge 10\%$ of $\langle u, k \rangle = -awm$
   with coefficient norm $L_\Gamma \le C \frac{m}{\sqrt{a} \log(1/a)}$, forcing $\delta \ge c a^{3/2} \log(1/a)$ with $c \ge 0.91$.

The PRIMARY NEXT ATTACK is therefore End-to-End Iterative Closure:
Couple the divergent phase selection bound $\delta \ge c a^{3/2} \log(1/a)$ with the mixed-window
density increment machinery from `docs/audits/DIRECT_INCREMENT_TRADEOFF_20261016.md` and
`docs/audits/MIXED_QUADRATIC_TERMINAL_20261016.md`:
1. Trace the quarter-cell density increment $\Delta a \ge \kappa \delta / (8a) \ge \frac{c \kappa}{8} a^{1/2} \log(1/a)$.
2. Verify that the iteration recurrence $a_{j+1} \ge a_j + c' a_j^{1/2} \log(1/a_j)$ reaches the terminal
   density ceiling $7/11$ in at most $J \le C / \sqrt{a_0}$ steps.
3. Verify that the host complexity parameter $r_{j+1} = r_j + 1$ satisfies the presentation budget
   $r [ \log(p / |\Omega|) + \log(48r) + \log\log p ] \le \log p / 100$ at all steps $j \le J$
   for $a_0 \ge \epsilon / (2 \log N)$, completing the unconditional proof of $r_4(N) = o(N / \log N)$.

Read `docs/audits/QUADRATIC_PROJECTION_SELECTION_20261021.md`, `docs/audits/DIRECT_INCREMENT_TRADEOFF_20261016.md`,
and `docs/audits/MIXED_QUADRATIC_TERMINAL_20261016.md` before proceeding.

The positive-density failure branch is closed by
`POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md`, with explicit use of
the classical qualitative four-term Szemerédi theorem. The remaining
DIRECT-Q-GAIN failure must be an eligible `a->0` sequence with bounded
`delta/a^(3/2)`. The classical theorem is not reproved, and no rate at
logarithmic density follows from its uncontrolled threshold.

Read the original framework before changing hypotheses:
`WEIGHTED_PAIR_REDUCTION_20261016.md`,
`DIRECT_INCREMENT_TRADEOFF_20261016.md`, and
`MIXED_QUADRATIC_TERMINAL_20261016.md`.
The terminal ceiling is `7/11+o(1)` under M13. Improving only that constant
does not supply the structural phase-selection step; the conditional
iteration parameters need no recalculation.

Every proposed counterexample must satisfy T5, the density range, actual
AP exclusion, original H, and the failed cap. The 76 finite witnesses,
the polynomial-density AP-free construction, and the October 19 block
construction each fail at least one condition. Refuting one fixed
multiplier is insufficient to negate the full DIRECT-Q-GAIN statement.

Use the latest checkpoint and `VERIFYING.md` for verification scope and
commands. Do not repeat unchanged suites merely to restart. Independently
audit a new proof and run the smallest relevant finite check. Preserve
historical sources, update all nine navigation/ledger files, and save a
dated checkpoint before ending. Saved notes do not imply background work.
