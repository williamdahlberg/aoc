from itertools import repeat, takewhile

line = open("9.input").read().strip()


def create_disk(l):
    disk = []
    for i, char in enumerate(l, start=1):
        disk.extend(repeat(-1 if (i / 2).is_integer() else i // 2, times=int(char)))
    return disk


def calc(l):
    return sum([i * n for i, n in enumerate(l) if n != -1])


# part 1
def shift(l):
    for n in reversed(l):
        if n == -1:
            l = l[:-1]
            continue
        try:
            first_empty = l.index(-1)
        except ValueError:
            return l

        l = l[:first_empty] + [n] + l[first_empty + 1 : -1]

    return l


# part 2


def file_shift(l):
    for block_id in reversed(range(10000)):
        try:
            old_ix = l.index(block_id)
        except ValueError:
            continue
        block_len = len(list(takewhile(lambda x: x == block_id, l[old_ix:])))
        old_end_ix = old_ix + block_len
        new_ix = find_spot(l, block_len)
        if new_ix and new_ix < old_ix:
            l = (
                l[:new_ix]
                + list(repeat(block_id, block_len))
                + [
                    -1 if x == block_id else x
                    for x in l[new_ix + block_len : old_end_ix]
                ]
                + l[old_ix + block_len :]
            )
    return l


def find_spot(l, s):
    i = 0
    count = 0
    while i < len(l):
        if count >= s:
            return i - s
        if l[i] == -1:
            count += 1
        else:
            count = 0
        i += 1
    return None


print(calc(file_shift(create_disk(line))))
