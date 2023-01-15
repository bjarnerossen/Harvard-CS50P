import sys


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments.")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments.")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file.")
    else:
        path = sys.argv[1]

    print(f"Number of line in file: {line_counter(path)} lines")


def line_counter(path):
    lines = []
    counter = 0

    try:
        with open(path) as file:
            for line in file:
                lines.append(line.lstrip())
    except FileNotFoundError:
        sys.exit("File does not exist.")

    for line in lines:
        if not line.startswith("#") and len(line) > 0:
            counter += 1

    return counter


if __name__ == "__main__":
    main()
