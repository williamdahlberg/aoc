from copy import copy


with open("6.input") as f:
    grid = [l.strip() for l in f.readlines()]


def find_start():
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


def get_char(pos):
    return grid[pos[1]][pos[0]]


def get_next(pos, direction):
    return tuple(map(sum, zip(pos, direction)))


def walk(pos, direction):
    new_pos = get_next(pos, direction)
    if get_char(new_pos) == "#":
        direction = turn_right(direction)
    new_pos = get_next(pos, direction)
    if get_char(new_pos) == "#":
        direction = turn_right(direction)
    new_pos = get_next(pos, direction)

    if -1 in new_pos:
        raise IndexError()

    return new_pos, direction


def find_cells():
    position, direction = find_start()
    print(f"start: {position=}, {direction=}")
    found = set()
    found.add(position)
    while True:
        try:
            position, direction = walk(position, direction)
        except IndexError:
            return found

        found.add(position)


def calc():
    print(len(find_cells()))


print(calc())
