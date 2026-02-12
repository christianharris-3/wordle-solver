from CustomerSolverAlgBase import CustomerSolverAlgBase

class OriginalSolver(CustomerSolverAlgBase):
    def __init__(self, word_length=5):
        super().__init__(word_length)

    def get_best_word(self, game_state, word_list):
        valid_words = self.get_best_words(game_state, word_list)
        return valid_words[0]

    def get_best_words(self, game_state, word_list):
        valid_words = game_state.filter_valid_words(word_list)
        self.letter_values = self.get_letter_values(valid_words)
        valid_words.sort(key=self.evaluate_word, reverse=True)
        return valid_words

    def evaluate_word(self, word):
        total = 0
        used = set()
        for i, letter in enumerate(word):
            if letter in used:
                continue
            total += self.letter_values[letter]
            used.add(letter)
        return total

    def get_letter_values(self, word_list) -> dict[str, int]:
        dict = {}
        for word in word_list:
            for letter in word:
                if letter in dict:
                    dict[letter] += 1
                else:
                    dict[letter] = 1
        return dict