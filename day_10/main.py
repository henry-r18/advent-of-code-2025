from unittest import TestCase
from itertools import combinations
import re

PUZZLE_INPUT = "puzzle_input.txt"


# def part_two(red_tiles: list[tuple]) -> int:
#     pass


def part_one(input: list[tuple]) -> int:
    """Find the product of the sequences of fewest button presses
    that result in the diagram for each line in the input."""
    fewest_button_presses = []
    for line in input:
        diagram, buttons, _ = line
        found_target_state = False
        # First try 1 button, then 2, then 3, etc
        for available_button_count in range(1, len(buttons) + 1):
            for attempt in combinations(buttons, available_button_count):
                target_state = set()
                for button in attempt:
                    target_state ^= button
                found_target_state = target_state == diagram
                if found_target_state:
                    fewest_button_presses.append(available_button_count)
                    break
            if found_target_state:
                break
    return sum(fewest_button_presses)


def load_input(file: str = PUZZLE_INPUT):
    """Load the input file and read box positions to a list of tuples."""
    with open(file, "r", encoding="utf-8") as f:
        input = []
        for line in f.readlines():
            match = re.match(r"\[(.*)\]\s(\(.*\))\s\{(.*)\}", line)
            if match:
                diagram, buttons, joltage = match.groups()
                diagram = set(
                    [index for index, item in enumerate(diagram) if item == "#"]
                )
                buttons = [
                    set(map(int, button.strip("()").split(",")))
                    for button in buttons.split()
                ]
                joltage = joltage.split(",")
                input.append((diagram, buttons, joltage))
        return input


def main():
    input = load_input()

    print(f"Part one: {part_one(input)}")
    # print(f"Part two: {calculate_largest_square_part_two(red_tiles)}")


if __name__ == "__main__":
    main()


class DayTenTestCase(TestCase):
    def setUp(self):
        self.test_input = load_input(file="test_input.txt")

    def test_part_one(self):
        fewest_presses_total = part_one(self.test_input)
        print(fewest_presses_total)
