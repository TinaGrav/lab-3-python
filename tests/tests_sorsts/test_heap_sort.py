from sorts.heap_sort import heap_sort
import unittest
class Test_heap_sort(unittest.TestCase):

   def test_heap_norm(self):
      self.assertEqual(heap_sort([1, 7, 9, 0, 2, 5]), [0, 1, 2, 5, 7, 9])


   def test_heap_long_list(self):
      self.assertEqual(heap_sort([7, 0, 8, 3, 10, 78, 1, 12, 34, 0, 11, 15, 1]), [0, 0, 1, 1, 3, 7, 8, 10, 11, 12, 15, 34, 78])


   def test_heap_big_nub(self):
      self.assertEqual(heap_sort([1038, 34800, 2745, 9103, 23759]), [1038, 2745, 9103, 23759, 34800])


   def test_heap_one(self):
      self.assertEqual(heap_sort([5]), [5])


   def test_heap_float(self):
      self.assertEqual(heap_sort([1.7, 0.9, 5.4, 3.2, 2.0]), sorted([1.7, 0.9, 5.4, 3.2, 2.0]))


   def test_heap_negative(self):
      self.assertEqual(heap_sort([-9, -19, -100, -2, -54]), [-100, -54, -19, -9, -2])