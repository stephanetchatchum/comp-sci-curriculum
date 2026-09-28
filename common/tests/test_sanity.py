"""
If this fails, `pip install -e .` did not work (or you forgot to activate
the venv) — fix that before anything else, since every project's tests
depend on `comp_sci_common` being importable.
"""
import comp_sci_common


def test_package_imports():
    assert comp_sci_common is not None
