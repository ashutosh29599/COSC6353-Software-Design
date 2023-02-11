from enums import Color

TARGET_WORD = "FAVOR"

class WordleGameEngine:

    def __init__(self, user_guess):
        self.user_guess = user_guess.upper()

    def compare_guess(self):
        output = []

        if len(TARGET_WORD) == len(self.user_guess):
            for i, letter in enumerate(TARGET_WORD):
                # print(letter, self.user_guess[i])
                if letter == self.user_guess[i]:
                    output.append(Color.GREEN)
                
                elif self.user_guess[i] in TARGET_WORD:
                    output.append(Color.YELLOW)
                
                else:
                    output.append(Color.GRAY)

        return output

# game = WordleGameEngine("rapid")
# print(game.compare_guess())

