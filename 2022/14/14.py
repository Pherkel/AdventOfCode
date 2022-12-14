import numpy as np

temp = [x.strip().split() for x in open("2022/14/input")]
data = []
for path in temp:
    data.append([(int(x.split(",")[0]), (int(x.split(",")[1])))
                for x in path if x != "->"])

grid = np.full((546, 170), ".")

start = (500, 0)

max_depth = 0

for ding in data:
    for idx in range(1, len(ding)):
        left_x = ding[idx-1][0]
        right_x = ding[idx][0]
        left_y = ding[idx-1][1]
        right_y = ding[idx][1]

        right_x += 1 if left_x < right_x else -1
        right_y += 1 if left_y < right_y else -1
        for x in range(left_x, right_x, 1 if left_x < right_x else -1):
            for y in range(left_y, right_y, 1 if left_y < right_y else -1):
                if y > max_depth:
                    max_depth = y

                grid[x][y] = "#"

print(f"max depth: {max_depth}")


def down(sand):
    return grid[sand[0]][sand[1]+1]


def left(sand):
    return grid[sand[0]-1][sand[1]]


def right(sand):
    return grid[sand[0]+1][sand[1]]


def down_left(sand):
    return grid[sand[0]-1][sand[1]+1]


def down_right(sand):
    return grid[sand[0]+1][sand[1]+1]


i_count = 0
sand = start

# move down until hitting something
while sand[1] <= max_depth:

    if down(sand) == '.':
        sand = (sand[0], sand[1]+1)
        continue

    # moving to the left
    if down_left(sand) == ".":
        sand = (sand[0]-1, sand[1]+1)
        continue

    # moving to the right
    if down_right(sand) == ".":
        sand = (sand[0]+1, sand[1]+1)
        continue

    # hit something but both sides are blocked
    grid[*sand] = "O"
    sand = start
    i_count += 1

print(i_count)
