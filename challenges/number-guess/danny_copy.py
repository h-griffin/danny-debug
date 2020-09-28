#Danny Rigdon - 09/18/2020
#HW05 - Guess the Number / Game

#Declare/initialize variables and CONSTANTS

CORRECT_NUMBER = 3
userGuess = 0
guessCount = 0
GUESS_LIMIT = 3
outOfGuesses = False
# QUESTION_ONE = ""
userAnswerOne = "Yes"
userAnswerTwo = "yes"
userAnswerThree = "YES"

#Does the user want to guess which number I am thinking of?

QUESTION_ONE = input("I am thinking of a number. Would you like to guess what that number is? (Yes or No) ")
if QUESTION_ONE == userAnswerOne:
    print("Great! Let's get started.")
elif QUESTION_ONE == userAnswerTwo:
    print("Great! Let's get started.")
elif QUESTION_ONE == userAnswerThree:
    print("Great! Let's get started.")
else:
    print("You're no fun!") + quit()
        
#Prompt user for entry / Process user input.

while userGuess != CORRECT_NUMBER and not(outOfGuesses):
    
    if guessCount < GUESS_LIMIT:
        userGuess = int(input("Please guess a number between 1 and 100: "))
        guessCount += 1
    else: outOfGuesses = True

    if userGuess < CORRECT_NUMBER:
        print("That guess is too low... are you trying? Guess again!")
        # userGuess = int(input("Please guess a number between 1 and 100: "))
    elif userGuess > CORRECT_NUMBER:
        print("That guess is too high... get your head in the game. Guess again!")
        # userGuess = int(input("Please guess a number between 1 and 100: "))
    else:
        print('awkward...')


#Display output results.

if outOfGuesses:
    print("You're no match for me... YOU LOSE!!!")
else:
    print("Great guess! The number was, in fact, " + str(CORRECT_NUMBER) + ".")