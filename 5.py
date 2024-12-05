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
    correct = []
    incorrect = []
    rules = rules_dict()
    for p in print_lines:
        numbers = list(map(int, p.split(",")))
        for i, n in enumerate(numbers):
            before_me = set(numbers[:i])
            intersection = set.intersection(rules[n], before_me)
            if intersection:
                incorrect.append(numbers)
                # incorrect
                break
        else:
            correct.append(numbers)

    return correct, incorrect


def middle(l):
    return l[int(len(l) / 2)]


def calc_correct():
    return sum(middle(p) for p in correct_prints()[0])


# Part 2