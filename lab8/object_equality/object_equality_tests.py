import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality(self):
      # Add test here
      p1 = Points(1.3, 2.0)
      p2 = Points(1.3, 2.0)
      #result1 = Points(p1)
      #result2 = Points(p2)
      self.assertEqual(p1, p2)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

