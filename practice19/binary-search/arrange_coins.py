class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        rows = 0
        remaining = n
        while(i <= n):
            remaining -= i
            if(remaining < 0):
                return rows
            
            rows += 1
            if(remaining == 0):
                return rows
            i += 1
        return 0