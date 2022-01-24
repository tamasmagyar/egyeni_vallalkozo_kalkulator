
def to_huf(amount: int) -> str:
    """
    Amount converted to huf with decimal marks, otherwise return 0 ft
    e.g. 1000 -> 1.000 ft
    """
    if amount == "-":
        return "-"
    try:

        decimal_marked = format(int(amount), ',d')
    except ValueError:
        return "0 ft"
    return f"{decimal_marked.replace(',', '.')} ft"

