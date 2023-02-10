from enums import Color

TARGET_WORD = "FAVOR"

class WordleGameEngine:

    def __init__(self, user_guess):
        self.user_guess = user_guess
        pass

    def compare_guess(self):
        output = []

        if len(TARGET_WORD) == len(self.user_guess):
            for i, letter in enumerate(TARGET_WORD):
                if letter == self.user_guess[i]:
                    output.append(Color.GREEN)
                
                elif letter in self.user_guess:
                    output.append(Color.YELLOW)
                
                else:
                    output.append(Color.GRAY)

        return output
