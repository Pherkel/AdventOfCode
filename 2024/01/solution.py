from collections import defaultdict
import numpy as np


def p1():
    with open("input.txt") as f:
        input = f.read().splitlines()
        input = np.array(
            [[int(x) for x in line.split("   ")] for line in input], dtype=int
        )

    sorted = np.sort(input, axis=0).T
    abs_diff = np.abs(np.diff(sorted, axis=0))
    print("solution1: ", np.sum(abs_diff))


def p2():
    with open("input.txt") as f:
        input = f.read().splitlines()
        input = np.array(
            [[int(x) for x in line.split("   ")] for line in input], dtype=int
        )

    lookup = defaultdict(int)
    for m in input[:, 1]:
        print(m)
        lookup[m] += 1

    res = 0
    for n in input[:, 0]:
        res += n * lookup[n]

    print("solution2: ", res)


p1()
p2()
