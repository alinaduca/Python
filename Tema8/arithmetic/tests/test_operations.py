import unittest
from arithmetic import operations

class TestArithmeticOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(operations.add(2, 3), 5)
        self.assertEqual(operations.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(operations.subtract(5, 3), 2)
        self.assertEqual(operations.subtract(1, 2), -1)

    def test_multiplication(self):
        self.assertEqual(operations.multiply(2, 3), 6)
        self.assertEqual(operations.multiply(-1, 4), -4)

    def test_division(self):
        self.assertEqual(operations.divide(6, 3), 2)
        self.assertEqual(operations.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            operations.divide(1, 0)

if __name__ == '__main__':
    unittest.main()