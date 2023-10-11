################################################
#           Author: Mikael Larsson             #
#           Version: 1.0                       #
#           Modified date: 2023-10-09          #
################################################

import random
import time
from game_structure import GameStructure
import libs as function_library

class MemoryGame(GameStructure):
    def __init__(self):
        # Initialize the MemoryGame, inheriting properties from GameStructure and setting its title and version
        super().__init__(title="Memory Game", version=1.0)
        self.sequence_length = 5  # Define the length of the sequence to be remembered
        
    def generate_sequence(self):
        # Generate a random sequence of alphanumeric characters of length sequence_length
        alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Pool of characters to choose from
        return [random.choice(alphanumeric) for _ in range(self.sequence_length)]

    def shuffle_sequence(self, sequence):
        # Return a shuffled copy of the provided sequence
        shuffled = sequence.copy()  # Create a copy to keep the original sequence intact
        random.shuffle(shuffled)  # Shuffle the copy
        return shuffled
    
    def play(self):
        # Setup screen and game state for a new round
        function_library.clear_screen()
        # Begin the game
        self.start_game()
        # Generate an original sequence for the player to remember
        original_sequence = self.generate_sequence()
        
        # Display the original sequence to the player
        print(f"Remember this sequence: {' '.join(original_sequence)}")
        # Allow the player a moment (3 seconds) to memorize the sequence
        time.sleep(3)  # Pause for 3 seconds, adjust the duration as per your preference
        
        # Clear the screen to hide the original sequence
        function_library.clear_screen()
        # Generate and display a shuffled version of the original sequence
        shuffled_sequence = self.shuffle_sequence(original_sequence)
        print(f"Shuffled sequence: {' '.join(shuffled_sequence)}")
        
        # Prompt the player to enter the original sequence
        user_input = input("Enter the original sequence (without spaces): ")
        
        # Compare the player's input to the original sequence and provide feedback
        if user_input == ''.join(original_sequence):
            # Setup screen and game state for a new round
            function_library.clear_screen()
            print("Correct!")  # Acknowledge correct answer
            self.score += 100  # Reward the player with 100 points (assuming a scoring system is being used)
        else:
            # Inform the player of their mistake and provide the correct sequence
            print(f"Sorry, incorrect. The original sequence was: {' '.join(original_sequence)}")
            self.score -= 100  # Penalize the player by deducting 100 points
        
        # Conclude the game
        self.end_game()
