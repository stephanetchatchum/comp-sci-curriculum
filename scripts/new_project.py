#!/usr/bin/env python3
"""
Scaffold a new curriculum project folder from the shared template.

Usage:
    python scripts/new_project.py --stage 1 --id s1p2 \
        --title "Root-Finding and Numerical Differentiation Toolkit"

Creates:
    stage1-scientific-programming/s1p2-root-finding-and-numerical-differentiation-toolkit/
        README.md   (pre-filled from scripts/templates/README_TEMPLATE.md)
        src/__init__.py
        tests/__init__.py
        data/.gitkeep
        results/.gitkeep

Deliberately does NOT write any solution code, test logic, or approach —
those come from you. This only saves you from retyping the same folder
skeleton 34 times.
"""
import argparse
import datetime
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

STAGE_NAMES = {
    0: ("stage0-computational-foundations", "Computational Foundations"),
    1: ("stage1-scientific-programming", "Scientific Programming"),
    2: ("stage2-mathematical-computing", "Mathematical Computing"),
    3: ("stage3-numerical-methods-dynamical-modeling", "Numerical Methods & Dynamical Modeling"),
    4: ("stage4-scientific-simulation-pdes", "Scientific Simulation — PDEs & Complex Systems"),
    5: ("stage5-advanced-computing-hpc", "Advanced Computational Science & HPC"),
    6: ("stage6-research-preparation", "Research Preparation"),
    7: ("stage7-capstone", "Capstone"),
}


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", type=int, required=True, choices=STAGE_NAMES.keys())
    parser.add_argument("--id", required=True, help="Project id from the tracker, e.g. s1p2")
    parser.add_argument("--title", required=True, help="Project title from the tracker")
    args = parser.parse_args()

    stage_dir_name, stage_display_name = STAGE_NAMES[args.stage]
    stage_dir = REPO_ROOT / stage_dir_name
    template_dir = stage_dir / "_project-template"

    if not template_dir.exists():
        sys.exit(f"Template folder not found: {template_dir}")

    folder_name = f"{args.id}-{slugify(args.title)}"
    dest_dir = stage_dir / folder_name

    if dest_dir.exists():
        sys.exit(f"Project folder already exists: {dest_dir}")

    shutil.copytree(template_dir, dest_dir)

    readme_template = (REPO_ROOT / "scripts" / "templates" / "README_TEMPLATE.md").read_text()
    filled = (
        readme_template
        .replace("{PROJECT_ID}", args.id)
        .replace("{PROJECT_TITLE}", args.title)
        .replace("{STAGE_NAME}", stage_display_name)
        .replace("{DATE}", datetime.date.today().isoformat())
    )
    (dest_dir / "README.md").write_text(filled)

    print(f"Created {dest_dir.relative_to(REPO_ROOT)}")
    print("Next: fill in the Problem statement and Approach sections before writing any code.")


if __name__ == "__main__":
    main()
