import pytest
from fuel import convert, gauge

def test_integer():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("x/.")

def test_x_greater_y():
    with pytest.raises(ValueError):
        convert("4/3")
        convert("5/2")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_correct_ints():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_incorrect_ints():
    assert convert("2/5") != 45
    assert convert("1/5") != 30

def test_gauge_value():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(35) != "55%"
    assert gauge(45) != "45"

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(1) != "1%"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(99) != "99%"