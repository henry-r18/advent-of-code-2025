from unittest import TestCase
from main import execute_rotation_sequence


class RotateDialTestCase(TestCase):
    def test_rotate_dial(self):
        # This test sequence comes from the challenge specs
        test_rotation_sequence = [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]
        expected_result = [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]

        starting_position = 50
        output = execute_rotation_sequence(starting_position, test_rotation_sequence)
        self.assertListEqual(output, expected_result)

    def test_large_numbers(self):
        test_rotation_sequence = [100, 150, 210]
        expected_result = [50, 0, 10]
        starting_position = 50
        output = execute_rotation_sequence(starting_position, test_rotation_sequence)
        self.assertListEqual(output, expected_result)
