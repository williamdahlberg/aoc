with open("4.input") as f:
    lines = [l.strip() for l in f.readlines()]

size = x, y = len(lines), len(lines[0])


def get(i, j):
    if i < 0 or j < 0:
        return ""
    try:
        return lines[i][j]
    except IndexError:
        return ""


def xmas():
    xmases = 0
    for i in range(x):
        for j in range(y):
            if get(i, j) == "X":
                words = [
                    get(i, j + 1) + get(i, j + 2) + get(i, j + 3),
                    get(i, j - 1) + get(i, j - 2) + get(i, j - 3),
                    get(i + 1, j) + get(i + 2, j) + get(i + 3, j),
                    get(i - 1, j) + get(i - 2, j) + get(i - 3, j),
                    get(i + 1, j + 1) + get(i + 2, j + 2) + get(i + 3, j + 3),
                    get(i + 1, j - 1) + get(i + 2, j - 2) + get(i + 3, j - 3),
                    get(i - 1, j + 1) + get(i - 2, j + 2) + get(i - 3, j + 3),
                    get(i - 1, j - 1) + get(i - 2, j - 2) + get(i - 3, j - 3),
                ]

                xmases += words.count("MAS")

    return xmases


# part 2
def x_mas():
    x_mases = 0
    for i in range(1, x - 1):
        for j in range(1, y - 1):
            if lines[i][j] == "A":
                diag_1 = lines[i - 1][j - 1] + lines[i + 1][j + 1]
                diag_2 = lines[i - 1][j + 1] + lines[i + 1][j - 1]
                if {diag_1, diag_2} <= {"MS", "SM"}:
                    x_mases += 1

    return x_mases


print(xmas())
print(x_mas())
