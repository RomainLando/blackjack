from src.deck import Deck
from src.hand import Hand

class Game:
    def __init__(self):
        pass

    def is_over(self, hand):
        return hand.value > 21

    def dealer_turn(self):
        while self.dealer_hand.value < 16 and not self.is_over(self.dealer_hand):
            self.dealer_hand.add_card(self.deck.deal_card())
        print("Dealer's hand is:")
        self.dealer_hand.display()

    def set_up(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand(True)

        for i in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def play(self):
        playing = True
        while playing:
            
            self.set_up()

            print("Your hand is:")
            self.player_hand.display()
            print("Dealer's hand is:")
            self.dealer_hand.dealer_initial_display()

            game_over = False

            while not game_over:

                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()
                print()
                if choice in ['hit', 'h']:
                    self.player_hand.add_card(self.deck.deal_card())
                    print("Your hand is:")
                    self.player_hand.display()
                    if self.is_over(self.player_hand):
                        print("You are over 21, you have lost...")
                        print()
                        game_over = True
                else:
                    self.dealer_turn()
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    print("Final Results")
                    print("Your hand:", player_hand_value)
                    print("Dealer hand:", dealer_hand_value)
                    
                    if self.is_over(self.dealer_hand):
                        print("Dealer went over, you win!")
                        print()
                    elif player_hand_value > dealer_hand_value:
                        print("You win!")
                        print()
                    elif player_hand_value == dealer_hand_value:
                        print("Tie!")
                        print()
                    else:
                        print("Dealer wins!")
                        print()
                    game_over = True
            
            play_again = input("Play again? [Yes / No] ").lower()
            while play_again not in ["y", "n", "yes", "no"]:
                play_again = input("Please enter 'yes' or 'no' (or y/n) ").lower()
            if play_again in ["no", "n"]:
                print("Thanks for playing!")
                playing = False
            else:
                continue