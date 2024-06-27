class Brain:

    def __init__(self, puzzle):
        # puzzle object
        self.puzzle = puzzle
        # matrix interpretation
        self.words_matrix = self.create_matrix()
        pass

    def create_matrix(self):
        return []

    def validate_words(self, input_list):
        for proposed, correct in zip(input_list, self.puzzle.words_hints_map.keys()):
            if str(proposed).lower() != str(correct).lower():
                return False
        return True
