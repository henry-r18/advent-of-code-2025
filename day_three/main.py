PUZZLE_INPUT = "puzzle_input.txt"


def find_optimal_batteries(battery_bank: str, digits: int) -> int:
    """Given a battery bank (string of numbers), find the greatest two numbers,
    without reordering the string.

    :param battery_bank: The input battery bank.
    :param digits: The number of digits desired for the optimal batteries output.
    """
    optimal_batteries = []
    start = 0
    stop = len(battery_bank) - digits
    while len(optimal_batteries) < digits:
        window = battery_bank[start : stop + 1]  # +1 to include right of window
        start += window.index(max(window))
        if start == stop:
            # If start is stop, rest of battery bank can be pushed to list
            optimal_batteries.append(battery_bank[start:])
            break
        optimal_batteries.append(battery_bank[start])
        start += 1
        stop += 1

    return int("".join(optimal_batteries))


def load_input(file: str) -> list:
    """Load the input file and read lines to list of lists"""
    with open(file, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def main():
    battery_banks = load_input(PUZZLE_INPUT)
    optimal_batteries_part_one = []
    optimal_batteries_part_two = []
    for battery_bank in battery_banks:
        optimal_batteries_part_one.append(find_optimal_batteries(battery_bank, 2))
        optimal_batteries_part_two.append(find_optimal_batteries(battery_bank, 12))

    print(f"Total output part one: {sum(optimal_batteries_part_one)}")
    print(f"Total output part two: {sum(optimal_batteries_part_two)}")


if __name__ == "__main__":
    main()
