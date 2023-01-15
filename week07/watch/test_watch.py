from watch import parse


def main():
    test_watch1()
    test_watch2()
    test_watch3()
    test_watch4()
    test_watch5()


def test_watch1():
    html = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    expected = 'https://youtu.be/xvFZjo5PgG0'

    try:
        assert parse(html) == expected
    except AssertionError:
        print(f"Youtube link in '{html}' was not {expected}.")


def test_watch2():
    html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    expected = 'https://youtu.be/xvFZjo5PgG0'

    try:
        assert parse(html) == expected
    except AssertionError:
        print(f"Youtube link in '{html}' was not {expected}.")


def test_watch3():
    html = '<iframe width="560" height="315" src="http://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    expected = 'https://youtu.be/xvFZjo5PgG0'

    try:
        assert parse(html) == expected
    except AssertionError:
        print(f"Youtube link in '{html}' was not {expected}.")


def test_watch4():
    html = '<iframe width="560" height="315" sr="http://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    expected = None

    try:
        assert parse(html) == expected
    except AssertionError:
        print(f"Youtube link in '{html}' was not {expected}.")


def test_watch5():
    html = '<iframe width="560" height="315" src="youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    expected = None

    try:
        assert parse(html) == expected
    except AssertionError:
        print(f"Youtube link in '{html}' was not {expected}.")


if __name__ == "__main__":
    main()
