import unittest
from fold import *

numList1 = []
numList2 = [1, 2, 3, 4]
numList3 = [4, 2, 3, 1]
numList4 = [0, 4, 3, 1]

class TestCases(unittest.TestCase):

   def test_sum(self):
      self.assertEqual(sum(numList4), 8)
      self.assertEqual(sum(numList2), 10)
      self.assertEqual(sum(numList3), 10)

   def test_index_of_smallest(self):
   	  self.assertEqual(index_of_smallest(numList1), -1)
   	  self.assertEqual(index_of_smallest(numList2), 0)
   	  self.assertEqual(index_of_smallest(numList3), 3)
      


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

