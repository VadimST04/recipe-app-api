"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_calc_module(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        expected_result = 11
        self.assertEquals(res, expected_result)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 15)
        expected_result = 5
        self.assertEqual(res, expected_result)
