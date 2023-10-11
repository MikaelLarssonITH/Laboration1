import random
from game_structure import GameStructure
import libs as function_library

class RockPaperScissors(GameStructure):
    def __init__(self):
        # Initializing the RockPaperScissors game, setting title and version via superclass
        super().__init__(title="Rock, Paper, Scissors", version=1.0)
        # Available choices for the game participants
        self.choices = ['rock', 'paper', 'scissors']
        # Placeholder for the computer's and user's selections
        self.computer_choice = None
        self.user_choice = None
    
    def get_computer_choice(self):
        """
        Randomly select the computer's choice from the available options.
        """
        self.computer_choice = random.choice(self.choices)
    
    def get_user_choice(self):
        """
        Retrieve the user's choice and ensure it's valid.
        """
        print("Options: rock, paper, scissors")
        # Continuous loop until the user provides a valid input
        while True:
            self.user_choice = input("Enter your choice: ").lower()
            # Validation of user input
            if self.user_choice in self.choices:
                break
            else:
                print("Invalid choice. Try again.")
    
    def determine_winner(self):
        """
        Determine and announce the winner based on choices.
        """
        # Case when both players choose the same option
        if self.user_choice == self.computer_choice:
            return "It's a tie!"
        # Win conditions for the user
        elif (self.user_choice == "rock" and self.computer_choice == "scissors") or \
             (self.user_choice == "scissors" and self.computer_choice == "paper") or \
             (self.user_choice == "paper" and self.computer_choice == "rock"):
            self.score += 100  # Assuming the existence of a scoring system, awarding 100 points to the user for winning
            return "You win!"
        else:
            # All other scenarios are a loss for the user
            self.score -= 100  # Subtracting 100 points for a loss
            return "You lose!"
    
    def play(self):
        """
        Play a round of Rock, Paper, Scissors and announce the results.
        """
        # Clearing the screen for clean gameplay visual
        function_library.clear_screen()
        # Commencing the game
        self.start_game()
        # Retrieving choices for both computer and user
        self.get_user_choice()
        self.get_computer_choice()
        # Displaying the choices and declaring the result
        print(f"Computer chose: {self.computer_choice}")
        print(self.determine_winner())
        # Ending the current game round
        self.end_game()
