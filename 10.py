grid = {
    x + y * 1j: (int(n), set())
    for y, r in enumerate(open("10.input").readlines())
    for x, n in enumerate(r.strip())
}


def path(zero_c, c, visited=None):
    visited = visited.add(c) if visited else set()
    for dir in (1, -1, 1j, -1j):
        new_n, new_s = grid.get(c + dir, (0, {}))
        if new_n == grid[c][0] + 1:
            new_s.add(zero_c)
            path(zero_c, c + dir, visited)


for c in grid:
    if grid[c][0] == 0:
        path(c, c)

print(sum([len(s) for _, (n, s) in grid.items() if n == 9]))
