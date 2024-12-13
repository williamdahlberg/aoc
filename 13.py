from collections import defaultdict
from functools import cache
import re


def find_xy(line):
    m = next(re.finditer(r"X[\+=](\d+).*Y[\+=](\d+)", line))
    return int(m[1]), int(m[2])


claws = []
for machine in open("13.input").read().split("\n\n"):
    lines = machine.split("\n")
    a = find_xy(lines[0])
    b = find_xy(lines[1])
    t = find_xy(lines[2])
    claws.append((a, b, t))


claw_tokens = defaultdict(list)


@cache
def press(claw_id, button_a, button_b, pressed_a, pressed_b, target):
    reached_x = button_a[0] * pressed_a + button_b[0] * pressed_b
    reached_y = button_a[1] * pressed_a + button_b[1] * pressed_b
    reached = reached_x, reached_y
    if reached == target:
        claw_tokens[claw_id].append(pressed_a * 3 + pressed_b)
        return
    target_x, target_y = target
    if reached_x > target_x or reached_y > target_y:
        return
    if pressed_a < 100:
        press(claw_id, button_a, button_b, pressed_a + 1, pressed_b, target)
    if pressed_b < 100:
        press(claw_id, button_a, button_b, pressed_a, pressed_b + 1, target)


for i, claw in enumerate(claws):
    a, b, t = claw
    press(i, a, b, 0, 0, t)

print(sum([min(v) for v in claw_tokens.values()]))
