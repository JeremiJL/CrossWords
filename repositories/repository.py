import oracledb
from gameplay.puzzle import Puzzle
from configparser import ConfigParser

connection = None
cursor = None


def connect():
    # read configurations
    configur = ConfigParser()
    configur.read('../configuration/config.ini')

    user = str(configur.get('repositories', 'username'))
    password = str(configur.get('repositories', 'password'))
    link = str(configur.get('repositories', 'host')) + "/" + str(configur.get('repositories', 'service'))

    global connection
    connection = oracledb.connect(user=user, password=password, dsn=link)
    global cursor
    cursor = connection.cursor()


def reformat(query_result):
    return str(query_result).replace("(", "").replace(")", ",").replace(",", "")


def get_max_index():
    cursor.execute("select max(gameId) from game")
    return reformat(cursor.fetchone())


def get_puzzle(puzzleId):

    # execute statement
    cursor.execute("select correct_word,hint from game join puzzle on game.gameId = puzzle.gameId where game.gameId = " + str(puzzleId) + " order by puzzle.puzzleId")

    # word -> hint dictionary
    word_hint = dict()
    for row in cursor:
        word_hint[row[0]] = row[1]

    # execute statement
    cursor.execute("select solution from game where gameId = " + str(puzzleId))

    # solution
    solution = reformat(cursor.fetchone())
    # new puzzle object
    return Puzzle(words_hints_map=word_hint, solution=solution)


if __name__ == '__main__':
    connect()
