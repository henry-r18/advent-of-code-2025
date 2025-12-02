from unittest import TestCase
from main import execute_rotation_sequence


class RotateDialTestCase(TestCase):
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
