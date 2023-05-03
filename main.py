# Added a Loading text when user decides to play
import time

# 3 Seconds for the timer
wait_time = 3


# Ask for user data

print("Welcome to the General knowledge Test Game!! ")

user_name = input("Whats your name?: ")

# This function is to ask the user if they want to execute the game


def user_confirmation():

    play = ""

    while True:
        play = input("Hey " + user_name +
                     "! are you ready to start playing? \n Yes or No? ").lower()
        if play == "yes":
            print(" ------------------- \n I knew it! \n  -------------------")
            break
        elif play == "no":
            print("Good Bye see you next time!")
            exit()
        else:
            print("Type Yes or No")


user_confirmation()


# Timer for the Loading text before playing
def loading_game():

    for i in range(wait_time):
        print(f" Loading game.{'.'*i} \n -------------------  ")
        time.sleep(1)


loading_game()


print("Let's Go!! \n ------------------- \n but first you need to know the Rules \n -------------------\n If you want to exit the program, just write Exit \n To answer the questions just write either A, B, C or D.\n")

# Question in a Tuple
questions = ("What is the name of the largest mammal in the world?: ",

             "What is the name of the famous dog from the comic strip 'Peanuts?': ",
             "Which planet in our solar system is known as the 'Red Planet'?",
             "Who is the famous fictional detective created by Sir Arthur Conan Doyle?: ",
             "What is the name of the wizard in the Harry Potter series?: ",
             "What is the name of the highest mountain in the world?: ",
             "What is the name of the famous cartoon character who is always chasing a bird?: ",
             "What is the name of the most famous movie about a giant gorilla?: ",
             "What is the name of the famous animated movie about a clownfish searching for his son?: ",
             "What is the name of the famous song by Queen that starts with the lyrics 'Is this the real life? Is this just fantasy?': "

             )

# Answer choices for the Questions in a Tuple
choices = (("A. Blue Whale ", "B. Elephant ", "C. Hippopotamus ", "D. Giraffe "),
           ("A. Garfield ", "B. Scooby-Doo ", "C. Snoopy ", "D. Pluto "),
           ("A. Venus ", "B. Mars ", "C. Saturn ", "D. Neptune "),
           ("A. Sherlock Holmes ", "B. Hercule Poirot ",
           "C. Miss Marple ", "D. Nancy Drew "),
           ("A. Ron Weasley", "B. Hermione Granger ",
           "C. Harry Potter ", "D. Albus Dumbledore "),
           ("A. Mount Everest ", "B. Mount Kilimanjaro ",
           "C. Mount Mckinley", "D. Mount Fuji "),
           ("A. Bugs Bunny ", "B.Tom ", "C. Jerry ", "D. Tweety "),
           ("A. King Kong ", "B. Godzilla ",
           "C. The Incredible Hulk ", "D. Jurassic Park "),
           ("A. The Lion King ", "B. Finding Nemo ", "C. Toy Story ", "D. Shrek "),
           ("A. Bohemian Rhapsody ", "B. We Will Rock You ", "C. Don't Stop Me Now ", "D. Somebody To Love "))


answers = ("A", "C", "B", "A", "D", "A", "D", "A", "B", "B")
guesses = []
score = 0
question_num = 0

# For loop to show Questions and Choices
for question in questions:
    print("<------------------>\n")
    print(question)
    for choice in choices[question_num]:
        print(choice)

    guess = input("Enter your Answer: ").upper()

    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("----CORRECT!----\n       | \n       | ")
    elif guess == "EXIT":
        exit()
    else:
        print("INCORRECT!\n Think before you answer lol ")

    question_num += 1

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
