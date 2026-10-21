# Open Lemmas and Sharp Remaining Obstructions — 14 October 2026

All downstream reductions from `COLLECTIVE-WSELECT` (or `WSELECT` / `SELECT` / `H`) to \(r_4(N)=o(N/\log N)\) are 100% proved and verified. Moreover, in Cycle 5 (`RESIDUAL_FIELD_AMPLIFICATION_20261014.md`), Theorem 2 **eliminated the \(W_\Gamma \lesssim a^4\) denominator barrier** in Branch I (via the pointwise Fourier cap \(|\widehat{\phi_\lambda^{\ge \gamma a}}(\xi)| \le \frac{w}{\gamma a}S_{\ge \gamma a}(\lambda)\)), and Theorem 3 proved that in Branch IIa (\(|T_u+S_u|\ge c_1 a^3\)) any winning dyadic shell \(\Gamma_j\) of size \(s \le c_2 a^{-3/4}\ell(a)^{-7/2}\) **already satisfies single-character `SELECT`**.

## 1. Primary Sufficient Open Lemma (`COLLECTIVE-WSELECT`)

Let \(R(a) = \log\log(e^2/a)\) and \(\ell(a) = \log(2/a)\).
**Conjecture (`COLLECTIVE-WSELECT`, proved sufficient in `THREE_BRANCH_AMPLIFICATION_20261014.md` Theorem 4)**:
For every \(\epsilon>0\) there exist \(\zeta\in(0,1/4]\), \(c>0\), and \(p_0(\epsilon)\) such that for every prime \(p\ge p_0(\epsilon)\), every narrow coordinate \(H\)-window \(\Omega\subset\mathbb{Z}_p\) (\(1\le d\le\sqrt{\log p}\), \(n\ge p\exp(-\sqrt{\log p})\)), every cyclically 4-AP-free \(A\subset\Omega\) with \(\epsilon/(2\log n)\le a\le 4/5\), and every intermediate quarter-arc factor \(F\) of added rank \(< M(a) := \lceil (\zeta/(\kappa^2 c))a^{-1/4}/\ell(a)\rceil\) satisfying \(\operatorname{Var}_\Omega(g) < \zeta a^{9/4} R(a)/\ell(a)\), there exists a nonempty character packet \(\Gamma\subset\mathbb{Z}_p\setminus\{0\}\) of size \(1\le |\Gamma|\le M(a)-\operatorname{rank}(F)\) such that
\[
c_\Gamma^* \bigl(\kappa^2 G_\Gamma + (1-\kappa^2)I_{|\Gamma|}\bigr)^{-1} c_\Gamma \ge c\,|\Gamma|\,a^{5/2} R(a).
\]

## 2. Sharp Remaining Sublemmas After Cycle 5 (`RESIDUAL_FIELD_AMPLIFICATION_20261014.md`)

### Sublemma 2A'' (Branch I — Packet Capture of \(S_{\ge a/2}(\lambda)\) without Denominator Condition)
By `RESIDUAL_FIELD_AMPLIFICATION_20261014.md` Theorem 2 (`(2.5)`), the denominator condition on \(W_\Gamma\) is now **redundant**:
- **Remaining step**: In Branch I (\(S_{\ge a/2}(1,1) \ge \frac{1}{4}a^4\)), prove that there exists a frequency packet \(\Gamma \subset \mathbb{Z}_p\setminus\{0\}\) of size \(|\Gamma| \le M(a) \sim a^{-1/4}/\ell(a)\) capturing a constant fraction \(\theta > 0\) of the pairing:
  \[
  \Bigl|\sum_{\xi\in\Gamma} \overline{c_\xi}\,\widehat{\phi_\lambda^{\ge a/2}}(\xi)\Bigr| \ge \theta\,S_{\ge a/2}(\lambda)
  \quad\text{or}\quad
  \Bigl|\sum_{\xi\in\Gamma} \overline{c_\xi}\,\widehat{\phi_\lambda^{(1)}}(\xi)\Bigr| \ge \theta\,S^{(2)}(\lambda).
  \]
  Once this single numerator capture holds, Theorem 2 (`(2.5)`) automatically yields \(\sum_{\xi\in\Gamma}|c_\xi|^2 \ge \frac{\theta^2 a^2}{4|\Gamma|w^2}\) and \(\max_{\xi\in\Gamma}|c_\xi|^2 \ge \frac{\theta^2 a^2}{4|\Gamma|^2 w^2}\)!

### Sublemma 2B'' (Branch II — Excluding the Flat Large-Shell Case \(s > c_2 a^{-3/4}\ell(a)^{-7/2}\) and Controlling \(K_u^{(3)}\))
By `RESIDUAL_FIELD_AMPLIFICATION_20261014.md` Theorem 3 (`(3.2)`), in Branch IIa (\(|T_u+S_u|\ge c_1 a^3\)) any winning dyadic shell \(\Gamma_j\) of size \(s = |\Gamma_j| \le c_2 a^{-3/4}\ell(a)^{-7/2}\) already gives single-character `SELECT` (\(\min_{\xi\in\Gamma_j}|c_\xi|^2 \ge c a^{5/2}\ell(a)\)).
- **Remaining step**:
  1. Rule out the flat large-shell regime \(s = |\Gamma_j| \in [c_2 a^{-3/4}\ell(a)^{-7/2},\ O(a^{-3})]\) (where \(\sum_{\xi\in\Gamma_j}|c_\xi|^2 \gtrsim a^2 s^{1/3}\ell(a)^{-2/3} \gtrsim a^{7/4}\)) using conditional Booleanity \(u^2 = (1-2g)u + g(1-g)\) and \(B q_E = B q_M = 0\).
  2. In Branch IIb (\(\langle \frac{1}{2}u + h, K_u^{(3)}\rangle_p \ge \frac{1}{4}a^4\)), capture a constant fraction of the pairing with \(K_u^{(3)}\) on a packet \(\Gamma\) of size \(\le M(a)\).
