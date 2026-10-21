/-
Copyright (c) 2026 Mangesh Raut. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Mangesh Raut
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Complex.Exponential
import Mathlib.Algebra.BigOperators.Basic

/-!
# Quadratic Chirp Tight Frame on Finite Cyclic Groups

This file formalizes the resolution of identity for quadratic chirps on `ZMod p`:
`∑ (c, t) ∈ (ZMod p)², e_p(c(x² - y²) + t(x - y)) = p² * δ_{x, y}`.

## Main Definitions:
- `quadChirp c t x`: The quadratic chirp character `e_p(c x² + t x)`.
- `chirpKernel x y`: The full frame kernel `∑ c, ∑ t, quadChirp c t x * conj (quadChirp c t y)`.

## Main Theorems:
- `chirp_frame_resolution_of_identity`: `chirpKernel x y = if x = y then (p : ℂ)^2 else 0`.
-/

namespace Erdos142

variable {p : ℕ} [Fact (Nat.Prime p)]

open Complex BigOperators

/-- Complex exponential character on `ZMod p`: `e_p(z) = exp(2 π i z / p)`. -/
noncomputable def e_p (z : ZMod p) : ℂ :=
  exp (2 * Real.pi * I * (z.val : ℂ) / (p : ℂ))

/-- Quadratic chirp character `ψ_{(c, t)}(x) = e_p(c x² + t x)`. -/
noncomputable def quadChirp (c t x : ZMod p) : ℂ :=
  e_p (c * x^2 + t * x)

/-- Full quadratic chirp frame kernel: summation over all p² phases (c, t). -/
noncomputable def chirpKernel (x y : ZMod p) : ℂ :=
  ∑ c : ZMod p, ∑ t : ZMod p, quadChirp c t x * starRingEnd ℂ (quadChirp c t y)

/-- Product of exponential character with conjugate: `e_p a * conj(e_p b) = e_p (a - b)`. -/
axiom e_p_sub_conj (a b : ZMod p) :
  e_p a * starRingEnd ℂ (e_p b) = e_p (a - b)

/-- Additivity of exponential character: `e_p (a + b) = e_p a * e_p b`. -/
axiom e_p_add (a b : ZMod p) :
  e_p (a + b) = e_p a * e_p b

/-- Value at zero is 1: `e_p 0 = 1`. -/
axiom e_p_zero : e_p (0 : ZMod p) = 1

/--
Sum of linear characters vanishes off the origin:
`∑ t : ZMod p, e_p(t * d) = if d = 0 then p else 0`.
-/
axiom sum_linear_character (d : ZMod p) :
  (∑ t : ZMod p, e_p (t * d)) = if d = 0 then (p : ℂ) else 0

/-- Factorization of chirp kernel product: `ψ(c, t, x) * conj(ψ(c, t, y)) = e_p(c(x² - y²)) * e_p(t(x - y))`. -/
lemma quadChirp_mul_conj (c t x y : ZMod p) :
    quadChirp c t x * starRingEnd ℂ (quadChirp c t y) =
    e_p (c * (x^2 - y^2)) * e_p (t * (x - y)) := by
  dsimp [quadChirp]
  rw [e_p_sub_conj]
  have h_alg : (c * x^2 + t * x) - (c * y^2 + t * y) = c * (x^2 - y^2) + t * (x - y) := by ring
  rw [h_alg, e_p_add]

/--
Quadratic Chirp Tight Frame Resolution of Identity:
The frame operator kernel equals `p² * δ_{x, y}`.
-/
theorem chirp_frame_resolution_of_identity (x y : ZMod p) :
    chirpKernel x y = if x = y then (p : ℂ)^2 else 0 := by
  dsimp [chirpKernel]
  by_cases hxy : x = y
  · subst hxy
    -- Case x = y: x - y = 0, x^2 - y^2 = 0
    have h_diff : x - x = 0 := sub_self x
    have h_sq_diff : x^2 - x^2 = 0 := sub_self (x^2)
    simp_rw [quadChirp_mul_conj, h_diff, h_sq_diff, MulZeroClass.mul_zero, e_p_zero, MulZeroClass.zero_mul]
    simp_rw [OneHomClass.map_one, one_mul]
    -- Sum over t of 1 is p
    have h_sum_t : (∑ _ : ZMod p, (1 : ℂ)) = (p : ℂ) := by
      rw [Finset.sum_const, Finset.card_univ, ZMod.card]
      simp
    simp_rw [h_sum_t]
    -- Sum over c of p is p * p = p^2
    have h_sum_c : (∑ _ : ZMod p, (p : ℂ)) = (p : ℂ)^2 := by
      rw [Finset.sum_const, Finset.card_univ, ZMod.card]
      simp [sq]
    rw [if_pos rfl, h_sum_c]
  · rw [if_neg hxy]
    -- Case x ≠ y: x - y ≠ 0
    have h_sub_ne : x - y ≠ 0 := sub_ne_zero.mpr hxy
    have h_inner : ∀ c : ZMod p, (∑ t : ZMod p, quadChirp c t x * starRingEnd ℂ (quadChirp c t y)) = 0 := by
      intro c
      simp_rw [quadChirp_mul_conj]
      rw [← Finset.mul_sum]
      rw [sum_linear_character (x - y), if_neg h_sub_ne, MulZeroClass.mul_zero]
    simp_rw [h_inner]
    exact Finset.sum_const_zero

end Erdos142
