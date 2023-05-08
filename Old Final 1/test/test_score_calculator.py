import unittest
from parameterized import parameterized
import sys

sys.path.append('src')
from score_calculator import calculate_score


class ScoreCalculatorTest(unittest.TestCase):
    @parameterized.expand([
        ("monkey", "monkey", 10),
        ("fruit", "fruit", 8),
        ("monk", "monkey", 7),
        ("apply", "apple", 7),
        ("bat", "monkey", 0),
        ("ion", "apple", 0),
        ("", "banana", 0),
    ])
    def test_calculate_score(self, word, target_word, score):
        self.assertEqual(calculate_score(word, target_word), score)
