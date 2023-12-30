import sys

from test_fibonacci import FibonacciTests

sys.path.append("src")

import fibonacci_memoized


class FibonacciMemoizedTest(FibonacciTests.FibonacciTest):

    def fibonacci_implementation(self):
        return fibonacci_memoized.fibonacci
