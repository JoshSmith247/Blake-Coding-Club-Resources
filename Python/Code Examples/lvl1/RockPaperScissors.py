# RockPaperScissors.py
__author__ = "Josh Smith"
# v. 0.0.3

# Import necessary libraries
import random
import time

# Create a function to run the code
def game():
    
    print("Let's play a game!")
    time.sleep(1)
    print("Choose r, p, or s.")
    time.sleep(1)

    # Collect input from user
    choice = input(">>>")

    # Decide on random choice for 'player 2'
    possibleChoices = ["r", "p", "s"]
    choice2Number = random.randint(0, 2) # random integer from 1 to 3

    choice2 = possibleChoices[choice2Number] # Get choice at index {choice2Number}

    time.sleep(2)
    print("Player 2: " + choice2)

    # Check choice to decide output
    result = ""
    if choice == "r":
        if choice2 == "r":
            result = "There was a tie."

        elif choice2 == "p":
            result = "You lose."

        elif  choice2 == "s":
            result = "You win!"

    elif choice == "p":
        if choice2 == "r":
            result = "You win!"

        elif choice2 == "p":
            result = "There was a tie."

        elif choice2 == "s":
            result = "You lose."

    elif choice == "s":
        if choice2 == "r":
            result = "You lose."

        elif choice2 == "p":
            result = "You win!"

        elif choice2 == "s":
            result = "There was a tie."

    time.sleep(1)
    print(result)

    # Check if player would like to play again. If so, run the function once more.

    playAgain = input("Play again? y/n")

    if playAgain == "y":
        game()
    else:
        print("Goodbye!")

game() # Run the function the first time (It has now been declared)