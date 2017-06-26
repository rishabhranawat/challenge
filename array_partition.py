class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs = []
        nums = sorted(nums)
        index = 0
        while(index < len(nums)):
            pairs.append((nums[index], nums[index+1]))
            index += 2
        
        s = 0
        for each in pairs:
            s += min(each)
        return s
a = Solution()
print(a.arrayPairSum([1, 4, 3, 2]))