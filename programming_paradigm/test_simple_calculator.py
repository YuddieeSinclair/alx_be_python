import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    #test case for the add function

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 5), 4)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(-10, -5), -15)


    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 5), -6)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(-10, -5), 50)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-1, 5), -0.2)
        self.assertEqual(self.calc.divide(-10, -5), 2)
        self.assertEqual(self.calc.divide(10, 0), None)
