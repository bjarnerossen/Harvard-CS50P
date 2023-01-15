from datetime import datetime
from seasons import get_minutes, num_to_txt


def test_get_minutes():
    date = datetime.strptime('1998-06-20', '%Y-%m-%d')
    expected = 806400
    assert get_minutes(date) == expected


def test_num_to_txt():
    minutes = '806400'
    expected = 'Eight hundred six thousand, four hundred minutes'
    assert num_to_txt(minutes) == expected
