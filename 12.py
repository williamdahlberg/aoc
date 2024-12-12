def measure(coord):
    char, visited = grid.get(coord, ("", True))
    if visited:
        return 0, 0, 0
    grid[coord] = (char, True)

    area, perimeter, edges = 1, 0, 0
    for dir in (1j, -1j, 1, -1):
        if grid.get(coord + dir, ("", True))[0] != char:
            perimeter += 1
            right = coord + dir * 1j
            top_right = coord + dir + dir * 1j
            if (
                grid.get(right, ("", ""))[0] != char
                or grid.get(top_right, ("", ""))[0] == char
            ):
                edges += 1

        else:
            a, p, e = measure(coord + dir)
            area += a
            perimeter += p
            edges += e

    return area, perimeter, edges


grid = {
    x + y * 1j: (c, False)
    for y, l in enumerate(open("12.input").readlines())
    for x, c in enumerate(l.strip())
}

measures = [measure(coord) for coord in grid]
print(list(map(sum, zip(*[(a * p, a * e) for a, p, e in measures]))))
