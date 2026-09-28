"""
One shared matplotlib style so that project #1 and project #34 look like
they came from the same scientist, not from 34 different tutorials.

Usage, from any project's src/ file:

    from comp_sci_common.plotting import use_house_style
    use_house_style()

Fill in `use_house_style()` the first time a plot's default look genuinely
bothers you (Stage 0 project 2, probably) -- don't over-engineer this
before you have an actual opinion about fonts/DPI/grid style formed from
looking at real output.
"""

import matplotlib.pyplot as plt


def use_house_style() -> None:
    """Apply the shared plot style. Currently a placeholder — customize me."""
    plt.rcParams.update({
        "figure.dpi": 110,
        "axes.grid": True,
        "grid.alpha": 0.3,
    })
