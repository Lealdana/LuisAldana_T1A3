from colored import fg, bg, attr
import time
import random
import os
import csv
from functions_a import score_menu, loading_game, user_confirmation, user_name


# Ask for user data

# This function is to ask the user if they want to execute the game

user_confirmation()


# Function to simulate loading the game, using timer library


loading_game()

# Introduction to the program

print(f"""{fg(1)}{bg(11)}
Let's Go!!

But first you need to know the Rules

If you want to exit the program, just write -- Exit --

To answer the questions just type the answer ie. Whats the largest continent in the world?
type: Africa {attr('reset')}
""")

# Question, choices and answer in Dictionary
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Rome", "Madrid"],
        "answer": "Paris".lower()
    },
    {
        "question": "Who is the author of 'The Catcher in the Rye'?",
        "choices": ["Hemingway", "Salinger", "Fitzgerald", "Twain"],
        "answer": "Salinger".lower()
    },
    {
        "question": "What is the largest continent in the world?",
        "choices": ["Africa", "Europe", "Asia", "North America"],
        "answer": "Asia".lower()
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Go", "Gd", "Au", "Ag"],
        "answer": "Au".lower()
    },
    {
        "question": "What is the highest mountain in Africa?",
        "choices": ["Mount Everest", "Kilimanjaro", "Mount Fuji", "Mount McKinley"],
        "answer": "Kilimanjaro".lower()
    }
]


# Randomize questions order
random.shuffle(questions)

# Some Variables
score = 0
num_questions = len(questions)
question_order = list(range(num_questions))
random.shuffle(question_order)


# Function to call questions and answers

def ask_question():
    global score
    # Get the current question
    for i in range(num_questions):
        # get the current question
        question = questions[question_order[i]]

        # ask the question and get the answer
        print(question["question"])
        random.shuffle(question["choices"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i + 1}. {choice}")

        # check the answer and update the score
        while True:
            answer = input("\nWrite your answer: ").lower()

            if answer == question["answer".lower()]:
                print(f"{fg(2)}{bg(15)}\nCorrect!\n{attr('reset')}")
                score += 15
                break
            elif answer.lower() == "exit":
                exit()
            elif answer.isdigit():
                print(f"{fg(2)}{bg(15)}\nPlease, type a letter.\n{attr('reset')}")
            else:
                if not answer.isdigit() and answer != question["answer".lower()]:
                    print("\nIncorrect!\n")
                    print("")
                    break


ask_question()

# Save Score to a CSV file and view it

score = int(score / len(questions) * 100)
print(f"{fg(2)}{bg(15)}Your score is: {score} You can do better than that!.\n{attr('reset')}")

# CSV file
filename = "scores.csv"
exists = os.path.isfile(filename)


# Variable to access a the score menu


while True: 
    view_score_menu = input(f"{fg(15)}{bg(13)}Do you want to see the score menu?\n Please type Yes or No?{attr('reset')}\n").lower()
    if view_score_menu  == "yes":
        break
    elif view_score_menu =="no":
        print("Thank you for playing")
        exit()
    else:
        print("Invalid input, Type Yes or NO")
        continue
        
    


# Function to save the user score


def saving_score(filename):
    while True:
        try:
            save_score = input(
                "Do you want to save your score? (yes or no): \n").lower()
            if save_score not in ["yes", "no"]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter either 'yes' or 'no'.\n")

    if save_score == "yes":
        with open(filename, mode="a", newline="") as score_file:
            fieldnames = ["name", "score"]
            writer = csv.DictWriter(score_file, fieldnames=fieldnames)
            print(f"{fg(7)}{bg(10)}\nDone{attr('reset')}\n")

            if not exists:
                writer.writeheader()

            writer.writerow({"name": user_name, "score": score})

# Function to view previous score


def view_previous_score(filename):
    while True:
        try:
            show_previous_scores = input(
                "Do you want to see previous scores? (yes or no): \n").lower()
            if show_previous_scores not in ["yes", "no"]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter either 'yes' or 'no'.")

    if show_previous_scores == "yes":
        with open(filename, mode="r") as score_file:
            reader = csv.DictReader(score_file)
            print("Previous Scores:")
            for row in reader:
                print(f"{row['name']}: {row['score']}")

# Function to delete previous score


def delete_score(filename):
    while True:
        try:
            delete_scores = input(
                "Do you want to delete previous scores? (yes or no): \n").lower()
            if delete_scores not in ["yes", "no"]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter either 'yes' or 'no'.")

    if delete_scores == "yes":
        with open(filename, mode="w", newline="") as score_file:
            writer = csv.writer(score_file)
            writer.writerow(["name", "score"])
            print(f"{fg(7)}{bg(10)}\nDone{attr('reset')}\n")


user_choice = ""

# Loop to go trough the score menu function

while user_choice != "4":
    user_choice = score_menu()
    if (user_choice == "1"):
        saving_score(filename)
    elif (user_choice == "2"):
        view_previous_score(filename)
    elif (user_choice == "3"):
        delete_score(filename)
    elif (user_choice == "4"):
        break
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.\n")
else:
    print("You chose not to see the score menu.")

print("Thank you for playing with us!")
