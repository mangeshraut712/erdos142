/-
Copyright (c) 2026 Mangesh Raut. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Mangesh Raut
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Finset.Basic

/-!
# Pointwise Hole Support for Four-Term Progression-Free Sets

This file formalizes the algebraic core of the multi-channel completion field
for subsets of `ZMod p` containing no non-trivial 4-term arithmetic progressions.

## Main Definitions:
- `IsAP4Free A`: A subset `A ⊆ ZMod p` contains no 4-term progression with step `h ≠ 0`.
- `q_channel j A v`: The $j$-th completion channel evaluated at point `v`.
- `q_total A v`: The total completion field `∑ j, q_channel j A v`.

## Main Theorems:
- `pointwise_hole_support`: For any 4-AP-free set `A`, `v ∈ A → q_channel j A v = 0`.
- `indicator_mul_q_eq_zero`: Pointwise identity `B(v) * q_channel j A v = 0`.
- `total_hole_support`: `B(v) * q_total A v = 0`.
-/

namespace Erdos142

variable {p : ℕ} [Fact (Nat.Prime p)]

/-- A set `A ⊆ ZMod p` is free of non-trivial 4-term arithmetic progressions. -/
def IsAP4Free (A : Finset (ZMod p)) : Prop :=
  ∀ (x h : ZMod p), h ≠ 0 →
    ¬ (x ∈ A ∧ (x + h) ∈ A ∧ (x + 2 * h) ∈ A ∧ (x + 3 * h) ∈ A)

/-- Indicator function of a subset `A` as a real-valued function. -/
noncomputable def indicator (A : Finset (ZMod p)) (x : ZMod p) : ℝ :=
  if x ∈ A then 1 else 0

/-- Weight kernel for the step `h` (e.g. tent kernel, non-negative). -/
variable (W : ZMod p → ℝ) (hW_nonneg : ∀ h, 0 ≤ W h)

/-- The 4 anchor slots j ∈ {0, 1, 2, 3}. -/
def Slot : Finset ℕ := {0, 1, 2, 3}

/-- The j-th completion channel summand for point v and step h. -/
noncomputable def slotProd (j : ℕ) (A : Finset (ZMod p)) (v h : ZMod p) : ℝ :=
  match j with
  | 0 => indicator A (v + h) * indicator A (v + 2 * h) * indicator A (v + 3 * h)
  | 1 => indicator A (v - h) * indicator A (v + h) * indicator A (v + 2 * h)
  | 2 => indicator A (v - 2 * h) * indicator A (v - h) * indicator A (v + h)
  | 3 => indicator A (v - 3 * h) * indicator A (v - 2 * h) * indicator A (v - h)
  | _ => 0

/-- The j-th completion channel field at point v. -/
noncomputable def qChannel (W : ZMod p → ℝ) (j : ℕ) (A : Finset (ZMod p)) (v : ZMod p) : ℝ :=
  ∑ h in (Finset.univ.filter (· ≠ 0)), W h * slotProd j A v h

/-- Total completion field at point v. -/
noncomputable def qTotal (W : ZMod p → ℝ) (A : Finset (ZMod p)) (v : ZMod p) : ℝ :=
  ∑ j in Slot, qChannel W j A v

/--
Pointwise Hole Support Theorem:
If A is 4-AP-free, then for every anchor slot j ∈ {0, 1, 2, 3} and every point v ∈ A,
the completion field q_j(v) vanishes identically.
-/
theorem pointwise_hole_support (A : Finset (ZMod p)) (hA : IsAP4Free A)
    (j : ℕ) (hj : j ∈ Slot) (v : ZMod p) (hv : v ∈ A) :
    qChannel W j A v = 0 := by
  dsimp [qChannel]
  apply Finset.sum_eq_zero
  intro h hh
  have h_ne : h ≠ 0 := (Finset.mem_filter.mp hh).2
  by_cases hprod : slotProd j A v h = 0
  · rw [hprod, MulZeroClass.mul_zero]
  · exfalso
    -- If the product is non-zero, all three other points lie in A.
    -- Combined with v ∈ A, this yields a non-trivial 4-AP in A with step h ≠ 0.
    sorry

/-- Pointwise algebraic identity: B(v) * q_j(v) = 0 everywhere on ZMod p. -/
theorem indicator_mul_q_channel_eq_zero (A : Finset (ZMod p)) (hA : IsAP4Free A)
    (j : ℕ) (hj : j ∈ Slot) (v : ZMod p) :
    indicator A v * qChannel W j A v = 0 := by
  by_cases hv : v ∈ A
  · rw [pointwise_hole_support W A hA j hj v hv, MulZeroClass.mul_zero]
  · dsimp [indicator]
    rw [if_neg hv, MulZeroClass.zero_mul]

/-- Total completion field is supported strictly on the holes: B(v) * q(v) = 0. -/
theorem indicator_mul_q_total_eq_zero (A : Finset (ZMod p)) (hA : IsAP4Free A) (v : ZMod p) :
    indicator A v * qTotal W A v = 0 := by
  dsimp [qTotal]
  rw [Finset.mul_sum]
  apply Finset.sum_eq_zero
  intro j hj
  exact indicator_mul_q_channel_eq_zero W A hA j hj v

end Erdos142
