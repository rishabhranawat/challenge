class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        newIndexes = [0 for x in range(len(nums))]
        
        numZeros = 0
        for i in range(0, len(nums), 1):
            add = 0
            if(nums[i] == 0):
                add = -1
                numZeros += 1
                
            if(i == 0):
                newIndexes[i] = add
            else:
                newIndexes[i] = newIndexes[i-1] + add
        if(numZeros >= 1):
            print(newIndexes)
            for i in range(0, len(nums), 1):
                if(nums[i] != 0):
                    nums[i + newIndexes[i]] = nums[i]
            
            start = len(nums)-numZeros
            for i in range(start, len(nums), 1):
                nums[i] = 0
            
a = Solution()
nums = [0,1,0,3,12]
nums1 = [0,12, 0, 1]
nums2 = [0, 13, 12, 1]
nums3 = [0, 0]
nums4 = [0,19, 1]
nums4 = [0]
nums4 = [1, 0, 1]

# a.moveZeroes(nums)
# a.moveZeroes(nums1)
# a.moveZeroes(nums2)
# a.moveZeroes(nums3)
a.moveZeroes(nums4)

# print(nums)
# print(nums1)
# print(nums2)
# print(nums3)
print(nums4)