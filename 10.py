grid = {
    x + y * 1j: (int(n), list())
    for y, r in enumerate(open("10.input").readlines())
    for x, n in enumerate(r.strip())
}


def path(zero_c, c):
    for dir in (1, -1, 1j, -1j):
        new_n, new_s = grid.get(c + dir, (0, []))
        if new_n == grid[c][0] + 1:
            new_s.append(zero_c)
            path(zero_c, c + dir)


[path(c, c) for c in grid if grid[c][0] == 0]
print(list(map(sum, zip(*[(len(set(s)), len(s)) for n, s in grid.values() if n == 9]))))
