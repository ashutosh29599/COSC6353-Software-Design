import unittest
from unittest.mock import patch
import sys


sys.path.append("src")
from input_reader import read_input, get_spell_checked_lines, spot_errors


class InputReaderTest(unittest.TestCase):
    def test_read_input(self):
        self.assertEqual(read_input("test_input.txt")[0], "My name is Ashutosh Kumar.")

    def test_read_input_empty_file(self):
        self.assertEqual(len(read_input("test_input_empty.txt")), 0)

    @patch('input_reader.read_input')
    def test_read_input_non_existent_file(self, read_input_mock):
        read_input_mock.side_effect = Exception("File not found!")

        self.assertRaisesRegex(Exception, "File not found!", read_input_mock, "non_existent_file.txt")

    def test_get_spell_checked_lines_empty_list(self):
        self.assertEqual(get_spell_checked_lines([]), [])

    def test_get_spell_checked_lines_send_one_correct_line(self):
        self.assertEqual(get_spell_checked_lines(["The cow jumped over the moon"]), ["The cow jumped over the moon"])

    def test_get_spell_checked_lines_send_two_correct_lines(self):
        self.assertEqual(
            get_spell_checked_lines(["The cow jumped over the moon", "the little dog laughed to see such sport"]),
                                    ["The cow jumped over the moon", "the little dog laughed to see such sport"])

    def test_get_spell_checked_lines_some_incorrect_words(self):
        self.assertEqual(get_spell_checked_lines(["The cow jumped over the moln"]), ["The cow jumped over the [moln]"])

    def test_get_spell_checked_lines_send_two_lines_one_correct_other_with_some_errors(self):
        self.assertEqual(
            get_spell_checked_lines(["The cow jumped over the moon", "the little dgo laughed to see such soprt"]),
                                    ["The cow jumped over the moon", "the little [dgo] laughed to see such [soprt]"])

    def test_get_spell_checked_lines_send_two_lines_both_with_some_errors(self):
        self.assertEqual(
            get_spell_checked_lines(["The cow jumped over the moln", "the little dgo laughed to see such soprt"]),
                                    ["The cow jumped over the [moln]", "the little [dgo] laughed to see such [soprt]"])

    @patch("input_reader.get_spell_checked_lines")
    @patch("input_reader.read_input")
    def test_spot_errors_calls_read_input_and_get_spell_checked_lines(self, read_input_mock, get_spell_checked_lines_mock):
        read_input_mock.return_value = ["The cow jumped over the moon"]
        get_spell_checked_lines_mock.return_value = ["The cow jumped over the moon"]
        spot_errors("input.txt")

        read_input_mock.assert_called_once_with("input.txt")
        get_spell_checked_lines_mock.assert_called_once_with(["The cow jumped over the moon"])

    @patch("input_reader.read_input")
    def test_spot_errors_passes_on_the_exception_from_read_input_to_caller(self, read_input_mock):
        read_input_mock.side_effect = Exception("File not found!")

        self.assertRaisesRegex(Exception, "File not found!", spot_errors, "non_existent_file.txt")
