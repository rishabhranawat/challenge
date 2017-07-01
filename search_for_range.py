class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start_end = {}
        target_on = False
        for i in range(0,len(nums), 1):
            val = nums[i]
            if(val not in start_end):
                if(val == target): 
                    target_on = True
                if(target_on != False and val != target):
                    break
                start_end[val] = [i, -1]
            else:
                start_end[val][1] = i 
        if(target not in start_end): return [-1, -1]
        if(start_end[target][1] == -1):
            start_end[target][1] = start_end[target][0] 
        return start_end[target]
a = Solution()
print(a.searchRange([1], 1))