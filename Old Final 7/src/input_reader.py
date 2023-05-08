from spell_checker import is_spelling_correct


def read_input(filename):
    with open(filename, 'r') as file:
        text = file.readlines()

    return text


def get_spell_checked_lines(lines):
    updated_lines = []
    for line in lines:
        new_line = ""
        words = line.split()
        for word in words:
            if not is_spelling_correct(word):
                new_line += f"[{word}] "
            else:
                new_line += f"{word} "
        new_line = new_line.rstrip()
        updated_lines.append(new_line)

    return updated_lines


def spot_errors(filename):
    return get_spell_checked_lines(read_input(filename))
