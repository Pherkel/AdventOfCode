with open("2022/07/input") as input:
    temp = [x.strip() for x in [x.strip() for x in input.readlines()]]

class Node:
    def __init__(self, name, size = 0, parent = None):
        self.name = name
        self.size = size
        self.subdirs = []
        self.parent = parent
        
    def __repr__(self):
        return f"{self.name}, {self.size}"

first_node = Node("/")
curr_dir = first_node

for ding in temp:
    splitter = ding.split(" ")
    if (splitter[0] == "$"):
        
        if (splitter[1] == "cd"):
            # set cur_dir to it's parent
            if(splitter[2] == ".."):
                curr_dir = curr_dir.parent
                continue
            else:
                # find the requested directory in the list of current children
                for d in curr_dir.subdirs:
                    if d.name == splitter[2]:
                        curr_dir = d
                        break
        continue         
    
    if(splitter[0] == "dir"):
        curr_dir.subdirs.append(Node(splitter[1], parent = curr_dir))
    
    elif(len(splitter) == 2):
        curr_dir.size += int(splitter[0])

# modifying the size of each individual node to include all of it's subdirectories
def total_size(node):
    for sub in node.subdirs:
        node.size += total_size(sub)
    return node.size

# must run only once!
occupied = total_size(first_node)

# solution for part 1
def total_sum(node, res):
    if (node.size <= 100000):
        res += node.size
    for sub in node.subdirs:
        res = total_sum(sub, res)
    
    return res

print(total_sum(first_node, 0))

req_space = 30000000 - (70000000 - occupied)
remove_cand = []

def biggest_dir(node):
    if (node.size >= req_space):
        remove_cand.append(node.size)
    for sub in node.subdirs:
        biggest_dir(sub)

biggest_dir(first_node)

print(sorted(remove_cand)[0])