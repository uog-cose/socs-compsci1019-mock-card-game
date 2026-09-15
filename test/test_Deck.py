import unittest
from card_game.card.entity.Deck import *

class DeckTest(unittest.TestCase):

    def test_generate_deck(self):
        self.assertEqual(52, len(generate_deck()))

    def test_create_deck(self):
        self.assertEqual(52, len(create_deck()))

    def test_create_deck_with_override(self):
        self.assertEqual(4, len(create_deck("H3,H4,C3,C4")))