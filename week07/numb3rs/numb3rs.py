import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        matches = re.search(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$", ip)
        split = matches.group(0).split(".")

        for num in split:
            if int(num) > 255:
                return False
        return True

    except AttributeError:
        return False

    except TypeError:
        return False


if __name__ == "__main__":
    main()
