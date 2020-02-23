class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x < 2):
            return 0

        start = 1
        end = x

        while(start < end):
            mid = start + int((start + end)/2)
            
            val = mid * mid
            
            if(val == x):
                return mid
            elif(val < x):
                start = mid + 1
            else:
                end = mid -1 

        return min(start, end)

a = Solution()
print(a.mySqrt(8))
print(a.mySqrt(4))
print(a.mySqrt(2))
print(a.mySqrt(9))
print(a.mySqrt(1024))