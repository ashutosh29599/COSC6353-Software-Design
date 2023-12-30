import unittest

from parameterized import parameterized


class FibonacciTests(object):
    class FibonacciTest(unittest.TestCase):

        @parameterized.expand([
            (0, 1),
            (1, 1),
            (2, 2),
            (5, 8),
            (10, 89),
            (30, 1346269),
        ])
        def test_fibonacci(self, position, fibonacci_value):
            self.assertEqual(fibonacci_value, self.fibonacci_implementation()(position))

        def test_fibonacci_raises_exception_for_negative_position(self):
            with self.assertRaises(Exception) as exception:
                self.fibonacci_implementation()(-1)

            self.assertEqual(str(exception.exception), "Negative value not allowed for position")
