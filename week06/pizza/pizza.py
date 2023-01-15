from tabulate import tabulate
import csv
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        file_name = sys.argv[1]

    print(get_menu(file_name))


def get_menu(file_name):

    menu = []

    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
    except (FileNotFoundError):
        sys.exit("File does not exist.")

    return tabulate(menu, headers='firstrow', tablefmt='grid')


if __name__ == "__main__":
    main()
