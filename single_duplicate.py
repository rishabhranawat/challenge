class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(nums)
        counter = 0
        while(counter < len(nums)-1):
            if(n[counter] == n[counter+1]): return n[counter]
            counter += 1
        return None
a = Solution()
print(a.findDuplicate([1, 2, 3, 3, 3, 4, 5, 6]))