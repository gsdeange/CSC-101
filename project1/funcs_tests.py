# Project 1
#
#Name: Garrett DeAngelis
# Intstructor: P. Hatalsky
# Section: 12

import funcs
import unittest

class TestCases(unittest.TestCase):

   def test_poundsToKG(self):
      self.assertAlmostEqual(funcs.poundsToKG(110), 49.89512)
      self.assertAlmostEqual(funcs.poundsToKG(130), 58.96696)

   def test_getMassObject(self):
      self.assertAlmostEqual(funcs.getMassObject('t'), 0.1)
      self.assertAlmostEqual(funcs.getMassObject('g'), 5.3)

   def test_getVelocityObject(self):
      self.assertAlmostEqual(funcs.getVelocityObject(30), 12.12435565298)
      self.assertAlmostEqual(funcs.getVelocityObject(96), 21.68870673876)

   def test_getVelocitySkater(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(49.89512,0.1,12.124355),0.02429968101)
      self.assertAlmostEqual(funcs.getVelocitySkater(58.96696, 5.3, 21.679483),1.9485701806)

if __name__ == '__main__':
   unittest.main()










