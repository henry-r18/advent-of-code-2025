from unittest import TestCase
from main import load_input, calculate_largest_square_part_one


class DayNineTestCase(TestCase):
    def setUp(self):
        self.test_input = load_input(file="test_input.txt")

    def test_find_nearest_neighbors(self):
        red_tiles = self.test_input
        largest_square = calculate_largest_square_part_one(red_tiles)
        print(largest_square)
