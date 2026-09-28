# Rounding the Value(val) and thier uncertainties(unc)
def rounding(val, unc):
    if (f"{unc:.1g}".strip("-0.+e") or "0") == "1" or (f"{unc:.1g}".strip("-0.+e") or "0") == "2":
        n_unc = f"{unc:.2g}"
    else:
        n_unc = f"{unc:.1g}"

    # Checking the number of decimal places of the uncertainty and rounding the value according to it
    if "." in n_unc:
        n_val = round(val, len(n_unc.split(".")[1]))
    else:
        n_val = round(val, 0)

    n_unc = float(n_unc)

    return n_val, n_unc
