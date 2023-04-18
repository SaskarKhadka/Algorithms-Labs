import unittest
from insertion_sort import insertion_sort
from merge_sort import merge_sort

class SortTest(unittest.TestCase):

    def test_insertion_sort(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        insertion_sort(input)

        self.assertListEqual(input, output)

        input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        insertion_sort(input)

        self.assertListEqual(input, output)

        input = [3, 6, 1, 8, 3, 9, 2, 10, 5, 4]
        output = [1, 2, 3, 3, 4, 5, 6, 8, 9, 10]

        insertion_sort(input)

        self.assertListEqual(input, output)

    
    def test_merge_sort(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        merge_sort(input, 0, len(input)-1)

        self.assertListEqual(input, output)

        input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        merge_sort(input, 0, len(input)-1)

        self.assertListEqual(input, output)

        input = [3, 6, 1, 8, 3, 9, 2, 10, 5, 4]
        output = [1, 2, 3, 3, 4, 5, 6, 8, 9, 10]

        merge_sort(input, 0, len(input)-1)

        self.assertListEqual(input, output)



if __name__=="__main__":
    unittest.main()