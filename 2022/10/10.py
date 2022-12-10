# addx starts at 1
# addx V takes 2 cycles -> after 2 cycles addx is increased by V
# noop takes one cycle, does nothing

with open("2022/10/input") as input:
    data = [x.split() for x in [x.strip() for x in input.readlines()]]

cycles = [1, 1]
x = 1

for inst in data:
    match inst[0]:
        case "noop": cycles.append(x)
        case "addx":
            new_x = x + int(inst[1])
            x = new_x
            cycles.append(new_x)
            cycles.append(new_x)

res = 0
for i in range(20, len(cycles), 40):
    print(cycles[i-1])
    res += i * cycles[i-1]

print(res)
