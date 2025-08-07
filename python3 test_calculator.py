import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(0, 5), -5)

    def test_divide(self):
        self.assertEqual(calculator.divide(8, 2), 4)
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
