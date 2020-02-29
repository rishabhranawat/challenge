class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		citations = sorted(citations)
		

		for i in range(0, len(citations), 1):
			cites = citations[i]
			atLeast = len(citations) - i
			other = i
			if(atLeast > )

a = Solution()
print(a.hIndex([1, 1, 2, 3]))
print(a.hIndex([3, 0, 6, 1, 5]))