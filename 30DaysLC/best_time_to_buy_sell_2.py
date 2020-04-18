class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		
		profit = 0
		i = 0
		while(i < len(prices)-1):
			buy = prices[i]
			j = i+1
			transactionProfit = 0
			while(j < len(prices) and prices[j] > prices[j-1]):
				transactionProfit = prices[j] - buy
				j += 1

			profit += transactionProfit
			i = j
		return profit

a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([1, 2, 3, 4, 5]))
print(a.maxProfit([5, 4, 3, 2, 1]))
print(a.maxProfit([1, 8, 3, 10, 1]))