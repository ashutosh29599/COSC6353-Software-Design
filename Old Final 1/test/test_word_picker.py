import unittest
from unittest.mock import patch, ANY
import sys

import word_picker

sys.path.append('src')
from word_picker import input_reader, get_random_word_given_a_seed, get_a_random_word, scramble_word, get_a_target_word_and_a_scrambled_word


class InputReaderTest(unittest.TestCase):
    def test_input_reader_reads_file(self):
        self.assertEqual(input_reader("input.txt"), ['monkey', 'fruit', 'banana', 'apple', 'cosmopolitan'])

    def test_input_reader_reads_empty_file(self):
        self.assertEqual(input_reader("input_empty.txt"), [])

    @patch('word_picker.input_reader')
    def test_input_reader_reads_non_existent_file(self, input_reader_mock):
        input_reader_mock.side_effect = Exception("File does not exist!")

        self.assertRaisesRegex(Exception, "File does not exist!", input_reader_mock, "input_non_existent.txt")

    def test_get_random_word_given_a_seed(self, seed=10384933884848448):
        word_list = ['monkey', 'fruit', 'banana', 'apple', 'cosmopolitan']

        self.assertIn(get_random_word_given_a_seed(word_list, seed), word_list)

    def test_get_random_word_given_a_seed_returns_two_different_random_words(self, seed=10384933884821785):
        word_list = ['monkey', 'fruit', 'banana', 'apple', 'cosmopolitan']

        random_word_1 = get_random_word_given_a_seed(word_list, seed)
        random_word_2 = get_random_word_given_a_seed(word_list, seed)

        self.assertIn(random_word_1, word_list)
        self.assertIn(random_word_2, word_list)
        self.assertNotEqual(random_word_1, random_word_2)

    @patch('word_picker.get_random_word_given_a_seed')
    @patch('word_picker.input_reader')
    def test_get_a_random_word_calls_input_reader_and_get_random_word_given_a_seed(self, input_reader_mock, get_random_word_given_a_seed_mock):
        input_reader_mock.return_value = ['monkey', 'fruit', 'banana', 'apple', 'cosmopolitan']
        get_random_word_given_a_seed_mock.return_value = 'banana'

        get_a_random_word("input.txt")

        input_reader_mock.assert_called_once_with("input.txt")
        get_random_word_given_a_seed_mock.assert_called_once_with(['monkey', 'fruit', 'banana', 'apple', 'cosmopolitan'], ANY)

    @patch('word_picker.input_reader')
    def test_get_a_random_word_raises_exception_if_word_list_is_empty(self, input_reader_mock):
        input_reader_mock.return_value = []

        self.assertRaisesRegex(Exception, "Word list is empty!", get_a_random_word, "input_empty.txt")

    def test_scramble_word_takes_a_word_and_scrambles_it(self):
        scrambled_word = scramble_word("monkey")

        self.assertEqual(sorted(scrambled_word), sorted("monkey"))

    def test_scramble_word_takes_an_empty_string_raises_exception(self):
        self.assertRaisesRegex(Exception, "No word provided.", scramble_word, "")

    @patch('word_picker.scramble_word')
    @patch('word_picker.get_a_random_word')
    def test_get_a_target_word_and_a_scrambled_word_calls_get_a_random_word_and_scramble_word(self, get_a_random_word_mock, scramble_word_mock):
        get_a_random_word_mock.return_value = "banana"
        scramble_word_mock.return_value = "nabana"

        get_a_target_word_and_a_scrambled_word("input.txt")

        get_a_random_word_mock.assert_called_once_with("input.txt")
        scramble_word_mock.assert_called_once_with("banana")
