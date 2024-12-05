from collections import defaultdict
import functools
import itertools


with open("5.input") as f:
    lines = [l.strip() for l in f.readlines()]


rule_lines = itertools.takewhile(lambda l: "|" in l, lines)
print_lines = itertools.takewhile(lambda l: "," in l, lines[::-1])


def rules_dict():
    rules = defaultdict(set)
    for rl in rule_lines:
        b, a = list(map(int, rl.split("|")))
        rules[b].add(a)
    return rules


def correct_prints():
    total = 0
    rules = rules_dict()
    for p in print_lines:
        numbers = list(map(int, p.split(",")))
        for i, n in enumerate(numbers):
            before_me = set(numbers[:i])
            intersection = set.intersection(rules[n], before_me)
            if intersection:
                # incorrect
                break
        else:
            total += middle(numbers)

    return total


def middle(l):
    return l[int(len(l) / 2)]


print(correct_prints())
