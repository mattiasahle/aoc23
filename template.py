def main():
    input = parse_input(read_input())


def parse_input(input):
    parsed_input = [line.rstrip("\n") for line in input]

    return parsed_input


def read_input():
    with open("in.txt", "r") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
