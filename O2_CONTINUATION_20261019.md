# O2 continuation — 19 October 2026

**Outcome D: rigorous partial results and an auxiliary obstruction.**
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN and P12 remain OPEN.
No counterexample satisfying all P12 hypotheses has been constructed.
This continues [the October18 report](O2_CONTINUATION_20261018.md).

## A failure sequence must have density tending to zero

[The uniform positive-density reduction](POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md)
proves explicit finite terminal errors on every T5 host at density
`a>=a0>0`. With `L=log p` and `log L>=4log(1/a0)`, the original baseline
has `mu0>=p^-0.03`, while `w>=p^-0.01`. The first-incidence and boundary
errors vanish uniformly over all permitted host presentations.

For each fixed finite m and AP-free occupancy bound R, the first moment
alone gives `a<=R/m+o(1)`. Combining this with the explicitly stated
classical qualitative four-term Szemerédi theorem rules out any eligible
sequence of relative densities bounded away from zero. This use of the
classical theorem supplies no quantitative rate, and the theorem itself
is not reproved here. Pair near-positivity is unnecessary for this
qualitative corollary, although the sharper finite estimate also uses it.

Consequently the exact negation now has just one possible form: for some
fixed epsilon>0 there must be an eligible sequence with

    a_n -> 0,
    sup_n delta_n/a_n^(3/2) < infinity.

The original logarithmic density lower bound and every geometric/AP-free
hypothesis are still required. The polynomial-density construction from
October18 is not such a sequence. An uncontrolled threshold p0(a0)
cannot be used with a0 depending on p to prove the local target.

## Booleanity and small phases do not imply W8 without AP exclusion

[The new covariance obstruction](O2_COVARIANCE_ATTACK_20261019.md)
constructs actual Boolean sets on the initial interval
`Omega={0,...,floor(p/4)-1}` with

    a~1/log p, delta=o(a^(3/2)),
    H=floor(|Omega|a^2/(48log p)), mu=(H+1)/p,
    R3+R4<=(-11/20+o(1))a^4wmu < -(1/2)a^4wmu.

These sets meet the density range, T5, initial-host geometry, original
weight prescription and negligible-diagonal condition. They deliberately
contain `{0,1,2,3}`, so they are NOT AP-free and do NOT refute P12.

The proof partitions the host into about `(log p)^(5/2)` blocks, independently
translates a verified 29-element cyclic AP-free mask modulo101 in each
block, and thins the retained points independently. Two concentration
steps control every global quadratic phase. The expected original-weight
count is at most `(10201/24389+o(1))a^4wmu`, whose leading constant is
less than9/20. Markov's inequality, an actual-density bracket for H, and
an explicit four-point insertion bound produce the stated sets.

Their exact Boolean chirp identities and all frame constraints hold.
Thus those identities, the phase cap, density, and a count below half
the main term are insufficient to prove W8. A successful proof must use
actual AP exclusion more strongly. This is an obstruction to a weakened
claim, not a new sufficient theorem or a target-domain AP-free example.

## Exact remaining task

For eligible AP-free sets under failed adequate phase selection, prove

    E_F(u)<=2U^2+2R3+a^4wmu, U=wa(1-a).                (W8)

The original-weight identity `R4=U^2-E_F/2` makes this exactly P12.
The cubic term and proper-host correction remain necessary. The alternative
is adequate phase selection directly, including both the positive and
small/zero completion-mean branches of the October18 certificate.

The next proof attempt should use the pointwise AP-free completion
identities `Bq_j=0`, or comparably strong arithmetic information, together
with the logarithmic-density/small-diagonal regime. The new construction
rules out replacing those identities merely by a reduced weighted count.
Neither a sufficient completion certificate nor W8 is proved.

## Audit and verification

Both new proofs received independent line-by-line mathematical audits.
The positive-density finite-envelope verifier passed 18,022 checks and
its isolated rerun matched the saved JSON. The covariance note separates
finite mask/count checks from its asymptotic probabilistic proof. The
current machine-readable verification record and source hashes are in
the latest dated checkpoint. Passing finite checks is not an asymptotic
proof of phase selection.
