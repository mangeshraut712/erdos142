# Independent derivation audit — 16 October 2026

Principal status D; local target OPEN. This is an internal mathematical
re-derivation and adversarial audit, not external peer review.

## Mixed-window terminal theorem

- **Normalized convolution:** f=(1_[0,H]*1_[-H,0])/eta, eta=(H+1)/p.
  Thus fhat=|Ihat|^2/eta, fhat(0)=eta, and sum fhat=f(0)=1.
  The persistent-baseline lower bound has exponent d+2s, not d+s.
- **Slot substitution:** put x=v-ih before expanding the weight. The
  quadratic coefficient in h is N-2iC, and the linear coefficient is
  2vC+B. Persistent constant phases are exactly C=B=N=0. The condition
  C!=0 selects one exceptional v per Fourier multi-index. Nonnegative
  weights therefore bound its vertex average by 1/p even with many
  resonances and exceptional vertices. No phase independence is used.
- **Gauss estimate:** the unnormalized quadratic exponential sum has
  squared magnitude p. Normalized magnitude is 1/sqrt(p). Summing weighted
  Gauss contributions costs at most 1/sqrt(p), not sqrt(p) or p^(-1).
- **Boundary and wraparound:** interval lifts are eroded by 12H at each
  end. All relative-slot polynomial changes are (j-i)L+(j^2-i^2)D and
  have magnitude <=12H. Circular positions and repeated constraints do
  not affect the argument. A whole short interval may be eroded away;
  then the finite bound can be vacuous without being false.
- **Hitting and diagonals:** F(x,0)=1. The normalized host diagonal is
  w/p; the occupied diagonal is aw/p. Nonzero differences have four
  distinct vertices because p>3. Counting holes gives the lower hitting
  bound; the exceptional masses contribute <=4/p to its upper bound.
- **First residual:** compare actual slot degrees to D_i only on Omega.
  Their discrepancy is supported on the eroded boundary. The mean-zero
  vector is B-a1_Omega with full-group mean zero; no arbitrary-factor
  orthogonality is asserted. This proves (M15)-(M16) in the stated scope.
- **Singular relative Gram:** no inverse Gram matrix is used in the new
  terminal or direct-cell proofs, so singularity does not create an
  omitted case. Old packet hypotheses still require their actual Gram.

## Direct increment and quantitative closure

- **Same cell:** random midpoint averaging gives a correlation at least
  kappa delta. The real cell discrepancies sum to zero; their positive
  mass is at least kappa delta/2. One of four cells has discrepancy at
  least kappa delta/8. Its density gain and retained occupied mass both
  follow from that single discrepancy. They are not selected separately.
- **Mass telescope:** mu_j=r_j a_j/a_(j+1), so the logarithmic loss is
  exactly log(a_final/a_initial)+sum log(1/r_j). A density gain alone
  would not justify the ledger.
- **Dyadic epochs:** the finite upper bounds are (L4), using actual
  infima of eta on each epoch. (L12) follows by a geometric sum over
  early epochs and an explicitly absorbed bound for the later epochs.
  The improved amplitude is a^(3/2)sqrt(ell)R, so the squared target is
  a^3 ell R^2, not a^(5/2)R.
- **Domain change:** the improved threshold uses the product domain
  (L10). Its size loss can exceed sqrt(log p); the old independent
  rank/size cutoffs cannot be silently retained. First-failure induction
  uses D*S=o(log p), D loglog p=o(log p), and S=o(log p).
- **Terminal errors:** (L10) gives mu_0>=p^(-1/50) and w>=p^(-1/100).
  The four errors in (L14) follow directly, including p^(-12/25) and
  p^(-97/100). Their convergence and H>=1 hold uniformly on the domain.
- **Transfer:** the elementary binomial/primorial proof supplies 3N<p<6N
  for sufficiently large N. Second differences of points in [N] have
  magnitude <2N<p, so cyclic exclusion transfers correctly.
- **Open input:** DIRECT-Q-P is not proved by any step of this audit.
  The terminal count and the conditional ledger do not imply its
  correlation premise. Consequently the target remains OPEN.

## Adversarial checks and scope

The generic pair-PSD shortcut was tested and refuted using a p=53
arithmetic kernel with exact negative rational quadratic form. Its
bounded function is non-Boolean; no target-density counterexample follows.
The independent sparse example proof works for 1/2<theta<2/3. Unaltered
Bernoulli sampling at epsilon/log p fails with the explicit probability
bound (L7), which does not exclude correlated AP-free constructions.

The old verifier rerun passed 21,465 finite checks without overwriting
historical outputs. The new verifier passes 1,642 finite checks, with
exact integer/rational and floating scopes separated. Small-prime error
bounds are often vacuous; no claim of asymptotic selection is based on
them. Maximum floating identity discrepancy is below 2.3e-16.
