from unittest import TestCase
from unittest.mock import patch
from src.game import Game
from src.hand import Hand
from src.card import Card
from src.deck import Deck
import io

class TestGame(TestCase):

    def setUp(self):
        pass
        self.game = Game()
        with patch('builtins.input', return_value="11"):
            with patch('sys.stdout', new=io.StringIO()):
                self.game.set_up()
    
    def test_pre_setup_game_attributes(self):
        self.game1 = Game()
        self.assertNotIn('deck', dir(self.game1))
        self.assertNotIn('player_hand', dir(self.game1))
        self.assertNotIn('dealer_hand', dir(self.game1))
    
    def test_post_setup_game_attributes(self):
        self.assertIn('deck', dir(self.game))
        self.assertIn('player_hand', dir(self.game))
        self.assertIn('dealer_hand', dir(self.game))
    
    def test_post_setup_game_deck_size(self):
        deck_size = len(self.game.deck.cards)
        self.assertEqual(48, deck_size)
    
    def test_post_setup_hand_sizes(self):
        player_hand_size = len(self.game.player_hand.cards)
        dealer_hand_size = len(self.game.dealer_hand.cards)
        self.assertEqual(2, player_hand_size)
        self.assertEqual(2, dealer_hand_size)
    
    def test_is_over_bust_hand(self):
        self.card2 = Card("Dimonds", "K")
        self.card4 = Card("Clubs", "9")
        self.card5 = Card("Clubs", "Q")
        self.hand = Hand()
        self.hand.add_card(self.card2)
        self.hand.add_card(self.card4)
        self.hand.add_card(self.card5)
        self.assertTrue(self.game.is_over(self.hand))
    
    def test_is_over_valid_hand(self):
        self.card2 = Card("Dimonds", "K")
        self.card4 = Card("Clubs", "9")
        self.hand = Hand()
        self.hand.add_card(self.card2)
        self.hand.add_card(self.card4)
        self.assertFalse(self.game.is_over(self.hand))
    
    def test_dealer_turn_adds_cards_to_hand_until_over_16(self):
        self.game1 = Game()
        self.deck1 = Deck()
        self.dealer_hand1 = Hand(True)
        self.game1.deck = self.deck1
        self.game1.dealer_hand = self.dealer_hand1
        with patch('sys.stdout', new=io.StringIO()):
            self.game1.dealer_turn()
            self.assertLess(16, self.game1.dealer_hand.value)     
    
    def test_play_player_chooses_to_stand(self):
        with patch('builtins.input') as mocked_inputs:
            mocked_inputs.side_effect = ["11", "s", "no"]
            with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                self.game.play()
                self.assertIn("Final Results", fake_stdout.getvalue())

    def test_play_player_chooses_to_hit_until_bust(self):
        with patch('builtins.input') as mocked_inputs:
            mocked_inputs.side_effect = [
                "11", "h", "11", "h", "11", "h",
                "11", "h", "11", "h", "11", "h",
                "11", "h", "11", "h", "11", "h", "n"
                ]
            with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                self.game.play()
                self.assertIn("You are over 21, you have lost...", fake_stdout.getvalue())