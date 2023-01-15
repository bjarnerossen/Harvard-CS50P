from jar import Jar
import pytest

def main():
    test_deposit_1()
    test_str()
    test_withdraw_1()
    test_withdraw_error()


def test_deposit_1():

    jar = Jar()
    deposit = 8
    expected = None

    assert jar.deposit(deposit) == expected

def test_str():

    jar = Jar()
    jar.deposit(8)
    expected = "🍪🍪🍪🍪🍪🍪🍪🍪"

    assert jar.__str__() == expected

def test_withdraw_1():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(10)

    expected = 2

    assert jar.cookies == expected

def test_withdraw_error():

    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(13)
        jar.withdraw(15)

def test_deposit_error():

    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(15)

if __name__ == "__main__":
    main()
