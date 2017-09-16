class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        tmp = 1
        for i in range(0, len(nums), 1):
            result[i] = tmp
            tmp *= nums[i]
        
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= tmp
            tmp *= nums[i]
        return result
a = Solution()
print(a.productExceptSelf([1, 2, 3]))