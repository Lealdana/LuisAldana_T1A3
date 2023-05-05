# Added a Loading text when user decides to play
import time
import random
import csv
import os


# 3 Seconds for the timer
wait_time = 3


# Ask for user data

print("Welcome to the General knowledge Test Game!!\n")

user_name = input("Whats your name?: ")

# This function is to ask the user if they want to execute the game


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


user_confirmation()


# Timer for the Loading text before playing
def loading_game():

    for i in range(wait_time):
        print(f" Loading game.{'.'*i} \n -------------------  ")
        time.sleep(1)


loading_game()

# Introduction to the program

print("Let's Go!!")
print(" ")
print("But first you need to know the Rules\n")
print("If you want to exit the program, just write -- Exit --\n")
print("To answer the questions just type the answer ie. Whats the largest continent in the world? \n type: Africa \n")

# Question, choices and answer in Dictionary
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Rome", "Madrid"],
        "answer": "Paris".lower()
    },
    {
        "question": "Who is the author of 'The Catcher in the Rye'?",
        "choices": ["Ernest Hemingway", "J.D. Salinger", "F. Scott Fitzgerald", "Mark Twain"],
        "answer": "J.D. Salinger".lower()
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
                print("\nCorrect!\n")
                score += 15
                break
            elif answer.lower() == "exit":
                exit()
            elif not answer.isalpha():
                print("\nPlease, type a letter.\n")
            else:
                if answer.isalpha() and answer != question["answer".lower()]:
                    print("\nIncorrect!\n")
                    print("")
                    break


ask_question()

# Save Score to a CSV file and view it

score = int(score / len(questions) * 100)
print(f"Your score is: {score} You can do better than that!.")


filename = "scores.csv"
exists = os.path.isfile(filename)

# Open CSV file, but if doesn't exist, creates it

while True:
    try:
        save_score = input(
            "Do you want to save your score? (yes or no): ").lower()
        if save_score not in ["yes", "no"]:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter either 'yes' or 'no'.")

if save_score == "yes":
    with open(filename, mode="a", newline="") as score_file:
        fieldnames = ["name", "score"]
        writer = csv.DictWriter(score_file, fieldnames=fieldnames)

        if not exists:
            writer.writeheader()

        writer.writerow({"name": user_name, "score": score})

# option to delete previous scores
while True:
    try:
        delete_scores = input(
            "Do you want to delete previous scores? (yes or no): ").lower()
        if delete_scores not in ["yes", "no"]:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter either 'yes' or 'no'.")

if delete_scores == "yes":
    with open(filename, mode="w", newline="") as score_file:
        pass

# Ask user to see previous score

while True:
    try:
        show_previous_scores = input(
            "Do you want to see previous scores? (yes or no): ").lower()
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
