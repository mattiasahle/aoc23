"""
Q: How many garden plots could the Elf reach in exactly 64 steps?

One step can be referred to as one round.
He must go one step from each current position.
Starts at S, which is a plot.
Cannot go to #, which is a rock.

Init:
num_of_steps = 0 // repeat until == 64
current_map = input
Set S as O in current_map
new_map = current_map

One round:
1.1 Check NSEW from each O in current_map
1.2 Add new O's to new_map
1.3 Remove O from current_map
2.  Set current_map = new_map
"""


def main():
    current_map = parse_input(read_input())
    num_of_steps = 0
    MAX_STEPS = 64

    current_map = set_S_to_O(current_map)
    current_map = add_border(current_map)
    print("Initial map:")
    print_map(current_map)

    while num_of_steps < MAX_STEPS:
        print(f"Step: {num_of_steps+1}")
        new_map = take_step(current_map)
        current_map = new_map.copy()
        num_of_steps += 1
        print_map(current_map)

    print(count_reachable_plots(current_map))


def count_reachable_plots(map):
    count = 0

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "O":
                count += 1

    return count


def take_step(current_map):
    new_map = current_map.copy()
    new_map = clear_map(new_map)
    # print("Incoming map:")
    # print_map(current_map)

    for i in range(len(current_map) - 1):
        if i == 0 or i == len(current_map):
            continue

        char_list = [*new_map[i]]
        char_list_N = [*new_map[i - 1]]
        char_list_S = [*new_map[i + 1]]

        for j in range(len(current_map[i])):
            if current_map[i][j] == "O":
                char_list[j] = "."
                # print(f"Replacing O with . at {i=}, {j=}")
                # print("WIP map:")
                # print_map(new_map)

                if char_list_N[j] == ".":
                    char_list_N[j] = "O"
                    # print(f"N: Setting O at i={i-1}, {j=}")

                if char_list_S[j] == ".":
                    char_list_S[j] = "O"
                    # print(f"S: Setting O at i={i+1}, {j=}")

                if char_list[j + 1] == ".":
                    char_list[j + 1] = "O"
                    # print(f"E: Setting O at {i=}, j={j+1}")

                if char_list[j - 1] == ".":
                    char_list[j - 1] = "O"
                    # print(f"W: Setting O at {i=}, j={j-1}")

                new_map[i] = "".join(char_list)
                new_map[i - 1] = "".join(char_list_N)
                new_map[i + 1] = "".join(char_list_S)
                # print("Result:")
                # print_map(new_map)

    return new_map


def clear_map(map):
    new_map = []

    for line in map:
        new_line = line.replace("O", ".")
        new_map.append(new_line)

    return new_map


def set_S_to_O(map):
    new_map = []

    for line in map:
        new_line = line.replace("S", "O")
        new_map.append(new_line)

    return new_map


def add_border(map):
    map_width = len(map[0])
    NS_border = "#" * map_width
    map.insert(0, NS_border)
    map.append(NS_border)

    for line in range(len(map)):
        map[line] = "#" + map[line] + "#"

    return map


def print_map(map):
    for line in map:
        print(line)
    print()


def parse_input(input):
    parsed_input = [line.rstrip("\n") for line in input]

    return parsed_input


def read_input():
    with open("in.txt", "r") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
