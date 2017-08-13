class Solution(object):
    def getPrimes(self, n):
        nums = [-1]*(n+1)
        nums[0] = 1
        for p in range(2, n, 1):
            i = p+p
            while(i < n):
                nums[i] = 0
                i += p
        return nums            
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = self.getPrimes(n)
        counter = 0
        for each in nums:
            if(each == -1):
                counter += 1
        return counter


a = Solution()
print(a.countPrimes(2))