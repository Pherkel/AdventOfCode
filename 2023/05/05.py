from collections import defaultdict
from tqdm import tqdm

with open("input.txt", "r") as f:
    input = f.read()

test_input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def solution_1(input):
    seeds = [int(x) for x in input.split("seeds: ")[1].split("\n")[0].split(" ")]  #

    seed_soil = input.split("seed-to-soil map:\n")[1].split("\n\n")[0]  #
    soil_fertilizer = input.split("soil-to-fertilizer map:\n")[1].split("\n\n")[0]  #
    fertilizer_water = input.split("fertilizer-to-water map:\n")[1].split("\n\n")[0]  #
    water_light = input.split("water-to-light map:\n")[1].split("\n\n")[0]  #
    light_temperature = input.split("light-to-temperature map:\n")[1].split("\n\n")[
        0
    ]  #
    temperature_humidity = input.split("temperature-to-humidity map:\n")[1].split(
        "\n\n"
    )[
        0
    ]  #
    humidity_location = input.split("humidity-to-location map:\n")[1].split("\n\n")[
        0
    ]  #

    maps = [
        seed_soil,
        soil_fertilizer,
        fertilizer_water,
        water_light,
        light_temperature,
        temperature_humidity,
        humidity_location,
    ]

    maps = ["\n".join([line for line in map.split("\n") if line != ""]) for map in maps]

    def lookup(num, dest_start, source_start, length):
        # print(f"lookup({num}, {dest_start}, {source_start}, {length})")
        if num >= source_start and num <= source_start + length:
            return num - source_start + dest_start
        else:
            return num

    places = defaultdict(int)
    for seed in seeds:
        source = seed
        dest = 0
        for idx, map in enumerate(maps):
            for line in map.split("\n"):
                dest_start, source_start, length = [
                    int(x) for x in line.strip().split(" ")
                ]
                # check if source is in range
                if source < source_start or source > source_start + length:
                    dest = source
                    continue
                temp = lookup(source, dest_start, source_start, length)

                dest = temp
                break
            source = dest
        places[seed] = dest

    print("Solution 1: ")
    print(min(places.values()))


def solution_2(input):
    seeds = [int(x) for x in input.split("seeds: ")[1].split("\n")[0].split(" ")]  #

    seed_soil = input.split("seed-to-soil map:\n")[1].split("\n\n")[0]  #
    soil_fertilizer = input.split("soil-to-fertilizer map:\n")[1].split("\n\n")[0]  #
    fertilizer_water = input.split("fertilizer-to-water map:\n")[1].split("\n\n")[0]  #
    water_light = input.split("water-to-light map:\n")[1].split("\n\n")[0]  #
    light_temperature = input.split("light-to-temperature map:\n")[1].split("\n\n")[
        0
    ]  #
    temperature_humidity = input.split("temperature-to-humidity map:\n")[1].split(
        "\n\n"
    )[
        0
    ]  #
    humidity_location = input.split("humidity-to-location map:\n")[1].split("\n\n")[
        0
    ]  #

    maps = [
        seed_soil,
        soil_fertilizer,
        fertilizer_water,
        water_light,
        light_temperature,
        temperature_humidity,
        humidity_location,
    ]

    maps = ["\n".join([line for line in map.split("\n") if line != ""]) for map in maps]

    for idx, map in enumerate(maps):
        maps[idx] = [
            [int(x) for x in line.strip().split(" ")] for line in map.split("\n")
        ]

    def lookup(num, dest_start, source_start, length):
        # print(f"lookup({num}, {dest_start}, {source_start}, {length})")
        if num >= source_start and num <= source_start + length:
            return num - source_start + dest_start
        else:
            return num

    min_place = 2**32 - 1
    for i in range(0, len(seeds), 2):
        for seed in tqdm(range(seeds[i], seeds[i] + seeds[i + 1] + 1)):
            source = seed
            dest = 0
            for map in maps:
                for dest_start, source_start, length in map:
                    # check if source is in range
                    if source < source_start or source > source_start + length:
                        dest = source
                        continue
                    temp = lookup(source, dest_start, source_start, length)

                    dest = temp
                    break
                source = dest
            if dest < min_place:
                min_place = dest

    print("Solution 2: ")
    print(min_place)


if __name__ == "__main__":
    solution_1(input)
    solution_2(input)
