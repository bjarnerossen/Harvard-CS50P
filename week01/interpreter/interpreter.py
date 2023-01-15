def main():
    x, y, z = input("Expression: ").strip().split(" ")
    print(f"{calculator(int(x), str(y), int(z)):.1f}")


def calculator(x, y, z):
    match y:
        case "+":
            return x +z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z
        case _:
            print("Please enter a valid operator.")



main()