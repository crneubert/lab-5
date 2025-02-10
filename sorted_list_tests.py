# Tests sorted lists.
# CSC 202, Lab 5
# Given tests, Summer '19

import unittest
from sorted_list import *


class TestSortedList(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing sorted list equality and representation"

        lst = SortedList()
        lst.array = [0, None, None, None]
        lst.size = 1

        self.assertEqual(lst, lst, msg)
        self.assertEqual(repr(lst),
         "SortedList(4, [0, None, None, None], 1)", msg)

        other = SortedList()
        other.array = [1, None, None, None]
        other.size = 1

        self.assertNotEqual(lst, other, msg)
        self.assertNotEqual(lst, lst.array, msg)

    def test02_insert(self):
        msg = "Testing inserting into sorted lists"

        lst = SortedList()
        insert(lst, -3)
        insert(lst, 3)
        insert(lst, -1)

        self.assertEqual(size(lst), 3, msg)
        self.assertEqual(get(lst, 0), -3, msg)
        self.assertEqual(get(lst, 1), -1, msg)
        self.assertEqual(get(lst, 2), 3, msg)

    def test03_remove(self):
        msg = "Testing removing from sorted lists"

        lst = SortedList()
        insert(lst, -3)
        insert(lst, 3)
        remove(lst, find(lst, 3))
        insert(lst, -1)

        self.assertEqual(size(lst), 2, msg)
        self.assertEqual(get(lst, 0), -3, msg)
        self.assertEqual(get(lst, 1), -1, msg)

    def test04_create(self):
        msg = "Testing creating sorted lists"

        lst = create([0, 1, 2], 3)
        insert(lst, -3)
        remove(lst, find(lst, 1))
        insert(lst, 3)
        remove(lst, find(lst, 3))
        insert(lst, -1)

        self.assertEqual(size(lst), 4, msg)
        self.assertEqual(get(lst, 0), -3, msg)
        self.assertEqual(get(lst, 1), -1, msg)
        self.assertEqual(get(lst, 2), 0, msg)
        self.assertEqual(get(lst, 3), 2, msg)

    def test05_insert(self):
        msg = "Testing allocating more memory for array"

        lst = create([0, 1, 2, 3, 4], 5)

        self.assertEqual(size(lst), 5, msg)
        self.assertEqual(get(lst, 0), 0, msg)
        self.assertEqual(get(lst, 1), 1, msg)
        self.assertEqual(get(lst, 2), 2, msg)
        self.assertEqual(get(lst, 3), 3, msg)
        self.assertEqual(get(lst, 4), 4, msg)

    def test06_find(self):
        msg = "Testing finding in long list"

        lst = create([0, 1, 2, 3, 4, 5, 6], 7)
        print(lst)
        sorted = find(lst, 5)

        self.assertEqual(sorted, 5, msg)

    def test07_find(self):
        msg = "Testing value not in sorted list"

        lst = create([0, 1, 2, 3, 4, 5, 6], 7)

        with self.assertRaises(ValueError):
            find(lst, -1)

    def test08_create(self):
        msg = "Testing creating and sorting an unsorted list"

        lst = create([0, 1, -8, 2, 10, -5], 6)

        self.assertEqual(size(lst), 6, msg)
        self.assertEqual(get(lst, 0), -8, msg)
        self.assertEqual(get(lst, 1), -5, msg)
        self.assertEqual(get(lst, 2), 0, msg)
        self.assertEqual(get(lst, 3), 1, msg)
        self.assertEqual(get(lst, 4), 2, msg)
        self.assertEqual(get(lst, 5), 10, msg)

    def test09_remove(self):
        msg = "Testing removing value out of range"

        lst = create([0, 1, 2, 3, 4, 5, 6], 7)

        with self.assertRaises(IndexError):
            remove(lst, 7)

    def test10_get(self):
        msg = "Testing getting value out of range"

        lst = create([0, 1, 2, 3, 4, 5, 6], 7)

        with self.assertRaises(IndexError):
            get(lst, -7)

if __name__ == "__main__":
    unittest.main()
