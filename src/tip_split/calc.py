"""Core bill-split math using Decimal, rounded half-up to cents."""
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

CENT = Decimal("0.01")


def _to_decimal(value) -> Decimal:
    try:
        d = Decimal(str(value))
    except (InvalidOperation, ValueError) as e:
        raise ValueError(f"not a number: {value!r}") from e
    return d


def money(d: Decimal) -> Decimal:
    return d.quantize(CENT, rounding=ROUND_HALF_UP)


def split_bill(bill, tip_pct=15, people=1) -> dict:
    """Return {bill, tip_pct, people, tip_total, grand_total, per_person} as Decimals (+ints)."""
    b = _to_decimal(bill)
    t = _to_decimal(tip_pct)
    if not b.is_finite() or not t.is_finite():
        raise ValueError("bill and tip_pct must be finite numbers")
    try:
        pd = Decimal(str(people))
    except Exception as e:
        raise ValueError(f"people must be an integer >= 1, got {people!r}") from e
    if not pd.is_finite() or pd % 1 != 0:
        raise ValueError(f"people must be an integer >= 1, got {people!r}")
    n = int(pd)
    if b < 0:
        raise ValueError("bill must be >= 0")
    if t < 0:
        raise ValueError("tip_pct must be >= 0")
    if n < 1:
        raise ValueError("people must be >= 1")
    tip_total = money(b * t / Decimal("100"))
    grand_total = money(b + tip_total)
    per_person = money(grand_total / n)
    return {
        "bill": money(b),
        "tip_pct": t,
        "people": n,
        "tip_total": tip_total,
        "grand_total": grand_total,
        "per_person": per_person,
    }
