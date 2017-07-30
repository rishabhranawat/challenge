class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set()
        for each in nums1:
            if(each in nums2):
                s.add(each)
        return list(s)
a = Solution()
a.intersection([1, 2, 2, 1], [2, 2])