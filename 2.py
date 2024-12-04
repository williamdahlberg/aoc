with open("2.input") as f:
    lines = f.readlines()

safe_reports = []
unsafe = []


def is_safe(levels):
    diffs = set(levels[i] - levels[i + 1] for i in range(len(levels) - 1))
    if diffs <= {1, 2, 3} or diffs <= {-1, -2, -3}:
        return True


def brute():
    for report in lines:
        levels = list(map(int, report.split(" ")))
        if is_safe(levels):
            safe_reports.append(report)
        else:
            # part 2
            for i in range(len(levels)):
                if is_safe(levels[:i] + levels[i + 1 :]):
                    safe_reports.append(report)
                    break
            else:
                unsafe.append(report)


## non-brute
def is_safe2(levels):
    # assuming increasing
    skipped = False
    i = 1
    while i < len(levels):
        diff = levels[i] - levels[i - 1]
        if not diff in (1, 2, 3):
            if skipped:
                return False
            skipped = True

            if i == len(levels) - 1:
                # Last level removed
                return True

            curr_skip = True
            diff = levels[i + 1] - levels[i - 1]
            if not diff in (1, 2, 3):
                curr_skip = False

            prev_skip = True
            if i == 1:
                prev_skip = False
            else:
                diff = levels[i] - levels[i - 2]
                if not diff in (1, 2, 3):
                    prev_skip = False

            if curr_skip and prev_skip:
                return False

            if curr_skip:
                i += 1

        i += 1
    return True


safe_non = []
unsafe_non = []


def non_brute():
    for report in lines:
        levels = list(map(int, report.split(" ")))
        if is_safe2(levels) or is_safe2(levels[::-1]):
            safe_non.append(report)
        else:
            unsafe_non.append(report)


# brute()
# non_brute()

# print(set(unsafe) - set(unsafe_non))


print(is_safe2([11, 12, 16, 17, 20, 21, 23, 24]))
non_brute()
print(len(safe_non))
