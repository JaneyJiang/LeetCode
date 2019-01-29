import unittest

from Remove_K_Digits import Solution

class removeKDigitsTest(unittest.TestCase):
    def test_remove_normal(self):
        num = "1432219"
        k = 3
        self.assertEqual(Solution().removeKdigits(num,k),'1219')
        self.assertEqual(Solution().removeKdigitsAdvance(num,k),'1219')
    
    def test_left_zero_is_front(self):
        num = "10200"
        k = 1
        #'0200'should represent as '200'
        self.assertEqual(Solution().removeKdigits(num,k),'200')
        self.assertEqual(Solution().removeKdigitsAdvance(num,k),'200')

    def test_remove_all(self):
        num = "10"
        k = 2
        self.assertEqual(Solution().removeKdigits(num,k),'0')
        self.assertEqual(Solution().removeKdigitsAdvance(num,k),'0')

    def test_increasing_list(self):
        num = "112"
        k = 1
        self.assertEqual(Solution().removeKdigits(num,k),'11')
        self.assertEqual(Solution().removeKdigitsAdvance(num,k),'11')

    def test_(self):
        num = "1234567890"
        k = 9
        self.assertEqual(Solution().removeKdigits(num,k),'0')
        self.assertEqual(Solution().removeKdigitsAdvance(num,k),'0')

if __name__ == "__main__":
    unittest.main()