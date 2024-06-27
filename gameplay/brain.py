def create_matrix(puzzle):
    words = dict(puzzle.words_hints_map).keys()
    solution = puzzle.solution
    positions = dict()

    for word, i in zip(words, range(len(words))):
        sol_index = str(word).index(solution[i])
        positions[word] = [sol_index, len(word) - sol_index]

    # row length
    max_length = max([p[0] for p in positions.values()]) + max([p[1] for p in positions.values()])
    solution_index = max([p[0] for p in positions.values()])

    # create empty matrix
    matrix = []
    for _ in words:
        # 0 - empty
        matrix.append([0 for _ in range(max_length)])

    # fill with letters placeholders
    for arr, word, i in zip(matrix, words, range(len(words))):
        sol = str(word).index(solution[i])
        start = solution_index - sol
        for k in range(start, start + len(word)):
            # 1 - letter
            arr[k] = 1

    # fill with solution index
    for arr in matrix:
        # 2 - solution
        arr[solution_index] = 2

    return matrix


def validate_words(letters, puzzle):

    correct_letters = ""
    for word in puzzle.words_hints_map.keys():
        for letter in word:
            correct_letters += letter

    for proposed, correct in zip(letters, correct_letters):
        if str(proposed).lower() != str(correct).lower():
            return False
    return True
