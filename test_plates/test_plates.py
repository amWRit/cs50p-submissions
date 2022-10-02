from plates import is_valid

def test_plate_length():
    assert is_valid("C") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("HELLO") == True
    assert is_valid("CS50") == True

def test_alpha_numeric():
    assert is_valid("HE123") == True
    assert is_valid("H,123") == False
    assert is_valid(" HE12 ") == False
    assert is_valid("HE12/3 ") == False
    assert is_valid("HE2.3 ") == False

def test_starting_chars():
    assert is_valid("C123") == False
    assert is_valid("CH123") == True
    assert is_valid("CHA123") == True

def test_starting_zero():
    assert is_valid("CS012") == False
    assert is_valid("CS12") == True

def test_valid_trailing_digits():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True