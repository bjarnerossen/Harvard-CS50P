# SKATE CAMP :skateboard:

## Video Demo:
[Video Demo](https://youtu.be/zUP6iP2aMsQ)

## Description:

**SKATE CAMP** is an application aimed at skateboarders that would like to improve their skateboarding skills and practice tricks in a playful way. **SKATE CAMP** functions as a digital skate coach, and guides the user in making progress. By using gamification well known games such as *Game of Skate* it makes it rewarding for the user to see progress. This app fully neglects the cumbersome process of manually keeping track of tricks / trick sets, as each player has a score that is keeping track of the progress.

>Skateboarding is a unique subculture that thrives on its community and by learning from each other. **SKATE CAMP** captures this energy in an application.

Wherever you go, with **SKATE CAMP** you can practice on your own and have your personal skate coach just in your pocket.

The main idea for this project was derived from [Bryggeriet’s high school](https://bryggerietsgymnasium.se/in-english/) located in Malmö, Sweden. The school has a profile focused in skateboarding, which makes them unique as a school. My aim with this application is to help all other skateboarders, that can't attend a school like Bryggeriets, but are still eager to make progress and seek guidance through a digital coach.

### What will your software do? What features will it have? How will it be executed?
**SKATE CAMP** is an interactive terminal-game, in which the user can intuitively navigate with keyboard-commands through the game.

At first, a user menu is being printed in the terminal. Then the user gets prompted for their input, and reprompted if their input is not a valid option in the menu.

In terms of features the build-up of this application is based on three different functions / interactive games:

1. **Practice (:boom: or :crying_cat_face:)** <br>
In practice the user can choose from a menu of four different levels of trick-difficulty "Rookie", "Easy", "Intermediate". Once a difficulty was chosen a function called *play_game* is being called and the user will be prompted for their username. The validation of the username is based on a regex, that only allows words consisting of 3-10 letters.

[![asciicast](https://asciinema.org/a/2fObN8kOwIKcsgJ6UfG6Xai2B.svg)](https://asciinema.org/a/2fObN8kOwIKcsgJ6UfG6Xai2B)

The given username will then be stored in a Class called *Player* to store the name and keep track of the score. In the next step, the user will be prompted for how often they want to practice i.e. how many tricks should the game output.

```Python
class Player:
    def __init__(self, name, score, total):
        self.name = name
        self.score = score
        self.total = total

    def update_score(self, add):
        self.score += add

    def update_total(self, total):
        self.total += total

    def get_percentage(self):
        return round(float(int(self.score) / int(self.total)) * 100)
```

Then a for loop starts, that outputs one trick at a time, randomly generated from the given trick-list. The user then can choose whether or not have landed the trick or not by typing "Y" for yes or "N" for no. This process is part of a while-loop that reprompts the user, if an invalid input is given by the user.

At the end of the game, the user gets to see a list of their landed tricks and their bailed ones in descending order. The quantity of landed tricks is stored in a counter variable *score* related to the *class Player*. The user can then see how many tricks have been landed in total and how many tricks that are in percentage.

Lastly, the user is prompted for a rematch. "Y" will start the *play_game* loop again, and "N" will lead the user back to the menu.

2. **Game of S.K.A.T.E.** <br>
[Game of Skate](https://en.wikipedia.org/wiki/Game_of_Skate) is a classic amongst the skateboarding community and it uses rules based upon the H.O.R.S.E. game played by basketball players. In **SKATE CAMP** the user tries to beat the computer.

Game of Skate follows a basic set of rules:
- One player sets a trick by doing a particular skateboarding trick of their choice
- If the trick is not landed, or the board did not fully rotate, another player attempts to set a trick
- Once a trick has been set (landed exactly), if the offensive player lands a trick in a line, the other player cannot do another trick within the line, the other player(s) must respond by doing the same trick in their first try. If they make it the game continues
-  If they miss it, they get a letter, starting with S, and so on, until they have missed five tricks, spelling SKATE, and they are out or the game is over.
- No trick may be set more than once in the same game and a skater defending on their last letter may receive two attempts at that trick.

For this application the game rules were modified, as the user is playing against the computer. In this modification of game of skate the user wins, when all tricks of the trick-list are landed. If the user didn't land all tricks and receives all letters of S.K.A.T.E. the game is over and the computer won.

Lastly, the user is prompted for a rematch. "Y" will start the *play_game* loop again, and "N" will lead the user back to the menu.

3. **Custom Set** <br>
The custom set option is based on the same algorithm as *play_game*. The only difference is that the user is able to build their own trick set. The user is prompted to add a trick to the set, one after another. Once the set is added it will be displayed on the screen and the user can choose how many rounds they would like to practice their trick-set. Once and input is given, the function *play_game* gets called again.

### What new skills will you need to acquire? What topics will you need to research?
I had to dive deeper into regex in order to create a robust regex for the username. Another skill I had to research were keys and lambda functions.

### What might you consider to be a good outcome for your project?
To have a program that has a functioning navigation menu and I am able to play a game of skate based on the different difficulty levels.

### A better outcome?
To make the custom-trick-set function work.

### The best outcome?
A fully functioning software, that includes all functionalities that I was planning to implement.

### Required libraries:
**3rd party libraries**<br>
tabulate: 0.9.0 or newer<br>
pyfiglet: 0.8. or newer<br>
simple_colors: 0.1.5 or newer<br>

**Python built in**<br>
sys<br>
random<br>
re<br>

### Future implementations:

- [ ] \(Optional) Game of Skate with the computer also performing tricks, based on a random function and weighted statistics based on the tricks difficulty.
- [ ] \(Optional) Game of Skate, where you can keep track of two user simultaneously play against real world skater.
- [ ] \(Optional) Add custom difficulty sets and save them.
- [ ] \(Optional) Save the stats and user in a file, so that once the program is restarted, older stats are loaded.
- [ ] \(Optional) Tips and tricks on performing certain tricks.
- [ ] \(Optional) Gamification: Have a scoreboard with the player that landed most tricks.
- [ ] \(Optional) Transfer this idea into a real application on the App Store or Android.
- [ ] \(Optional) Custom set selection of trick-buttons, to make the selection easier.