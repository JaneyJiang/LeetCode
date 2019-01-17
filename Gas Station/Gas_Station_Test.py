import unittest

from Gas_Station import Solution

class canCompleteCircuitTest(unittest.TestCase):
    def test_has_circuit(self):
        gas  = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        self.assertEqual(Solution().canCompleteCircuit(gas,cost),3)

    def test_has_no_circuit(self):
        gas  = [2,3,4]
        cost = [3,4,3]
        self.assertEqual(Solution().canCompleteCircuit(gas,cost),-1)

    def test_same_gas_cost(self):
        gas  = [1,1,1]
        cost = [1,1,1]
        self.assertEqual(Solution().canCompleteCircuit(gas,cost),0)

    def test_has_circuit(self):
        gas  = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        self.assertEqual(Solution().canCompleteCircuitAdvance(gas,cost),3)

    def test_has_no_circuit(self):
        gas  = [2,3,4]
        cost = [3,4,3]
        self.assertEqual(Solution().canCompleteCircuitAdvance(gas,cost),-1)

    def test_same_gas_cost(self):
        gas  = [1,1,1]
        cost = [1,1,1]
        self.assertEqual(Solution().canCompleteCircuitAdvance(gas,cost),0)

    

if __name__ == "__main__":
    unittest.main()