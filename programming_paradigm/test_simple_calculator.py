import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        # for two postive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 200), 300)

        # for two negative numbers
        self.assertEqual(self.calc.add(-3, -2), -5)

        # for a positive and a negative number
        self.assertEqual(self.calc.add(10, -5), 5)
        self.assertEqual(self.calc.add(-5, 5), 0)

        # with zero
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(0, 90), 90)

    def test_subtraction(self):
        # for two postive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(100, 200), -100)

        # for a positive and a negative number
        self.assertEqual(self.calc.subtract(10, -5), 15)

        # for two negative numbers
        self.assertEqual(self.calc.subtract(-3, -2), 1)

         # with zero
        self.assertEqual(self.calc.subtract(90, 0), 90)
        self.assertEqual(self.calc.subtract(0, 90), -90)

    def test_multiplication(self):
        # for two postive numbers
        self.assertEqual(self.calc.multiply(5, 3), 15)

         # for a positive and a negative number
        self.assertEqual(self.calc.add(10, -5), -50)

if __name__ == '__main__':
    inittest.main()