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
            return '0'
        remove = list()
        i =  0
        cur = i
        i +=1
        while cur<N and i<N and k:
            if num[cur] > num[i]:
                remove.append(cur)
                cur = i
            else:
                remove.append(i)
                i+=1
            k-=1
        #return [num[i] for i range(N) if i in remove]
        return str(int(''.join([num[i] for i in range(N) if i not in remove])))

num = "1432219"
k = 3
Solution().removeKdigits(num,k)