import unittest
from lab_1 import square, find_kth_largest, longest_peak

class TestFunctions(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square([-4, -2, 0, 1, 3]), [0, 1, 4, 9, 16])
        self.assertEqual(square([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])
    
    def test_find_kth_largest(self):
        self.assertEqual(find_kth_largest([15, 7, 22, 9, 36, 2, 42, 18], 3), (22, 2))
    
    def test_longest_peak(self):
        self.assertEqual(longest_peak([1, 3, 5, 4, 2, 8, 3, 7]), 5)
        
if __name__ == '__main__':
    unittest.main()
