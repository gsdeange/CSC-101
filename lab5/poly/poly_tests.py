import unittest
import poly
poly1 = [1, 2, 3]
poly2 = [3, 2, 1]
poly3 = [3, 8, 14, 8, 3]
poly4 = [4, 4, 4]
poly5 = [5, 6, 7]
poly6 = []
class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
  
  
   

   # Add tests here
   def test_poly_add2(self):
      self.assertListAlmostEqual(poly.poly_add2(poly1, poly2), poly4) 
      self.assertListAlmostEqual(poly.poly_add2(poly1, poly4), poly5)
   def test_poly_mult2(self):
      self.assertListAlmostEqual(poly.poly_mult2(poly1, poly2), poly3)
      self.assertListAlmostEqual(poly.poly_mult2(poly2, poly1), poly3)
   

if __name__ == '__main__':
   unittest.main()
h