class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		s = [x for x in nums]
		s = sorted(s)
		start = 0
		end = len(nums)-1
		counter = 0
		while(start <= end):
			nums[counter] = s[start]
			counter += 1
			if(counter >= len(nums)): break
			nums[counter] = s[end]
			counter += 1
			start += 1
			end -= 1
		print(nums)


a = Solution()
a.wiggleSort([1, 2, 3])

