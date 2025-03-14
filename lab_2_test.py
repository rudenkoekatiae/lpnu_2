import unittest
from lab_2 import can_place_cows, largest_min_distance

class TestAggressiveCows(unittest.TestCase):
    def test_example(self):
        self.assertEqual(largest_min_distance(5, 3, [1, 2, 8, 4, 9]), 3)

if __name__ == "__main__":
    unittest.main()