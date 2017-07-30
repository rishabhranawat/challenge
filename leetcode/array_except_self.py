class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        memo = {}
        for i in range(0, len(nums), 1):
            s = "".join(0:i)+"".join(i+1:len(nums))
            print(s)
a = Solution()
print(a.productExceptSelf([1, 2, 3,4]))