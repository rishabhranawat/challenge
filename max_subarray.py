class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0): return None
        if(len(nums) == 1): return nums[0]

        for i in range(1, len(nums), 1):
            nums[i] = nums[i]+nums[i-1]

        start = 1
        maxVal = nums[0]
        while(start < len(nums)):
            end = start
            s = nums[end]
            if(s > maxVal): maxVal = s
            while(end < len(nums)):
                s = nums[end] - nums[start-1]
                if(s > maxVal):
                    maxVal = s
                end += 1
            start += 1
        return maxVal

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(a.maxSubArray([1, 2]))