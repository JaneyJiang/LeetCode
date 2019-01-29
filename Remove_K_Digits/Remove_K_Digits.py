class Solution(object):
    '''
    删除数字字符串中指定的字符个数，使留下的数字值最小，并以数字形式的字符串显示，即除非本身是0，否则开头不能是0.
    '''
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        N = len(num)
        if k >= N:
            return str(0)
        k = N-k
        res = list()
        index = 0
        while k>0:
            pre_min = min(num[index:N-k+1])
            slice_index = num[index:N-k+1].index(pre_min)
            index = index+slice_index+1
            res.append(pre_min)
            k-=1
        return str(int(''.join(res)))

    def removeKdigitsAdvance(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        N = len(num)
        if k >= N:
            return str(0)
        res = list()
        for n in num:
            while k and res and res[-1]>n:#这里必须使用循环，把之前比当前数字大的数都移除。
                res.pop()
                k -=1
            res.append(n)
        if k :#如果k>0则说明前面的:-k个就是我们要找的，-k:后面的数比之前大。
            return str(int(''.join(res[:-k])))
        return str(int(''.join(res)))