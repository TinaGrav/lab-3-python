from sorts.quick_sort import quick_sort
import unittest
class Test_quick_sort(unittest.TestCase):

   def test_quick_norm(self):
      self.assertEqual(quick_sort([1, 10, 3, 4, 8, 2, 7, 8]), [1, 2, 3, 4, 7, 8, 8, 10])


   def test_quick_negative(self):
      self.assertEqual(quick_sort([-78, -10, -100, -4, -193]), [-193, -100, -78, -10, -4])


   def test_quick_long_list(self):
      self.assertEqual(quick_sort([9, 0, 8, 4, 10, 88, 1, 12, 34, 0, 19, 15, 1]), [0, 0, 1, 1, 4, 8, 9, 10, 12, 15, 19, 34, 88])


   def test_quick_big_nub(self):
      self.assertEqual(quick_sort([1038, 34800, 2745, 9103, 23759]), [1038, 2745, 9103, 23759, 34800])


   def test_quick_one(self):
      self.assertEqual(quick_sort([9]), [9])


   def test_bubble_float(self):
      self.assertEqual(quick_sort([1.7, 0.9, 5.4, 3.2, 2.0]), sorted([1.7, 0.9, 5.4, 3.2, 2.0]))


