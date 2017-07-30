class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(0, len(findNums), 1):
            index = nums.index(findNums[i])
            for j in range(index, len(nums), 1):
                if(nums[j] > findNums[i]):
                    ret.append(nums[j])
                    break
                if(j == len(nums)-1):
                    ret.append(-1)
        return ret
a = Solution()
print(a.nextGreaterElement([2,4],[1, 2, 3,4]))