from brain import Brain
from puzzle import Puzzle
from repositories import repository

words_hints = {"color":"feature of every object","trolley":"for shop items",
                   "rock":"hard","mice":"runs from cat","key":"unlocks"}
solution = "pompelon"

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


repo = repository.Repository()

repo.save(puzzle)
# repo.find_max_id()

print(repo.list_all_game_ids())