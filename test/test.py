import unittest
import main


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(main.add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(main.add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(main.add(1, -2), -1)
        self.assertEqual(main.add(-1, 2), 1)


if __name__ == '__main__':
    unittest.main()
