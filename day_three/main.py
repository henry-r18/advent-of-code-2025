PUZZLE_INPUT = "puzzle_input.txt"


def find_optimal_batteries(battery_bank: list[str]) -> int:
    """Given a battery bank (string of numbers), find the greatest two numbers,
    without reordering the string."""
    # Start by finding max within list
    max_battery = max(battery_bank)
    # Then get first index of max battery
    first_max_battery_index = battery_bank.index(max_battery)
    # If max is last item in list,
    # then it must be second battery...
    if max_battery == battery_bank[-1]:
        second_battery = max_battery
        # and first battery will be max excluding last item.
        first_battery = max(battery_bank[:-1])
    # Otherwise, first battery is max, and second is max after index of first max
    else:
        first_battery = max_battery
        second_battery = max(battery_bank[first_max_battery_index + 1 :])

    return int(first_battery + second_battery)


def load_input(file: str) -> list[list]:
    """Load the input file and read lines to list of lists"""
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        return [list[str](line) for line in lines]


def main():
    battery_banks = load_input(PUZZLE_INPUT)
    optimal_batteries = []
    for battery_bank in battery_banks:
        optimal_batteries.append(find_optimal_batteries(battery_bank))

    print(f"Total output of batteries is: {sum(optimal_batteries)}")


if __name__ == "__main__":
    main()
