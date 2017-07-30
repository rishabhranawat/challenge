class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pairs = {}
        if(k == 0): return False
        for i in range(0, len(nums),1):
            val = nums[i]
            if(val in pairs):
                if(len(pairs[val]) == 2):
                    pairs[val][0] = pairs[val][1]
                    pairs[val][1] = i
                else:
                    pairs[val].append(i)
                if(abs(pairs[val][0] - pairs[val][1]) <= k): return True
            else:
                pairs[val] = [i]
        return False
a = Solution()
print(a.containsNearbyDuplicate([1, 0, 1, 1], 1))