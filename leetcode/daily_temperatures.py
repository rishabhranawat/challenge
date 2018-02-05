class Solution(object):
	def dailyTemperatures(self, temperatures):
		"""
		:type temperatures: List[int]
		:rtype: List[int]
		"""
		diffs = []
		for i in range(0, len(temperatures)-1, 1):
			diffs.append(temperatures[i+1]-temperatures[i])
		
		waiting = []
		for i in range(0, len(diffs), 1):
			if(diffs[i] > 0): waiting.append(1)
			else:
				found = False
				for j in range(i+1, len(diffs), 1):
					if(diffs[j] + diffs[i] >= 0):
						found = True
						waiting.append(j - i + 1)
						break
				if(not found): waiting.append(0)
		waiting.append(0)
		return waiting
a = Solution()
print(a.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
