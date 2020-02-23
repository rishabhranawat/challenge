class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        
        i = 0
        while(i < len(nums)):
            nums[nums[i]-1] = True
            i += 1
        
        for i in range(0, len(nums), 1):
            if(nums[i] != True):
                ret.append(i+1)
        return ret

solver = Solution()
print(solver.findDisappearedNumbers([4,3,2,7,8,2,3,1]))