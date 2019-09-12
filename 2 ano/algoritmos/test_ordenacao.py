import unittest
from ordenacao import bubble_sort

class TestOrdenacao(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4], "errado...")   
        self.assertEqual(bubble_sort([101, 1, 45, 55, 67, 2, 3, 4]), [1, 2, 3, 4, 45, 55, 67, 101], "errado...") 
        self.assertEqual(bubble_sort(list(range(1000, -1,-1))), list(range(0, 1001)), "errado...") 
if __name__ == '__main__':
    unittest.main()