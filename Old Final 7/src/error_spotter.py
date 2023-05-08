from input_reader import spot_errors


def display_errors(filename):
    lines = spot_errors(filename)

    for line in lines:
        print(line)


if __name__ == "__main__":
    display_errors("input2.txt")
