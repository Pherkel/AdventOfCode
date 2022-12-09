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

elems = [vec2D(0, 0) for x in range(10)]

positions.add((0, 0))
for inst in data:
    dr = get_vec(inst)
    # apply direction n times to head node
    for i in range(inst[1]):
        elems[-1].add(dr)
        # step through nodes from head to tail and apply movement rules to each
        for j in reversed(range(len(elems)-1)):
            # get difference vector from previous node
            diff = vec2D.diff(elems[j+1], elems[j])

            # diff is allowed
            if (abs(diff.x) <= 1 and abs(diff.y) <= 1):
                continue

            # only need ones!
            if diff.x > 0:
                elems[j].x += 1
            elif diff.x < 0:
                elems[j].x -= 1

            if diff.y > 0:
                elems[j].y += 1
            elif diff.y < 0:
                elems[j].y -= 1

        positions.add(vec2D.get_tup(elems[0]))

print(len(positions))
