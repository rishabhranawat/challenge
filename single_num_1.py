class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        
        start = 0
        end = len(snums)-1
        
        if(len(snums) == 1): 
            return snums[0]

        while(start < end):
            if(snums[start] != snums[start+1]): return snums[start]
            if(snums[end] != snums[end-1]): return snums[end]
            start += 2
            end -= 2
        return -1

a = Solution()
print(a.singleNumber([0, 1, 1]))