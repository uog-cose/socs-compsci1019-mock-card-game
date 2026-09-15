import unittest
from unittest.mock import MagicMock
from card_game.card.CardGame import *

class TestCardGame(unittest.TestCase):

    def test_create_dealer(self):
        names = ["Star Dealer\n"]
        create_dealer(names)
        self.assertEqual("Star Dealer\n", players[0][FIRST_NAME])
