class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        m = min(nums)
        for j in range(0, len(nums), 1):
            if(j == 0): memo[j] = nums[j]
            else:
                memo[j] = memo[j-1]*nums[j]
            if(memo[j] > m): m = memo[j]

        for i in range(1, len(nums), 1):
            for j in range(i, len(nums), 1):
                if(memo[i-1] == 0 and j == i):
                    memo[j] = nums[j]
                elif(memo[i-1] == 0):
                    memo[j] = memo[j-1]*nums[j]
                else:
                    memo[j] = memo[j]/memo[i-1]
                if(memo[j] > m): m = memo[j]
        return m

    def max(self, nums):
        if(not len(nums)): return 0

        ma = nums[0]
        mi = nums[0]

        mav = ma

        for i in range(1, len(nums), 1):
            if(nums[i] < 0):
                temp = mi
                mi = ma
                ma = mi

            ma = max(nums[i], nums[i]*ma)
            mi = min(nums[i], nums[i]*mi)

            mav = max(mav, ma)
        return mav

a = Solution()
print(a.maxProduct([1,0,-1,2,3,-5,-2]))