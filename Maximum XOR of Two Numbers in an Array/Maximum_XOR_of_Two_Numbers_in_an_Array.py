class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #max_len can also use 31 as told
        max_len = len(bin(max(nums)))-2
        max_value = 0
        mask = 0
        for i in range(max_len-1,-1,-1):
            cur_mask = 1<<i
            mask |= cur_mask
            max_possible = max_value | cur_mask
            mask_bitsets=set([mask&num for num in nums])
            for mask_bit in mask_bitsets:
                if mask_bit^max_possible in mask_bitsets:
                    max_value = max_possible
                    break
        return max_value