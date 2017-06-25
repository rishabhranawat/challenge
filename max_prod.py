class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        n = len(nums)-1
        t = s[n]*s[n-1]*s[n-2]
        t1 = s[n]*s[0]*s[1]
        
        if(t1 > t): return t1
        else: return t
