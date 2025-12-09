PUZZLE_INPUT = "puzzle_input.txt"


def find_invalid_ids_part_two(id_range: range):
    # In part two, invalid IDs are those
    # with a sequence repeated at least twice,
    # e.g. 1111111 or 1212121212 or 6464
    invalid_ids = []
    for id in id_range:
        id_list = list(str(id))

        # Break ID list into chunks of length n,
        # incrementing n from 1 to the length of the ID list (exclusive).
        # Join the chunks, and if all are equal, we have found an invalid ID.
        for n in range(1, len(id_list)):
            groups = ["".join(id_list[i : i + n]) for i in range(0, len(id_list), n)]
            # If all groups are the same, indicates an invalid ID.
            # We'll break on first encounter of this equality.
            if all(groups[0] == group for group in groups):
                invalid_ids.append(id)
                break

    return invalid_ids


def find_invalid_ids_part_one(id_range: range):
    # Per puzzle, invalid IDs in part one
    # are those with repeated sequences, e.g. 6464 or 123123
    invalid_ids = []
    for id in id_range:
        id_length = len(str(id))
        # if length of ID is odd, cannot have repeated sequence
        if id_length % 2 != 0:
            continue
        else:
            first_half, second_half = (
                str(id)[: id_length // 2],
                str(id)[id_length // 2 :],
            )
            if first_half == second_half:
                print(f"Found repeating sequence: {id}")
                invalid_ids.append(id)
    return invalid_ids


def parse_id_range(range_str: str) -> range:
    start, stop = range_str.split("-")
    # Stop is not included in range iterable, hence + 1
    return range(int(start), int(stop) + 1)


def load_input(file: str) -> list[str]:
    """Load the input file and split ID ranges."""
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        # ID ranges are provided as comma-separated list
        return content.strip().split(",")


def main():
    id_range_strs = load_input(PUZZLE_INPUT)
    id_ranges = [parse_id_range(id_range_str) for id_range_str in id_range_strs]

    all_invalid_ids_part_one = []
    for id_range in id_ranges:
        print(f"Searching {id_range} for invalid IDs...")
        all_invalid_ids_part_one.extend(find_invalid_ids_part_one(id_range))

    all_invalid_ids_part_two = []
    for id_range in id_ranges:
        print(f"Searching {id_range} for invalid IDs...")
        all_invalid_ids_part_two.extend(find_invalid_ids_part_two(id_range))

    print(f"Sum of all invalid IDs Part 1: {sum(all_invalid_ids_part_one)}")
    print(f"Sum of all invalid IDs Part 2: {sum(all_invalid_ids_part_two)}")


if __name__ == "__main__":
    main()
