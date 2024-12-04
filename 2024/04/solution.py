import re
import numpy as np


def p1():
    with open("input.txt") as f:
        input = [r.strip() for r in f.readlines()]

    as_arr = np.array([np.array(list(r)) for r in input])

    row_strings = input.copy()
    col_strings = ["".join(c.tolist()) for c in as_arr.T.copy()]
    rl_diagonal_strings = [
        "".join(np.diagonal(as_arr, i).tolist())
        for i in range(-as_arr.shape[1], as_arr.shape[0])
    ]
    lr_diagonal_strings = [
        "".join(np.diagonal(np.fliplr(as_arr), i).tolist())
        for i in range(-as_arr.shape[1], as_arr.shape[0])
    ]

    res = 0
    for s in (
        row_strings
        + ["_"]
        + col_strings
        + ["_"]
        + rl_diagonal_strings
        + ["_"]
        + lr_diagonal_strings
    ):
        res += len(re.findall(r"XMAS", s))
        res += len(re.findall(r"XMAS", s[::-1]))

    print("solution1: ", res)


def p2():
    with open("input.txt") as f:
        input = [r.strip() for r in f.readlines()]

    as_arr = np.array([np.array(list(r)) for r in input])

    conv_kernel_1 = np.array([["M", "_", "S"], ["_", "A", "_"], ["M", "_", "S"]])
    conv_kernel_2 = np.array([["M", "_", "M"], ["_", "A", "_"], ["S", "_", "S"]])
    conv_kernel_3 = np.array([["S", "_", "S"], ["_", "A", "_"], ["M", "_", "M"]])
    conv_kernel_4 = np.array([["S", "_", "M"], ["_", "A", "_"], ["S", "_", "M"]])

    conv_kernesl = [conv_kernel_1, conv_kernel_2, conv_kernel_3, conv_kernel_4]

    res = 0
    for row in range(as_arr.shape[0] - 2):
        for col in range(as_arr.shape[1] - 2):
            sub_arr = as_arr[row : row + 3, col : col + 3]
            for conv_kernel in conv_kernesl:
                if np.all(np.where(conv_kernel == "_", True, sub_arr == conv_kernel)):
                    res += 1

    print("solution2: ", res)


p1()
p2()
