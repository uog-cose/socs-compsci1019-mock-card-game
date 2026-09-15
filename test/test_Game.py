import unittest
from unittest.mock import MagicMock
from card_game.Game import *
from card_game.Player import *
from card_game.card.entity.PlayerType import *

class TestGame(unittest.TestCase):

    def test_get_computer_players_names(self):
        self.assertEqual("Star Dealer\n", get_computer_players_names()[0])
        
    def test_add_player_count(self):
        clear_players()
        player = create_player(USER, "Derek")
        add_player(player)
        self.assertEqual(1, len(players))
        
    def test_add_player_name(self):
        clear_players()
        name = "Derek"
        player = create_player(USER, name)
        add_player(player)
        self.assertEqual(name, get_player(0)[FIRST_NAME])

    def test_clear_players(self):
        name = "Derek"
        player = create_player(USER, name)
        add_player(player)
        clear_players()
        self.assertEqual(0, len(players))
        
    def test_create_player_count(self):
        name = "Derek"
        player = create_player(USER, name)
        self.assertEqual(5, len(player.keys()))
        
    def test_create_player_name(self):
        name = "Derek"
        player = create_player(USER, name)
        self.assertEqual(name, player[FIRST_NAME])
        
    def test_create_human_player(self):
        clear_players()
        name = "Derek"
        player = create_human_player(name)
        self.assertEqual(name, get_player(0)[FIRST_NAME])
        
    def test_get_next_computer_name_first(self):
        names = ["Derek", "Xi", "Fredric"]
        self.assertEqual("Derek", get_next_computer_name(names))    
    
    def test_get_next_computer_name_second(self):
        names = ["Derek", "Xi", "Fredric"]
        get_next_computer_name(names)
        self.assertEqual("Xi", get_next_computer_name(names)) 
    
    def test_initiate_players(self):
        clear_players()
        initiate_players("Derek", 3)
        self.assertEqual(3, len(players))
        
    def test_initiate_players_type(self):
        clear_players()
        initiate_players("Derek", 3)
        self.assertEqual(COMPUTER, get_player(1)[COMPETITOR_TYPE])
    
    def test_reset_players(self):
        clear_players()
        initiate_players("Derek", 3)
        get_player(0)[WINNER] = True
        reset_players()
        self.assertFalse(get_player(1)[WINNER])
        
    def test_determine_winner_by_score_decrease(self):
        clear_players()
        initiate_players("Derek", 3)
        get_player(0)[SCORE] = 20
        get_player(1)[SCORE] = 18
        get_player(2)[SCORE] = 16
        self.assertEqual(get_player(0), determine_winner())
        
        
    def test_determine_winner_by_score_increase(self):
        clear_players()
        initiate_players("Derek", 3)
        get_player(0)[SCORE] = 16
        get_player(1)[SCORE] = 18
        get_player(2)[SCORE] = 20
        self.assertEqual(get_player(2), determine_winner())
        
    def test_determine_winner_by_score_decrease_with_winner(self):
        clear_players()
        initiate_players("Derek", 3)
        get_player(0)[SCORE] = 20
        get_player(1)[SCORE] = 18
        get_player(2)[SCORE] = 16
        get_player(2)[WINNER] = True
        self.assertEqual(get_player(2), determine_winner())
        
        
    def test_determine_winner_by_score_increase_with_winner(self):
        clear_players()
        initiate_players("Derek", 3)
        get_player(0)[SCORE] = 16
        get_player(0)[WINNER] = True
        get_player(1)[SCORE] = 18
        get_player(2)[SCORE] = 20
        self.assertEqual(get_player(0), determine_winner())
        
    def test_set_finish_game(self):
        finish_game = True
        self.assertTrue(finish_game)