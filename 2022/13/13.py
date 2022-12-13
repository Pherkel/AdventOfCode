with open("2022/13/input") as input:
    data = [[*map(eval, x.split())]
            for x in input.read().split('\n\n')]


def valid(left, right):
    if len(left) == 0 and len(right) > 0:
        return True
    if len(left) > 0 and len(right) == 0:
        return False
    if len(left) == 0 and len(right) == 0:
        return True

    if type(left[0]) == int and type(right[0]) == list:
        return valid([left.pop(0)], right.pop(0)) and valid(left, right)

    if type(right[0]) == int and type(left[0]) == list:
        return valid(left.pop(0), [right.pop(0)]) and valid(left, right)

    if type(left[0]) == int and type(right[0]) == int:
        if left[0] < right[0]:
            return True
        if left[0] > right[0]:
            return False
        if left[0] == right[0]:
            left.pop(0)
            right.pop(0)
            return valid(left, right)

    if type(left[0] == list) and type(right[0] == list):
        return valid(left.pop(0), right.pop(0)) and valid(left, right)

# fucking


def valid2(left, right):
    match left, right:
        case int(), int():
            if left < right:
                return -1
            if left > right:
                return 1
            if left == right:
                return 0
        case int(), list():
            return valid2([left], right)
        case list(), int():
            return valid2(left, [right])
        case list(), list():
            for val in map(valid2, left, right):
                if val:
                    return val
            return valid2(len(left), len(right))


res = 0

for i in range(0, len(data)):
    if valid2(*data[i]) == -1:
        res += i + 1
print(res)
