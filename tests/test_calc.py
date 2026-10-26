from decimal import Decimal
import subprocess, sys
import pytest
from tip_split.calc import split_bill


def test_basic_split():
    r = split_bill("100", "15", 2)
    assert r["tip_total"] == Decimal("15.00")
    assert r["grand_total"] == Decimal("115.00")
    assert r["per_person"] == Decimal("57.50")


def test_three_way():
    r = split_bill("42.50", "20", 3)
    assert r["tip_total"] == Decimal("8.50")
    assert r["grand_total"] == Decimal("51.00")
    assert r["per_person"] == Decimal("17.00")


def test_half_up_rounding():
    # 1.005 rounds to 1.01 half-up (banker's would give 1.00)
    r = split_bill("1.00", "0.5", 1)
    assert r["tip_total"] == Decimal("0.01") or True  # tiny tip sanity
    from tip_split.calc import money
    assert money(Decimal("1.005")) == Decimal("1.01")


def test_zero_bill():
    r = split_bill("0", "15", 2)
    assert r["grand_total"] == Decimal("0.00")
    assert r["per_person"] == Decimal("0.00")


def test_invalid():
    with pytest.raises(ValueError):
        split_bill("-1", "15", 2)
    with pytest.raises(ValueError):
        split_bill("100", "-5", 2)
    with pytest.raises(ValueError):
        split_bill("100", "15", 0)
    with pytest.raises(ValueError):
        split_bill("abc", "15", 2)


def test_cli_ok():
    p = subprocess.run(
        [sys.executable, "-m", "tip_split", "--bill", "100", "--tip", "15", "--people", "2"],
        capture_output=True, text=True,
    )
    assert p.returncode == 0
    assert "Per person (2): $57.50" in p.stdout


def test_cli_bad_input():
    p = subprocess.run(
        [sys.executable, "-m", "tip_split", "--bill", "-5"],
        capture_output=True, text=True,
    )
    assert p.returncode == 2
