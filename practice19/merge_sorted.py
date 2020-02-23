class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for each in nums2:
            nums1[m + i] = each
            i += 1
        
        nums1.sort()

a = Solution()

nums1 = [1,2,3,0,0,0]
a.merge(nums1, 3, [2,5,6], 3)
print(nums1)