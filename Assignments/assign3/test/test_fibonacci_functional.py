import sys

from test_fibonacci import FibonacciTests

sys.path.append("src")

import fibonacci_functional


class FibonacciFunctionalTest(FibonacciTests.FibonacciTest):

    def fibonacci_implementation(self):
        return fibonacci_functional.fibonacci
