invalid_symbols = [
    " ",
    ".",
    "?",
    "!",
    ",",
    ":",
    ";",
    "(",
    ")",
    "[",
    "]",
    "'",
    "-",
    '"',
    "/",
    "\\",
    "`",
    "@",
    "#",
    "*",
]


def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Initialising variables for the plate and numeric count
    plate_name = ""
    num_count = 0

    # Validating the users input
    # If the string contains more or equal to two char and less or equal to six, continue.
    if len(s) >= 2 and len(s) <= 6:
        # If the first and second char is part of the alphabet, continue.
        if s[0].isalpha() and s[1].isalpha():
            # Loop through each character in string s
            for char in s:
                # Check for each character if any of them is part of the list with invalid symbols
                if char not in invalid_symbols:
                    # Check for the first number in string and make sure it is not 0, increment numberic count
                    if char.isnumeric() and num_count == 0 and char != "0":
                        num_count += 1
                        plate_name += char
                    elif char.isnumeric() and num_count > 0:
                        num_count += 1
                        plate_name += char
                    elif char.isalpha() and num_count < 1:
                        plate_name += char

    if plate_name == s:
        return True
    else:
        return False


main()