# I got part 1 easily today, but struggled with part 2.
# Reddit seemed to agree it was difficult.
# I liked the object-oriented approach I found here best,
# out of the answers I reviewed on Reddit:
# See @https://github.com/hermes85pl/advent-of-code-2025/blob/main/day09/part2.py.
# Might code is adapted very closely from the linked repo.
# Learned about `chain` and `pairwise` from `itertools` today.

from itertools import combinations, chain, pairwise
from math import prod

PUZZLE_INPUT = "puzzle_input.txt"


class Rectangle:
    x_min: int
    x_max: int
    y_min: int
    y_max: int

    def __init__(self, p1: tuple, p2: tuple) -> None:
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        self.x_min, self.x_max = min(x1, x2), max(x1, x2)
        self.y_min, self.y_max = min(y1, y2), max(y1, y2)

    def overlaps_with(self, other: "Rectangle") -> bool:
        return not (
            self.x_max <= other.x_min
            or other.x_max <= self.x_min
            or self.y_max <= other.y_min
            or other.y_max <= self.y_min
        )

    def area(self) -> int:
        x_len = self.x_max - self.x_min + 1
        y_len = self.y_max - self.y_min + 1
        return x_len * y_len


def calculate_largest_square_part_two(red_tiles: list[tuple]) -> int:
    """Given a list of coordinates for red tiles in a grid,
    calculate the largest square that can be formed between two diagonal squares."""
    edges = [
        Rectangle(p, q)
        for p, q in chain(
            pairwise(red_tiles), [(red_tiles[-1], red_tiles[0])]
        )  # this creates looping chain
    ]

    return max(
        rectangle.area()
        for rectangle in (Rectangle(p, q) for p, q in combinations(red_tiles, 2))
        if not any(rectangle.overlaps_with(edge) for edge in edges)
    )


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
    print(f"Part two: {calculate_largest_square_part_two(red_tiles)}")


if __name__ == "__main__":
    main()
