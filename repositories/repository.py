import oracledb
from gameplay.puzzle import Puzzle
from configparser import ConfigParser


def reformat(query_result):
    return str(query_result).replace("(", "").replace(")", ",").replace(",", "").replace("\'", "")


def connect():
    # read configurations
    configur = ConfigParser()
    configur.read('configuration/config.ini')

    user = str(configur.get('database', 'username'))
    password = str(configur.get('database', 'password'))
    link = str(configur.get('database', 'host')) + "/" + str(configur.get('database', 'service'))

    return oracledb.connect(user=user, password=password, dsn=link)


class Repository:
    def __init__(self):
        self.connection = connect()
        self.cursor = self.connection.cursor()

    def find(self, puzzle_id):
        # execute statement
        self.cursor.execute(
            "select correct_word,hint from game join puzzle on game.gameId = puzzle.gameId where game.gameId = " + str(
                puzzle_id) + " order by puzzle.puzzleId")

        # word -> hint dictionary
        word_hint = dict()
        for row in self.cursor:
            word_hint[row[0]] = row[1]

        # execute statement
        self.cursor.execute("select solution from game where gameId = " + str(puzzle_id))

        # solution
        solution = reformat(self.cursor.fetchone())

        # new puzzle object
        return Puzzle(words_hints_map=word_hint, solution=solution)

    def save(self, puzzle):
        # save new game instance
        game_id = int(self.find_max_game_id()) + 1
        self.cursor.execute(
            "insert into game (solution,gameId) values(" + str('\'' + puzzle.solution + '\'') + "," + str(
                game_id) + ")")

        # save puzzle instances
        for (word, hint) in puzzle.words_hints_map.items():
            puzzle_id = int(self.find_max_puzzle_id()) + 1
            self.cursor.execute(
                "insert into puzzle (gameId,correct_word,hint,puzzleId) "
                "values(" + str(game_id) + "," + str('\'' + word + '\'') + "," + str('\'' + hint + '\'') +
                "," + str(puzzle_id) + ")")

        self.connection.commit()

    def find_max_game_id(self):
        # find the greatest id
        max_id = reformat(self.cursor.execute("select max(gameId) from game").fetchone())
        return max_id

    def find_max_puzzle_id(self):
        # find the greatest id
        max_id = reformat(self.cursor.execute("select max(puzzleId) from puzzle").fetchone())
        return max_id

    def list_all_game_ids(self):
        game_ids = reformat(self.cursor.execute("select gameId from game").fetchall())
        game_ids = [int(game_id) for game_id in game_ids.replace("[","").replace("]","").split(" ")]
        return game_ids


if __name__ == '__main__':
    connect()
