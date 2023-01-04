from unittest import TestCase
from unittest.mock import patch
from src.hand import Hand
from src.card import Card
import io


class TestHand(TestCase):

    def setUp(self):
        self.card1 = Card("Spades", "A")
        self.card2 = Card("Dimonds", "K")
        self.card3 = Card("Hearts", "A")
        self.card4 = Card("Clubs", "9")
        self.card5 = Card("Clubs", "Q")
        self.player_hand = Hand()
        self.dealer_hand = Hand(True)

    def test_init_hand_has_no_cards(self):
        self.assertEqual([], self.player_hand.cards)
    
    def test_init_hand_value(self):
        self.assertEqual(0, self.player_hand.value)

    def test_init_dealer_status_for_player(self):
        self.assertEqual(False, self.player_hand.dealer)

    def test_init_dealer_status_for_dealer(self):
        self.assertEqual(True, self.dealer_hand.dealer)
    
    def test_get_value_of_hand(self):
        self.assertEqual(0, self.player_hand.get_value())
    
    def test_add_to_value_of_hand(self):
        self.player_hand.add_to_value(5)
        self.assertEqual(5, self.player_hand.get_value())
    
    def test_calculate_value_of_numbered_card_by_player_hand(self):
        self.player_hand.calculate_value(self.card4)
        new_value = self.player_hand.get_value()
        self.assertEqual(9, new_value)

    def test_calculate_value_of_ace_by_dealer_hand(self):
        self.dealer_hand.calculate_value(self.card1)
        new_value = self.dealer_hand.get_value()
        self.assertEqual(11, new_value)
    
    def test_calculate_value_of_king_by_dealer_hand(self):
        self.dealer_hand.calculate_value(self.card2)
        new_value = self.dealer_hand.get_value()
        self.assertEqual(10, new_value)

    def test_add_card_to_hand(self):
        self.dealer_hand.add_card(self.card1)
        self.assertEqual(1, len(self.dealer_hand.cards))
        self.assertEqual(11, self.dealer_hand.get_value())
    
    def test_add_multiple_cards_until_user_is_bust(self):
        self.dealer_hand.add_card(self.card1)
        self.dealer_hand.add_card(self.card2)
        self.dealer_hand.add_card(self.card3)
        self.assertRaises(ValueError, self.dealer_hand.add_card, self.card4)
        self.assertEqual(3, len(self.dealer_hand.cards))
        self.assertEqual(22, self.dealer_hand.get_value())
    
    def test_add_cards_king_and_ace(self):
        self.dealer_hand.add_card(self.card1)
        self.dealer_hand.add_card(self.card2)
        self.assertEqual(2, len(self.dealer_hand.cards))
        self.assertEqual(21, self.dealer_hand.get_value())

    def test_add_cards_king_queen_ace(self):
        self.dealer_hand.add_card(self.card2)
        self.dealer_hand.add_card(self.card5)
        self.dealer_hand.add_card(self.card1)
        self.assertEqual(3, len(self.dealer_hand.cards))
        self.assertEqual(21, self.dealer_hand.get_value())

    def test_add_cards_nine_ace_ace(self):
        self.dealer_hand.add_card(self.card4)
        self.dealer_hand.add_card(self.card3)
        self.dealer_hand.add_card(self.card1)
        self.assertEqual(3, len(self.dealer_hand.cards))
        self.assertEqual(21, self.dealer_hand.get_value())
    
    def test_add_ace_to_player_hand_as_11(self):
        with patch('builtins.input', return_value="11"):
            self.player_hand.calculate_value(self.card1)
            self.assertEqual(11, self.player_hand.get_value())

    def test_add_ace_to_player_hand_as_1(self):
        with patch('builtins.input', return_value="1"):
            self.player_hand.calculate_value(self.card1)
            self.assertEqual(1, self.player_hand.get_value())

    def test_display_method_one_card(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.player_hand.add_card(self.card4)
            self.player_hand.display()
        self.assertEqual("9 of Clubs\nHand value: 9\n\n", fake_stdout.getvalue())

    def test_display_method_two_card(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.player_hand.add_card(self.card4)
            self.player_hand.add_card(self.card2)
            self.player_hand.display()
        self.assertEqual("9 of Clubs\nK of Dimonds\nHand value: 19\n\n", fake_stdout.getvalue())

    def test_dealer_initial_display_method_two_card(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.dealer_hand.add_card(self.card4)
            self.dealer_hand.add_card(self.card2)
            self.dealer_hand.dealer_initial_display()
        self.assertEqual("hidden\nK of Dimonds\n\n", fake_stdout.getvalue())

    def test_dealer_initial_display_method_three_card_with_blackjack(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.dealer_hand.add_card(self.card2)
            self.dealer_hand.add_card(self.card5)
            self.dealer_hand.add_card(self.card3)
            self.dealer_hand.dealer_initial_display()
        self.assertEqual("K of Dimonds\nQ of Clubs\nA of Hearts\nHand value: 21\n\n", fake_stdout.getvalue())