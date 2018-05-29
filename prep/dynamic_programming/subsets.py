import copy

class Solution:
	def getSubsets(self, s):
		return self.getSubsetsHelper(s)
	
	def getSubsetsHelper(self, s):
		subsets = [[[]]]
		for i, a_i in enumerate(s):
			previous_subset = subsets[i]
			current_subset = []
			for each in previous_subset:
				k = copy.deepcopy(each)
				current_subset.append(copy.deepcopy(each))
				k.append(a_i)
				current_subset.append(k)
				
			subsets.append(current_subset)
		return subsets

a = Solution()
print(a.getSubsets([1, 2, 3, 4, 5]))