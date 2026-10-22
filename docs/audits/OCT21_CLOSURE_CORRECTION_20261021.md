# Correction of the October 21 closure claims

Audit begun 21 October; completed 22 October 2026. This supersedes the
closure claims in commit `51854a2` and its October 21 predecessor drafts.
**The local target, DIRECT-Q-GAIN, and conditional P12/W8 remain OPEN.**
The obstacle is a missing proof, not merely pending external peer review.

## 1. What failed

The completion, frame, and projection notes contain valid identities, but
their proposed quantitative consequences do not follow.

- Completion E11 drops the uncontrolled cubic term from the exact relation
  `awm = 4a^4T + 3R1 + 2R2 + R3 - 4a^2w/p`.
  Substituting an equivalent residual identity supplies no lower bound.
  The small/zero completion-mean branch remains unresolved on eligible hosts.
  Interior completion channels count gapped triples, not just ordinary 3-APs.
- Completion E13 miscalculates a denominator:
  `sqrt(a(1-a))*sqrt(a/(1-a))*m = am`. The resulting bound is correlation
  at most 1, not at most `1-a`. An upper bound tending to 1 would not prove
  collinearity in any case.
- Projection QP11 assumes an unproved small orthogonal residual `z`.
  A negative total inner product does not force each spectral contribution
  to be negative, nor does a global norm bound by itself control every mode.
- Projection QP12 reverses the exact variance inequality. The identity is
  `||k||_Omega^2 = a m^2/(1-a) + ||z||_Omega^2`, so the displayed main term
  is a LOWER bound. No upper bound of that size follows from hole support.
- The claim that at most `ceil(1/a)` phases capture a fixed fraction of the
  cross-spectrum is asserted, not proved. A large individual term also
  gives no lower bound for every subsequent selected term.
- The proposed effective bandwidth and extra `log(1/a)` gain have no proved
  lemma. A tent Fourier transform is not a hard spectral cutoff, and the
  original weight does not automatically concentrate the quadratic
  transform of the completion field.
- Ratios measured on 27 tiny, hand-selected cases do not establish a
  uniform constant `c >= 0.91`, a divergent multiplier, or an asymptotic rate.

Consequently the claimed unconditional iteration closure, effective bound
`r_4(N)/N = O(1/(log N (loglog N)^2))`, phase transition at `H=1`, and
higher-degree selection conclusions are unsupported. Conditional bookkeeping
or finite algebra within those drafts must be assessed separately.

## 2. P12/W8 were not refuted

The October 21 argument discarded the failed-selection hypothesis.
On reachable AP-free hosts, the established one-sided pair estimate gives

    Q = R3+R4 <= -(1-o(1)) a^4 w mu.

It does not give equality: `R2 >= -o(main)` is not `R2=o(main)`.
The exact covariance identity then gives a LOWER bound for the W8 excess,
not the claimed asymptotic equality.

P12 asks that **failed adequate phase selection** imply
`Q >= -a^4 w mu/2` on this eligible domain. Its contradiction with AP
exclusion would prove that failed selection cannot occur. That is the
intended proof strategy, not a refutation of the conditional lemma.
A refutation needs an instance satisfying all antecedents, including failed
selection. None was supplied. The October 19 construction contains a 4-AP
and likewise cannot refute the conjunction of hypotheses.

## 3. Exact finite counterchecks and their limits

The new [regression verifier](../../verification/scripts/verify_oct21_closure_correction_20261021.py)
and [report](../../verification/results/OCT21_CLOSURE_CORRECTION_VERIFICATION_20261021.json)
independently enumerate cyclic AP exclusion, use rational arithmetic for
completion moments, and label Fourier calculations as floating diagnostics.

| Instance, full host | Exact result or numerical diagnostic | Consequence |
|---|---|---|
| `p=11, H=2, A={0,1,2}` | `m=8/363`; `||k||^2=32/14641`; `a m^2/(1-a)=8/43923` | Actual variance is 12 times the purported upper bound |
| `p=5, H=1, A={0,1,2}` | `q=(0,0,0,1/5,1/5)`, `m=2/25`, correlation squared `1` | Refutes the purported upper bound `(1-a)^2=4/25` |
| `p=101, H=2`, 15-point set recorded in the report | Seven most-negative-real-part phases capture about `0.0288413` of the complex inner product magnitude | The broad finite `0.10` capture claim fails |

These examples fail T5 and their original prescribed radius is zero.
They diagnose broad auxiliary overclaims and invalid proof steps; **they
are not counterexamples to eligible P12 or DIRECT-Q-GAIN**. A separate
argument restricted to the full eligible domain could still be possible.

