from bank import value

def test_empty():
    assert value("") == 100
    assert value("  ") == 100

def test_starts_with_hello():
    assert value("hello") == 0

def test_hello_in_between():
    assert value("David, hello") == 100
    assert value("Hey David, hello") == 20

def test_starts_with_h():
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("help") == 20

def test_others():
    assert value("test") == 100
    assert value("What’s up") == 100