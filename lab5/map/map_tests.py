import unittest
import map

n = 1
n2 = 3
test1 = [0, 1, 2, 3, 4]

test2 = [0, 1, 4, 9, 16]
test3 = [5, 6, 7, 8, 9]
test4 = [25, 36, 49, 64, 81]
test5 = [1, 2, 3, 4, 5]
test6 = [8, 9, 10, 11, 12]
test7 = [True, False, True, False, True]
test8 = [False, True, False, True, False]

class TestCases(unittest.TestCase):
		 
   def test_square_all(self):
      self.assertAlmostEqual(map.square_all(test1), test2)
      self.assertAlmostEqual(map.square_all(test3), test4)
   def test_add_n_all(self):
      self.assertAlmostEqual(map.add_n_all(test1, n), test5)
      self.assertAlmostEqual(map.add_n_all(test3, n), test6)
   #def test_even_or_odd_all(self):
   #   for i in range(len(test1)):
   #      self.assertAlmostEqual(map.even_or_odd_all(test1[i]), test7[i])
   #      self.assertAlmostEqual(map.even_or_odd_all(test3[i]), test8[i])
	  
   
      
   


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

