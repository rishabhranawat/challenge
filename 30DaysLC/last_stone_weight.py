import heapq

class Solution(object):
	def lastStoneWeight(self, stones):
		"""
		:type stones: List[int]
		:rtype: int
		"""
		stones = [-1*x for x in stones]
		heapq.heapify(stones)
		while(len(stones) > 1):
			v1 = heapq.heappop(stones)
			v2 = heapq.heappop(stones)
			heapq.heappush(stones, v1 - v2)
		return abs(stones[0])
a = Solution()
print(a.lastStoneWeight([2,7,4,1,8,1]))