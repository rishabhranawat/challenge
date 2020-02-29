class Solution(object):
	def findRadius(self, houses, heaters):
		"""
		:type houses: List[int]
		:type heaters: List[int]
		:rtype: int
		"""
		heaters=sorted(heaters)
		diff = 0
		for each in houses:
			adj = self.findMinDiff(heaters, each)
			if(each < heaters[0]):
				diff = max(diff, abs(heaters[0]-each))
			elif(each > heaters[-1]):
				diff = max(diff, abs(each - heaters[-1]))
			else:
				diff = max(diff, self.findMinDiff(heaters, each))

		return diff


	def findMinDiff(self, heaters, house):

		hi = len(heaters)-1
		lo = 0

		while(lo + 1 < hi):
			mid = int((hi+lo)/2)
			if(heaters[mid] == house): return 0
			if(heaters[mid] > house):
				hi = mid
			else:
				lo = mid
		return min(abs(house - heaters[hi]), abs(house - heaters[lo]))

a = Solution()
print(a.findRadius([1,2,3],[2]))
print(a.findRadius([1,2,3,4],[1,4]))
print(a.findRadius([1, 2, 3, 4, 5], [1]))

print(a.findRadius([1, 2, 3, 4, 5], [1, 5]))

print(a.findRadius([1, 2, 3, 4, 5], [2, 3]))

print(a.findRadius([1, 2, 3, 4, 5], [4]))

print(a.findRadius([1, 2, 3, 4, 5], [2, 5]))

print(a.findRadius([1, 2, 3, 4], [2, 3]))

print(a.findRadius([1, 2, 3, 4], [2]))

print(a.findRadius([1, 5], [2]))
print(a.findRadius([1,2,3,5,15], [2,30]))

print(a.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))
