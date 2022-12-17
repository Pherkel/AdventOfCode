from copy import deepcopy
from typing import Type
from numpy import argmin, argmax

pusher = [*open("2022/17/test_input").readline()]


class V2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other) -> None:
        return V2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return V2D(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Stone:
    def __init__(self, occupies: list[Type[V2D]]) -> None:
        self.occ = occupies
        self.settled = False

    def bottom_edge(self) -> int:
        return self.occ[argmin([vec.x for vec in self.occ])]

    def top_edge(self) -> int:
        return self.occ[argmax([vec.x for vec in self.occ])]

    def left_edge(self) -> int:
        return self.occ[argmin([vec.y for vec in self.occ])]

    def right_edge(self) -> int:
        return self.occ[argmax([vec.y for vec in self.occ])]

    def __repr__(self):
        return str([vec for vec in self.occ])


class Validator:

    @staticmethod
    def left(s: Stone, grid: list[list]):
        if s.left_edge().y <= 0:
            return False
        for vec in s.occ:
            if grid[vec.x][vec.y - 1] == '#':
                return False
        return True

    @staticmethod
    def right(s: Stone, grid: list[list]):
        if s.right_edge().y >= 6:
            return False
        for vec in s.occ:
            if grid[vec.x][vec.y + 1] == '#':
                return False
        return True

    @staticmethod
    def down(s: Stone, grid: list[list]):
        for vec in s.occ:
            if (grid[vec.x - 1][vec.y]) == "#":
                return False
        return True


def grid_printer(grid):
    for row in reversed(grid):
        print("\n")
        for col in row:
            print(col, end="")
    print("")


stones = [
    Stone([V2D(0, 2), V2D(0, 3), V2D(0, 4), V2D(0, 5)]),
    Stone([V2D(1, 2), V2D(2, 3), V2D(1, 3), V2D(0, 3), V2D(1, 4)]),
    Stone([V2D(0, 2), V2D(0, 3), V2D(0, 4), V2D(1, 4), V2D(2, 4)]),
    Stone([V2D(0, 2), V2D(1, 2), V2D(2, 2), V2D(3, 2)]),
    Stone([V2D(1, 2), V2D(0, 2), V2D(0, 3), V2D(1, 3)])
]

height = 0

grid = [["#"]*7]

p = 0
for i in range(0, 1000000000000):
    # spawn new stone
    curr_stone: list[Type[V2D]] = deepcopy(stones[i % 5])

    # extend grid to fit new stone
    if len(grid) < height + curr_stone.top_edge().x + 5:
        [grid.append(["."]*7)
         for _ in range(len(grid), height + curr_stone.top_edge().x + 5)]

    # place current stone at where it should spawn
    for i in range(len(curr_stone.occ)):
        curr_stone.occ[i] += V2D(height + 4, 0)

    # repeat until stone is not falling anymore
    while True:
        # apply pushing force
        curr_dir = pusher[p % len(pusher)]
        p += 1

        match curr_dir:
            case "<":
                if Validator.left(curr_stone, grid):
                    for i in range(len(curr_stone.occ)):
                        curr_stone.occ[i] -= V2D(0, 1)
            case ">":
                if Validator.right(curr_stone, grid):
                    for i in range(len(curr_stone.occ)):
                        curr_stone.occ[i] += V2D(0, 1)

        # check if move downwards is possible:
        if Validator.down(curr_stone, grid):
            # move downwards
            for i in range(len(curr_stone.occ)):
                curr_stone.occ[i] -= V2D(1, 0)
        else:  # draw stone into grid
            for vec in curr_stone.occ:
                grid[vec.x][vec.y] = "#"

            height = max(curr_stone.top_edge().x, height)
            break
print(height)
