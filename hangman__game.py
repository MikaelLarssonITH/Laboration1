################################################
#           Author: Mikael Larsson             #
#           Version: 1.0                       #
#           Modified date: 2023-10-09          #
################################################

from game_structure import GameStructure
import libs as function_library

class Hangman(GameStructure):
    """
    Hangman game class derived from GameStructure.
    This class controls the logic for a game of Hangman.
    """

    def __init__(self, filename):
        """
        Initialize a new instance of Hangman.
        
        Args:
        filename (str): The path to the file containing possible words to guess.
        """
        # Call the __init__ method of the superclass and set game title and version
        super().__init__(title="Hangman", version=1.2)
        self.filename = filename
        # Reset game sets up necessary variables for a fresh game start
        self.reset_game()

    def select_random_word(self):
        """
        Retrieve a random word from a CSV file.

        Returns:
        str: A randomly selected word from the file.
        """
        # Utilize a custom library function to get a random line (word) from the specified CSV file
        return function_library.random_line_csv(self.filename)

    def display(self):
        """
        Display the current state of the game: the word as guessed so far and the remaining attempts.
        """
        # The guessed-so-far word and the remaining lives are printed to console
        print(" ".join(self.guess_word))
        print(f"Attempts remaining: {self.lives}")

    def guess(self, letter):
        """
        Check whether a guessed letter is in the secret word.

        Args:
        letter (str): The letter guessed by the player.
        """
        # Check if guessed letter is in the secret word
        if letter in self.secret_word:
            # Update the player's guessed word view with the correctly guessed letter
            for index, char in enumerate(self.secret_word):
                if char == letter:
                    self.guess_word[index] = letter
        else:
            # If guessed letter is not in the secret word, decrease the lives count
            self.lives -= 1

    def is_game_over(self):
        """
        Check whether the game is over, due to either win or loss.
        
        Returns:
        bool: True if the game is over, False otherwise.
        """
        # Scoring (assuming scoring functionality is present in the superclass or elsewhere)
        self.score = self.lives * 100 # Assuming scoring involves remaining lives

        # Check for win condition (no blanks remaining in the guessed word)
        if "_" not in self.guess_word:
            print("\nCongratulations! You won.")
            return True
        # Check for loss condition (no lives remaining)
        elif self.lives <= 0:
            print(f"\nSorry, you lost. The correct word was: {self.secret_word}")
            return True
        return False
    
    def reset_game(self):
        """
        Reset the game state for a new round of Hangman.
        """
        # Setup the secret word, the player's current guessed word view, and lives
        self.secret_word = self.select_random_word()
        self.guess_word = ["_"] * len(self.secret_word)
        self.lives = 6

    def play(self):
        """
        Execute a round of Hangman: gameplay loop, user input handling, and win/loss checking.
        """
        # Setup screen and game state for a new round
        
        self.reset_game()
        self.start_game()  # Commencing the gameplay
        
        # Gameplay loop, continues until the game is over due to win or loss
        while not self.is_game_over():
            function_library.clear_screen()
            self.display()
            guess = input("Guess a letter: ")
            
            # Input validation loop, ensuring the player inputs a single letter
            while len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Please enter a single letter")
                guess = input("Guess a letter: ")
            
            # Proceed with the player's valid guess
            self.guess(guess.lower())
        
        # End the current game round
        self.end_game()
