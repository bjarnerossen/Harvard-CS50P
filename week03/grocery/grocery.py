def main():
    add_to_list()


def add_to_list():
    d = {}

    while True:
        # prompt the user for their items
        try:
            item = input().strip().upper()
            if item in d:
                d[item] += 1
            # if the item is in the dict (d), increment count by 1
            else:
                d[item] = 1

        # catch CTRL + D to end the order session
        except EOFError:
            # sort grocery dict alphabetically
            for item in dict(sorted(d.items())):
                print(f"{d[item]} {item}")
            break


main()