from collections import defaultdict
from itertools import product, combinations

lines = [l.strip() for l in open("8.input").readlines()]
size = width, height = len(lines[0]), len(lines)
coordinates = list(product(range(width), range(height)))
grid = {(x, y): lines[y][x] for x, y in coordinates}
symbols = defaultdict(list)
[symbols[grid[c]].append(c) for c in coordinates if grid[c] != "."]

pairs = []
for coords in symbols.values():
    pairs.extend(list(combinations(coords, r=2)))

interferences = set()
for pair in pairs:
    (x1, y1), (x2, y2) = pair
    interferences |= {(x1, y1), (x2, y2)}
    xdiff = x2 - x1
    ydiff = y2 - y1

    new1 = (x1 - xdiff, y1 - ydiff)
    while grid.get(new1, None):
        interferences.add(new1)
        new1 = (new1[0] - xdiff, new1[1] - ydiff)

    new2 = (x1 + xdiff, y1 + ydiff)
    while grid.get(new2, None):
        interferences.add(new2)
        new2 = (new2[0] + xdiff, new2[1] + ydiff)

    if grid.get(new1, None):
        interferences.add(new1)
    if grid.get(new2, None):
        interferences.add(new2)

print(len(interferences))
