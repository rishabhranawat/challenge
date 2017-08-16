class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0): return 0
        s = [0]*len(nums)
        s[0] = nums[0]
        ma = s[0]
        for i in range(1, len(nums), 1):
            if(i == 1): 
                s[1] = nums[1]
                ma = max(s[i], ma)

            else:
                s[i] = nums[i] + max(s[0:i-1])
                ma = max(s[i], ma)
        return ma
a = Solution()
print(a.rob([1, 2]))
print(a.rob([100, 700, 200, 800, 900, 100, 1000]))