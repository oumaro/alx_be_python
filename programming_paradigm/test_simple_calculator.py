#!/usr/bin/env python3
"""
Unit tests for the SimpleCalculator class.
"""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""

    def setUp(self):
        """
        Set up a new SimpleCalculator instance before each test.
        This method is called before each test function is executed.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method of the SimpleCalculator."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, 0), 100)
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtraction(self):
        """Test the subtract method of the SimpleCalculator."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_multiplication(self):
        """Test the multiply method of the SimpleCalculator."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(15, 1), 15)
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.0), 3.0)

    def test_division(self):
        """Test the divide method of the SimpleCalculator."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        self.assertAlmostEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Test for division by zero, which should return None
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None")

if __name__ == '__main__':
    unittest.main()
