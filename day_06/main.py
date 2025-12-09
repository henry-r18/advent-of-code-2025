from copy import deepcopy
from math import prod

PUZZLE_INPUT = "puzzle_input.txt"


def calculate_result_part_two(left_justified_grid: list[str]) -> int:
    """Given a grid with left-justified problems arranged in columns,
    find the grand total by applying the operators to the columns,
    as described in the puzzle.

    :param left_justified_grid: The transposed grid.
    :return: The grand total from all operations in the grid.
    """
    grand_total = 0
    operators = left_justified_grid.pop().split()

    # Reorient columns to rows to form problem grid
    grid = list(zip(*left_justified_grid))
    problems = ["".join(line) for line in grid]
    # We need to collect the new rows to form problem lists,
    # splitting at lines that are all " ", which indicates a column break.
    # Then create a new list with sub-lists representing each problem.
    problems = []
    start = 0
    for i, line in enumerate(grid):
        if all([elem == " " for elem in line]):
            problems.append([int("".join(line)) for line in grid[start:i]])
            start = i + 1
    if start < len(grid):
        problems.append([int("".join(line)) for line in grid[start:]])

    # This results in a list of tuples,
    # each with a problem list and its operator
    problems_with_operators = list(zip(problems, operators))

    for problem in problems_with_operators:
        grand_total += sum(problem[0]) if problem[1] == "+" else prod(problem[0])
    return grand_total


def calculate_result_part_one(transposed_grid: list[list]) -> int:
    """Given a transposed grid where each row represents a problem to solve,
    perform the operation indicated by the last element in each row.

    :param transposed_grid: The transposed grid.
    :return: The grand total from all operations in the grid.
    """
    grand_total = []
    for row in transposed_grid:
        operator = row.pop()
        row = [int(elem) for elem in row]
        total = sum(row) if operator == "+" else prod(row)
        grand_total.append(total)
    return sum(grand_total)


def transpose_grid(grid: list[list]) -> list[list]:
    """Given a grid of rows and columns,
    transpose the grid so that the columns are the rows and vice versa.

    :param grid: A list of lists, representing a grid.
    :return: The transposed grid.
    """
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]


def load_input_part_two(file: str = PUZZLE_INPUT):
    """Load the input file to a left-justified grid."""
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        max_line_length = max(map(len, lines))
        return [line.ljust(max_line_length).rstrip("\n") for line in lines]


def load_input(file: str = PUZZLE_INPUT):
    """Load the input file and read sections to lists of their respective types."""
    with open(file, "r", encoding="utf-8") as f:
        return [line.split() for line in f.readlines()]


def main():
    grid = load_input()
    transposed_grid = transpose_grid(grid)
    grand_total_part_one = calculate_result_part_one(transposed_grid)

    left_justified_grid = load_input_part_two()
    grand_total_part_two = calculate_result_part_two(left_justified_grid)

    print(f"Part one: {grand_total_part_one}")
    print(f"Part two: {grand_total_part_two}")


if __name__ == "__main__":
    main()
