from heapq import heapify, heappop, heappush
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if(len(nums1) == 0 or len(nums2) == 0): return []
        if(k == 0): return []
        pairs = []

        for i in range(0, len(nums1), 1):
            for j in range(0, len(nums2), 1):
                pairs.append([i, j])
        
        hist = {}
        l = []
        for each in pairs:
            s = nums1[each[0]]+nums2[each[1]]
            l.append(s)
            if(s in hist):
                hist[s].append(each)
            else:
                hist[s] = [each]
        
        heapify(l)
        ret = []
        indi = []
        while(k > 0 and len(l) > 0):
            n = heappop(l)
            ps = hist[n]
            for each in ps:
                if(k == 0): return ret
                indiPair = [each[0], each[1]]
                newPair = [nums1[each[0]], nums2[each[1]]]
                if(indiPair not in indi):
                    ret.append(newPair)
                    indi.append(indiPair)
                    k -= 1
        return ret
                
a = Solution()
print(a.kSmallestPairs([1,2,4], [-1,1,2], 100))
print(a.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print(a.kSmallestPairs([1,1,2], [1,2,3], 10))