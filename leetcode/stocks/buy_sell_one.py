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
    
    def maxProf(self, prices):

        min_price = prices[0]
        max_prof = 0

        for i in range(0, len(prices), 1):
            if(prices[i] < min_price):
                min_price = prices[i]
            else:
                prof = prices[i] - min_price
                if(prof > max_prof):
                    max_prof = prof
        return max_prof


a = Solution()
print(a.maxProf([7, 1, 5, 3, 6, 4]))
