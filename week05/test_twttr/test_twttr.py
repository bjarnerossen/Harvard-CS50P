from twttr import shorten


def test_shorten():
    # All vowels should be removed in a string
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("twitter") == "twttr"
    assert shorten("CS50P") == "CS50P"
    assert shorten("Lovely day.") == "Lvly dy."
