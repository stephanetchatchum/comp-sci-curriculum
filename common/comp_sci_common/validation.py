"""
Small, honest validation helpers used across every stage.

The curriculum's own timeline names this progression explicitly:
  Stage 0-1: correctness by hand
  Stage 2-3: convergence & error order
  Stage 3-4: calibration against real data
  Stage 4-5: held-out validation
  Stage 5-6: uncertainty quantification

This module is where the *reusable* pieces of that progression live, so
that "did I check this properly?" is a function call, not a one-off block
you retype (and half-remember) in every project.

Start this file empty. Add to it only when a project needs a check you
expect to need again — e.g. after Stage 1-2 you'll likely want:

    def relative_error(computed, reference): ...
    def estimate_convergence_order(errors, step_sizes): ...

Do not pre-write these before you've hit the project that needs them —
writing validation code before you have a concrete case to validate
against is how you end up with helpers that quietly check the wrong
thing.
"""
