class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if(len(nums) == 0): return []
        elif(len(nums) == 1): return [str(nums[0])]

        start = 0
        end = 0
        
        start_val = nums[start]
        while(end < len(nums)-1):
            if(nums[end]+1 != nums[end+1]):
                if(start != end):
                    res.append(str(nums[start])+"->"+str(nums[end]))
                else:
                    res.append(str(nums[start]))
                start = end+1
                end = start
            else:
                end += 1
        if(end != start):
            res.append(str(nums[start])+"->"+str(nums[end]))
        else:
            res.append(str(nums[start]))
        return res
a = Solution()
print(a.summaryRanges([0, 2, 3, 5, 6, 7, 8, 10, 11]))