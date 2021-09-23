"""
GuessingGame.py

A program allows the user to play a  game to guess a number with 3 different modes.
"""

import random


def guessNumber(guessesNum, maxNum):  # returns if the user could guess the answer
    # sets the answer of game to a random number
    answer = random.randint(1, maxNum)
    counter = 0

    while counter != guessesNum:  # user keeps guessing until number of guesses it used
        try:
            guess = int(input("\nPlease enter a guess: "))
            if guess > answer:  # user guessed too low
                print("Try guessing lower. You have",
                      (guessesNum - (counter + 1)), "guesses left.")

            elif guess < answer:  # user guessed too high
                print("Try guessing higher. You have",
                      (guessesNum - (counter + 1)), "guesses left.")
            else:
                return True  # returns the user guessed the answer

            counter += 1

        except:  # user tried to enter something that wasn't a positive integer
            print("Please only enter a positive integer.")
    return False  # returns the user ran out of guesses


def setMode(mode):  # returns number of guesses and max range based on user selection
    if mode == 1:  # rookie mode
        guessesNum = 4
        maxNum = 10
    elif mode == 2:  # amateur mode
        guessesNum = 8
        maxNum = 100
    elif mode == 3:  # pro mode
        guessesNum = 15
        maxNum = 500
    return guessesNum, maxNum


def playAgain():  # asks user if they want to replay the game
    while True:
        again = input("\nDo you want to play again? (y/n): ").lower()

        if again in ("no", "n"):  # user doesn't want to replay
            return True

        elif again in ("yes", "y"):  # user wants to replay
            return False
        else:
            print("Please answer with 'y' or 'n'")


def main():
    mode = 0
    print("Welcome to Guess. This is a small guessing game")

    while mode != 4:  # user can replay until they enter 4
        try:
            print("1. Rookie   -   1 to 10     (4 guesses)\n"
                  + "2. Amateur  -   1 to 100    (8 guesses)\n"
                  + "3. Pro      -   1 to 500    (15 guesses)\n"
                  + "4. Quit")
            mode = int(input("\nEnter a mode (1-4): "))

            if 0 < mode < 4:  # user has entered a valid mode
                guessesNum, maxNum = setMode(mode)
                if guessNumber(guessesNum, maxNum):
                    # displays message depending if user guessed right
                    print("\nCongratulations! You guessed it right!")
                else:
                    print("\nOh no! You ran out of guesses.")

                if playAgain():  # asks if user wants to replay
                    mode = 4
            elif mode == 4:  # user quits
                break
            else:
                print("Please only enter a number from 1 to 4.")

        except:  # input was not an integer from 1 to 4
            print("Please only enter a number from 1 to 4: ")


main()
