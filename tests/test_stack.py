from class_stack import Stack
import unittest
class Test_stack(unittest.TestCase):

   def test_stack_len(self):
      self.assertEqual(Stack([2, 4, 6]).__len__(), 3)


   def test_stack_len_empty(self):
      self.assertEqual(Stack([]).__len__(), 0)


   def test_stack_push(self):
      stack = Stack([1, 2, 3])
      stack.push(4)
      result = stack
      self.assertEqual(result, [1, 2, 3, 4])

   def test_stack_push_empty(self):
      stack = Stack([])
      stack.push(4)
      stack.push(0)
      result = stack
      self.assertEqual(result, [4, 0])


   def test_pop_empty(self):
      with self.assertRaises(IndexError):
         Stack([]).pop()


   def test_pop(self):
      stack = Stack([4, 0, 9])
      stack.pop()
      result = stack
      self.assertEqual(result, [4, 0])


   def test_peek(self):
      self.assertEqual(Stack([2, 4, 6]).peek(), 6)


   def test_peek_empty(self):
      with self.assertRaises(IndexError):
         Stack([]).peek()


   def test_isempty(self):
      self.assertEqual(Stack([2, 4, 6]).is_empty(), False)


   def test_isempty_not(self):
      self.assertEqual(Stack([]).is_empty(), True)


   def test_min(self):
      self.assertEqual(Stack([2, 4, 6]).min(), 2)


   def test_min_empty(self):
      with self.assertRaises(IndexError):
         Stack([]).min()