def main():
    tank = calc_fuel("Fraction: ")


def calc_fuel(prompt):
    while True:
        tank = input(prompt).strip()
        try:
            x, y = tank.split("/", 1)
            if int(x) <= int(y) and int(y) != 0:
                fuel_gauge = (int(x)/int(y)) * 100
                if fuel_gauge >= 99:
                    print("F")
                    break
                elif fuel_gauge < 99 and fuel_gauge > 1:
                    print(f"{fuel_gauge:.0f}%")
                    break
                else:
                    print("E")
                    break

        # Catching the exceptions
        except (ValueError, ZeroDivisionError):
            pass
        else:
            pass


main()