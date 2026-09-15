import unittest
from card_game.Player import *
from card_game.card.entity.Hand import *
from card_game.card.game.TwentyOne.TwentyOne import *

class TestTwentyOne(unittest.TestCase):
    
    def test_score_hand_ace_high(self):
        self.assertEqual(max_score, score_hand(create_hand("HA,HK")))
        
    def test_score_hand_ace_low(self):
        self.assertEqual(14, score_hand(create_hand("HA,HK,H3")))
        
    def test_score_hand_five(self):
        self.assertEqual(20, score_hand(create_hand("H2,H3,H4,H5,H6")))
        
    def test_score_hand_bust(self):
        self.assertEqual(0, score_hand(create_hand("HK,H3,H4,H5,H6")))
        
    def test_computer_plays_no_draw(self):
        player = create_player(COMPUTER, "Comp 1")
        player[HAND] = create_hand("HA,HK")
        deck = create_deck()
        computer_plays(player, deck)
        self.assertEqual(['HA', 'HK'], player[HAND])
        
    def test_computer_plays_draw(self):
        player = create_player(COMPUTER, "Comp 1")
        player[HAND] = create_hand("DK,H2")
        deck = create_deck("HA,D2,D3,D4")
        computer_plays(player, deck)
        self.assertEqual(['DK', 'H2', 'D4'], player[HAND])
        
    def test_computer_plays_draw_twice(self):
        player = create_player(COMPUTER, "Comp 1")
        player[HAND] = create_hand("D7,H2")
        deck = create_deck("HA,D2,D3,D4")
        computer_plays(player, deck)
        self.assertEqual(['D7', 'H2', 'D4', 'D3'], player[HAND])