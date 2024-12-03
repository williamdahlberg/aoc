with open("1.input") as f:
    lines = f.readlines()

lefts, rights = [], []
for line in lines:
    first, second = line.split("   ")
    lefts.append(int(first))
    rights.append(int(second))

difflist = zip(sorted(lefts), sorted(rights))
diff = sum(abs(f - s) for f, s in difflist)
print(f"{diff=}")

# Part 2
from collections import Counter

left_counts = Counter(lefts)
right_counts = Counter(rights)

sim = 0
for n, c in left_counts.items():
    sim += n * c * right_counts[n]

print(f"{sim=}")
