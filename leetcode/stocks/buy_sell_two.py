class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        if(len(prices) == 0): return 0
        b = prices[0]
        prevs = {}
        m = 0
        tots = 0
        b_tag = 0
        i = 1
        while(i < len(prices)):
            prof = prices[i] - b
            if(prof > 0):
                if(b_tag in prevs):
                    if(prof > prevs[b_tag]):
                        prevs[b_tag] = prof
                else:
                    prevs[b_tag] = prof
            if(prof < m and prices[i] <= b):
                b = prices[i]
                b_tag = i
            elif(prof > m):
                m = prof
            i += 1
        for key, value in prevs.items():
            tots += value
        return tots
a = Solution()
print(a.maxProfit([7, 2, 5, 3, 6, 1, 10]))
print(a.maxProfit([1]))
print(a.maxProfit([2,1,2,0,1]))