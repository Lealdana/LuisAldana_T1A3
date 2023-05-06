from colored import fg, bg, attr
import time
print(f"{fg(1)}Welcome to the General knowledge Test Game!!\n")

#Variable to know the User name and using trough the game
user_name = input("Whats your name?: ")

#Ask user if wants to execute the game
def user_confirmation():

    play = ""

    while True:
        play = input("Hey " + user_name +
                     "! are you ready to start playing? \n \nType Yes or No?: \n").lower()
        if play == "yes":
            print(" ------------------- \n I knew it! \n  -------------------\n")
            break
        elif play == "no":
            print("Good Bye see you next time!")
            exit()
        else:
            print("Type Yes or No\n")

#Simulate loading the game, timer set to 3 seconds
def loading_game():
    wait_time = 3
    for i in range(wait_time):
        print(f" Loading game.{'.'*i} \n -------------------  ")
        time.sleep(1)

#Score menu to save, show previous score or delete scores.
def score_menu():
    print("1. Enter 1 to save your score")
    print("2. Enter 2 show previous scores")
    print("3. Enter 3 to delete all previous scores")
    print("4. Enter 4 to Exit")
    choice = input("\nEnter a number for the corresponding action: \n")
    return choice
