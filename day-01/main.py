"""Advent of Code 2025 - Day 01

A safe dial ranges from 0 to 99. Each click increments 1.
Provided a set of instructions for how many clicks to turn left or right
(negative or positive increment, respectively), return the number of times
the dial is in position 0.
"""

ROTATION_SEQUENCE_FILE = "challenge_input.txt"
# Values defined in challenge
STARTING_POSITION = 50
DIAL_TICK_COUNT = 100  # There are 100 ticks on the dial (0-99)


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
) -> tuple[int, int]:
    """Given a starting position on the dial,
    return the new position after rotating the dial.

    :param starting_position: The starting position on the dial.
    :param increment: The increment to apply using modulus operator.
    :param tick_count: The number of ticks on the dial.
    :return: The new position after rotating the dial,
        and the number of times the dial passes or lands on 0 during this turn.
    """
    times_position_at_zero = 0

    # If the increment is negative,
    # use the modulus of the difference between the tick count and the starting position,
    # plus the absolute value of the increment, divided by the tick count
    # to calculate the number of times the dial passes or lands on 0.
    # This avoids the issue of negative increments larger than the tick count counting twice,
    # when they should only count once. Consider the case starting at 0 and incrementing by -110
    # to see why the calculation for positive increments is not sufficient.
    if increment < 0:
        times_position_at_zero += (
            (tick_count - starting_position) % tick_count + abs(increment)
        ) // tick_count
    else:
        times_position_at_zero += (starting_position + increment) // tick_count
    # Calculate the new position after rotating the dial
    # by taking the modulus of the sum of the starting position and the increment.
    new_position = (starting_position + increment) % tick_count

    return new_position, times_position_at_zero


def execute_rotation_sequence(
    starting_position: int,
    rotation_sequence: list[int],
) -> tuple[list[int], int]:
    """Executes the rotation sequence listed in the input file,
    from the given starting position.

    :param starting_position: Starting position for the dial.
    :param rotation_sequence: Increments to apply to dial.
    :return: The list of positions after each rotation,
        and the total number of times the dial passes or lands on 0 during the sequence.
    """
    rotation_results = []
    total_times_position_at_zero = 0
    for increment in rotation_sequence:
        new_position, times_position_at_zero = rotate_dial(starting_position, increment)
        rotation_results.append(new_position)
        starting_position = new_position
        total_times_position_at_zero += times_position_at_zero
    return rotation_results, total_times_position_at_zero


def main():
    """Entry-point for program."""
    try:
        rotation_sequence = load_rotation_sequence(ROTATION_SEQUENCE_FILE)
        rotation_results, total_times_index_at_zero = execute_rotation_sequence(
            starting_position=STARTING_POSITION, rotation_sequence=rotation_sequence
        )
        # Part One asks for count of zeros in rotation results
        zero_count = rotation_results.count(0)
        print(f"Part One answer: {zero_count}")
        # Part Two asks for the total number of times the dial hits position 0
        print(f"Part Two answer: {total_times_index_at_zero}")

    except ValueError as e:
        print(f"Input values invalid: {e}")


if __name__ == "__main__":
    main()
