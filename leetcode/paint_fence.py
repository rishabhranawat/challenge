class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if(n == 0): return 0
        if(n == 1): return k
        if(k == 1): return 0

        paintSame = k
        paintDifferent = k*(k-1)
        for i in range(3, n+1):
            paintSame, paintDifferent = paintSame, (paintSame+paintDifferent)*(k-1)
        return paintSame + paintDifferent
a = Solution()
print(a.numWays(3, 1))
