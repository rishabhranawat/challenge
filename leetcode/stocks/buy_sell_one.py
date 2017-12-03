class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices) == 0): return 0
        b = prices[0]
        m = 0
        for i in range(1, len(prices), 1):
            prof = prices[i] - b

            # Check if this transaction will increase the profit
            # if not, and if the price is lower than the current
            # replace
            if(prof < m and prices[i] <= b):
                b = prices[i]
            elif(prof > m):
                m = prof
        return m
        

a = Solution()
print(a.maxProfit([0]))