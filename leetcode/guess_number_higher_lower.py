# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        while(start <= end):
            mid = (start+end)/2
            g = guess(mid)
            if(g == 0): return mid
            elif(g == -1):
                end = mid - 1
            else:
                start = mid + 1
        return None
a = Solution()
a.guessNumber(10)