#this is the function tester
import unittest
import funcs


class TestString(unittest.TestCase):

   def test_listmaker(self):
      self.assertEqual(funcs.listmaker(1), [0])
   def test_make_columns(self):
   	  self.assertEqual(funcs.make_columns(funcs.get_puzzle("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")), [['W', 'C', 'A', 'L', 'P', 'O', 'L', 'Y', 'X', 'U'], ['A', 'B', 'Z', 'D', 'O', 'E', 'G', 'C', 'V', 'U'], ['Q', 'M', 'X', 'W', 'N', 'D', 'Q', 'S', 'D', 'I'], ['H', 'I', 'W', 'L', 'D', 'S', 'C', 'L', 'M', 'U'], ['G', 'V', 'K', 'F', 'T', 'O', 'K', 'O', 'G', 'N'], ['T', 'Q', 'W', 'X', 'M', 'Y', 'G', 'A', 'S', 'I'], ['T', 'Q', 'I', 'P', 'V', 'Q', 'M', 'C', 'X', 'X'], ['W', 'E', 'I', 'I', 'A', 'G', 'M', 'U', 'C', 'F'], ['E', 'L', 'I', 'P', 'M', 'O', 'C', 'Z', 'Y', 'N'], ['E', 'S', 'L', 'V', 'N', 'B', 'T', 'M', 'Z', 'U']]
)
   def test_get_puzzle(self):
   	  self.assertEqual(funcs.get_puzzle("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"), [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'Z', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'W', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']])



if __name__ == '__main__':
   unittest.main()
