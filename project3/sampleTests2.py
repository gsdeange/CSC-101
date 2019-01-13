import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
      
   def test_check_rows0(self):
      puzzle = []
      puzzle.append([3, 5, 2, 1, 4])
      puzzle.append([5, 1, 3, 4, 2])
      puzzle.append([2, 4, 1, 5, 3])
      puzzle.append([1, 2, 4, 3, 5])
      puzzle.append([4, 3, 5, 2, 1])
      self.assertTrue(check_rows_valid(puzzle))
      
   def test_check_columns0(self):
      puzzle = []
      puzzle.append([3, 5, 2, 1, 4])
      puzzle.append([5, 1, 3, 4, 2])
      puzzle.append([2, 4, 1, 5, 3])
      puzzle.append([1, 2, 4, 3, 5])
      puzzle.append([4, 3, 5, 2, 1])
      self.assertTrue(check_columns_valid(puzzle))
      
   def test_check_cages0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertTrue(check_cages_valid(puzzle, cages))
      
   def test_check_valid0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertTrue(check_valid(puzzle, cages))
      
   def test_get_cages0(self):
      cages = [[9, 3, 0, 5, 6],
               [7, 2, 1, 2],
               [10, 3, 3, 8, 13],
               [14, 4, 4, 9, 14, 19],
               [3, 1, 7]
               [8, 3, 10, 11, 16]
               []			   ]
      self.assertEqual(cages, get_cages())

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

