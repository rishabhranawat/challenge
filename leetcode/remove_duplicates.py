class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0): return 0
        current = 0
        next_rep = current + 1
        l = 0
        while(next_rep < len(nums)):
        	if(nums[current] == nums[next_rep]):
        		next_rep += 1
        	else:
        		current += 1
        		l += 1
        		nums[current] = nums[next_rep]
        return l+1

a = Solution()
print(a.removeDuplicates([1, 1, 2,2, 3, 4, 5, 5, 5]))