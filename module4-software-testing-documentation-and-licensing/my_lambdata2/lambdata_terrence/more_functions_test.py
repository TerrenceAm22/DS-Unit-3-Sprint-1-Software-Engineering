import unittest
from random import randint
from more_functions import add, multiply, subtract

class Testing_Case(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(10, 8), 80)
        self.assertEqual(multiply(2, 10), 20)
    def test_add(self):
        self.assertEqual(add(5, 10), 15)
        



if __name__ == '__main__':
    unittest.main()

