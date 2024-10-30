import art
import random

# set global constants
EASY_LIVES = 10
HARD_LIVES = 5

# determine difficulty level and return amount of lives
def game_level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LIVES
    else:
        return HARD_LIVES

# compare guess with chosen number and return lives left
def compare_guess(guess, chosen_number, turns):
    if guess > chosen_number:
        print("Too high.")
        return turns - 1
    elif guess < chosen_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You win! The number is {chosen_number}.")

def guessing_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # declare variable using returned global constants
    turns = game_level()
    # declare initial guess variable, which will change with user input
    guess = 0

    chosen_number = random.randint(1, 100)

    # runs through options while guess doesn't match chosen number
    while guess != chosen_number:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Guess a number: "))

        # changes turns amount using the compare function
        turns = compare_guess(guess, chosen_number, turns)

        # when turns run out, game over
        if turns == 0:
            print("You've run out of guesses. You lose.")
            break

# restarts game
while input("Do you want to play Guess The Number? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 5)
    guessing_game()
