import unittest
from unittest.mock import patch
import sys


sys.path.append('src')
from spell_checker import parse_text, get_response_for, is_spelling_correct


class SpellCheckerTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_parse_text_true(self):
        self.assertTrue(parse_text("true"))

    def test_parse_text_false(self):
        self.assertFalse(parse_text("false"))

    def test_get_response_for_returns_some_response(self):
        self.assertGreater(len(get_response_for("monkey")), 0)

    @patch('spell_checker.parse_text')
    @patch('spell_checker.get_response_for')
    def test_is_spelling_correct_calls_get_response_for_and_parse_text(self, get_response_for_mock, parse_text_mock):
        get_response_for_mock.return_value = "true"
        parse_text_mock.return_value = True
        is_spelling_correct("monkey")

        get_response_for_mock.assert_called_once_with("monkey")
        parse_text_mock.assert_called_once_with("true")

    @patch('spell_checker.get_response_for')
    def test_is_spelling_correct_passes_exception_from_get_response_for(self, get_response_for_mock):
        get_response_for_mock.side_effect = Exception("Exception from get response for")

        self.assertRaisesRegex(Exception, "Exception from get response for", is_spelling_correct, "monkey")
