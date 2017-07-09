class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start =0
        end=x
        while(start <= end):
            mid = (start + end)/2
            v = mid*mid
            vm = (mid-1)*(mid-1)
            vp = (mid+1)*(mid+1)
            if(v == x):
                return mid
            if(v < x and x < vp): 
                return mid
            if(v > x and x > vm):
                return mid-1
            if(v < x):
                start = mid + 1
            else:
                end = mid - 1
        return None

a = Solution()
print(a.mySqrt(155825289))