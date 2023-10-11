################################################
#           Author: Mikael Larsson             #
#           Version: 1.0                       #
#           Modified date: 2023-10-09          #
################################################

class GameStructure:
    """
    A general structure for a game class, providing basic attributes and methods 
    to manage game state, score, and version.
    """
    
    def __init__(self, title="", score=0, version=0):
        """
        Initialize a new instance of the game.
        
        :param title: str, title of the game
        :param score: int, score achieved in the game
        :param version: float, version of the game
        """
        self.title = title  # Title of the game
        self.score = score  # Score achieved in the game
        self.version = version  # Version of the game
        self.is_running = False  # Flag to check if the game is running
        
   
    def start_game(self):
        """
        Start the game and print a starting message.
        """
        self.is_running = True  # Set the game state to running
        print(f"Starting {self.title}...")

    def end_game(self):

        print(f"Thanks for playing {self.title}! Your score: {self.score}")
        while True:
            # Ask the user if they want to play again or return to main menu
            choice = input("Do you want to play again? (y/n): ")
            if choice.lower() == 'y':
                self.play()  # Restart the game
                break  # Once the game ends, break out of the while loop
            elif choice.lower() == 'n':
                print("Returning to the main menu...")
                break  # Break out of the while loop and return to the main menu
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

    def play(self):
        """
        Placeholder method for game play logic. To be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the play method.")

    def display_instructions(self):
        """
        Placeholder method for displaying game instructions. To be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the display_instructions method.")

