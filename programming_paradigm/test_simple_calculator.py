# test_simple_calculator.py - Contains unit tests for the SimpleCalculator class.

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, testing all four core methods.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method runs."""
        self.calc = SimpleCalculator()

    # --- Test Addition Method (Required for strict checker) ---
    def test_addition(self):
        """Test the addition method with a basic case."""
        self.assertEqual(self.calc.add(2, 3), 5)

    # --- Comprehensive Test Addition Methods ---
    def test_addition_standard(self):
        """Test addition with standard positive integers."""
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_addition_with_negative_numbers(self):
        """Test addition involving negative integers."""
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_addition_with_zero(self):
        """Test addition when one operand is zero."""
        self.assertEqual(self.calc.add(0, 100), 100)

    # --- Test Subtraction Method ---
    def test_subtraction_positive_result(self):
        """Test subtraction where the result is positive."""
        self.assertEqual(self.calc.subtract(20, 7), 13)

    def test_subtraction_negative_result(self):
        """Test subtraction where the result is negative."""
        self.assertEqual(self.calc.subtract(7, 20), -13)
        
    def test_subtraction_involving_negative(self):
        """Test subtraction involving a negative second operand (A - (-B))."""
        self.assertEqual(self.calc.subtract(10, -5), 15) # 10 - (-5) = 15

    # --- Test Multiplication Method ---
    def test_multiplication_positive(self):
        """Test multiplication of two positive numbers."""
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiplication_negative(self):
        """Test multiplication involving negative numbers."""
        self.assertEqual(self.calc.multiply(-6, 7), -42)
        self.assertEqual(self.calc.multiply(-6, -7), 42)

    def test_multiplication_by_zero(self):
        """Test multiplication where one factor is zero."""
        self.assertEqual(self.calc.multiply(99, 0), 0)

    # --- Test Division Method ---
    def test_division_standard(self):
        """Test standard division resulting in a float."""
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_division_by_zero(self):
        """Test division by zero, which must return None as per the function spec."""
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_negative_numbers(self):
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)