import unittest
from app import add, multiply

class TestApplication(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_multiplication(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_addition_negative(self):
        self.assertEqual(add(-10, 5), -5)

if __name__ == "__main__":
    unittest.main()
