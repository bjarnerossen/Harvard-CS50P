from random import randint


def main():
    # prompt user for level and assign to variable level
    level = get_level()
    # initialize score to keep track of score throughout game
    score = 0

    for _ in range(5):
        while True:
            try:
                x = generate_integer(level)
                y = generate_integer(level)
                answer = x + y

                for _ in range(3):
                    print(f"{x} + {y} =", end="")
                    response = input("")
                    if int(response) == answer:
                        score = score + 1
                        break
                    else:
                        print("EEE")
                        print(f"{x} + {y} = ", end="")
                        response = input("")
                        print(f"{x} + {y} = {x+y}")
                break

            except ValueError:
                pass

    print(f"score: {score}")


def get_level():
    while True:
        try:
            level = input("Level: ")

            if int(level) >= 1 and int(level) <= 3:
                break

        except ValueError:
            pass
    return int(level)


def generate_integer(level):
    if int(level) == 1:
        return randint(0, 9)

    elif int(level) == 2:
        return randint(10, 99)

    else:
        return randint(100, 999)


if __name__ == "__main__":
    main()