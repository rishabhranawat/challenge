class Solution(object):
	def findMissingIndex(self, arr, val, mi):
		if(val in arr):
			return arr.index(val)
		if(val < mi): return 0
		counter = 0
		jump = 1
		while(counter+jump < len(arr)):
			if(arr[counter] < val and arr[counter+jump] > val):
				return counter
			counter += 1
		return None

	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		N = len(citations)
		if(N > 0):
			l = max(citations)+1
			mi = min(citations)
		else:
			mi = 0
			return 0
		index = [0]
		no_more_than_h_at_least = {}
		

		for i in range(0, l, 1):
			ind = self.findMissingIndex(citations, i, mi)
			no_more_than_h_at_least[i] = [ind, N-ind]


		for i, val in no_more_than_h_at_least.items():
			h = i
			have_at_least_h = val[1]
			if(have_at_least_h >= h):
				have_no_more_than = val[0]
				if(have_no_more_than <= N-h):
					index.append(h)
		return max(index)


a = Solution()
# print(a.hIndex([0, 1, 3, 5, 6]))
# print(a.hIndex([1, 1]))
# print(a.hIndex([0, 1]))
# print(a.hIndex([100]))
print(a.hIndex([1, 1, 3]))