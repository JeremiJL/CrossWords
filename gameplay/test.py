from brain import *
from puzzle import Puzzle
from repositories import repository
from services import service

words_hints = {"color":"feature of every object","trolley":"for shop items",
                   "rock":"hard","mice":"runs from cat","key":"unlocks"}
solution = "clock"

puzzle = Puzzle(words_hints,solution)

# brain = Brain(puzzle)
#
# matrix = brain.words_matrix
#
# for row in matrix:
#     print(row)
#
# for row in brain.logic_matrix:
#     print(row)


service = service.Service()
repo = service.repository

print(repo.find(1).words_hints_map)

# repo.save(puzzle)
# repo.find_max_id()

print(repo.list_all_game_ids())

matrix = create_matrix(puzzle)

for row in matrix:
    for el in row:
        print(el, end=", ")
    print("")


print(validate_words(["color","trolley","rock","mice","key"],puzzle))


