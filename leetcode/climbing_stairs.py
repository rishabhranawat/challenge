class Solution(object):
    def __init__(self):
        self.memo = {0: 1}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        print(n, self.memo)
        if(n < 0):
            return 0
        if(n in self.memo):
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.memo[n]

a = Solution()
print(a.climbStairs(4))