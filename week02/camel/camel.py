def main():
    camel_case = input("camelCase: ").strip()
    print(f"snake_case: {convert_snake_case(camel_case)}")


def convert_snake_case(string):
    new_variable = ""
    for letter in string:
        if letter.isupper():
            new_variable += "_" + letter.lower()
        else:
            new_variable += letter

    return new_variable


main()
