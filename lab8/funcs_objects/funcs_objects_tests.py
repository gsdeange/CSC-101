import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
      # Add code here.
      p1 = Points(1.1, 2.0)
      p2 = Points(1.1, 2.0)
      self.assertEqual(p2.x, p1.x)
      self.assertEqual(p2.y, p1.y)	
	  
   def test_circle(self):
      # Add code here.
      p = Points(1, 2)
      c = Circle(10, p)
      c2 = Circle(10, p)
      self.assertEqual(c.center,  c2.center)
	  
	  # Add other testing functions
	  
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

