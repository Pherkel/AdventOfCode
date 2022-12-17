import numpy as np
from multiprocessing import freeze_support, Pool


class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def __sub__(self, other):
        return T(x - y for x, y in zip(self, other))

    def __rmul__(self, other):
        return T(other * x for x in self)

    def __repr__(self): return f"({self[0]}, {self[1]})"

    def x(self): return self[0]
    def y(self): return self[1]

    @staticmethod
    def manhattan(s, b):
        return abs(s[0] - b[0]) + abs(s[1] - b[1])


data = [(
    T((int(x.split(" ")[2].split("=")[1].strip(",")),
      int(x.split(" ")[3].split("=")[1].strip(":")))),
    T((int(x.split(" ")[8].strip(",").split("=")[-1]), int(x.split(" ")[9].strip().split("=")[-1]))))
    for x in open("2022/15/input").readlines()]

print([x**2 for x in range(0, 10)])

# make first pass to determine the grid size and
# offsets in each direction to not get negative nums
# calculate maximum manhattan distance to extend grid properly
x_min = float("inf")
x_max = float("-inf")
y_min = float("inf")
y_max = float("-inf")
dist_max = 0

sensors = set([x[0] for x in data])
beacons = set([x[1] for x in data])

for s, b in data:
    x_min = min(s[0], b[1], x_min)
    x_max = max(s[0], b[0], x_max)
    y_min = min(s[1], b[1], y_min)
    y_max = max(s[1], b[1], y_max)
    dist_max = max(dist_max, T.manhattan(s, b))

# second attempt: just check for all x in the specified y if (x,y) is within a sensors range
# third attempt: multithread that bitch


def checker(startx, starty, endx, endy):
    for x in range(startx, endx):
        for y in range(starty, endy):
            curr = T((x, y))
            beacon = True
            for s, b in data:
                if T.manhattan(s, curr) <= T.manhattan(s, b) or curr in beacons or curr in sensors:
                    beacon = False
                    break
            if beacon:
                print(x*4000000 + 1, flush=True)


def main():
    length = 4000001
    size = 8
    """
    x_start = [x for x in range(0, 3500000, 500000)]
    x_end = [x for x in range(500000, 4000000, 500000)]
    y_start = [x for x in range(0, 3500000, 500000)]
    y_end = [x for x in range(500000, 4000000, 500000)]
    """

    temp = []

    for row in range(0, length, size):
        for col in range(0, length, size):
            temp.append((row, row+size, col, col+size))

    with Pool(8) as pool:
        L = pool.starmap(checker, temp)


if __name__ == "__main__":
    freeze_support()
    main()


"""
for x in range(0, 4000001):
    for y in range(0, 4000001):
        curr = T((x, y))
        beacon = True
        for s, b in data:
            if T.manhattan(s, curr) <= T.manhattan(s, b) or curr in beacons or curr in sensors:
                beacon = False
                break
        if beacon:
            print(x * 4000000 + y)
            exit(0)
"""
"""
x_min -= dist_max
y_min -= dist_max
x_max += 2*dist_max
y_max += 2*dist_max

grid = np.full((x_max + 1, y_max + 1), ".")

# fill grid
for s, b in data:
    grid[*(s + T((dist_max, dist_max)))] = "S"
    grid[*(b + T((dist_max, dist_max)))] = "B"


for s, b in data:
    curr_max_dist = T.manhattan(s, b)
    for x in range(len(data)):
        for y in range(len(data[0])):
            if grid[x][y] == "." and T.manhattan(s, T((x, y))) <= curr_max_dist:
                grid[x][y] = "#"

# print grid
for x in range(len(grid)):
    print(f"{x}: ", end="")
    for y in range(len(grid[0])):
        print(grid[x][y], end="")
    print("\n")

print(grid[10 + dist_max][:])
"""
