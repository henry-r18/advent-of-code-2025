from unittest import TestCase
from day_01.main import execute_rotation_sequence
from day_02.main import (
    parse_id_range,
    find_invalid_ids_part_one,
    find_invalid_ids_part_two,
)
from day_03.main import find_optimal_batteries
from day_04.main import find_accessible_rolls
from day_05.main import find_fresh_ids_part_one, find_fresh_ids_part_two
from day_06.main import transpose_grid, calculate_result_part_two
from day_07.main import load_input as d7_load_input, count_beams_part_one


class DayOneTestCase(TestCase):
    def test_rotate_dial(self):
        # This test sequence comes from the challenge specs
        test_rotation_sequence = [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]
        expected_result = [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]

        starting_position = 50
        rotation_results, total_times_index_at_zero = execute_rotation_sequence(
            starting_position, test_rotation_sequence
        )
        self.assertListEqual(rotation_results, expected_result)

    def test_large_numbers(self):
        test_rotation_sequence = [100, 150, 210]
        expected_result = [50, 0, 10]
        starting_position = 50
        rotation_results, total_times_index_at_zero = execute_rotation_sequence(
            starting_position, test_rotation_sequence
        )
        self.assertListEqual(rotation_results, expected_result)

    def test_count_times_past_zero(self):
        # These values derived from challenge
        test_rotation_sequence = [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]
        expected_result = [
            82,
            52,
            0,
            95,
            55,
            0,
            99,
            0,
            14,
            32,
        ]

        starting_position = 50
        rotation_results, total_times_index_at_zero = execute_rotation_sequence(
            starting_position, test_rotation_sequence
        )
        self.assertListEqual(rotation_results, expected_result)
        self.assertEqual(
            total_times_index_at_zero, 6
        )  # Expected result taken from challenge


class DayTwoTestCase(TestCase):
    def setUp(self) -> None:
        test_input = [
            "11-22",
            "95-115",
            "998-1012",
            "1188511880-1188511890",
            "222220-222224",
            "1698522-1698528",
            "446443-446449",
            "38593856-38593862",
            "565653-565659",
            "824824821-824824827",
            "2121212118-2121212124",
        ]

        self.test_id_ranges = [parse_id_range(range_str) for range_str in test_input]

    def test_find_invalid_ids_part_one(self):
        all_invalid_ids = []
        for id_range in self.test_id_ranges:
            invalid_ids = find_invalid_ids_part_one(id_range)
            all_invalid_ids.extend(invalid_ids)
        print(sum(all_invalid_ids))

    def test_find_invalid_ids_part_two(self):
        all_invalid_ids = []
        for id_range in self.test_id_ranges:
            all_invalid_ids.extend(find_invalid_ids_part_two(id_range))
        print(all_invalid_ids)
        print(sum(all_invalid_ids))


class DayThreeTestCase(TestCase):
    def setUp(self) -> None:
        self.test_input = (
            ("987654321111111", 98),
            ("811111111111119", 89),
            ("234234234234278", 78),
            ("818181911112111", 92),
            ("999999999999999", 99),
        )

    def test_find_optimal_batteries_part_one(self):
        for battery_bank, expected_output in self.test_input:
            with self.subTest(
                battery_bank=battery_bank, expected_output=expected_output
            ):
                optimal_batteries = find_optimal_batteries(battery_bank, 5)


class DayFourTestCase(TestCase):
    def setUp(self) -> None:
        input_text = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

        self.test_input = [list(line) for line in input_text.split("\n")]

    def test_find_accessible_rolls(self):
        shelves = self.test_input
        total_accessible_rolls = find_accessible_rolls(shelves)
        print(total_accessible_rolls)


class DayFiveTestCase(TestCase):

    def setUp(self) -> None:
        input_text = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
        # range(int(start), int(stop) + 1)  # +1 makes ranges inclusive
        sections = input_text.split("\n\n")
        range_strs, id_strs = [section.splitlines() for section in sections]
        range_bounds = [range_str.split("-") for range_str in range_strs]
        ranges, ids = [
            range(int(start), int(stop) + 1) for start, stop in range_bounds
        ], [int(id_str) for id_str in id_strs]
        self.test_input = (ranges, ids)

    def test_find_fresh_ids_part_one(self):
        ranges, ids = self.test_input
        fresh_ids_count = find_fresh_ids_part_one(ranges, ids)
        print(fresh_ids_count)

    def test_find_fresh_ids_part_two(self):
        ranges, _ = self.test_input
        fresh_ids_count = find_fresh_ids_part_two(ranges)
        print(fresh_ids_count)


class DaySixTestCase(TestCase):
    def setUp(self):
        input_text = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

        lines = input_text.splitlines()
        max_line_length = max(map(len, lines))
        self.test_input = [line.ljust(max_line_length) for line in lines]

    # def test_input_parsing(self):
    #     lines = self.test_input
    #     operators = lines.pop().split()
    #     print(operators)
    #     # Reorient columns to rows to form problem grid
    #     grid = list(zip(*lines))
    #     problems = ["".join(line) for line in grid]
    #     # We need to collect the new rows to form problem lists,
    #     # splitting at lines that are all " ", which indicates a column break.
    #     # Then create a new list with sub-lists representing each problem.
    #     problems = []
    #     start = 0
    #     for i, line in enumerate(grid):
    #         if all([elem == " " for elem in line]):
    #             problems.append([int("".join(line)) for line in grid[start:i]])
    #             start = i + 1
    #     if start < len(grid):
    #         problems.append([int("".join(line)) for line in grid[start:]])

    #     # This results in a list of tuples,
    #     # each with a problem list and its operator
    #     problems_with_operators = list(zip(problems, operators))

    # def test_transpose_list(self):
    #     transposed_grid = transpose_grid(self.test_input)
    #     expected_result = [
    #         ["123", "45", "6", "*"],
    #         ["328", "64", "98", "+"],
    #         ["51", "387", "215", "*"],
    #         ["64", "23", "314", "+"],
    #     ]
    #     self.assertListEqual(transposed_grid, expected_result)

    # def test_calculate_result_part_two(self):
    #     transposed_grid = transpose_grid(self.test_input)
    #     calculate_result_part_two(transposed_grid)


class DaySevenTestCase(TestCase):
    def setUp(self) -> None:
        self.test_input = d7_load_input("day_seven/test_input.txt")

    def test_count_beams_part_one(self):
        splitters = count_beams_part_one(self.test_input)
        print(splitters)
