from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """   
        counter = Counter(s)
        ans = 0
        all_even = True
        for count in counter.values():
            ans += count
            if count % 2 == 1:
                if all_even:
                    all_even = False
                ans -= 1
        return ans if all_even else ans+1

