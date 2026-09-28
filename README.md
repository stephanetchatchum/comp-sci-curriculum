# Computational Science Curriculum — Working Repo

This repo is where every project from the curriculum tracker actually gets
built. One repo, one Python environment, one growing toolbox — because in
real computational work you rarely start from zero on each project: you
reuse solvers, plotting helpers, and validation utilities you already trust.

## Why this structure (and not just 34 loose folders)

- **Stages are namespaces, not silos.** Stage 3's ODE solver becomes an
  import in Stage 4's PDE solver. Keeping them in one repo with a shared
  `common/` package makes that reuse natural instead of copy-pasted.
- **Every project folder has the same shape.** Once you've done one, you
  never have to think about *where something goes* again — only about the
  physics/math/code itself. Muscle memory for structure = more brain budget
  for the actual problem.
- **`tests/` exists from Project 1, not "eventually."** The curriculum's
  own timeline says reproducibility and correctness habits start at Stage
  0–1. A folder with no tests/ silently teaches you that testing is
  optional. It isn't.
- **`data/` and `results/` are separated from `src/`.** Code is what you
  version-control and reason about. Data and generated output are not —
  they're either fetched/regenerated, or explicitly checked in as small
  reference fixtures. This is the same reason you never `git add` a build
  artifact.

## Layout

```
comp-sci-curriculum/
├── common/                        # Shared, importable package (pip install -e .)
│   └── comp_sci_common/
│       ├── __init__.py
│       ├── integrators.py         # grows over Stage 1 → 3 → 5
│       ├── linalg.py              # grows over Stage 2
│       ├── validation.py          # convergence checks, analytic comparisons
│       └── plotting.py            # consistent matplotlib style across all projects
│
├── stage0-computational-foundations/
│   └── s0p1-quantities-units-uncertainty/   # <- one real project, created via scripts/new_project.py
│       ├── README.md               # problem statement, approach, validation plan, results
│       ├── src/
│       ├── tests/
│       ├── data/
│       └── results/
│
├── stage1-scientific-programming/
├── stage2-mathematical-computing/
├── stage3-numerical-methods-dynamical-modeling/
├── stage4-scientific-simulation-pdes/
├── stage5-advanced-computing-hpc/
├── stage6-research-preparation/
├── stage7-capstone/
│
├── docs/
│   └── LEARNING_LOG.md            # one entry per project: what broke, what you learned
├── environment/
│   ├── requirements-core.txt      # Stage 0-4 stack
│   └── requirements-hpc-ml.txt    # Stage 5+ extras (numba, scikit-learn, mpi4py...)
├── scripts/
│   └── new_project.py             # scaffolds a new project folder from the template
├── pyproject.toml                 # makes `common` importable + configures pytest
├── .gitignore
└── README.md
```

## One-time setup

See `environment/SETUP.md`.

## Starting a new project from the tracker

```bash
python scripts/new_project.py --stage 1 --id s1p2 \
  --title "Root-Finding and Numerical Differentiation Toolkit"
```

This clones `_project-template/` into the right stage folder, pre-fills the
README with the project id/title, and leaves `src/`, `tests/`, `data/`,
`results/` empty and ready.

## The one rule

Every project's README gets its **Validation** section filled in *before*
you consider the project done — a result you haven't checked against a
known answer, an analytic limit, or a convergence test isn't a result yet,
it's a guess with a plot attached.
