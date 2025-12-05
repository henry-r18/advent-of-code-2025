PUZZLE_INPUT = "puzzle_input.txt"


def find_fresh_ids(ranges: list[range], ids: list[int]) -> int:
    """Given one list of ranges and another of IDs,
    find all IDs that are within the ranges.

    :param ranges: A list of ranges.
    :param ids: A list of IDs.
    :return: The count of IDs that are within the ranges.
    """
    fresh_id_count = 0

    for id in ids:
        for range in ranges:
            if id in range:
                fresh_id_count += 1
                break  # prevent double-counting IDs
    return fresh_id_count


def load_input(file: str = PUZZLE_INPUT):
    """Load the input file and read sections to lists of their respective types."""
    with open(file, "r", encoding="utf-8") as f:
        sections = f.read().split("\n\n")
        range_strs, id_strs = [section.splitlines() for section in sections]
        range_bounds = [range_str.split("-") for range_str in range_strs]
        ranges, ids = [
            range(int(start), int(stop) + 1) for start, stop in range_bounds
        ], [int(id_str) for id_str in id_strs]
        return (ranges, ids)


def main():
    ranges, ids = load_input()
    fresh_ids_count = find_fresh_ids(ranges, ids)
    print(fresh_ids_count)


if __name__ == "__main__":
    main()
