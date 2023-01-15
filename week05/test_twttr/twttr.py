def main():
    word = str(input("Input: ").strip())
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    new_string = ""
    for letter in word:
        if letter not in vowels:
            new_string += letter
    return new_string


if __name__ == "__main__":
    main()
