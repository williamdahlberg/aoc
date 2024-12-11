from collections import Counter


def blink(stone, num):
    if stone == "0":
        return Counter({"1": num})
    elif len(stone) % 2 == 0:
        half1 = stone[: len(stone) // 2]
        half2 = str(int(stone[len(stone) // 2 :]))
        return Counter({half1: num}) + Counter({half2: num})
    else:
        return Counter({str(int(stone) * 2024): num})


stones = open("11.input").read().split()
c = Counter(stones)
for i in range(75):
    new_c = Counter()
    for stone, amount in c.items():
        new_c += blink(stone, amount)
        c = new_c

print(c.total())
