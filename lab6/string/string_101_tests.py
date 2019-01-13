import unittest
from string_101 import *

test1 = "pizza"
test2 = "calcudoku"

class TestString(unittest.TestCase):
   def test_rot13(self):
      self.assertEqual(str_rot_13(test1), "cvmmn")
      self.assertEqual(str_rot_13(test2), "pnyphqbxh")
   def test_translate(self):
   	  self.assertEqual(str_translate_101("banana", "a", "z"), "bznznz")
   	  self.assertEqual(str_translate_101("ascii", "i", "a"), "ascaa")  

if __name__ == '__main__':
   unittest.main()
