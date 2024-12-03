def valid_level_checker(r):
    increasing = all(r[i] < r[i + 1] for i in range(len(r) - 1))
    decreasing = all(r[i] > r[i + 1] for i in range(len(r) - 1))
    max_dist_less_than_3 = all(abs(r[i] - r[i + 1]) <= 3 for i in range(len(r) - 1))

    return max_dist_less_than_3 and (increasing or decreasing)


def p1():
    with open("input.txt") as f:
        reports = f.read().splitlines()
        reports = [[int(x) for x in line.split(" ")] for line in reports]

    res = 0
    for r in reports:
        valid = valid_level_checker(r)
        if valid:
            res += 1

    print("solution1: ", res)


def p2():
    with open("input.txt") as f:
        reports = f.read().splitlines()
        reports = [[int(x) for x in line.split(" ")] for line in reports]

    res = 0
    for r in reports:
        valid = valid_level_checker(r)
        if valid:
            res += 1
        else:
            for i in range(len(r)):
                r_copy = r.copy()
                r_copy.pop(i)
                valid = valid_level_checker(r_copy)
                if valid:
                    res += 1
                    break

    print("solution2: ", res)


p1()
p2()
