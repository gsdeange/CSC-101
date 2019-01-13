import unittest
from char import *

test1 = "l"
test2 = "Z"

class TestChar(unittest.TestCase):
   def test_lower(self):
      self.assertEqual(is_lower_101(test1), True)
      self.assertEqual(is_lower_101(test2), False)
   def test_char_rot_13(self):
   	  self.assertEqual(char_rot_13(test1), "y")
   	  self.assertEqual(char_rot_13(test2), "N")



if __name__ == '__main__':
   unittest.main()

