with open("input.txt", "r") as f:
    input = f.read()

test_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def is_symbol(char):
    return char not in "0123456789."


def check_boundaries(line_idx, pos, line_length):
    if line_idx < 0 or line_idx >= line_length:
        return False
    if pos < 0 or pos >= line_length:
        return False
    return True


def solution_1(input):
    lines = input.strip().split("\n")
    num_block_idx: list[
        list[int, list[int]]
    ] = []  # [part_num, [line_idx, start_idx, end_idx]
    for l_idx, line in enumerate(lines):
        i = 0
        while i < len(line):
            j = 1
            if line[i].isdigit():
                number = line[i]
                num_block_idx.append([0, [0, 0, 0]])
                while i + j < len(line) and line[i + j].isdigit():
                    number += line[i + j]
                    j += 1

                num_block_idx[-1][0] = int(number)
                num_block_idx[-1][1] = [l_idx, i, i + j - 1]
            i += j
    res = 0
    for num_block in num_block_idx:
        line_idx, start_idx, end_idx = num_block[1]

        for pos in range(start_idx, end_idx + 1):
            # up
            if check_boundaries(line_idx - 1, pos, len(lines)) and is_symbol(
                lines[line_idx - 1][pos]
            ):
                res += num_block[0]
                break
            # down
            if check_boundaries(line_idx + 1, pos, len(lines)) and is_symbol(
                lines[line_idx + 1][pos]
            ):
                res += num_block[0]
                break
            # left
            if check_boundaries(line_idx, pos - 1, len(lines)) and is_symbol(
                lines[line_idx][pos - 1]
            ):
                res += num_block[0]
                break
            # right
            if check_boundaries(line_idx, pos + 1, len(lines)) and is_symbol(
                lines[line_idx][pos + 1]
            ):
                res += num_block[0]
                break
            # diagonal, left up
            if check_boundaries(line_idx - 1, pos - 1, len(lines)) and is_symbol(
                lines[line_idx - 1][pos - 1]
            ):
                res += num_block[0]
                break
            # diagonal, right up
            if check_boundaries(line_idx - 1, pos + 1, len(lines)) and is_symbol(
                lines[line_idx - 1][pos + 1]
            ):
                res += num_block[0]
                break
            # diagonal, left down
            if check_boundaries(line_idx + 1, pos - 1, len(lines)) and is_symbol(
                lines[line_idx + 1][pos - 1]
            ):
                res += num_block[0]
                break
            # diagonal, right down
            if check_boundaries(line_idx + 1, pos + 1, len(lines)) and is_symbol(
                lines[line_idx + 1][pos + 1]
            ):
                res += num_block[0]
                break

    print("Solution 1: ")
    print(res)


def solution_2(input):
    print("Solution 2: ")


if __name__ == "__main__":
    solution_1(input)
    solution_2(test_input)
