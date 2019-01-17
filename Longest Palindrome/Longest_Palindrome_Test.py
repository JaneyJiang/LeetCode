import unittest
#from Longest_Palindrome_Dict import Solution
from Longest_Palindrome_Counter import Solution

class LongestPalindromeTest(unittest.TestCase):
    def test_all_even_letters(self):
        input_str = "aabbccddee"
        self.assertEqual(Solution().longestPalindrome(input_str),len(input_str))
    def test_null_input(self):
        input_str = ""
        self.assertEqual(Solution().longestPalindrome(input_str),len(input_str))
    def test_one_letter(self):
        input_str = "a"
        self.assertEqual(Solution().longestPalindrome(input_str),len(input_str))
    def test_null_even_letter(self):
        input_str = "abc"
        self.assertEqual(Solution().longestPalindrome(input_str),1)
    def test_case_letters(self):
        input_str = "aA"
        self.assertEqual(Solution().longestPalindrome(input_str),1)
    

if __name__=="__main__":
    unittest.main()