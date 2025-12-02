PUZZLE_INPUT = "puzzle_input.txt"


def find_invalid_ids(id_range: range):
    # Per puzzle, invalid IDs are those with repeated sequences
    # e.g. 6464 or 123123
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

    all_invalid_ids = []
    for id_range in id_ranges:
        print(f"Searching {id_range} for invalid IDs...")
        all_invalid_ids.extend(find_invalid_ids(id_range))

    print(f"Sum of all invalid IDs: {sum(all_invalid_ids)}")


if __name__ == "__main__":
    main()
