class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if(len(nums) <= 1): return len(nums)
		m = 1
		for i in range(0, len(nums), 1):
			prev = nums[i]
			j = i+1
			leng = 1
			while(j < len(nums)):
				if(prev == 2):
					print(prev, nums[j])
				if(nums[j] > prev):
					prev = nums[j]
					leng += 1
				j += 1
		return m
		
a = Solution()
print(a.lengthOfLIS([10,9,2,5,3,4]))