# tip-split

Tiny CLI to split a bill with tip. Stdlib only, no dependencies. Python ≥ 3.9.

## Run (no install)

```sh
git clone https://github.com/igorjpimenta/tip-split.git
cd tip-split
PYTHONPATH=src python3 -m tip_split --bill 100 --tip 15 --people 2
```

Expected output:

```
Bill: $100.00
Tip (15%): $15.00
Total: $115.00
Per person (2): $57.50
```

## Usage

```sh
PYTHONPATH=src python3 -m tip_split --bill 42.50 --tip 20 --people 3
PYTHONPATH=src python3 -m tip_split --help
```

- `--bill` (required): subtotal, e.g. `100` or `42.50`
- `--tip` (default `15`): tip percent, must be ≥ 0
- `--people` (default `1`): headcount, integer ≥ 1

Math uses `Decimal` rounded half-up to cents. Invalid input exits `2` with `error: …`.

## Test

```sh
PYTHONPATH=src python3 -m pytest -q
```

CI runs pytest on Python 3.9 and 3.12.
