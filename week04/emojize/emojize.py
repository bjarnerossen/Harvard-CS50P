# Importing package with emoji codes
import emoji


def main():
    print(emojize("Input: "))


def emojize(prompt):
    # Prompting the user for a string and convert into emoji
    user_input = str(emoji.emojize(input(prompt)))
    return f"Output: {user_input}"


if __name__ == "__main__":
    main()
