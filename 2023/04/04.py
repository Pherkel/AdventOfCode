with open("input.txt", "r") as f:
    input = f.read()
    
test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def solution_1(input):
    res = 0
    input.strip()
    for game in input.splitlines():
        solution, trial = game.split(" | ")[0].split(": ")[-1].split(" "), game.split("|")[1].strip().split(" "), 
        
        solution = [int(x) for x in solution if x != ""]
        trial = [int(x) for x in trial if x != ""]
        print(solution, trial)
        curr_res = 0
        for t in trial :
            if t in solution :
                print(t)
                if curr_res == 0 :
                    curr_res = 1
                else:
                    curr_res *= 2
                
        res += curr_res
        
    print("Solution 1: ")
    print(res)


def solution_2():
    print("Solution 2: ")


if __name__ == "__main__":
    solution_1(input)
    solution_2()
