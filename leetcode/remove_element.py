class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        wall = 0
        index = 0
        while(index < len(nums)):
            if(nums[index] == val):
                temp = nums[wall]
                nums[wall] = val
                nums[index]=temp
                wall += 1
            index += 1
        nums.reverse()
        print(nums)
        return len(nums) - wall
a = Solution()
print(a.removeElement([2, 3, 3, 2], 2))