import unittest
from ordenacao import (bubble_sort, bubble_sort2,
    insertion_sort, selection_sort, _merge, 
    merge_sort, quick_sort, quick_sort2)

"""
py -m unittest -v test_ordenacao
"""


class TestOrdenacao(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([1]), [1], "errado...")   
        self.assertEqual(bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4], "errado...")   
        self.assertEqual(bubble_sort([101, 1, 45, 55, 67, 2, 3, 4]), [1, 2, 3, 4, 45, 55, 67, 101], "errado...") 
        self.assertEqual(bubble_sort(list(range(1000, -1,-1))), list(range(0, 1001)), "errado...")


    def test_bubble_sort2(self):
        self.assertEqual(bubble_sort2([1]), [1], "errado...")   
        self.assertEqual(bubble_sort2([4, 3, 2, 1]), [1, 2, 3, 4], "errado...")   
        self.assertEqual(bubble_sort2([101, 1, 45, 55, 67, 2, 3, 4]), [1, 2, 3, 4, 45, 55, 67, 101], "errado...") 
        self.assertEqual(bubble_sort2(list(range(1000, -1,-1))), list(range(0, 1001)), "errado...")


    def test_insertion_sort(self):
        # insertion
        self.assertEqual(insertion_sort([1]), [1], "errado...")   
        self.assertEqual(insertion_sort([4, 3, 2, 1]), [1, 2, 3, 4], "errado...")   
        self.assertEqual(insertion_sort([101, 1, 45, 55, 67, 2, 3, 4]), [1, 2, 3, 4, 45, 55, 67, 101], "errado...") 
        self.assertEqual(insertion_sort(list(range(1000, -1,-1))), list(range(0, 1001)), "errado...") 


    def test_selection_sort(self):
        # selection
        self.assertEqual(selection_sort([1]), [1], "errado...")   
        self.assertEqual(selection_sort([4, 3, 2, 1]), [1, 2, 3, 4], "errado...")   
        self.assertEqual(selection_sort([101, 1, 45, 55, 67, 2, 3, 4]), [1, 2, 3, 4, 45, 55, 67, 101], "errado...") 
        self.assertEqual(selection_sort(list(range(1000, -1,-1))), list(range(0, 1001)), "errado...") 


    def test_merge(self):
        self.assertEqual(_merge([1,2,3], [2,3]), [1,2,2,3,3], "errado")
        self.assertEqual(_merge([1,2,3], [3]), [1,2,3,3], "errado")
        self.assertEqual(_merge([1,2], [3,4]), [1,2,3,4], "errado")
        self.assertEqual(_merge([1,2,3], [4,5]), [1,2,3,4,5], "errado")
        self.assertEqual(_merge([1,2,3,4], [4,5,6,7]), [1,2,3,4,4,5,6,7], "errado")


    def test_merge_sort(self):
        self.assertEqual(merge_sort([1]), [1], "errado...")   
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4], "errado...")   
        self.assertEqual(merge_sort([101, 1, 45, 55, 67, 2, 3, 4]), [1, 2, 3, 4, 45, 55, 67, 101], "errado...") 
        self.assertEqual(merge_sort(list(range(1000, -1,-1))), list(range(0, 1001)), "errado...") 
 

    def test_quick_sort(self):
        self.assertEqual(quick_sort([1]), [1], "errado...")   
        self.assertEqual(quick_sort([4, 3, 2, 1]), [1, 2, 3, 4], "errado...")   
        self.assertEqual(quick_sort([101, 1, 45, 55, 67, 2, 3, 4]), [1, 2, 3, 4, 45, 55, 67, 101], "errado...")
        # RecursionError: maximum recursion depth exceeded while calling a Python object = 1000
        self.assertEqual(quick_sort(list(range(500, -1,-1))), list(range(0, 501)), "errado...") 


    def test_quick_sort2(self):
        self.assertEqual(quick_sort2([1]), [1], "errado...")   
        self.assertEqual(quick_sort2([4, 3, 2, 1]), [1, 2, 3, 4], "errado...")   
        self.assertEqual(quick_sort2([101, 1, 45, 55, 67, 2, 3, 4]), [1, 2, 3, 4, 45, 55, 67, 101], "errado...")
        # RecursionError: maximum recursion depth exceeded while calling a Python object = 1000
        self.assertEqual(quick_sort2(list(range(500, -1,-1))), list(range(0, 501)), "errado...") 

if __name__ == '__main__':
    unittest.main()