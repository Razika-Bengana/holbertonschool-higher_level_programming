#usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """def test"""
    def test_max_integer(self):
        """create test_max_integer:funtion value
        """
        self.assertEqual(max_integer([2, 3, 6]), 5)
        self.assertEqual(max_integer([3, 5, 7]), 6)
        self.assertEqual(max_integer([9, 3, 2]), 9)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-3, -2, -5]), -2)
        self.assertEqual(max_integer([]), None)
        self.assertNotEqual(max_integer([3, 7, 5]), 8)
        self.assertNotIn(max_integer([5, 4, 9), [9, 4, 6])
        self.assertIsInstance(max_integer([2, 4, 6]), int)
        self.assertTrue(max_integer([5, 4, 8]), int)
        self.assertFalse(max_integer([0, 0, 0]), False)

        if __name__ == '__main__':
            unittest.main()
