from sorts.bubble_sort import bubble_sort
import unittest
class Test_bubble_sort(unittest.TestCase):

   def test_bubble_norm(self):
      self.assertEqual(bubble_sort([1, 0, 5, 3, 2]), [0, 1, 2, 3, 5])

   def test_bubble_float(self):
      self.assertEqual(bubble_sort([1.7, 0.9, 5.4, 3.2, 2.0]), sorted([1.7, 0.9, 5.4, 3.2, 2.0]))


   def test_bubble_long_list(self):
      self.assertEqual(bubble_sort([7, 0, 8, 3, 10, -9, 78, 1, 12, 34, 0, 11, 15, 1]), [-9, 0, 0, 1, 1, 3, 7, 8, 10, 11, 12, 15, 34, 78])


   def test_bubble_negative(self):
      self.assertEqual(bubble_sort([-9, -19, -100, -2, -54]), [-100, -54, -19, -9, -2])


   def test_bubble_one(self):
      self.assertEqual(bubble_sort([1]), [1])