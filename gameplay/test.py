from brain import Brain
from puzzle import Puzzle

words_hints = {"color":"feature of every object","trolley":"for shop items",
                   "rock":"hard","mice":"runs from cat","key":"unlocks"}
solution = "clock"

puzzle = Puzzle(words_hints,solution)

brain = Brain(puzzle)

matrix = brain.words_matrix

for row in matrix:
    print(row)

for row in brain.logic_matrix:
    print(row)
