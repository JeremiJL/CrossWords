class Brain:

    def __init__(self, puzzle):
        # puzzle object
        self.puzzle = puzzle
        # words list
        self.words_list = (puzzle.words_hints_map.keys())
        # matrix interpretation
        self.words_matrix = None
        # logic interpretation for view
        self.logic_matrix = None
        # compute matrices
        self.create_matrices()
        pass

    def create_matrices(self):

        # compute row width
        left = []
        right = []
        for word, letter in zip(self.words_list, self.puzzle.solution):
            new_left = word.index(letter)
            new_right = len(word) - new_left
            left.append(new_left)
            right.append(new_right)

        row_width = max(left) + max(right)
        index_of_solution = max(left)

        # two-dimensional array storing consecutive letters in cells
        matrix = []
        # fill matrix with empty space
        for row in range(len(self.words_list)):
            matrix.append([None for _ in range(row_width)])
        # fill matrix with letters
        for word, letter, row in zip(self.words_list, self.puzzle.solution, range(0,len(self.words_list))):
            start_index = index_of_solution - word.index(letter)
            for col in range(start_index,start_index + len(word)):
                matrix[row][col] = word[col - start_index]

        # two-dimensional array storing logic of the puzzle
        # 2 - represents solution space, 1 - represents word space, 0 - empty
        logic = []
        for row in range(len(matrix)):
            logic.append([])
            for col in range(len(matrix[row])):
                if matrix[row][col] is None:
                    logic[row].append(0)
                elif col == index_of_solution:
                    logic[row].append(2)
                else:
                    logic[row].append(1)

        # assign
        self.words_matrix = matrix
        self.logic_matrix = logic

    def validate_words(self, input_list):
        for proposed, correct in zip(input_list, self.words_list):
            if str(proposed).lower() != str(correct).lower():
                return False
        return True
