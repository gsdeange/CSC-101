import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):

   def test_displayLMState(self):
      pass
   def test_displayLMState2(self):
      pass
   def test_getFuelRate(self):
      pass
   def test_getFuelRate2(self):
      pass
   def test_updateAltitude(self):
      self.assertAlmostEqual(updateAltitude(10, 3, 4), 15)
   def test_updateAltitude2(self):
      self.assertAlmostEqual(updateAltitude(20, 6, 8), 30)
   def test_updateVelocity(self):
      self.assertAlmostEqual(updateVelocity(5, 5), 10)
   def test_updateVelocity2(self):
      self.assertAlmostEqual(updateVelocity(10.0, 5.0), 15.0)
   def test_updateFuel(self):
      self.assertAlmostEqual(updateFuel(10.0, 5.0), 5.0)
   def test_updateFuel2(self):
      self.assertAlmostEqual(updateFuel(15.0, 10.0), 5.0)
   def test_displayLMLandingStatus(self):
      pass
   def test_displayLMLandingStatus2(self):
      pass
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   
   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 10), 1.62)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

