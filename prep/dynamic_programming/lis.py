class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [0]*len(nums)
        a[0] = 1
        for i in range(0, len(nums), 1):
            for j in range(0,i,1):
                if(nums[j]+1 < nums[i]):
                    a[i] = 1 + max(a[:i])
        return a[-1]


        
a = Solution()
print(a.longestConsecutive([4,10,4,3,8,9]))
print(a.longestConsecutive([1, 2]))