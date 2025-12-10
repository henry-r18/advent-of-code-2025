from itertools import combinations
from math import dist, prod

PUZZLE_INPUT = "puzzle_input.txt"


def calculate_largest_square_part_one(red_tiles: list[tuple]) -> int:
    """Given a list of coordinates for red tiles in a grid,
    calculate the largest square that can be formed between two diagonal squares."""
    return max(
        [
            prod(map(lambda i, j: abs(i - j + 1), tile_1, tile_2))
            for tile_1, tile_2 in combinations(red_tiles, 2)
        ]
    )


def load_input(file: str = PUZZLE_INPUT):
    """Load the input file and read box positions to a list of tuples."""
    with open(file, "r", encoding="utf-8") as f:
        return [tuple(map(int, line.strip().split(","))) for line in f.readlines()]


def main():
    red_tiles = load_input()

    print(f"Part one: {calculate_largest_square_part_one(red_tiles)}")
    # print(f"Part two: {calculate_product_largest_circuits_part_two(junction_boxes)}")


if __name__ == "__main__":
    main()
