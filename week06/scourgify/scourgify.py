import csv
import os
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit(f"Could not read {sys.argv[1]}")
    elif ".csv" not in sys.argv[1] and sys.argv[2]:
        sys.exit("Not a CSV file")
    else:
        scourgify(sys.argv[1], sys.argv[2])


def scourgify(input_file, output_file):

    with open(input_file) as csv_read_file:
        column = csv.DictReader(csv_read_file)

        with open(output_file, "w") as csv_write_file:
            fieldnames = ["first", "last", "house"]
            column_writer = csv.DictWriter(
                csv_write_file, fieldnames=fieldnames)

            # Write header to the output file
            column_writer.writeheader()

            # Write the CSV data to the output file
            for row in column:
                last, first = row["name"].split(",")
                house = row["house"]

                column_writer.writerow(
                    {"first": first.strip(), "last": last, "house": house}
                )


if __name__ == "__main__":
    main()
