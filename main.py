import art
import random

# Turns for difficulty level
easy_level = 10
hard_level = 5

# Function to compare guess against answer
def check_guess(user_guess, answer, turns):
    if user_guess > answer:
        print("Too high.")
        return turns - 1
    elif user_guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You guessed it! The correct number is {answer}.")
        return

# Function to determine difficulty level
def game_level():
    level = input("Choose a difficulty. Type 'easy' or hard': ")
    if level == "easy":
        return easy_level
    else:
        return hard_level

def game():
    # Header for game
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choose random number between 1 and 100
    chosen_num = random.choice(range(1, 101))

    # Sets number of turns
    turns = game_level()
    guess = 0

    # Create while loop to keep user guessing until turns run out or user guesses correctly
    while guess != chosen_num:
        print(f"You have {turns} attempts remaining.")
        # User guesses number
        guess = int(input("What number do you guess? "))

        # Call comparison function
        turns = check_guess(guess, chosen_num, turns)
        if turns == 0:
            print("You've run out of guesses. Game over.")
            return
        elif guess != chosen_num:
            print("Guess again!")

# Runs game
game()
