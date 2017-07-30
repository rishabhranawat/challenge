class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pairs ={}
        for each in nums:
            if(each in pairs):
                return True
            else:
                pairs[each] = 1
        return False
a = Solution()
print(a.containsDuplicate([1, 2, 3, 4, 5, 4, 4]))