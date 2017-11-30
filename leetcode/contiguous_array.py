class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tracker = {}
        for i in range(0, len(nums), 1):
            if(i == 0): tracker[i] = [0, 0]
            else: tracker[i] = [tracker[i-1][0], tracker[i-1][1]]
            if(nums[i] == 0): tracker[i][0]+=1
            else: tracker[i][1]+=1

        backward = {}
        n = len(nums)-1
        for j in range(n, 0, -1):
            index = n - j
            if(j == n): backward[index] = [0, 0]
            else: backward[index] = [backward[index-1][0], backward[index-1][1]]
            if(nums[j] == 0): backward[index][0]+=1
            else: backward[index][1]+=1

        m = -1
        for length, vals in tracker.items():
            if(vals[0] == vals[1]):
                if(m < length):m = length+1

        for k, v in backward.items():
            if(v[0] == v[1] and v[0]+v[1] > m):
                m = v[0]+v[1]
        return m

a = Solution()
# print(a.findMaxLength([0,1]))
# print(a.findMaxLength([0, 1, 0]))
# print(a.findMaxLength([0, 1, 0, 1, 0, 1, 0, 0, 0]))
print([0,0,1,0,0,0,1,1])
print(a.findMaxLength([0,0,1,0,0,0,1,1]))
