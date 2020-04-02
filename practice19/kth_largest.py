import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        kl = heapq.nlargest(k, nums)
        return kl[k-1]

a = Solution()
print(a.findKthLargest([1, 2, 3, 4, 1, 2, 3], 2))
