from bank import value


def test_value():
    assert value("hello") == 0
    assert value("hey, hi, how are you?") == 20
    assert value("what's up!") == 100
    assert value("123123") == 100
    assert value("HELLO") == 0
