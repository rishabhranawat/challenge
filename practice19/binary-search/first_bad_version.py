# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 1 or isBadVersion(1)):
            return 1
        
        if(isBadVersion(n) and not isBadVersion(n-1)):
            return n
        
        start = 1
        end = n
        
        while(start <= end):
            
            mid = int((start + end)/2)
            if(isBadVersion(mid)):
                if(not isBadVersion(mid-1)):
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1
        return None
            