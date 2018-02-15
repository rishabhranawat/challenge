from heapq import *

class Solution(object):
	def mergeSortedArrays(self, a, b):
		ret = []

		i = 0
		j = 0
		while(i < len(a) and j < len(b)):
			a_v = a[i]
			b_v = b[j]

			if(a_v <= b_v):
				ret.append(a_v)
				i += 1
			else:
				ret.append(b_v)
				j += 1

		if(i <= len(a)-1):
			while(i < len(a)):
				ret.append(a[i])
				i += 1

		if(j <= len(b)-1):
			while(j < len(b)):
				ret.append(b[j])
				j += 1

		return ret

	# def optimizedHeap(self, a, b):
	# 	min_heap = 
	# 	heappush()

	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		if(len(nums2) == 0 and len(nums1) == 0): return None
		merged = self.mergeSortedArrays(nums1, nums2)
		if(len(merged)%2 == 0):
			index = len(merged)/2
			return (merged[index-1]+merged[index])/2.
		else:
			index = (len(merged)+1)/2
			return merged[index-1]

a = Solution()
print(a.findMedianSortedArrays([1, 3], [2]))