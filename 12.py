from operator import mul


grid = {
    x + y * 1j: (c, False)
    for y, l in enumerate(open("12.input").readlines())
    for x, c in enumerate(l.strip())
}


def measure(coord):
    char, visited = grid[coord]
    if visited:
        return 0, 0
    grid[coord] = (char, True)

    area, perimeter = 1, 0
    for dir in (1j, -1j, 1, -1):
        new_coord = coord + dir
        if not new_coord in grid:
            perimeter += 1
        elif grid[new_coord][0] == grid[coord][0]:
            a, p = measure(new_coord)
            area += a
            perimeter += p
        else:
            perimeter += 1

    return area, perimeter


measures = [measure(coord) for coord in grid]
print(sum(map(mul, *zip(*measures))))
