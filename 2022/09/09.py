import numpy as np

with open("2022/09/input") as input:
    data = [[x.split()[0], int(x.split()[1])] for x in input.readlines()]


def get_vec(inst):
    match inst[0]:
        case "U": return vec2D(0, 1)
        case "D": return vec2D(0, -1)
        case "R": return vec2D(1, 0)
        case "L": return vec2D(-1, 0)


class vec2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def add_xy(self, x, y):
        self.x += x
        self.y += y

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    @staticmethod
    def get_tup(vec):
        return (vec.x, vec.y)

    @staticmethod
    def diff(vec1, vec2):
        return vec2D(vec1.x - vec2.x, vec1.y - vec2.y)


positions = set()

pos_head = vec2D(0, 0)
pos_tail = vec2D(0, 0)

positions.add((0, 0))
for inst in data:
    dr = get_vec(inst)
    for i in range(inst[1]):
        pos_head.add(dr)

        diff = vec2D.diff(pos_head, pos_tail)

        if abs(diff.x) == 2 and diff.y == 0:
            pos_tail.x += diff.x / 2

        if abs(diff.y) == 2 and diff.x == 0:
            pos_tail.y += diff.y / 2

        if (abs(diff.x) == 1 and abs(diff.y) == 2):
            pos_tail.x += diff.x
            pos_tail.y += diff.y / 2

        if (abs(diff.x) == 2 and abs(diff.y) == 1):
            pos_tail.x += diff.x / 2
            pos_tail.y += diff.y

        positions.add(vec2D.get_tup(pos_tail))

print(len(positions))
