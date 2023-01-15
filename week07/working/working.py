import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(
            r"^([0-9]{1,2})( |:)([0-9]{0,2}) ?(AM|PM) to ([0-9]{1,2})( |:)([0-9]{0,2}) ?(AM|PM)",
            s,
        )
        parse = list(matches.groups(0))

    except (AttributeError, ValueError):
        raise (AttributeError, ValueError)
    try:
        if parse[2] == "":
            parse[2] = "00"
        if parse[6] == "":
            parse[6] = "00"

        if validate(parse):

            if int(parse[0]) == 12 and parse[3] == "AM":
                first_hour = 00
            elif int(parse[0]) == 12 and parse[3] == "PM":
                first_hour = 12

            elif parse[3] == "AM":
                first_hour = int(parse[0])
            else:
                first_hour = int(parse[0]) + 12

            if len(parse[2]) > 0:
                first_minutes = int(parse[2])
            else:
                first_minutes = 00

            if int(parse[4]) == 12 and parse[7] == "AM":
                second_hour = 00
            elif int(parse[4]) == 12 and parse[7] == "PM":
                second_hour = 12

            elif parse[7] == "AM":
                second_hour = int(parse[4])
            else:
                second_hour = int(parse[4]) + 12

            if len(parse[6]) > 0:
                second_minutes = int(parse[6])
            else:
                second_minutes = 00

        return f"{first_hour:02}:{first_minutes:02} to {second_hour:02}:{second_minutes:02}"

    except ValueError:
        raise ValueError


def validate(parse):
    try:
        if int(parse[0]) > 12 or int(parse[0]) < 0:
            raise ValueError
        if int(parse[4]) > 12 or int(parse[4]) < 0:
            raise ValueError
        if int(parse[2]) > 59 or int(parse[2]) < 0:
            raise ValueError
        if int(parse[6]) > 59 or int(parse[6]) < 0:
            raise ValueError

    except ValueError:
        raise ValueError

    return True


if __name__ == "__main__":
    main()
