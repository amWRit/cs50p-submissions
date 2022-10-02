from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(4)
    assert jar.capacity == 4


def test_str():
    jar = Jar(0)
    assert str(jar) == ""
    jar = Jar(1)
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar = Jar(12)
    jar.deposit(12)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    ...

def test_deposit():
    jar = Jar(5)
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    ...


def test_withdraw():
    jar = Jar(4)
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪"
    ...

def test_bad_deposit():
    jar = Jar(4)
    with pytest.raises(ValueError):
        jar.deposit(5)
    jar = Jar(12)
    with pytest.raises(ValueError):
        jar.deposit(14)

def test_bad_withdrawal():
    jar = Jar(4)
    jar.deposit(4mkdir \)
    with pytest.raises(ValueError):
        jar.withdraw(5)
    jar = Jar(12)
    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.withdraw(14)