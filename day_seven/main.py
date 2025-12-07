from collections import defaultdict

PUZZLE_INPUT = "puzzle_input.txt"


def count_beams_part_two(manifold: list[list[str]]) -> int:
    """Given a matrix representing the tachyon manifold,
    count the possible paths for the beam, if it only splits one way
    at each splitter."""
    starting_position = (0, manifold[0].index("S"))
    i, j = starting_position

    # Use integer dict to keep track of possible beam paths
    beams = defaultdict(int)
    beams[j] = 1  #  Initial beam from start

    for i in range(len(manifold)):
        beam_paths = defaultdict(int)

        for j in beams:
            count = beams[j]
            if manifold[i][j] == "^":
                beam_paths[j - 1] += count
                beam_paths[j + 1] += count
            else:
                beam_paths[j] += count
        beams = beam_paths
    return sum(beams.values())


def count_beams_part_one(manifold: list[list[str]]) -> int:
    """Given a matrix representing the tachyon manifold,
    count the number of times the beam will be split."""
    beam_count = 0
    for i, row in enumerate(manifold):
        for j, elem in enumerate(row):
            if elem == "S":
                manifold[i + 1][j] = "|"
                continue
            if elem == "." and manifold[i - 1][j] == "|":
                manifold[i][j] = "|"
                continue
            if elem == "^" and manifold[i - 1][j] == "|":
                if j - 1 >= 0:
                    manifold[i][j - 1] = "|"
                if j + 1 <= len(row) - 1:
                    manifold[i][j + 1] = "|"
                beam_count += 1

    return beam_count


def load_input(file: str = PUZZLE_INPUT):
    """Load the input file and read sections to lists of their respective types."""
    with open(file, "r", encoding="utf-8") as f:
        return [list(line.strip()) for line in f.readlines()]


def main():
    manifold_part_one = load_input()
    beam_count_part_one = count_beams_part_one(manifold_part_one)

    manifold_part_two = load_input()
    beam_count_part_two = count_beams_part_two(manifold_part_two)

    # print(f"Part one: {beam_count_part_one}")
    print(f"Part two: {beam_count_part_two}")


if __name__ == "__main__":
    main()
