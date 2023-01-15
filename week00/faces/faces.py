def main():
    user_input = input().strip()
    print(convert(user_input))

def convert(str):
    converted_emoticon = str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_emoticon

main()