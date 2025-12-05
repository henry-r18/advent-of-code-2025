PUZZLE_INPUT = "puzzle_input.txt"


def find_accessible_rolls(shelves: list[list], total_accessible_rolls: int = 0) -> int:
    """Given a grid representing shelves, count the number of accessible rolls,
    defined as those with fewer than 4 rolls in their adjacent 8 positions.

    :param shelves: The shelves input, as a list of lists.
    :return: The count of the number of accessible rolls,
    and the shelves with the accessible rolls removed.
    """
    accessible_rolls = []
    for row, shelf in enumerate(shelves):
        for column, item in enumerate(shelf):
            if item == "@":
                # Check adjacent positions
                adjacent_roll_count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i, j) != (0, 0):  # don't check current position
                            if (
                                row + i >= 0
                                and column + j >= 0
                                and row + i < len(shelf)
                                and column + j < len(shelves)
                            ):  # stay within bounds
                                if shelves[row + i][column + j] == "@":
                                    adjacent_roll_count += 1
                if adjacent_roll_count < 4:
                    accessible_rolls.append((row, column))
    # If no more accessible rolls, return total
    if not accessible_rolls:
        return total_accessible_rolls
    # Otherwise recurse
    for row, column in accessible_rolls:
        shelves[row][column] = "."
    total_accessible_rolls += len(accessible_rolls)
    return find_accessible_rolls(shelves, total_accessible_rolls)


def load_input(file: str) -> list[list]:
    """Load the input file and read lines to list of lists"""
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().splitlines()
        return [list(line) for line in content]


def main():
    shelves = load_input(PUZZLE_INPUT)
    total_accessible_rolls = find_accessible_rolls(shelves)
    print(total_accessible_rolls)


if __name__ == "__main__":
    main()
