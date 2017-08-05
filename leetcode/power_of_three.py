# Without loop can be done using
# the max int value and maxINT%n == 0

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 1
        while(x <= n):
            if(x == n): return True
            x = x*3
        return False
