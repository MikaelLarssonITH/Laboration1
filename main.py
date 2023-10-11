################################################
#           Author: Mikael Larsson             #
#           Version: 1.0                       #
#           Modified date: 2023-10-09          #
################################################

# Import necessary modules for each game
import hangman__game
import libs as function_library
import rps_game
import memory_game
import blackjack_game

def play_hangman():
    """
    Initialize and play a round of Hangman.
    """
    # Initialize a game instance with a CSV file containing words, then play the game
    game = hangman__game.Hangman('wordlist.csv') # Note: Currently only supports CSV files!
    game.play()

def play_rock_paper_scissors():
    """
    Initialize and play a round of Rock, Paper, Scissors.
    """
    # Initialize and play the Rock, Paper, Scissors game
    game = rps_game.RockPaperScissors()
    game.play()

def play_memory_game():
    """
    Initialize and play a round of Memory Game.
    """
    # Initialize and play the Memory Game
    game = memory_game.MemoryGame()
    game.play()

def play_blackjack():
    """
    Initialize and play a round of Blackjack.
    """
    # Initialize and play the Blackjack game
    game = blackjack_game.Blackjack()
    game.play()

def menu_display():
    """
    Display the main menu options to the console.
    """
    # Display the game menu and available options
    print("####################################")
    print("Welcome to the Game Menu!")
    print(f"####################################\n")
    print("Please select a game to play:")
    print("1. Hangman")
    print("2. Rock, Paper, Scissors")
    print("3. Memory")
    print("4. Blackjack")
    print("9. Quit")


def main_menu():
    """
    Execute the main menu logic, handling user input and game launching.
    """
    # Keep the menu running until the user decides to quit
    while True:
        # Clear the console each time we return to the main menu
        function_library.clear_screen() 

        # Display the menu options
        menu_display()
        
        # Get user's choice
        choice = input("Enter a number to pick a game: ")

        # Start the chosen game or quit based on user's input
        if choice == "1":
            play_hangman()
        elif choice == "2":
            play_rock_paper_scissors()
        elif choice == "3":
            play_memory_game()
        elif choice == "4":
            play_blackjack()
        elif choice == "9":
            # Exit the game loop, ending the program
            print("Thanks for playing. Goodbye!")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1 and 3.")
    

# Ensure the script is being run directly
if __name__ == "__main__":
    main_menu()
