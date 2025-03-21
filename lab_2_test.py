import unittest
from lab_2 import can_place_cows, largest_min_distance, place_cows, generate_cow_names
class TestAggressiveCows(unittest.TestCase):
    def test_can_place_cows(self):
        self.assertTrue(can_place_cows([1, 2, 4, 8, 9], 3, 3))
        self.assertFalse(can_place_cows([1, 2, 4, 8, 9], 3, 5))

if __name__ == "__main__":
    unittest.main()
