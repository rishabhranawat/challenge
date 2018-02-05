import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        denoms = []        
        for i in range(1, n+1, 1):
            denoms.append(i**2)
            if(i**2 > n): break
        
        total = [sys.maxint-1]*(n+1)
        total[0] = 0
        for i in range(0, len(total), 1):
            for j in range(0, len(denoms), 1):
                if(i >= denoms[j]):
                    if(total[i-denoms[j]]+1 < total[i]):
                        total[i] = total[i-denoms[j]]+1
        return total[n]

a = Solution()
print(a.numSquares(7691))