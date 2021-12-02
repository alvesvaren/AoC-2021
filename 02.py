from typing import Callable
import aoc

data = aoc.get_input(2).splitlines()

pos1, depth1 = 0, 0
pos2, depth2 = 0, 0

for instruction in data:
    name, count = instruction.split()
    count = int(count)

    if name == "down":
        depth1 += count
    elif name == "up":
        depth1 -= count
    elif name == "forward":
        pos1 += count

aim = 0

for instruction in data:
    name, count = instruction.split()
    count = int(count)

    if name == "down":
        aim += count
    elif name == "up":
        aim -= count
    elif name == "forward":
        pos2 += count
        depth2 += aim * count

print("Part 1:", pos1 * depth1)
print("Part 2:", pos2 * depth2)
