class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        
        mv = -1
        for i in range(0, len(nums),1):
            mv = max(nums[i]^m, mv)
        return mv

    def bruteXOR(self, nums):
        mv = -1
        for i in range(0, len(nums), 1):
            for j in range(0, len(nums), 1):
                mv = max(nums[i]^nums[j], mv)
        return mv
        
a = Solution()
print(a.findMaximumXOR([3, 10, 5, 25, 2, 8]))
print(a.bruteXOR([3, 10, 5, 25, 2, 8]))

print(a.findMaximumXOR([30, 10, 5, 25, 2, 8]))
print(a.bruteXOR([30, 10, 5, 25, 2, 8]))

print(a.findMaximumXOR([8,10,2]))
print(a.bruteXOR([8,10,2]))
