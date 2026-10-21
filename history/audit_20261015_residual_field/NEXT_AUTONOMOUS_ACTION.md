# Next Autonomous Action — 14 October 2026

## Highest-Priority Mathematical Target

With the \(W_\Gamma \lesssim a^4\) denominator barrier in Branch I eliminated (`RESIDUAL_FIELD_AMPLIFICATION_20261014.md` Theorem 2: any packet \(\Gamma\) capturing a \(\theta\)-fraction of \(S_{\ge \gamma a}(\lambda)\) automatically satisfies \(\sum_{\xi\in\Gamma}|c_\xi|^2 \ge \frac{\theta^2\gamma^2 a^2}{|\Gamma|w^2}\) and \(\max_{\xi\in\Gamma}|c_\xi|^2 \ge \frac{\theta^2\gamma^2 a^2}{|\Gamma|^2 w^2}\)) and the small-shell regime \(|\Gamma_j| \le c_2 a^{-3/4}\ell(a)^{-7/2}\) in Branch IIa settled (`Theorem 3`), the next autonomous action is to attack `Sublemma 2A''` and `Sublemma 2B''` in `OPEN_LEMMAS.md`:

1. **In `Sublemma 2A''` (Branch I Numerator Capture)**:
   Bound the effective Fourier bandwidth of \(\phi_\lambda^{\ge a/2} = 1_\Omega 1_{g\ge a/2} q_\lambda\) (or \(\phi_\lambda^{(1)} = 1_\Omega g q_\lambda\)) against \(u\) by exploiting the exact convolution orthogonality \(\widehat{B} * \widehat{q_E} = \widehat{B} * \widehat{q_M} = 0\) and \(\|K_u^{(3)}\|_2^2 \le 4U\|u\|_{U^3}^4\), showing that a packet \(\Gamma\) of size \(\le M(a)\) captures a positive fraction \(\theta\) of \(S_{\ge a/2}(\lambda)\).
2. **In `Sublemma 2B''` (Branch II Large-Shell Exclusion & \(K_u^{(3)}\) Capture)**:
   Rule out flat dyadic shells \(\Gamma_j \subset \operatorname{Spec}(u)\) of size \(s \in [c_2 a^{-3/4}\ell(a)^{-7/2}, O(a^{-3})]\) carrying \(\sum_{\xi\in\Gamma_j}|c_\xi|^2 \gtrsim a^2 s^{1/3}\ell(a)^{-2/3} \gtrsim a^{7/4}\) by combining Riesz-product / additive-energy bounds on \(\Gamma_j\) with \(u^2 = (1-2g)u + g(1-g)\) and \(B q_E = B q_M = 0\).
