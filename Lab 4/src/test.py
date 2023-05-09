import unittest
from knapsack import zeroone_knapsack_dynamic_prog, zeroone_knapsack_brute_force, fractional_knapsack_brute_force, fractional_knapsack_greedy
from item import Item


class TestSearch(unittest.TestCase):

    def test_zeroone_knapsack(self):
        '''
        Test for 0/1 knapsack
        '''
        items = [
            Item("Chair", 10, 60),
            Item("Chair", 20, 100),
            Item("Chair", 30, 120),
        ]
        dynamic_max_value = zeroone_knapsack_dynamic_prog(
            items, 50)
        sol, bruteF_max_value = zeroone_knapsack_brute_force(
            items, 50)
        self.assertEqual(dynamic_max_value, bruteF_max_value)

    def test_fractional_knapsack(self):
        '''
        Test for Fractional knapsack
        '''
        items = [
            Item("Chair", 10, 60),
            Item("Chair", 20, 100),
            Item("Chair", 30, 120),
        ]
        sol, bruteF_max_value = fractional_knapsack_brute_force(
            items, 50)
        sol2, greedy_max_value = fractional_knapsack_greedy(
            items, 50)
        self.assertEqual(greedy_max_value, bruteF_max_value)

    def test_zeroone_knapsack_dynamic_prog(self):
        '''
        Test for 0/1 knapsack by dynamic programming
        '''
        items = [
            Item("Chair", 10, 60),
            Item("Chair", 20, 100),
            Item("Chair", 30, 120),
        ]
        max_value = zeroone_knapsack_dynamic_prog(
            items, 50)
        self.assertEqual(max_value, 220)

    def test_zeroone_knapsack_brute_force(self):
        '''
        Test for 0/1 knapsack by brute force
        '''
        items = [
            Item("Chair", 10, 60),
            Item("Chair", 20, 100),
            Item("Chair", 30, 120),
        ]
        sol, max_value = zeroone_knapsack_brute_force(
            items, 50)
        self.assertEqual(max_value, 220)

    def test_fractional_knapsack_brute_force(self):
        '''
        Test for fractional knapsack by brute force
        '''
        items = [
            Item("Chair", 10, 60),
            Item("Chair", 20, 100),
            Item("Chair", 30, 120),
        ]
        sol, max_value = fractional_knapsack_brute_force(
            items, 50)
        self.assertEqual(max_value, 240)

    def test_fractional_knapsack_greedy(self):
        '''
        Test for fractional knapsack by greedy approach
        '''
        items = [
            Item("Chair", 10, 60),
            Item("Chair", 20, 100),
            Item("Chair", 30, 120),
        ]
        sol, max_value = fractional_knapsack_greedy(
            items, 50)
        self.assertEqual(max_value, 240)


if __name__ == "__main__":
    unittest.main()
