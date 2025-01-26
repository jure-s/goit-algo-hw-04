import unittest
from merge_k_lists import merge_k_lists

class TestMergeKLists(unittest.TestCase):
    def test_multiple_sorted_lists(self):
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        self.assertEqual(merge_k_lists(lists), expected)

    def test_single_list(self):
        lists = [[1, 2, 3]]
        expected = [1, 2, 3]
        self.assertEqual(merge_k_lists(lists), expected)

    def test_empty_lists(self):
        lists = [[], [], []]
        expected = []
        self.assertEqual(merge_k_lists(lists), expected)

    def test_mixed_empty_and_non_empty_lists(self):
        lists = [[1, 2, 3], [], [4, 5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(merge_k_lists(lists), expected)

    def test_no_lists(self):
        lists = []
        expected = []
        self.assertEqual(merge_k_lists(lists), expected)

    def test_large_numbers(self):
        lists = [[1000000, 1000001], [999999, 1000002]]
        expected = [999999, 1000000, 1000001, 1000002]
        self.assertEqual(merge_k_lists(lists), expected)

if __name__ == "__main__":
    unittest.main()