class Solution(object):
	def findMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		for i in range(0, len(nums), 1):
			if(nums[i] == 0):
				nums[i] = -1

		prefs = [0]
		for i in range(0, len(nums),1):
			prefs.append(prefs[-1] + nums[i])

		trackIndex = {}
		answer = 0
		for i in range(0, len(prefs), 1):
			pref = prefs[i]
			if(pref in trackIndex):
				answer = max(answer, i - trackIndex[pref])
			else:
				trackIndex[pref] = i

		return answer

a = Solution()
print(a.findMaxLength([0, 1]))