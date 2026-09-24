import unittest
from unittest.mock import patch
from card_game.communication.ConsoleInOut import *

class test_mock_ConsoleInOut(unittest.TestCase):

    @patch("card_game.communication.ConsoleInOut.get_string")
    def test_get_input_string(self, mock_input):
        name = "Derek"
        mock_input.return_value = name
        self.assertEqual(name, get_input_string("What is your name"))

    def test_get_input_integer(self):
        #Sub-task 1: Mock Console Input Integer
        pass

    def test_get_input_string_builtin(self):
        #Sub-task 3 – Mock Console Input With Built In
        pass

    def test_get_input_integer_builtin(self):
        pass