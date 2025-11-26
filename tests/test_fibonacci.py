from fact_fibo.fibonacci import fibo_recursive
from fact_fibo.fibonacci import fibo
import unittest

class Test_fibo(unittest.TestCase):

   def test_fibo_norm(self):
      self.assertEqual(fibo(10), 55)


   def test_fibo_big(self):
      self.assertEqual(fibo(128), 251728825683549488150424261)


   def test_fibo_very_big(self):
      with self.assertRaises(ValueError):
         fibo(6000000)


   def test_fibo_negative(self):
      with self.assertRaises(ValueError):
         fibo(-5000)


   def test_fibo_zero(self):
      with self.assertRaises(ValueError):
         fibo(0)


class Test_fibo_recursive(unittest.TestCase):

   def test_fibo_recurs_norm(self):
      self.assertEqual(fibo_recursive(1), 1)

   def test_fibo_recurs_norm(self):
      self.assertEqual(fibo_recursive(40), 102334155)

   def test_fibo_recurs_very_big(self):
      with self.assertRaises(ValueError):
         fibo_recursive(0)


   def test_fibo_recurs_very_big(self):
      with self.assertRaises(ValueError):
         fibo_recursive(80000)


   def test_fact_recurs_negative(self):
      with self.assertRaises(ValueError):
         fibo_recursive(-37000)