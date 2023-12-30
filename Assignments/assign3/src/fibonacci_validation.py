def validate_position(fibonacci):
    def validate_and_call(position, *args):
        if position < 0:
            raise Exception("Negative value not allowed for position")

        return fibonacci(position, *args)

    return validate_and_call
