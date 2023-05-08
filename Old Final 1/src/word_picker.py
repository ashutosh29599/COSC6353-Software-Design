import random
import time


def input_reader(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()

    return words


def get_random_word_given_a_seed(word_list, seed):
    if (not hasattr(get_random_word_given_a_seed, "seed")) or (get_random_word_given_a_seed.seed != seed):
        get_random_word_given_a_seed.seed = seed
        random.seed(seed)

    return random.choice(word_list)


def get_a_random_word(filename):
    seed = time.time_ns()
    word_list = input_reader(filename)

    if len(word_list) == 0:
        raise Exception("Word list is empty!")

    return get_random_word_given_a_seed(word_list, seed)


def scramble_word(word):
    if len(word) == 0:
        raise Exception("No word provided.")

    letters = list(word)
    random.shuffle(letters)

    return ''.join(letters)


def get_a_target_word_and_a_scrambled_word(filename):
    target_word = get_a_random_word(filename)

    return target_word, scramble_word(target_word)
