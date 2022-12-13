with open("2022/12/input") as input:
    data = [list(x.strip().split()[0]) for x in input.readlines()]

dist = [[float("inf") for x in range(len(data[0]))] for x in range(len(data))]

queue = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "S":
            data[i][j] = "a"
            queue.append((i, j))
            dist[i][j] = 0
        if data[i][j] == "E":
            end = (i, j)
            data[i][j] = "z"


def valid(source, target):
    res = ord(data[target[0]][target[1]]) - \
        ord(data[source[0]][source[1]]) <= 1
    return res


def get_neighbors(u):
    res = []
    for i in range(-1 if u[0] > 0 else 1, 2 if u[0] < len(data) - 1 else 0, 2):
        res.append((u[0] + i, u[1]))
    for j in range(-1 if u[1] > 0 else 1, 2 if u[1] < len(data[0]) - 1 else 0, 2):
        res.append((u[0], u[1] + j))
    return res


while queue:
    u = queue.pop(0)
    for n in get_neighbors(u):
        if valid(u, n) and dist[n[0]][n[1]] == float("inf"):
            dist[n[0]][n[1]] = dist[u[0]][u[1]] + 1
            queue.append(n)

print(dist[end[0]][end[1]])
# part 2

a_list = []
dist_list = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "a":
            a_list.append((i, j))

for a in a_list:
    dist = [[float("inf") for x in range(len(data[0]))]
            for x in range(len(data))]
    queue = [a]
    dist[a[0]][a[1]] = 0

    while queue:
        u = queue.pop(0)
        for n in get_neighbors(u):
            if valid(u, n) and dist[n[0]][n[1]] == float("inf"):
                dist[n[0]][n[1]] = dist[u[0]][u[1]] + 1
                queue.append(n)
    dist_list.append(dist[end[0]][end[1]])

print(min(dist_list))
