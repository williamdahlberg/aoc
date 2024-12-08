from copy import copy


with open("6.input") as f:
    lines = [l.strip() for l in f.readlines()]


def find_start(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            match char:
                case "^":
                    return (j, i), (0, -1)
                case "v":
                    return (j, i), (0, 1)
                case "<":
                    return (j, i), (-1, 0)
                case ">":
                    return (j, i), (1, 0)


def turn_right(direction):
    return {
        (0, -1): (1, 0),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (1, 0): (0, 1),
    }[direction]


def get_char(pos, grid):
    return grid[pos[1]][pos[0]]


def get_next(pos, direction):
    return tuple(map(sum, zip(pos, direction)))


def walk(pos, direction, grid):
    new_pos = get_next(pos, direction)
    if get_char(new_pos, grid) == "#":
        direction = turn_right(direction)
    new_pos = get_next(pos, direction)
    if get_char(new_pos, grid) == "#":
        direction = turn_right(direction)
    new_pos = get_next(pos, direction)

    if -1 in new_pos:
        raise IndexError()

    return new_pos, direction


def find_cells():
    position, direction = find_start(lines)
    print(f"start: {position=}, {direction=}")
    found = set()
    found.add(position)
    while True:
        try:
            position, direction = walk(position, direction, lines)
        except IndexError:
            return found

        found.add(position)


def calc():
    print(len(find_cells()))


# part 2
def get_new_grid(pos, char):
    new_grid = copy(lines)
    old_line = new_grid[pos[1]]
    new_line = old_line[: pos[0]] + char + old_line[pos[0] + 1 :]
    new_grid[pos[1]] = new_line
    return new_grid


def find_working_positions():
    working_positions = set()
    for x, y in find_cells():
        pos = (x, y)
        if get_char(pos, lines) != ".":
            continue
        new_grid = get_new_grid(pos, "#")
        if try_position(new_grid):
            working_positions.add(pos)
    return working_positions


def try_position(grid):
    vector = find_start(grid)
    found = set()
    found.add(vector)
    while True:
        try:
            vector = walk(*vector, grid)
        except IndexError:
            return False

        if vector in found:
            return True
        found.add(vector)


calc()
print(len(find_working_positions()))
