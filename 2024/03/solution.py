import re


def p1():
    with open("input.txt") as f:
        command = f.read().strip()

    regex = re.compile(r"mul\(\d+,\d+\)")
    exps = regex.findall(command)
    res = sum([m[0] * m[1] for m in [eval(exp.replace("mul", "")) for exp in exps]])

    print("solution1: ", res)


def p2():
    with open("input.txt") as f:
        command = f.read().strip()

    regex = re.compile(r"(?:mul\(\d+,\d+\)|do\(\)|don't\(\))")
    matches = regex.findall(command)

    res = 0
    do = True
    for m in matches:
        if m.startswith("do()"):
            do = True
        elif m.startswith("don't()"):
            do = False
        elif m.startswith("mul") and do:
            m = eval(m.replace("mul", ""))
            res += m[0] * m[1]

    print("solution2: ", res)


p1()
p2()
