from unittest import TestCase
from main import rotate_dial


class RotateDialTestCase(TestCase):
    def test_rotate_dial(self):
        # This test sequence comes from the challenge specs
        test_rotation_sequence = [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]
        expected_result = [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]

        starting_position = 50
        output = []
        for increment in test_rotation_sequence:
            new_starting_position = rotate_dial(
                increment=increment, starting_position=starting_position
            )
            starting_position = new_starting_position
            output.append(starting_position)

        self.assertListEqual(output, expected_result)
