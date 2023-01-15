# 3rd party
from pyfiglet import Figlet
from tabulate import tabulate
from simple_colors import *

# Python built in
import sys
import random
import re

# Own functions / libraries
from helpers.ascii_art import figlet
from helpers.helpers import *

# import Skater class
from classes.skater import Player


def main():
    start_game = True
    while start_game:
        print_menu()
        try:
            print("\n")
            user_input = int(input().strip())

            if user_input not in [1, 2, 3, 4]:
                print("\n Invalid key. Please try again.")
                print_menu()
                continue

            # If the user inputs a 1, call practice function.
            elif user_input == 1:
                start_game = False
                practice()

            elif user_input == 2:
                start_game = False
                tricks = [
                    "Kickflip",
                    "FS 180 Kickflip",
                    "BS 180 Kickflip",
                    "Tre Flip",
                    "Fakie Ollie",
                    "Fakie Kickflip",
                    "Fakie FS Kickflip",
                    "Fakie BS Kickflip",
                    "Varial Kickflip",
                    "Ollie",
                    "FS 180 Ollie",
                    "BS 180 Ollie",
                    "Fakie FS 180 Ollie",
                    "Fakie BS 180 Ollie",
                    "Shuvit",
                    "FS Pop Shuvit",
                    "BS Pop Shuvit",
                ]
                game_of_skate(tricks)

            elif user_input == 3:
                custom_set()
                start_game = False

            elif user_input == 4:
                start_game = False
                sys.exit("\n\nSee you next time! 🤙🏼\n")

        except TypeError as err:
            print(f"\n\nInput not part of the menu. Please try again.\n")
            print_menu()

        except ValueError as err:
            print("\n\nInput not part of the menu. Please try again.\n")
            print_menu()

        except KeyboardInterrupt:
            sys.exit("\n\nSee you next time! 🤙🏼\n")


def practice():
    print_practice_menu()

    choice = True
    while True:
        try:
            print("\n")
            choice = int(input().strip())

            if choice not in [1, 2, 3, 4]:
                print("\n Invalid key. Please try again.")
                print(
                    tabulate(table, headers, tablefmt="rounded_grid"),
                    sep="\n\n",
                    end="\n",
                )

            # If the skater chose difficulty "Rookie" then do the following:
            if choice == 1:
                try:
                    # List containing rookie level tricks
                    rookie_tricks = [
                        "Ollie",
                        "FS 180 Ollie",
                        "BS 180 Ollie",
                        "Fakie FS 180 Ollie",
                        "Fakie BS 180 Ollie",
                        "Shuvit",
                        "FS Pop Shuvit",
                        "BS Pop Shuvit",
                    ]

                    play_game(rookie_tricks)
                    choice = False

                except KeyboardInterrupt:
                    practice()
                choice = False

            elif choice == 2:
                try:
                    # List containing rookie level tricks
                    rookie_tricks = [
                        "Ollie",
                        "FS 180 Ollie",
                        "BS 180 Ollie",
                        "Fakie FS 180 Ollie",
                        "Fakie BS 180 Ollie",
                        "Shuvit",
                        "FS Pop Shuvit",
                        "BS Pop Shuvit",
                    ]

                    play_game(rookie_tricks)
                    choice = False

                except KeyboardInterrupt:
                    practice()
                choice = False

            elif choice == 3:
                # List containing intermediate level tricks
                intermediate_tricks = [
                    "Nollie",
                    "Nollie BS 180",
                    "Nollie FS 180",
                    "Nollie Kickflip",
                    "Heelflip",
                    "Switch Ollie",
                    "Switch FS 180",
                    "Switch BS 180",
                ]

                play_game(intermediate_tricks)

                choice = False

            elif choice == 4:
                main()

        except KeyboardInterrupt:
            sys.exit("\n\nSee you next time! 🤙🏼\n")


def print_menu():

    # Initialising figlet library
    font = Figlet(font="slant")
    render = font.renderText("SKATE CAMP")

    # Defining lists as inputs for the tabulate method
    table = [
        ["1.", "Practice"],
        ["2.", "Game of skate"],
        ["3.", "Custom Set"],
        ["4.", "Exit/Quit"],
    ]
    headers = ["Key", "Option"]

    # Print full menu once in the beginning
    figlet()
    print(render, end="")
    print(tabulate(table, headers, tablefmt="rounded_grid"), end="\n\n")


