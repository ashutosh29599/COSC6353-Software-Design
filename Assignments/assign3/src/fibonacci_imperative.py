from fibonacci_validation import validate_position


@validate_position
def fibonacci(position):
    previous, current = 1, 1

    for _ in range(2, position + 1):
        [current, previous] = [current + previous, current]

    return current
