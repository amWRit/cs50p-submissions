from numb3rs import validate

def test_invalid_format():
    assert validate("127.0.0") == False
    assert validate("255.255") == False
    assert validate("127") == False
    assert validate("75.456.76.65") == False

def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

def test_invalid_ip():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_not_numbers():
    assert validate("cat") == False