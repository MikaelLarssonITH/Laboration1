################################################
#           Author: Mikael Larsson             #
#           Version: 1.0                       #
#           Modified date: 2023-10-09          #
################################################

import random
from game_structure import GameStructure
import libs as function_library

class Blackjack(GameStructure):
    def __init__(self):
        # Call the constructor of the parent class GameStructure to set the title and version
        super().__init__(title="Blackjack", version=1.0)
        # Define a deck of cards, where 10, 10, 10, and 11 represent J, Q, K, and A respectively
        # The deck is replicated 4 times to simulate a standard deck of cards
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 
        self.player_hand = []  # Initialize player's hand
        self.dealer_hand = []  # Initialize dealer's hand

    def deal_cards(self):
        # Deal two cards each to the player and the dealer by appending random cards from the deck to their hands
        for _ in range(2):
            self.player_hand.append(random.choice(self.deck))
            self.dealer_hand.append(random.choice(self.deck))

    def calculate_score(self, hand):
        # Calculate the score of a hand. Aces (represented by 11) can be worth 1 if the score exceeds 21.
        score = sum(hand)  # Sum up the card values in the hand
        number_of_aces = hand.count(11)  # Count the number of aces in the hand
        
        # While the score is over 21 and there are aces in the hand, subtract 10 for each ace
        while score > 21 and number_of_aces:
            score -= 10
            number_of_aces -= 1
        
        return score

    def get_player_move(self):
        # Get player's decision to hit or stand, ensuring they enter a valid move
        while True:
            move = input("Do you want to [H]it or [S]tand? ").lower()
            if move in ['h', 's']:
                return move

    def play(self):
        function_library.clear_screen()  # Clear screen at the start of the game
        
        # Mark the beginning of a game
        self.start_game()
        # Ensure that hands are empty at the start of the game to avoid carrying over cards from previous games
        self.player_hand = [] 
        self.dealer_hand = []
        # Deal initial cards
        self.deal_cards()
        
        # Main game loop
        while True:
            function_library.clear_screen()  # Clear screen during every loop for clean UI
            # Display player's hand and score
            print(f"Your hand: {self.player_hand}, score: {self.calculate_score(self.player_hand)}")
            # Show one of dealer's cards and keep the other hidden
            print(f"Dealer's hand: {self.dealer_hand[0]} and a hidden card")
            
            # Check for Blackjack, if true player wins
            if self.calculate_score(self.player_hand) == 21:
                print("Blackjack! You win!")
                self.score += 100  # Assuming a scoring system where player gains 100 points for winning
                break

            # Get player's move and proceed accordingly
            move = self.get_player_move()
            
            # Player decides to hit
            if move == 'h':
                # Add another card to player's hand
                self.player_hand.append(random.choice(self.deck))
                function_library.clear_screen()
                # Check if player's score is over 21 (bust). If true, player loses
                if self.calculate_score(self.player_hand) > 21:
                    self.score -= 100  # Assuming player loses 100 points for losing
                    print(f"Your final hand: {self.player_hand}, score: {self.calculate_score(self.player_hand)}")
                    print("Bust! You lose.")
                    break
            # Player decides to stand
            else:
                # Dealer takes cards while its score is less than 17
                while self.calculate_score(self.dealer_hand) < 17:
                    self.dealer_hand.append(random.choice(self.deck))
                
                # Display final hands and scores for player and dealer
                print(f"Your final hand: {self.player_hand}, score: {self.calculate_score(self.player_hand)}")
                print(f"Dealer's final hand: {self.dealer_hand}, score: {self.calculate_score(self.dealer_hand)}")
                
                # Determine winner based on scores, announcing result to player
                if self.calculate_score(self.dealer_hand) > 21 or \
                    self.calculate_score(self.player_hand) > self.calculate_score(self.dealer_hand):
                    print("You win!")
                elif self.calculate_score(self.player_hand) == self.calculate_score(self.dealer_hand):
                    print("It's a tie!")
                else:
                    print("You lose!")
                break
        
        # Mark the end of a game
        self.end_game()
