import unittest
import time

import fibonacci_recursive
import fibonacci_memoized


class PerformanceTest(unittest.TestCase):
    def test_memoized_version_is_at_least_ten_times_faster_than_recursive_version(self):
        def performance_test_for(fibonacci_implementation):
            start_time = time.time()
            fibonacci_implementation(30)

            return time.time() - start_time

        recursive_time = performance_test_for(fibonacci_recursive.fibonacci)
        memoized_time = performance_test_for(fibonacci_memoized.fibonacci)

        self.assertGreaterEqual(recursive_time, 10 * memoized_time)
