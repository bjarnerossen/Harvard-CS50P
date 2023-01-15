from numb3rs import validate


def main():
    test_validade_ip1()
    test_validade_ip2()
    test_validade_ip3()
    test_validade_ip4()
    test_validade_ip5()
    test_validade_ip6()


def test_validade_ip1():
    ip = '255.1.9.85'
    expected = True

    try:
        assert validate(ip) == expected
    except AssertionError:
        print(f"Validate IP '{ip}' was not {expected}.")


def test_validade_ip2():
    ip = '900.13.92.85'
    expected = False

    try:
        assert validate(ip) == expected
    except AssertionError:
        print(f"Validate IP '{ip}' was not {expected}.")


def test_validade_ip3():
    ip = '90.13.92.a85'
    expected = False

    try:
        assert validate(ip) == expected
    except AssertionError:
        print(f"Validate IP '{ip}' was not {expected}.")


def test_validade_ip4():
    ip = '90.13.92.94.1'
    expected = False

    try:
        assert validate(ip) == expected
    except AssertionError:
        print(f"Validate IP '{ip}' was not {expected}.")


def test_validade_ip5():
    ip = '90.13.92'
    expected = False

    try:
        assert validate(ip) == expected
    except AssertionError:
        print(f"Validate IP '{ip}' was not {expected}.")


def test_validade_ip6():
    ip = '90.13.92.90.'
    expected = False

    try:
        assert validate(ip) == expected
    except AssertionError:
        print(f"Validate IP '{ip}' was not {expected}.")


if __name__ == "__main__":
    main()
