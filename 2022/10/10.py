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
    res += i * cycles[i-1]


# sprite is at x +/- 1
# cycle number mod 39 = current pos for each row
# if current pos is within sprite range = draw # else draw .

# go through every cycle, current pos within row = cycle mod 40
# if cycle[i] == i mod 40:

row = 0
k = 0
for i in range(0, len(cycles)):
    if i % 40 in {cycles[i] - 1, cycles[i], cycles[i] + 1}:
        print("#", end="")
    else:
        print(".", end="")
    if i % 40 == 39:
        print("")
