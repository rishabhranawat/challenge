import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = []
        for each in nums:
            s.append(each*-1)
        
        heapq.heapify(s)
        n = None
        while(k > 0):
            n = heapq.heappop(s)
            k-=1
        return (n*-1)