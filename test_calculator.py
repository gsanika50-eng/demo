import unittest
from calculator import add, subtract, multiply, divide, calculate

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 5), -4)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_calculate(self):
        self.assertEqual(calculate("add", 10, 5), 15)
        self.assertEqual(calculate("+", 10, 5), 15)
        self.assertEqual(calculate("subtract", 10, 5), 5)
        self.assertEqual(calculate("-", 10, 5), 5)
        self.assertEqual(calculate("multiply", 10, 5), 50)
        self.assertEqual(calculate("*", 10, 5), 50)
        self.assertEqual(calculate("divide", 10, 5), 2)
        self.assertEqual(calculate("/", 10, 5), 2)
        with self.assertRaises(ValueError):
            calculate("unknown", 10, 5)

if __name__ == "__main__":
    unittest.main()
