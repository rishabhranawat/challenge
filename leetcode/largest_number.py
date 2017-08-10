class Solution:
	def compare(self, n1, n2):
		if(n1 + n2 > n2 + n1):
			return False
		elif(n1 + n2 < n2 + n1):
			return True

	def largestNumber(self, nums):
		nums = [str(x) for x in nums]
		for i in range(0, len(nums), 1):
			for j in range(i, len(nums), 1):
				if(self.compare(nums[i], nums[j])):
					temp = nums[i]
					nums[i] = nums[j]
					nums[j] = temp

		return "".join(map(str, nums)).lstrip('0') or '0'

a = Solution()
print(a.compare(145, 2100))
print(a.largestNumber([0, 0]))
        