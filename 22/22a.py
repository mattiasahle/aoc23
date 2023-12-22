import numpy as np
import bisect


def main():
    input = parse_input(read_input())
    print(input)
    input = sort_input(input)


def sort_input(input):
    sorted_list = []

    for coordinate_pair in input:
        min_z = min(coordinate_pair[0][2], coordinate_pair[1][2])

        min_z_coordinate = 0
        if min_z == coordinate_pair[0][2]:
            min_z_coordinate = 0
        else:
            min_z_coordinate = 1


def parse_input(input):
    parsed_input = [line.rstrip("\n") for line in input]
    parsed_input = [line.split("~") for line in parsed_input]
    parsed_input = [
        [coordinate.split(",") for coordinate in line] for line in parsed_input
    ]

    parsed_input = np.array(parsed_input)
    parsed_input = parsed_input.astype(int)

    return parsed_input


def read_input():
    with open("xin.txt", "r") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
