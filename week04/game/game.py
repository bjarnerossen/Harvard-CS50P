from random import randint


def main():

    while True:
        try:
            level = int(input("Level: ").strip())

            if level >= 1:
                random_num = randint(1, level)
                guess(random_num)
                break

        # Reprompt the user in case of a Type or Value error.
        except (TypeError, ValueError):
            continue

def guess(random_num):

    while True:
        user_input = int(input("Guess: ").strip())

        # Check if the guess is too big or too small.
        try:
            if user_input < random_num:
                print("Too small!")
            elif user_input > random_num:
                print("Too large!")
            else:
                print("Just right!")
                break

        # Reprompt the user in case of a Type or Value error.
        except (TypeError, ValueError):
            continue


if __name__ == "__main__":
    main()