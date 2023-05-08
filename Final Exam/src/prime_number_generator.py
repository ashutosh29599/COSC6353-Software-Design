def is_prime(number):
    if number == 1:
        return False
    else:
        return not any(map(lambda i: number % i == 0, range(2, int(number**0.5) + 1)))


def generate_list_of_prime_numbers_of_length(length):
    prime_numbers = []
    number_currently_being_tested = 2

    while len(prime_numbers) != length:
        if is_prime(number_currently_being_tested):
            prime_numbers.append(number_currently_being_tested)
        number_currently_being_tested += 1

    return prime_numbers
