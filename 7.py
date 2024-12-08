from operator import add, mul


with open("7.input") as f:
    lines = [l.strip() for l in f.readlines()]


def cat(x, y):
    return int(f"{x}{y}")


def get_values(numbers):
    values = [numbers[0]]
    for n in numbers[1:]:
        values = [op(v, n) for v in values for op in (mul, add, cat)]
    return values


total = 0
for line in lines:
    result, *numbers = list(map(int, line.replace(":", "").split()))

    total += result if result in get_values(numbers) else 0
print(total)

# p1 right 12940396350192
# p2 wrong 12940396445074
