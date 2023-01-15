class Game:
    def __init__(self):
        # Initialising empty lists to store landed and bailed tricks
    skater = Skater()

    # Initialising empty lists to store landed and bailed tricks
    landed = []
    bailed = []

    # Initialising counter variables to keep track of landed and bailed tricks
    counter_landed = 0
    counter_bailed = 0

    def play_game():
        i = int(input("How many rounds do you want to practice? "))
        for _ in range(i):
            try:
                # Get and print random trick
                random_trick = random.choice(list)
                print(cyan(random_trick, 'bold'), end='\n')

                # Prompt the skater if landed or not
                landed_option = str(
                    input("Landed?\n Press'Y' OR 'N'\n").upper())

                if landed_option not in ["YES", "Y", "NO", "N"]:
                    pass

                elif landed_option in ["Yes", "Y"]:
                    # Add landed trick to landed-trick-list
                    landed.append(random_trick)
                    counter_landed += 1

                elif landed_option in ["No", "N"]:
                    # Add bailed trick to bailed-trick-list
                    bailed.append(random_trick)
                    counter_bailed += 1

            except KeyboardInterrupt:
                sys.exit("\n See you next time!\n")

        # 💥
        # Print landing result:
        print(
            f"BANGIN! You've landed {cyan(counter_landed, 'bold')} tricks:\n")

        # Calling helper function to print landed tricks orderd in descending order
        get_trick_dict(landed)
        print("\n\n")

        # 😿
        # Print bailed result:
        print("Not landed:\n")

        # Calling helper function to print bailed tricks orderd in descending order
        get_trick_dict(bailed)
