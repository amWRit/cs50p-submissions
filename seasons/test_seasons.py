from seasons import validate, number_of_minutes, minutes_into_words
import pytest

def test_valid_format():
    assert validate("1999-01-31") == True
    assert validate("2000-12-12") == True
    assert validate("2019-09-26") == True

def test_invalid_format():
    with pytest.raises(SystemExit):
        validate("201-09-26")
    with pytest.raises(SystemExit):
        validate("2011/09/26")
    with pytest.raises(SystemExit):
        validate("January 9, 1999")
    with pytest.raises(SystemExit):
        validate("2011-09-33")
    with pytest.raises(SystemExit):
        validate("2011-19-04")

def test_minutes_conversion():
    assert number_of_minutes("1999-01-01", True) == 525600
    assert number_of_minutes("1999-12-31", True) == 1440
    assert number_of_minutes("1998-01-01", True) == 1051200

def test_words_conversion():
    assert minutes_into_words("525600") == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_into_words("1440") == "One thousand, four hundred forty minutes"
    assert minutes_into_words("1051200") == "One million, fifty-one thousand, two hundred minutes"