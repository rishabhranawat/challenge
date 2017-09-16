class Solution:
	def threeSum(self, nums):
		nums = sorted(nums)
		combs = []

		for i in range(0, len(nums), 1):
			if(i > 0 or nums[i] != nums[i-1]):
				low = i+1
				high = len(nums)-1
				req = 0 - nums[i]
				while(low < high):
					if(nums[low]+nums[high] == req):
						arr = sorted([nums[i], nums[low], nums[high]])
						if(arr not in combs):
							combs.append(arr)
						while(low < high and nums[low] == nums[low+1]): 
							low += 1
						while(low < high and nums[high-1] == nums[high]): 
							high -= 1
						low += 1
						high -= 1
					elif(nums[low]+nums[high] < req):
						low += 1
					else:
						high -= 1
		return combs
a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
