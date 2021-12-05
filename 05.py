import aoc
from itertools import chain
from collections import defaultdict

data = aoc.get_input(5).splitlines()

normal_vents = defaultdict(int)
all_vents = defaultdict(int)

for line in data:
    start, end = line.split(" -> ")
    x1, y1, x2, y2 = map(int, chain(start.split(","), end.split(",")))

    if (x1 == x2) or (y1 == y2):
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                normal_vents[(x, y)] += 1
                all_vents[(x, y)] += 1
    else:
        for ix, x in enumerate(range(x1, x2+1) if x1 <= x2 else range(x1, x2-1, -1)):
            all_vents[(x, y1 + (ix if y2 > y1 else -ix))] += 1


count1 = sum(count >= 2 for count in normal_vents.values())
count2 = sum(count >= 2 for count in all_vents.values())

print("Part 1:", count1)
print("Part 2:", count2)
