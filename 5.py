from collections import defaultdict
from copy import copy
import functools
import itertools


with open("5.input") as f:
    lines = [l.strip() for l in f.readlines()]


rule_lines = itertools.takewhile(lambda l: "|" in l, lines)
print_lines = itertools.takewhile(lambda l: "," in l, lines[::-1])


@functools.lru_cache()
def rules_dict():
    rules = defaultdict(set)
    for rl in rule_lines:
        b, a = list(map(int, rl.split("|")))
        rules[b].add(a)
    return rules


def divided_prints():
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
    return sum(middle(p) for p in divided_prints()[0])


# Part 2
def fix_incorrect():
    fixed = []
    rules = rules_dict()
    for p in divided_prints()[1]:
        new_p = copy(p)
        for i in range(len(new_p)):
            n = new_p[i]
            # Find error before
            for j in range(i):
                m = new_p[j]
                if m in rules[n]:
                    # It's the earliest instance of something n needs to be before
                    new_p = new_p[:j] + [n] + new_p[j:i] + new_p[i + 1 :]
                    break
        fixed.append(new_p)

    return fixed


def calc_incorrect():
    return sum(middle(p) for p in fix_incorrect())


print(calc_incorrect())
