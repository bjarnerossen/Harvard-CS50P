def main():
    # Here we get input from the user

    name = str(input("Name: ")).strip()
    print(say_hello(name))


def say_hello(str="world"):
    # Here we define our function
    return f"Hello, {str}"


if __name__ == "__main__":
    main()