# Import the random module to select a word randomly from the list
import random

# Define the WordGuessGame class
class WordGuessGame:
    def __init__(self):
        # List of words to guess from
        self.words = ["python", "programming", "challenge", "developer", "learning"]

        # Randomly select a word to guess
        self.word_to_guess = random.choice(self.words).lower()

        # Initialize an empty list to keep track of the player's guesses
        self.guesses = []

        # Set the maximum number of incorrect attempts allowed
        self.max_attempts = 6

    # Method to display the current state of the word based on the player's guesses
    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guesses:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

    # Method to process the player's guess
    def make_guess(self, guess):
        self.guesses.append(guess.lower())

        # If the guessed letter is not in the word, reduce the number of attempts left
        if guess.lower() not in self.word_to_guess:
            self.max_attempts -= 1

    # The main game loop
    def play_game(self):
        print("Welcome to the Word Guessing Game!")
        print("Try to guess the word.")
        print("Each incorrect guess reduces your remaining attempts.")
        print("Good Luck!\n")

        # Game continues until the word is guesses or attempts run out
        while "_" in self.display_word() and self.max_attempts > 0:
            print(f"Word: {self.display_word()}")
            print(f"Attempts remaining: {self.max_attempts}")
            guess = input("Enter a letter: ")

            # Check if the input is a single alphabet character
            if len(guess) == 1 and guess.isalpha():
                self.make_guess(guess)
            else:
                print("Invalid input. Please enter a single letter.")

        # Check if the game was won or lost and print the appropriate message
        if "_" not in self.display_word():
          print(f"Congratulations! You guessed the word: {self.word_to_guess}")
        else:
          print(f"Sorry, you ran out of attempts. The word was: {self.word_to_guess}")

# Entry point of the script
def main():
    game = WordGuessGame()
    game.play_game()

# Check if the script is being run directly (as opposed to being imported) and call main
if __name__ == "__main__":
    main()