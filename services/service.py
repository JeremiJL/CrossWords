import random

from repositories.repository import Repository
from gameplay.brain import create_matrix, validate_words, create_puzzle


class Service:
    def __init__(self):
        self.repository = Repository()
        self.puzzle = None

    def get_random_game_code(self):
        codes = self.repository.list_all_game_ids()
        return codes[random.randint(0, len(codes) - 1)]

    def get_matrix(self, code):
        puzzle = self.repository.find(code)
        return create_matrix(puzzle)

    def validate(self, letters, code):
        puzzle = self.repository.find(code)
        return validate_words(letters, puzzle)

    def check_code(self, code):
        return int(code) in self.repository.list_all_game_ids()

    def get_hints(self, code):
        puzzle = self.repository.find(code)
        return puzzle.words_hints_map.values()

    def check(self, words):
        try:
            puzzle = create_puzzle(words)
            try:
                create_matrix(puzzle)
            except ValueError:
                return False
        except IndexError:
            return False
        return True

    def save_puzzle(self, words):
        puzzle = create_puzzle(words)
        print(type(puzzle))
        return self.repository.save(puzzle)
