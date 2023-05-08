def calculate_score(word, target_word):
    score = 0

    for letter in word:
        if letter in target_word:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                score += 1
            else:
                score += 2

    return score
