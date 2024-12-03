import re

with open("3.input") as f:
    memory = f.read()


def find_total(memory_string):
    total = 0
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", memory_string):
        total += int(match.group(1)) * int(match.group(2))

    return total


# part 2
total = 0
dos = memory.split("do()")
for do in dos:
    parts = do.split("don't()")
    total += find_total(parts[0])

print(total)
