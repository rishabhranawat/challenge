import sys

class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		maxS = -1*sys.maxsize
		windowS = 0
		for i in range(0, len(nums), 1):
			windowS = windowS + nums[i]
			maxS = max(maxS, windowS)
			windowS = max(windowS, 0)
		return maxS
			
		
a = Solution()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))