from tabnanny import check
import aoc
from pprint import pprint
from itertools import chain

numbers, *_boards = aoc.get_input(4).split("\n\n")

numbers = *map(int, numbers.strip().split(",")),
_boards = [board.replace("  ", " ") for board in _boards]

boards = []


def check_bingo(board: list[list[int]], marked: list[int]):
    for row in board:
        if all(x in marked for x in row):
            return True
    
    for col in zip(*board):
        if all(x in marked for x in col):
            return True

def calc_sum(board: list[list[int]], number: int):
    numsum = sum(filter(lambda x: x not in drawn, chain(*board)))
    return numsum * number

for board in _boards:
    board = board.splitlines()
    board = [[int(num) for num in line.strip().split(" ")] for line in board]
    boards.append(board)

drawn = []
boards_won = set()
boards_indexes = set(range(len(boards)))

part1 = None
part2 = None

for number in numbers:
    drawn.append(number)
    for i, board in enumerate(boards):
        if check_bingo(board, drawn):
            boards_won.add(i)
            if part1 is None:
                part1 = calc_sum(board, number)
        boards_not_won = boards_won ^ boards_indexes
        if len(boards_not_won) == 1:
            part2 = calc_sum(boards[next(iter(boards_not_won))], number)


print("Part 1:", part1)
print("Part 2:", part2)