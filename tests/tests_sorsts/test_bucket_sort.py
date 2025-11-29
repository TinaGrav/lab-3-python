from sorts.bucket_sort import bucket_sort
import unittest
class Test_bucket_sort(unittest.TestCase):

   def test_bucket_norm(self):
      self.assertEqual(bucket_sort([2, 0, 6, 5, 2]), [0, 2, 2, 5, 6])


   def test_bucket_norm_with_bucket_number(self):
      self.assertEqual(bucket_sort([2, 0, 6, 5, 2], 2), [0, 2, 2, 5, 6])


   def test_bucket_long_list(self):
      self.assertEqual(bucket_sort([7, 0, 8, 3, 10, 78, 1, 12, 34, 0, 11, 15, 1]), [0, 0, 1, 1, 3, 7, 8, 10, 11, 12, 15, 34, 78])


   def test_bucket_big_nub(self):
      self.assertEqual(bucket_sort([1038, 34800, 2745, 9103, 23759]), [1038, 2745, 9103, 23759, 34800])


   def test_bucket_one(self):
      self.assertEqual(bucket_sort([7]), [7])


   def test_bucket_float(self):
       self.assertEqual(bucket_sort([1.2, 3.4, 1.1, 2.7, 0.6]), sorted([1.2, 3.4, 1.1, 2.7, 0.6]))


   def test_bucket_negative_float(self):
      with self.assertRaises(ValueError):
         bucket_sort([-1.2, -3.4, -1.1, -2.7, -0.6]), sorted([-1.2, -3.4, -1.1, -2.7, -0.6])
