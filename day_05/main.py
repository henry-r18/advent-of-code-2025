PUZZLE_INPUT = "puzzle_input.txt"


def _merge_overlapping_ranges(ranges: list[range]) -> list[range]:
    """Merge overlapping ranges where possible, returning a list of merged ranges.

    :param ranges: A list of ranges.
    :return: A list of merged ranges.
    """
    # Sort ranges by starting points
    ranges.sort(key=lambda range: range.start)

    # Init merged ranges list with first range in sort
    merged_ranges = [ranges[0]]

    for current_range in ranges[1:]:
        if current_range.start <= merged_ranges[-1].stop:
            # Overwrite overlapping range
            merged_ranges[-1] = range(
                merged_ranges[-1].start, max(merged_ranges[-1].stop, current_range.stop)
            )
        else:
            merged_ranges.append(current_range)
    return merged_ranges


def find_fresh_ids_part_two(ranges: list[range]) -> int:
    """Given a list of ranges, return the count of all unique IDs in the ranges.

    :param ranges: A list of ranges.
    :return: The count of unique IDS within the ranges.
    """
    merged_ranges = _merge_overlapping_ranges(ranges)
    return sum([range.stop - range.start for range in merged_ranges])


def find_fresh_ids_part_one(ranges: list[range], ids: list[int]) -> int:
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
            # Stop + 1 because ranges are supposed to be inclusive
            range(int(start), int(stop) + 1)
            for start, stop in range_bounds
        ], [int(id_str) for id_str in id_strs]
        return (ranges, ids)


def main():
    ranges, ids = load_input()
    fresh_ids_count_part_one = find_fresh_ids_part_one(ranges, ids)
    fresh_ids_count_part_two = find_fresh_ids_part_two(ranges)
    print(f"Part one answer: {fresh_ids_count_part_one}")
    print(f"Part two answer: {fresh_ids_count_part_two}")


if __name__ == "__main__":
    main()
