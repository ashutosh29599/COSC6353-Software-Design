import functools

import fibonacci_recursive


@functools.cache
def fibonacci(position):
    return fibonacci_recursive.fibonacci(position, fibonacci)
