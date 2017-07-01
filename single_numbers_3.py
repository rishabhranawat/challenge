class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        
        start = 0
        end = len(nums)-1
        if(len(nums) < 2): return nums[0]
        while(start < end):
            if(nums[start] != nums[start+2]): return nums[start]
            if(nums[end] != nums[end-2]): return nums[end]
            start += 3
            end -= 3
        return -1
a = Solution()