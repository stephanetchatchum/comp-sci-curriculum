# One-time environment setup

Do this once, from the repo root (`comp-sci-curriculum/`).

## 1. Install Git and Python 3.10+

- Check what you already have: `git --version` and `python3 --version`
  (or `python --version` on Windows).
- If missing: Git from https://git-scm.com, Python from https://python.org
  (tick "Add to PATH" on Windows).

## 2. Create and activate a virtual environment

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

You'll know it worked because your shell prompt gets a `(.venv)` prefix.
Do this every time you open a new terminal to work on the curriculum —
forgetting it is the #1 cause of "but it worked yesterday."

## 3. Install the core dependencies + the local `common` package

```bash
pip install --upgrade pip
pip install -r environment/requirements-core.txt
pip install -e .
```

`pip install -e .` is the important one: it installs `common/` in
*editable* mode, so `import comp_sci_common` works from any stage folder,
and edits to `common/` are picked up immediately without reinstalling.

## 4. Initialize Git

```bash
git init
git add .
git commit -m "Initial repo structure"
```

From here on: **one commit per meaningful step**, not one commit per
project. "Bisection method passing on textbook example," "Newton's method
diverging case documented," "Root-finding toolkit: README + validation
section done" are three separate, good commits. A commit history that
reads like a lab notebook is worth more to future-you than a clean-looking
final diff.

## 5. Verify everything works

```bash
pytest
```

You should see `0 passed` (or a small number from `common/tests/`) with no
import errors. That's the whole point of this check — not that you have
tests yet, but that the *machinery* for running them is wired correctly
before you need it under pressure at 11pm before a deadline.

## 6. When you reach Stage 5

```bash
pip install -r environment/requirements-hpc-ml.txt
```

If `rasterio`, `GDAL`, or `Cartopy` fail to build via pip (very common —
they wrap system C libraries), install
[Miniforge](https://github.com/conda-forge/miniforge) and use
`conda install -c conda-forge <package>` for those specific ones only;
keep everything else in the pip-managed `.venv`.
