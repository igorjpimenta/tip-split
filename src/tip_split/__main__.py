"""CLI: `python -m tip_split --bill 100 --tip 15 --people 2`."""
import argparse
from .calc import split_bill

VERSION = "0.1.0"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="tip-split", description="Split a bill with tip.")
    p.add_argument("--bill", required=True, help="Bill subtotal, e.g. 100 or 42.50")
    p.add_argument("--tip", default="15", help="Tip percent (default: 15)")
    p.add_argument("--people", default="1", help="Number of people (default: 1)")
    p.add_argument("--version", action="version", version=f"tip-split {VERSION}")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        r = split_bill(args.bill, args.tip, args.people)
    except ValueError as e:
        print(f"error: {e}")
        return 2
    print(f"Bill: ${r['bill']:.2f}")
    print(f"Tip ({r['tip_pct']}%): ${r['tip_total']:.2f}")
    print(f"Total: ${r['grand_total']:.2f}")
    print(f"Per person ({r['people']}): ${r['per_person']:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
