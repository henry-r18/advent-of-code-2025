from unittest import TestCase
from main import load_input, calculate_product_largest_circuits_part_one


class DayEightTestCase(TestCase):
    def setUp(self):
        self.test_input = load_input(file="test_input.txt")

    def test_find_nearest_neighbors(self):
        junction_boxes = self.test_input
        product_largest_circuits = calculate_product_largest_circuits_part_one(
            junction_boxes
        )
        print(product_largest_circuits)
