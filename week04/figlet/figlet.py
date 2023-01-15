import sys
from pyfiglet import Figlet
from random import choice


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # In case no command-line-arguments are passed in, do this:
    if len(sys.argv) == 1:
        user_input = input("Input: ").strip()
        figlet.setFont(font=choice(fonts))
        print(figlet.renderText(user_input))

    # In the case of of correctly passed parameters, do this:
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and str(sys.argv[2]) in fonts:
            user_input = input("Input: ").strip()
            figlet.setFont(font=str(sys.argv[2]))
            print(figlet.renderText(user_input))
        else:
            sys.exit("Usage: figlet.py --font font_name")

    # Catching errors
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
