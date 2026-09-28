"""
Numerical integration / ODE-solving toolkit.

This module starts EMPTY on purpose. You build it up yourself, project by
project, as the curriculum reaches the relevant stage:

  Stage 1 (s1p2)  -> finite-difference derivative estimators
  Stage 3 (s3p1)  -> euler_step(), rk4_step(), adaptive_rk45() -- built
                      from scratch and validated against SciPy, not
                      imported from it
  Stage 5 (s5p1)  -> a numba-accelerated variant of whichever integrator
                      profiling identifies as the bottleneck

Rule for this file specifically: every function you add here must already
have passed its own project's validation step (Stage 6's "Correctness by
hand" / "Convergence & error order" habits) before it gets promoted here.
This file is for functions you've already proven correct, not drafts.
"""
