from plates import is_valid


def test_startwith():
    # Vanity plates must start with at least two letters
    assert is_valid("1") == False
    assert is_valid("22") == False
    assert is_valid("AA") == True


def test_minmax():
    # Vanity plates must contain a minimum of two and a maximum of six letters
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABCDEF") == True


def test_numbers():
    assert is_valid("123456") == False
    assert is_valid("123ABC") == False
    assert is_valid("XYZ012") == False
    assert is_valid("AB12C3") == False
    assert is_valid("AB12CA") == False
    assert is_valid("ABC123") == True


def test_blockedsymbols():
    # Testing if any of the symbols from the invalid_symbols list pass
    assert is_valid("ABC?!-") == False
    assert is_valid(". 12[]") == False
    assert is_valid("/B^D3*") == False
