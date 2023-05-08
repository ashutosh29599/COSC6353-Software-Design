import unittest
from parameterized import parameterized
import sys

sys.path.append('src')
from prime_number_generator import is_prime, generate_list_of_prime_numbers_of_length


class PrimeNumberGeneratorTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    @parameterized.expand([
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (525, False)
    ])
    def test_is_prime_takes_a_prime_number_returns_true(self, number, primality):
        self.assertEqual(is_prime(number), primality)

    @parameterized.expand([
        (5, [2, 3, 5, 7, 11]),
        (10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    ])
    def test_generate_list_of_prime_numbers_of_length(self, length, list_of_prime_numbers):
        self.assertEqual(generate_list_of_prime_numbers_of_length(length), list_of_prime_numbers)
