import re

with open("input.txt") as f:
    i = f.read().strip()

test_input = """Time:      7  15   30
Distance:  9  40  200"""


def solution_1(input):
    time, distance = input.split("\n")
    time, distance = re.findall(r"\d+", time), re.findall(r"\d+", distance)
    time, distance = [int(i) for i in time], [int(i) for i in distance]

    res = 1
    for t, d in zip(time, distance):
        num = 0
        for accel in range(t):
            if (t - accel) * accel > d:
                num += 1
        res *= num
    print("Solution 1: ")
    print(res)
    print()


def solution_2(input):
    time, distance = input.split("\n")
    time, distance = re.findall(r"\d+", time), re.findall(r"\d+", distance)
    time, distance = "".join(time), "".join(distance)
    time, distance = int(time), int(distance)

    res = 0
    for accel in range(time):
        if (time - accel) * accel > distance:
            res += 1

    print("Solution 2: ")
    print(res)


if __name__ == "__main__":
    solution_1(i)
    solution_2(i)
