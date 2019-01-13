import unittest
import groups
test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test2 = [1, 2, 3, 4, 5, 6, 7, 8]
ans2 = [[1, 2, 3], [4, 5, 6], [7, 8]]
test3 = [1, 2, 3, 4, 5, 6, 7]
ans3 = [[1, 2, 3], [4, 5, 6], [7]]

class TestCases(unittest.TestCase):
   def test_groups_of_3(self):
      self.assertEqual(groups.groups_of_3(test1), ans1)
   def test_groups_of_3_2(self):
      self.assertEqual(groups.groups_of_3(test2), ans2)
   def test_groups_of_3_3(self):
      self.assertEqual(groups.groups_of_3(test3), ans3)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()