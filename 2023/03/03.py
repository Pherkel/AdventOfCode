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


def number_at_pos(num_block_idx: list[list[int, list[int]]], pos: tuple[int, int]):
    line_idx, pos = pos
    for num_block in num_block_idx:
        if num_block[1][0] == line_idx and num_block[1][1] <= pos <= num_block[1][2]:
            return num_block[0]
    return 0


def solution_2(input):
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

    gear_idx: list[tuple(int, int)] = []  # [(line_idx, pos)]
    for l_idx, line in enumerate(lines):
        for pos, char in enumerate(line):
            if char == "*":
                gear_idx.append((l_idx, pos))

    res = 0
    for gear in gear_idx:
        line_idx, pos = gear
        adj_nums = []
        added_nums = []
        # up
        if check_boundaries(line_idx - 1, pos, len(lines)):
            num = number_at_pos(num_block_idx, (line_idx - 1, pos))
            if num != 0 and num not in added_nums:
                adj_nums.append(num)
                added_nums.append(num)
        # down
        if check_boundaries(line_idx + 1, pos, len(lines)):
            num = number_at_pos(num_block_idx, (line_idx + 1, pos))
            if num != 0 and num not in added_nums:
                adj_nums.append(num)
                added_nums.append(num)
        # left
        if check_boundaries(line_idx, pos - 1, len(lines)):
            num = number_at_pos(num_block_idx, (line_idx, pos - 1))
            if num != 0 and num not in added_nums:
                adj_nums.append(num)
                added_nums.append(num)
        # right
        if check_boundaries(line_idx, pos + 1, len(lines)):
            num = number_at_pos(num_block_idx, (line_idx, pos + 1))
            if num != 0 and num not in added_nums:
                adj_nums.append(num)
                added_nums.append(num)
        # diagonal, left up
        if check_boundaries(line_idx - 1, pos - 1, len(lines)):
            num = number_at_pos(num_block_idx, (line_idx - 1, pos - 1))
            if num != 0 and num not in added_nums:
                adj_nums.append(num)
                added_nums.append(num)
        # diagonal, right up
        if check_boundaries(line_idx - 1, pos + 1, len(lines)):
            num = number_at_pos(num_block_idx, (line_idx - 1, pos + 1))
            if num != 0 and num not in added_nums:
                adj_nums.append(num)
                added_nums.append(num)
        # diagonal, left down
        if check_boundaries(line_idx + 1, pos - 1, len(lines)):
            num = number_at_pos(num_block_idx, (line_idx + 1, pos - 1))
            if num != 0 and num not in added_nums:
                adj_nums.append(num)
                added_nums.append(num)
        # diagonal, right down
        if check_boundaries(line_idx + 1, pos + 1, len(lines)):
            num = number_at_pos(num_block_idx, (line_idx + 1, pos + 1))
            if num != 0 and num not in added_nums:
                adj_nums.append(num)
                added_nums.append(num)
        print(adj_nums)
        if len(adj_nums) == 2:
            res += adj_nums[0] * adj_nums[1]

    print("Solution 2: ")
    print(res)


if __name__ == "__main__":
    solution_1(input)
    solution_2(input)
