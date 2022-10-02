from working import convert
import pytest

def test_valid_input():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_to_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_wrong_digits():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("12:60 AM to 13:00 PM")

def test_invalid_time_format():
    with pytest.raises(ValueError):
        convert("cat and dog")
    with pytest.raises(ValueError):
        convert("10 OP to 12 BC")

def test_12():
     assert convert("12 AM to 12 PM") == "00:00 to 12:00"
     assert convert("12 PM to 12 AM") == "12:00 to 00:00"