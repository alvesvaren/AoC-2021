import aoc
import re
from itertools import chain
from collections import defaultdict

data = aoc.get_input(5).splitlines()

normal_vents = defaultdict(int)
all_vents = defaultdict(int)

max_x, max_y = 0, 0

for line in data:
    start, end = line.split(" -> ")
    x1, y1, x2, y2 = map(int, chain(start.split(","), end.split(",")))
    
    if (x1 == x2) or (y1 == y2):
        for x in range(min(x1, x2), max(x1, x2)+1):
            if x > max_x:
                max_x = x
            for y in range(min(y1, y2), max(y1, y2)+1):
                if y > max_y:
                    max_y = y
                normal_vents[(x, y)] += 1
                all_vents[(x, y)] += 1

    else:
        x_range = range(x1, x2+1) if x1 <= x2 else range(x1, x2-1, -1)
        y_range = range(y1, y2+1) if y1 <= y2 else range(y1, y2-1, -1)

        for ix, x in enumerate(x_range):
            for iy, y in enumerate(y_range):
                if ix == iy:
                    all_vents[(x, y)] += 1



count1 = sum(lines_at_coord >= 2 for _, lines_at_coord in normal_vents.items())
count2 = sum(lines_at_coord >= 2 for _, lines_at_coord in all_vents.items())

print("Part 1:", count1)
print("Part 2:", count2)