def print_practice_menu():
    # Defining lists as inputs for the tabulate method
    table = [["1.", "Rookie"], ["2.", "Easy"],
             ["3.", "Intermediate"], ["4.", "Back"]]
    headers = ["Key", "Option"]

    # Printing menu for skater to choose difficulty
    print("\n\nPlease choose difficulty")
    print(tabulate(table, headers, tablefmt="rounded_grid"), end="\n")


def play_game(list):
    name = str(input(r"What's your name? " + "").strip())
    pattern = "^[a-zA-Z]{3,10}$"
    while not re.match(pattern, name):
        if len(name) > 10:
            print(red("Usernames should contain max. 10 letter.", "italic"))
        elif len(name) < 3:
            print(red("Usernames must contain min. 3 letters.", "italic"))
        else:
            print(red("Only letters from A - Z are allowed.", "italic"))
        name = str(input(r"What's your name? " + "").strip())
    if re.match(pattern, name):
        skater = Player(f"{name}", 0, 0)
        print(skater.name)

    # Initialising empty lists to store landed and bailed tricks
    landed = []
    bailed = []

    # Initialising counter variables to keep track of landed and bailed tricks
    counter_landed = 0
    counter_bailed = 0

    game = True
    while game:
        i = int(input("\nHow many rounds do you want to practice? "))
        print("\n")
        skater.update_total(i)
        for _ in range(i):

            try:
                # Get and print random trick
                random_trick = random.choice(list)
                print(cyan(random_trick, "bold"), end="\n")

                # Prompt the skater if landed or not
                landed_option = str(
                    input("Landed? Press'Y' OR 'N'\n").upper())

                while landed_option not in ["YES", "Y", "NO", "N"]:
                    print(red("Please enter a valid input", "italic"))
                    print(cyan(random_trick, "bold"), end="\n")
                    landed_option = str(
                        input("Landed? Press'Y' OR 'N'\n").upper())

                if landed_option in ["Yes", "Y"]:
                    # Add landed trick to landed-trick-list
                    print("💥")
                    landed.append(random_trick)
                    counter_landed += 1

                elif landed_option in ["No", "N"]:
                    # Add bailed trick to bailed-trick-list
                    print("😿")
                    bailed.append(random_trick)
                    counter_bailed += 1

            except KeyboardInterrupt:
                sys.exit("\n See you next time! 🤙🏼\n")

        count_perc = round(float(int(counter_landed) / int(i)) * 100)
        skater.update_score(counter_landed)

        # Print landing result:
        if counter_landed != 1:
            print(
                f"\nBANGIN!💥 You've landed {cyan(counter_landed, 'bold')} tricks:")
        else:
            print(
                f"\nBANGIN!💥 You've landed {cyan(counter_landed, 'bold')} trick:")

        # Calling helper function to print landed tricks orderd in descending order
        get_trick_dict(landed)

        print("\n")

        # Print bailed result:
        print("😿 Not landed:")

        # Calling helper function to print bailed tricks orderd in descending order
        get_trick_dict(bailed)

        user_input = str(input("\nRematch? 'Y' or 'N'\n").upper().strip())
        if user_input in ["Y" or "YES"]:
            print(f"Your current score: {cyan(skater.score, 'bold')}")
            print(f"Relative landed: {cyan(skater.get_percentage(), 'bold')}%")

            # Resetting lists to store landed and bailed tricks
            landed = []
            bailed = []

            # Resetting counter variables to keep track of landed and bailed tricks
            counter_landed = 0
            counter_bailed = 0

            # Restarting while loop in order to start rematch
            game = True

        elif user_input in ["N" or "NO"]:
            game = False
            print(f"{skater.name}'s final score: {cyan(skater.score, 'bold')}")
            print(f"Relative landed: {cyan(skater.get_percentage(), 'bold')}%")
            main()


