import sys

from test_fibonacci import FibonacciTests

sys.path.append("src")

import fibonacci_recursive


class FibonacciRecursiveTest(FibonacciTests.FibonacciTest):

    def fibonacci_implementation(self):
        return fibonacci_recursive.fibonacci
