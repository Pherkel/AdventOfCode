from functools import reduce

with open("2022/11/input") as input:
    data = []
    temp = [x.strip() for x in input.readlines()]
    for i in range(0, 55, 7):
        inst = {"items": 0, "op": [], "test": "0", "t": -1, "f": -1}
        inst["items"] = [int(x.strip(",")) for x in temp[i+1].split(" ")[2:]]
        inst["op"].append(temp[i+2].split(" ")[-2])
        inst["op"].append(temp[i+2].split(" ")[-1])
        inst["test"] = int(temp[i+3].split(" ")[-1])
        inst["t"] = int(temp[i+4][-1])
        inst["f"] = int(temp[i+5][-1])
        data.append(inst)

inspector = [0 for x in range(len(data))]

kgV = reduce(lambda x, y: x*y, [x["test"] for x in data])

for i in range(10000):
    for idx, monkey in enumerate(data):
        while len(monkey["items"]) != 0:
            match monkey["op"][0]:
                case "+":
                    if monkey["op"][1] == "old":
                        monkey["items"][0] += monkey["items"][0]
                    else:
                        monkey["items"][0] += int(monkey["op"][1])
                case "*":
                    if monkey["op"][1] == "old":
                        monkey["items"][0] *= monkey["items"][0]
                    else:
                        monkey["items"][0] *= int(monkey["op"][1])

            monkey["items"][0] = monkey["items"][0] % kgV

            if monkey["items"][0] % monkey["test"] == 0:
                data[monkey["t"]]["items"].append(monkey["items"][0])
            else:
                data[monkey["f"]]["items"].append(monkey["items"][0])

            monkey["items"].pop(0)
            inspector[idx] += 1
    print(f"Round: {i}")

inspector.sort(reverse=True)
# part 1
print(inspector[0]*inspector[1])
