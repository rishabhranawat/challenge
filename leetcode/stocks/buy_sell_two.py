class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        max_prof = 0
        for i in range(0, len(prices)-1, 1):
            if(prices[i+1] - prices[i] > 0): max_prof += (prices[i+1] - prices[i])
        return max_prof

a = Solution()
print(a.maxProfit([7, 2, 5, 3, 6, 1, 10]))
print(a.maxProfit([1]))
print(a.maxProfit([2,1,2,0,1]))