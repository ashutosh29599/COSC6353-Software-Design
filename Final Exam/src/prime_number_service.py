from prime_number_generator import generate_list_of_prime_numbers_of_length


def display_prime_numbers(number_of_prime_numbers_requested, prime_numbers_list):

    print(f"Here are {number_of_prime_numbers_requested} primes starting from 2: {prime_numbers_list}")


if __name__ == "__main__":
    number_of_prime_numbers = int(input("Please enter a number greater than or equal to 1: "))

    list_of_prime_numbers = generate_list_of_prime_numbers_of_length(number_of_prime_numbers)

    display_prime_numbers(number_of_prime_numbers, list_of_prime_numbers)
