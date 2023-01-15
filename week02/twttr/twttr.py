def main():
    user_input = input("Input: ").strip()
    print(f"Output: {shorten(user_input)}")


def shorten(str):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    word = ""
    for c in str:
        if c not in vowels:
            word += c
    return word


main()
