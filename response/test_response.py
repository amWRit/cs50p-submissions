from response import validate

def test_valid_emails_with_one_domain():
    assert validate("hello@world.edu") == "Valid"
    assert validate("hello_mister@world.edu") == "Valid"

def test_valid_emails_with_multiple_domains():
    assert validate("hello@world.earth.edu") == "Valid"
    assert validate("hello@earth.universe.edu") == "Valid"

def test_no_at_symbol():
    assert validate("hello at world.edu") == "Invalid"
    assert validate("helloat world dot edu") == "Invalid"

def test_too_many_ats():
    assert validate("hello@@world.edu") == "Invalid"
    assert validate("hello@@@world.edu") == "Invalid"
