# Added a Loading text when user decides to play
import time
import random
import csv
g

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
print("To answer the questions just type the answer\n")

# Question, choices and answer in Dictionary
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Who is the author of 'The Catcher in the Rye'?",
        "choices": ["Ernest Hemingway", "J.D. Salinger", "F. Scott Fitzgerald", "Mark Twain"],
        "answer": "J.D. Salinger"
    },
    {
        "question": "What is the largest continent in the world?",
        "choices": ["Africa", "Europe", "Asia", "North America"],
        "answer": "Asia"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Go", "Gd", "Au", "Ag"],
        "answer": "Au"
    },
    {
        "question": "What is the highest mountain in Africa?",
        "choices": ["Mount Everest", "Kilimanjaro", "Mount Fuji", "Mount McKinley"],
        "answer": "Kilimanjaro"
    }
]

random.shuffle(questions)

score = 0
num_questions = len(questions)
question_order = list(range(num_questions))
random.shuffle(question_order)


# For loop to show Questions and Choices

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
        answer = input("Write your answer: ").lower()

        # check the answer and update the score
        if answer == question["answer".lower()]:
            print("Correct!")
            score += 15
        elif answer.lower() == "exit":
            exit()
        else:
            print("Incorrect!\n")
        print("")


ask_question()


# print("answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()
# print("This were your answers!: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()
score = int(score / len(questions) * 100)
print(f"Your score is: {score} You can do better than that!.")
