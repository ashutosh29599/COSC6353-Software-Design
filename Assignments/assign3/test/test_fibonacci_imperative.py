import sys

from test_fibonacci import FibonacciTests

sys.path.append("src")

import fibonacci_imperative


class FibonacciImperativeTest(FibonacciTests.FibonacciTest):

    def fibonacci_implementation(self):
        return fibonacci_imperative.fibonacci

    def test_canary(self):
        self.assertTrue(True)
