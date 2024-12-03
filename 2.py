with open("2.input") as f:
    lines = f.readlines()

safe_report_count = 0


def is_safe(levels):
    diffs = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]
    if set(diffs) <= {1, 2, 3} or set(diffs) <= {-1, -2, -3}:
        return True


for report in lines:
    levels = list(map(int, report.split(" ")))
    if is_safe(levels):
        safe_report_count += 1
    else:
        # part 2
        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i + 1 :]):
                safe_report_count += 1
                break

print(f"{safe_report_count=}")
