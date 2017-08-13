class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0): return None
        if(len(nums) == 1): return 0
        for i in range(0, len(nums), 1):
            if(i == 0):
                if(nums[i+1] < nums[i]): return i
            if(i == len(nums)-1):
                if(nums[i-1] < nums[i]): return i
            if(nums[i-1] < nums[i] and nums[i+1]<nums[i]): return i
        return None