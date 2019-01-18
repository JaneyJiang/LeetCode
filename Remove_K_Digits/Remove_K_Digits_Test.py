import unittest

from Remove_K_Digits import Solution

class removeKDigitsTest(unittest.TestCase):
    def test_remove_normal(self):
        num = "1432219"
        k = 3
        self.assertEqual(Solution().removeKdigits(num,k),'1219')
    
    def test_left_zero_is_front(self):
        num = "10200"
        k = 1
        #'0200'should represent as '200'
        self.assertEqual(Solution().removeKdigits(num,k),'200')
    def test_remove_all(self):
        num = "10"
        k = 2
        self.assertEqual(Solution().removeKdigits(num,k),'0')

if __name__ == "__main__":
    unittest.main()