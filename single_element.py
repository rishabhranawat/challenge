class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while(start < end):
            if(nums[start] != nums[start+1]): return nums[start]
            if(nums[end] != nums[end-1]): return nums[end]
            start += 2
            end -= 2
        return -1
a = Solution()
print(a.singleNonDuplicate([3,3,7,7,10,11,11]))