from unittest import TestCase
from day_one.main import execute_rotation_sequence
from day_two.main import (
    parse_id_range,
    find_invalid_ids_part_one,
    find_invalid_ids_part_two,
)
from day_three.main import find_optimal_batteries


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
            (list("987654321111111"), 98),
            (list("811111111111119"), 89),
            (list("234234234234278"), 78),
            (list("818181911112111"), 92),
            (list("999999999999999"), 99),
        )

    def test_find_optimal_batteries_part_one(self):
        for battery_bank, expected_output in self.test_input:
            with self.subTest(
                battery_bank=battery_bank, expected_output=expected_output
            ):
                optimal_batteries = find_optimal_batteries(battery_bank)
                self.assertEqual(optimal_batteries, expected_output)
