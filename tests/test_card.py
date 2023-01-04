import unittest
from src.card import Card


class TestCard(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades", "A")
    
    def test_card_has_value(self):
        self.assertEqual("A", self.card1.value)
    
    def test_card_has_suit(self):
        self.assertEqual("Spades", self.card1.suit)
    