class Solution(object):
	def arrayNesting(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		s = [-1]*len(nums)

		for k in range(0, len(nums), 1):
			a_k = nums[k]
			p = set()

			while(s[a_k] == -1 and a_k not in p):
				p.add(a_k)
				a_k = nums[a_k]
			if(s[a_k] != -1): s[k] = s[a_k]
			else:s[k] = len(p)
		return (max(s))
a = Solution()
a.arrayNesting([5,4,0,3,1,6,2])


