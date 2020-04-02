class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr = [0 for x in nums]
        n = len(nums)
        for i in range(0, len(nums), 1):
            newIndex = i + k
            if(newIndex >= n):
                newIndex = newIndex % n
            arr[newIndex] = nums[i]
        
        
        for i in range(0, n, 1):
            nums[i] = arr[i]
a = Solution()

nn = [1, 2, 3, 4, 5, 6, 7]
nn2 = [-1,-100,3,99] 
a.rotate(nn, 3)
a.rotate(nn2, 1)
print(nn2)