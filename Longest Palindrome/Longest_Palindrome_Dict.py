class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """   
        if not s:
            return 0
        ans = 0
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 0
            d[c]+=1
        all_even = True
        for c,count in d.items():   
            ans += count
            if count%2==1:
                if all_even:
                    all_even = False
                ans -=1
        return ans if all_even else ans+1