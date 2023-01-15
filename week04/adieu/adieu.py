import inflect


def main():
    # connecting to inflect module
    p = inflect.engine()
    # creating an empty list to save names in
    names = []

    while True:
        try:
            user_input = str((input("Name: ").strip()))
            names.append(user_input)
        # catch CTRL + D to end the order session
        except EOFError:
            print(f"Adieu, adieu, to {p.join(names)}", end="\n")
            quit()


if __name__ == "__main__":
    main()
