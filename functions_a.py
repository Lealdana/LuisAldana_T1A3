# Imported colored library and installed in Venv to add colour to the output
from colored import fg, bg, attr
# Import Time library to use it for the loading game function simulation
import time
welcome = print(
    f'{fg(1)}{bg(15)}Welcome to the General knowledge Test Game!!{attr("reset")}\n')

# Variable to know the User name and using trough the game
user_name = input(f"{fg(10)}{bg(8)}Whats your name?: {attr('reset')}\n")

# Ask user if wants to execute the game


def user_confirmation():
    global user_name, welcome
    play = ""

    while True:
        play = input("Hey " + user_name +
                     "! are you ready to start playing? \n \nType Yes or No?:  \n").lower()
        if play == "yes":
            print(" ------------------- \n I knew it! \n  -------------------\n")
            break
        elif play == "no":
            print(f"{fg(1)}{bg(15)}Good Bye see you next time! {attr('reset')}")
            exit()
        else:
            print("Type Yes or No\n")

# Simulate loading the game, timer set to 3 seconds


def loading_game():
    wait_time = 3
    for i in range(wait_time):
        print(
            f"{fg(10)}{bg(8)} Loading game.{'.'*i} \n -------------------  {attr('reset')}")
        time.sleep(1)

# Score menu to save, show previous score or delete scores.


def score_menu():
    print(f"{fg(2)}{bg(2)}1. Enter 1 to save your score{attr('reset')}")
    print(f"{fg(3)}{bg(16)}2. Enter 2 show previous scores{attr('reset')}")
    print(f"{fg(4)}{bg(17)}3. Enter 3 to delete all previous scores{attr('reset')}")
    print(f"{fg(5)}{bg(18)}4. Enter 4 to Exit{attr('reset')}")
    choice = input("\nEnter a number for the corresponding action:  \n")
    return choice
