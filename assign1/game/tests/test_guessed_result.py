import unittest
import sys
 
# setting path
sys.path.append('../game')


from guessed_result import GuessedResult
from enums import Color


class TestGuessedResult(unittest.TestCase):

    def test_get_guessed_word(self):
        colors = [Color.YELLOW, Color.GREEN, Color.GRAY, Color.GRAY, Color.GRAY]
        guessed_result = GuessedResult("rapid", colors)
        self.assertEqual(guessed_result.word, "rapid")

    # def test_get_colors(self):
    #     colors = [Color.YELLOW, Color.GREEN, Color.GRAY, Color.GRAY, Color.GRAY]
    #     guessed_result = GuessedResult("rapid", colors)
    #     self.assertEqual(guessed_result.colors, [Color.YELLOW, Color.GREEN, Color.GRAY, Color.GRAY, Color.GRAY])

if __name__ == "__main__":
    test = TestGuessedResult()
    test.test_get_guessed_word()