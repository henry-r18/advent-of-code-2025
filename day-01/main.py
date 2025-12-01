"""Advent of Code 2025 - Day 01

A safe dial ranges from 0 to 99. Each click increments 1.
Provided a set of instructions for how many clicks to turn left or right
(negative or positive increment, respectively), return the number of times
the dial is in position 0.
"""

from pathlib import Path
from tracemalloc import start

ROTATION_SEQUENCE_FILE = "rotation_sequence.txt"
# Values defined in challenge
STARTING_POSITION = 50
DIAL_TICK_COUNT = 100  # There are 100 ticks on the dial, 0-99


def load_rotation_sequence(file: str) -> list[int]:
    """Loads input rotation sequence from file
    and returns a list of integers representing turns of dial.

    :param file: The input file.
    :raises ValueError: If prefixes for input lines are not "L" or "R".
    """
    rotation_sequence = []
    with open(file, "r") as f:
        for line in f:
            direction = line[0]  # First char indicates direction
            magnitude = int(line[1:])  # Remainder of str is magnitude. Cast to int

            # Validate input. Direction must be either "L" or "R"
            if direction not in ["L", "R"]:
                raise ValueError

            rotation_sequence.append(magnitude if direction == "R" else -magnitude)
    return rotation_sequence


def rotate_dial(
    starting_position: int,
    increment: int,
    tick_count: int = DIAL_TICK_COUNT,
):
    """Given a starting position on the dial,
    return the new position after rotating dial
    (i.e. using modulus operator for circular indexing)

    :param starting_position: The starting position on the dial.
    :param tick_count: The number of ticks in the dial.
    :param increment: The increment to apply using modulus operator.
    """
    # The remainder of the incremented position divided by the tick count,
    # given by the modulo operator, equals the final position after turning the dial.
    return (starting_position + increment) % tick_count


def apply_sequence(starting_position: int, rotation_sequence: list[int]):
    """Applies rotation sequence to dial from starting position.

    :param starting_position: Starting position for the dial.
    :param rotation_sequence: Increments to apply to dial.
    """
    current_position = starting_position
    for increment in rotation_sequence:
        current_position += increment


def main():
    """Entry-point for program."""
    try:
        rotation_sequence = load_rotation_sequence(ROTATION_SEQUENCE_FILE)

        starting_position = STARTING_POSITION
        rotation_results = []
        for increment in rotation_sequence:
            new_position = rotate_dial(starting_position, increment)
            rotation_results.append(new_position)
            starting_position = new_position
        zero_count = rotation_results.count(0)
        print(zero_count)

    except ValueError as e:
        print(f"Input values invalid: {e}")


if __name__ == "__main__":
    main()
