from um import count

def test_only_um():
    assert count("um") == 1
    assert count("hello um world") == 1
    assert count("hello um world  um") == 2

def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("hello, um, world") == 1
    assert count("hello um: world  um?") == 2
    assert count("Thanks, um, regular expressions make sense now.") == 1

def test_caps_um():
    assert count("Um?") == 1
    assert count("hello, Um, world") == 1
    assert count("hello Um: world Um?") == 2

def test_um_beginning():
    assert count("Um?") == 1
    assert count("Um, world") == 1
    assert count("Um: world Um?") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

def test_um_in_between():
    assert count("yummy") == 0
    assert count("hello, mum, how are you") == 0
    assert count("hello, mum, how are you, um") == 1
