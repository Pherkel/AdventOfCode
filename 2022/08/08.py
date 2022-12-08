import numpy as np

with open("2022/08/input") as input:
    data = np.asarray([list(x.strip()) for x in input.readlines()], int)


def solve1():
    dim_x = len(data[0])
    dim_y = len(data)

    res = 0
    for y in range(dim_y):
        for x in range(dim_x):
            v1 = True
            v2 = True
            v3 = True
            v4 = True

            # check all above
            for i in range(y):
                if data[i][x] >= data[y][x]:
                    v1 = False
                    break

            # check all below
            for i in range(dim_y - y - 1):
                #print(f"comaring {data[y + i][x]} >= {data[y][x]} ==> {data[y + i][x] >= data[y][x]}")
                if data[y + i + 1][x] >= data[y][x]:
                    v2 = False
                    break

            # check all left
            for i in range(x):
                if data[y][i] >= data[y][x]:
                    v3 = False

            # check all right
            for i in range(dim_x - x - 1):
                if data[y][x+i + 1] >= data[y][x]:
                    v4 = False

            if (v1 or v2 or v3 or v4):
                res += 1

    return res


def solve2():
    dim_x = len(data[0])
    dim_y = len(data)

    scores = []

    for y in range(1, dim_y):
        for x in range(1, dim_x):
            v1 = 0
            v2 = 0
            v3 = 0
            v4 = 0

            # check all above
            for i in reversed(range(y)):
                v1 += 1
                if data[i][x] >= data[y][x]:
                    break

            # check all below
            for i in range(dim_y - y - 1):
                v2 += 1
                if data[y + i + 1][x] >= data[y][x]:
                    break

            # check all left
            for i in reversed(range(x)):
                v3 += 1
                if data[y][i] >= data[y][x]:
                    break

            # check all right
            for i in range(dim_x - x - 1):
                v4 += 1
                if data[y][x + i + 1] >= data[y][x]:
                    break

            scores.append(v1*v2*v3*v4)

    return max(scores)


print(solve1())
print(solve2())
