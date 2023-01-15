def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = str(s)

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

    final_plate = ""
    num_count = 0
    if len(s) <= 6 and len(s) >= 2:
        if s[0].isalpha() and s[1].isalpha():
            for char in s:
                if char not in invalid_symbols:
                    if char.isnumeric() and char != "0" and num_count == 0:
                        num_count += 1
                        final_plate += char
                    elif char.isnumeric() and num_count > 0:
                        num_count += 1
                        final_plate += char
                    elif char.isalpha() and num_count < 1:
                        final_plate += char

    else:
        return False

    if final_plate == s:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