## 4. A surviving exact identity: the fourth moment needs no AP exclusion

For any subset `A` of an odd-prime field, put `n=|A|`, `alpha=n/p`, and
`Q_B(c,t)=p^-1 sum_x B(x)e_p(-cx^2-tx)`. Then

    sum_(c,t) |Q_B(c,t)|^4 = 2 alpha^2 - alpha/p,
    sum_(c,t)!=(0,0) |Q_B(c,t)|^4
        = 2 alpha^2 - alpha/p - alpha^4.                 (C1)

Proof: orthogonality converts the sum to `p^-2` times the number of ordered
quadruples in `A^4` with equal pair sums and equal pair square-sums. Because
2 is invertible, the pair products also agree. Thus the two unordered pairs
are identical. There are two orderings for each distinct pair and one for
each repeated pair, giving `2n^2-n` solutions. Removing the zero phase
subtracts `alpha^4`.

For nonempty A this implies the earlier lower bound
`sum_nonzero |Q_B|^4 >= alpha^2(1-alpha^2)` whether or not A is AP-free.
That lower bound cannot, by itself, justify the claimed concentration of
`Q_k conjugate(Q_u)`. The verifier checks the solution classification on
both AP-free and AP-rich Boolean sets. C1 is a direct elementary identity;
no novelty beyond this audit is asserted.

## 5. Correct normalization and the conditional certificate

Take `chi_gamma(x)=e_p(cx^2+tx)`,
`Q_f(gamma)=E_p f conjugate(chi_gamma)`, and
`psi_gamma=chi_gamma-E_p chi_gamma`. For mean-zero f, character
orthogonality gives

    f = (1/p) sum_gamma Q_f(gamma) psi_gamma,
    sum_gamma |Q_f(gamma)|^2 = p ||f||_p^2.             (C2)

Indeed the centered kernel is `p^2 1_(x=y)-p`; averaging against f and
dividing by p proves reconstruction. The frame energy follows by pairing
with f. Zero-phase terms vanish. The original notes mixed opposite Fourier
sign conventions; C2 uses one consistent convention throughout.

For a proper host extend the centered completion field by zero:
`k=P(q-m)`, equivalently `q-mP` when q is already supported on Omega.
Do not subtract m on the entire ambient group. Let `u=B-aP` and
`<f,g>=E_p f conjugate(g)`. Hole support gives `<k,u>=-awm`.
For any subset Gamma define

    k_Gamma = (1/p) sum_Gamma Q_k psi,
    xi_gamma = Q_k(gamma) conjugate(Q_u(gamma))/p,
    L_Gamma = (1/p) sum_Gamma |Q_k(gamma)|.

Then `<k_Gamma,u>=sum_Gamma xi`. For `L_Gamma>0`, the triangle inequality
proves

    delta >= |sum_Gamma xi| / (w L_Gamma).             (C3)

When `m>0`, this can be written `delta >= theta_Gamma a m/L_Gamma`,
where `theta_Gamma=|sum_Gamma xi|/(awm)`. A partial sum need not be a
fraction bounded by 1. C3 does not assert that a useful Gamma exists.
The full canonical frame has zero reconstruction error, but its generic
coefficient estimate is only
`L_can <= sqrt((p^2-1)/p) ||k||_p`.
Zero reconstruction error supplies neither the missing norm bound nor
spectral concentration. The exact norm decomposition and its lower bound
remain valid; the small-error/small-coefficient certificate is still conditional.

The exact cyclic AP-free chirp identity and the dual residual identities
E1–E6 in the completion draft survive this audit, with their stated
normalizations. None resolves the missing inequalities above.

## 6. Formalization and verification scope

`formalization/lean/Erdos142/HoleSupport.lean` contains `sorry`.
`TightFrame.lean` declares four additional axioms for character facts.
These files are formalization drafts, not a completed formal proof. Python
CI neither compiles them nor removes those assumptions. No Lean build is
claimed in this audit.

The disputed drafts and publication summaries are preserved under
[history/proof_audit_20261021](../../history/proof_audit_20261021/), with
hash manifests. The manuscript is marked withdrawn. Existing numerical
scripts remain finite diagnostics, even where old check labels use theorem
names. The added regression suite tests the actual erroneous steps.

The next research step is to prove the missing concentration and residual
control on genuinely eligible hosts, including the completion low-mean
branch, or prove conditional W8 directly. Merely enlarging the numerical
sample or restating the tight frame identity will not close the gap.