# 🛹 GAME OF SKATE 🛹
def game_of_skate(list):
    # Initialising counter variable to keep track bailed tricks
    counter_bailed = 0

    tricks = []

    game = True
    while game:
        try:
            # Get and print random trick
            random_trick = random.choice(list)
            while random_trick not in tricks:
                tricks.append(random_trick)
                print(f"{cyan(random_trick, 'bold')}")

                # Prompt the skater if landed or not
                landed_option = str(
                    input("Landed?\nPress'Y' OR 'N'\n\n").upper())

                while landed_option not in ["Yes", "Y", "No", "N"]:
                    print(cyan(random_trick, 'bold'), end='\n')
                    landed_option = str(
                        input("Landed?\n Press'Y' OR 'N'\n").upper())

                if landed_option in ["No", "N"]:
                    if counter_bailed == 0:
                        counter_bailed += 1
                        print(f'Score: {red("S", "bold")}', end="\n\n")
                    elif counter_bailed == 1:
                        counter_bailed += 1
                        print(f'Score: {red("S-K", "bold")}', end="\n\n")
                    elif counter_bailed == 2:
                        counter_bailed += 1
                        print(f'Score: {red("S-K-A", "bold")}', end="\n\n")
                    elif counter_bailed == 3:
                        counter_bailed += 1
                        print(f'Score: {red("S-K-A-T", "bold")}', end="\n\n")
                    elif counter_bailed == 4:
                        counter_bailed += 1
                        print(f'Score: {red("S-K-A-T-E", "bold")}', end="\n\n")
                        print(f'{red("GAME OVER", "bold")}', end="\n\n")
                        game = False

                if len(list) == len(tricks):
                    if counter_bailed == 0:
                        print(f'\nBANGIN!💥 YOU WON!', end="\n\n")
                        game = False
                    elif counter_bailed == 1:
                        print(
                            f'\nYOU WON!🤙🏼 SCORE: {red("S", "bold")}', end="\n\n")
                        game = False
                    elif counter_bailed == 2:
                        print(
                            f'\nYOU WON!🤙🏼 SCORE: {red("S-K", "bold")}', end="\n\n")
                        game = False
                    elif counter_bailed == 3:
                        print(
                            f'\nYOU WON!🤙🏼 SCORE: {red("S-K-A", "bold")}', end="\n\n")
                        game = False
                    elif counter_bailed == 4:
                        print(
                            f'\nYOU WON!🤙🏼 SCORE: {red("S-K-A-T", "bold")}', end="\n\n")
                        game = False

        except KeyboardInterrupt:
            sys.exit("\n See you next time!\n")

        if game == False:
            user_input = str(input("Rematch? 'Y' or 'N'\n").upper().strip())
            if user_input in ["Y" or "YES"]:

                # Resetting list to store tricks
                tricks = []

                # Resetting counter variables to keep track of landed and bailed tricks
                counter_bailed = 0

                # Restarting while loop in order to start rematch
                game = True

            elif user_input in ["N" or "NO"]:
                game = False
                main()


def custom_set():
    tricks = [
        "Ollie",
        "FS 180 Ollie",
        "BS 180 Ollie",
        "Fakie FS 180 Ollie",
        "Fakie BS 180 Ollie",
        "Shuvit",
        "FS Pop Shuvit",
        "BS Pop Shuvit",
        "Kickflip",
        "FS 180 Kickflip",
        "BS 180 Kickflip",
        "Tre Flip",
        "Fakie Ollie",
        "Fakie Kickflip",
        "Fakie FS Kickflip",
        "Fakie BS Kickflip",
        "Varial Kickflip",
        "Nollie",
        "Nollie BS 180",
        "Nollie FS 180",
        "Nollie Kickflip",
        "Heelflip",
        "Switch Ollie",
        "Switch FS 180",
        "Switch BS 180"
    ]

    # Convert tricks list to uppercase
    converted_tricks = [letter.upper() for letter in tricks]

    trick_set = []

    # Creating a set to check duplicates in trick_set list
    seen_tricks = set(trick_set)

    i = int(input("How many tricks do you want to add? "))

    # Set counter variable to 0.
    count = 0

    # Getting the tricks from the user
    while count < i:
        trick_input = str(input("Pick your trick: ").strip().upper())
        if trick_input in converted_tricks:
            new_trick = trick_input.capitalize()
            if new_trick not in seen_tricks:
                seen_tricks.add(new_trick)
                trick_set.append(new_trick)
                count += 1
            else:
                print(
                    f"\n{new_trick} is already in the trick set - please enter again\n")
                None
        else:
            print(
                f"\n{trick_input} not available - please enter again\n")
            None

    print(f"Your Set: {*trick_set,}\n")
    play_game(trick_set)


#     options = ["Yes", "No"]
#     item = random.choices(options, cum_weights=(90, 10), k=1)
#     print(item)

if __name__ == "__main__":
    main()
