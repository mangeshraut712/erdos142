import Lake
open Lake DSL

package «erdos142» where
  -- Package configuration options

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

@[default_target]
lean_lib «Erdos142» where
  -- Library configuration options
