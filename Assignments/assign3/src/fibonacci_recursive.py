from fibonacci_validation import validate_position


@validate_position
def fibonacci(position, fibonacci_function=None):
    fibonacci_function = fibonacci if fibonacci_function is None else fibonacci_function

    return 1 if position < 2 else fibonacci_function(position - 1) + fibonacci_function(position - 2)
