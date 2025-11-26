from sorts.counting_sort import counting_sort
import unittest
class Test_counting_sort(unittest.TestCase):

   def test_counting_norm(self):
      self.assertEqual(counting_sort([1, 0, 5, 3, 2]), [0, 1, 2, 3, 5])


   def test_counting_long_list(self):
      self.assertEqual(counting_sort([7, 0, 8, 3, 10, 78, 1, 12, 34, 0, 11, 15, 1]), [0, 0, 1, 1, 3, 7, 8, 10, 11, 12, 15, 34, 78])


   def test_counting_big_nub(self):
      self.assertEqual(counting_sort([1038, 34800, 2745, 9103, 23759]), [1038, 2745, 9103, 23759, 34800])


   def test_counting_one(self):
      self.assertEqual(counting_sort([5]), [5])
