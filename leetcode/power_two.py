class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n == 1): return True
        s = 2
        while(s <= n):
            if(s == n):return True
            s *= 2
        return False
a = Solution()
print(a.isPowerOfTwo(3))