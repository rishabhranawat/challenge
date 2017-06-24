class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        if(nums[0] > target): return 0
        while(index < len(nums)):
            if(nums[index] == target): return index
            if(index == len(nums)-1): return index+1
            if(nums[index] < target and nums[index+1] > target): return index+1
            index += 1
        return None
a = Solution()
print(a.searchInsert([1, 3, 5, 6], 5))
print(a.searchInsert([1, 3, 5, 6], 0))
