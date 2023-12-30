from functools import reduce

from fibonacci_validation import validate_position


@validate_position
def fibonacci(position):
    def generate_fibonacci_sequence(fibonacci_sequence, _):
        return [fibonacci_sequence[-1], sum(fibonacci_sequence)]

    return reduce(generate_fibonacci_sequence, range(position - 1), [1, 1])[-1]
