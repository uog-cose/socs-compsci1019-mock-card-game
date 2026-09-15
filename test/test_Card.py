import unittest
from card_game.card.entity.Card import  *

class CardTest(unittest.TestCase):
    
    club_four = "C4"

    def test_to_string(self):
        self.assertEqual("C4", str(self.club_four))

    def test_get_card_ordinal(self):
        self.assertEqual(4, get_card_ordinal(self.club_four))

    def test_get_card_score(self):
        self.assertEqual(4, get_card_score(self.club_four))

    def test_get_card_ordinal_ace(self):
        self.assertEqual(14, get_card_ordinal("HA"))

    def test_get_card_ordinal_king(self):
        self.assertEqual(13, get_card_ordinal("HK"))
        
    def test_get_card_ordinal_ten(self):
        self.assertEqual(10, get_card_ordinal("H10"))

    def test_get_card_score_ace(self):
        self.assertEqual(11, get_card_score("HA"))

    def test_suit_face_order(self):
        self.assertEqual("C4", suit_face_order(self.club_four))
