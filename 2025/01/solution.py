with open("01.txt", "r") as f:
    lines = f.readlines()

# (L/R, int)
lines = [(l[0], int(l[1:])) for l in lines]

# 1
curr = 50
pw = 0
for l in lines:
    curr = curr + l[1] if l[0] == "R" else curr - l[1]
    curr = curr % 100
    if curr == 0: pw += 1 
    
print(pw)

# 2
curr = 50
pw = 0 
for l in lines:
    d = l[0]
    s = l[1]
    while s:
        curr = curr + 1 if d == "R" else curr - 1
        curr = curr % 100
        if curr == 0: pw += 1
        s -= 1
        
print(pw)