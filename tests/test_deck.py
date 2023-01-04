import unittest
from src.deck import Deck


class TestDeck(unittest.TestCase):

    def setUp(self): 
        self.deck = Deck()

    def test_number_of_cards(self): 
        number_of_cards = len(self.deck.cards)
        self.assertEqual(52, number_of_cards)
    
    def test_count_method(self):
        number_of_cards = self.deck.count()
        self.assertEqual(52, number_of_cards)
    
    def test_deck_after_card_dealt(self):
        self.deck.deal(1)
        number_of_cards = len(self.deck.cards)
        self.assertEqual(51, number_of_cards)
    
    def test_deal_1_card(self):
        dealt_cards = self.deck.deal(1)
        number_of_dealt_cards = len(dealt_cards)
        self.assertEqual(1, number_of_dealt_cards)
    
    def test_deal_2_cards(self):
        dealt_cards = self.deck.deal(2)
        number_of_dealt_cards = len(dealt_cards)
        self.assertEqual(2, number_of_dealt_cards)

    def test_deal_10_cards(self):
        dealt_cards = self.deck.deal(10)
        number_of_dealt_cards = len(dealt_cards)
        self.assertEqual(10, number_of_dealt_cards)

    def test_deal_all_cards(self):
        dealt_cards = self.deck.deal(52)
        number_of_dealt_cards = len(dealt_cards)
        self.assertEqual(52, number_of_dealt_cards)
    
    def test_deal_more_cards_than_deck(self):
        self.deck.deal(20)
        number_of_cards = self.deck.count()
        dealt_cards = self.deck.deal(40)
        number_of_dealt_cards = len(dealt_cards)
        self.assertEqual(number_of_cards, number_of_dealt_cards)

    def test_deal_from_empty_deck(self):
        self.deck.deal(52)
        self.assertRaises(ValueError, self.deck.deal, 1)
    
    def test_deal_card_method_returns_top_card(self):
        top_card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertIs(top_card, dealt_card)
    
    def test_shuffle_changes_card_order(self):
        pre_shuffle_deck = self.deck.cards.copy()
        self.deck.shuffle()
        post_shuffle_deck = self.deck.cards
        self.assertNotEqual(pre_shuffle_deck, post_shuffle_deck)
    
    def test_cannot_shuffle_not_full_deck(self):
        self.deck.deal(1)
        self.assertRaises(ValueError, self.deck.shuffle)
    
