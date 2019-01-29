import unittest

from Maximum_XOR_of_Two_Numbers_in_an_Array import Solution

class removeKDigitsTest(unittest.TestCase):
    def test_normal(self):
        nums = [3, 10, 5, 25, 2, 8]
        self.assertEqual(Solution().findMaximumXOR(nums),28)

    def test_more_than_one_highbit(self):
        nums = [8,2,10]
        self.assertEqual(Solution().findMaximumXOR(nums),10)
    
    def test_one_num(self):
        nums = [1]
        self.assertEqual(Solution().findMaximumXOR(nums),0)
    
    def test_same_nums(self):
        nums = [8,8,8,8,8]
        self.assertEqual(Solution().findMaximumXOR(nums),0)

    def test_with_zeros(self):
        nums = [0,0,0,1,2]
        self.assertEqual(Solution().findMaximumXOR(nums),3)

if __name__ == "__main__":
    unittest.main()