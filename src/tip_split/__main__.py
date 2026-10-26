"""Entry point: `python -m tip_split` (skeleton — full CLI lands in PR2)."""
import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="tip-split", description="Split a bill with tip.")
    p.add_argument("--version", action="version", version="tip-split 0.1.0")
    return p


def main(argv=None) -> int:
    parser = build_parser()
    parser.parse_args(argv)
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
