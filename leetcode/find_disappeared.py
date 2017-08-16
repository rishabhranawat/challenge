class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ns = [0]*len(nums)
        for i in range(0, len(nums), 1):
            ns[nums[i]-1] = 1
        
        ret = []
        for j in range(0, len(ns), 1):
            if(ns[j] == 0): ret.append(j+1)
        return ret

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0, len(nums), 1):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(0, len(nums), 1) if nums[i] > 0]