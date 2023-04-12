import unittest
from search import linear_search, binary_search


class TestSearch(unittest.TestCase):

    # Test for linear search
    def test_linear_search(self):
        self.assertEqual(linear_search([4, 2, 6, 1, 7, 3], 1), 3)

    # Test for binary search
    def test_binary_search(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(data, 6), 5)


if __name__ == "__main__":
    unittest.main()
