menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = calc_price("Item: ")


def calc_price(prompt):
    total = 0
    while True:
        # Make user input case insensitive and print total
        try:
            order = input(prompt).strip().title()
            if order in menu:
                total += menu[order]
                print(f"${total:.2f}")

        # Catch CTRL + D to end the order session
        except (EOFError, KeyError):
            print("", end="\n")
            break

main()
