import math
import unittest


def calculate_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n должно быть натуральным числом")

    factorials = [math.factorial(i) for i in range(1, n + 1)]
    return factorials


class FactorialCalculatorTest(unittest.TestCase):
    def test_positive_integer_input(self):
        self.assertEqual(calculate_factorial(5), [1, 2, 6, 24, 120])

    def test_zero_input(self):
        self.assertEqual(calculate_factorial(0), [])

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-5)

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            calculate_factorial(3.5)


if __name__ == "__main__":
    unittest.main()
