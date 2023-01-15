import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matches = re.search(
            r'^<iframe.+src="http(s)?://(www\.)?youtube.com/embed/(\w+)"', s)
        if matches:
            return f"https://youtu.be/" + matches.group(3)

    except AttributeError:
        print("No matches are found")
        return None


if __name__ == "__main__":
    main()
