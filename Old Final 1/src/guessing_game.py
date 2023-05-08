from word_picker import get_a_target_word_and_a_scrambled_word
from score_calculator import calculate_score


def play():
    target_word, scrambled_word = get_a_target_word_and_a_scrambled_word("input.txt")

    while True:
        guessed_word = input(f"What do you think this word is? {scrambled_word}\n")

        score = calculate_score(guessed_word, target_word)
        print(f"You've got {score} points!\n")

        if guessed_word == target_word:
            print("Yay! You guessed the correct word!")
            break


if __name__ == "__main__":
    play()
