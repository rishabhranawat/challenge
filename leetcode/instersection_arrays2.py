class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        pairs_nums1 = {}
        for num in nums1:
            if(num in pairs_nums1):
                pairs_nums1[num] += 1
            else:
                pairs_nums1[num] = 1
        
        s = []
        for n in nums2:
            if(n in pairs_nums1):
                if(pairs_nums1[n] > 0):
                    s.append(n)
                    pairs_nums1[n] -=1
        return s
a = Solution()
a.intersect([1, 2, 2, 1], [2, 2])