class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = None
        s = None
        t = None
        
        
        for i in range(0, len(nums), 1):
            number = nums[i]
            if(number < t): continue
            else:
                if(number > t and number > s and number > f):
                    t = s
                    s = f
                    f = number
                elif(number > t and number > s and number < f):
                    t = s
                    s = number
                elif(number > t and number < s and number < f):
                    t = number
        if(t != None): return t
        else: return f
a = Solution()
print(a.thirdMax([1,2]))