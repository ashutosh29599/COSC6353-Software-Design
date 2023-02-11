import unittest
import sys
 
# setting path
sys.path.append('../game')

from wordle_game_engine import WordleGameEngine
from enums import Color

class TestWordleGameEngine(unittest.TestCase):

    def test_compare_guess(self):
        colors = [Color.YELLOW, Color.GREEN, Color.GRAY, Color.GRAY, Color.GRAY]

        game = WordleGameEngine("rapid")
        result = game.compare_guess()

        self.assertEqual(result, colors)

if __name__ == "__main__":
    test = TestWordleGameEngine()
    test.test_compare_guess()
