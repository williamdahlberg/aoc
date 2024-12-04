with open("4.input") as f:
    lines = [l.strip() for l in f.readlines()]

size = x, y = len(lines), len(lines[0])


def xmas():
    xmases = 0
    for i in range(x):
        for j in range(y):
            if lines[i][j] == "X":
                # forward
                if (
                    j + 3 < y
                    and lines[i][j + 1] + lines[i][j + 2] + lines[i][j + 3] == "MAS"
                ):
                    xmases += 1
                # backward
                if (
                    j - 3 >= 0
                    and lines[i][j - 1] + lines[i][j - 2] + lines[i][j - 3] == "MAS"
                ):
                    xmases += 1
                # down
                if (
                    i + 3 < x
                    and lines[i + 1][j] + lines[i + 2][j] + lines[i + 3][j] == "MAS"
                ):
                    xmases += 1
                # up
                if (
                    i - 3 >= 0
                    and lines[i - 1][j] + lines[i - 2][j] + lines[i - 3][j] == "MAS"
                ):
                    xmases += 1

                # diagonal down right
                if (
                    j + 3 < y
                    and i + 3 < x
                    and lines[i + 1][j + 1] + lines[i + 2][j + 2] + lines[i + 3][j + 3]
                    == "MAS"
                ):
                    xmases += 1

                # diagonal down left
                if (
                    j - 3 >= 0
                    and i + 3 < x
                    and lines[i + 1][j - 1] + lines[i + 2][j - 2] + lines[i + 3][j - 3]
                    == "MAS"
                ):
                    xmases += 1

                # diagonal up right
                if (
                    j + 3 < y
                    and i - 3 >= 0
                    and lines[i - 1][j + 1] + lines[i - 2][j + 2] + lines[i - 3][j + 3]
                    == "MAS"
                ):
                    xmases += 1

                # diagonal up left
                if (
                    j - 3 >= 0
                    and i - 3 >= 0
                    and lines[i - 1][j - 1] + lines[i - 2][j - 2] + lines[i - 3][j - 3]
                    == "MAS"
                ):
                    xmases += 1

    return xmases


# part 2
def x_mas():
    x_mases = 0
    for i in range(1, x - 1):
        for j in range(1, y - 1):
            if lines[i][j] == "A":
                mases = 0
                if lines[i - 1][j - 1] == "M" and lines[i + 1][j + 1] == "S":
                    mases += 1
                if lines[i - 1][j - 1] == "S" and lines[i + 1][j + 1] == "M":
                    mases += 1
                if lines[i - 1][j + 1] == "M" and lines[i + 1][j - 1] == "S":
                    mases += 1
                if lines[i - 1][j + 1] == "S" and lines[i + 1][j - 1] == "M":
                    mases += 1

                if mases == 2:
                    x_mases += 1
    return x_mases


print(x_mas())
