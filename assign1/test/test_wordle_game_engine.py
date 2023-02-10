import unittest

from wordle_game_engine import WordleGameEngine
from enums import Color

class TestWordleGameEngine(unittest.TestCase):

    def test_compare_guess(self):
        colors = [Color.YELLOW, Color.GREEN, Color.GRAY, Color.GRAY, Color.GRAY]

        game = WordleGameEngine("rapid")
        result = game.compare_guess()

        self.assertEqual(result, [Color.YELLOW, Color.GREEN, Color.GRAY, Color.GRAY, Color.GRAY])