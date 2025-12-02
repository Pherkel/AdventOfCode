with open("input.txt", "r") as f:
    # [[start, end]]
    id_ranges = [
        (int(r[0]), int(r[1])) for r in [r.split("-") for r in f.readline().split(",")]
    ]

invalid_ids = []
for id_range in id_ranges:
    for id in range(id_range[0], id_range[1] + 1):
        id_str = str(id)
        length = len(id_str)
        if id_str[: (length // 2)] == id_str[(length // 2) :]:
            invalid_ids.append(id)

print(sum(invalid_ids))

invalid_ids = []
for id_range in id_ranges:
    for id in range(id_range[0], id_range[1] + 1):
        id_str = str(id)
        length = len(id_str)
        is_invalid = False
        for pattern_len in range(1, length // 2 + 1):
            if length % pattern_len == 0:
                pattern = id_str[:pattern_len]
                if pattern * (length // pattern_len) == id_str:
                    is_invalid = True
                    break
        if is_invalid:
            invalid_ids.append(id)

print(sum(invalid_ids))