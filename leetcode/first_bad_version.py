def isBadVersion(n):
    x = [5, 6]
    return n in x

class Solution(object):
    def check(self, start, end):
        if(start == end): return end
        prevMid = start
        while(start < end):
            mid = (start + end)/2
            if(isBadVersion(mid)):
                return self.check(prevMid, mid)
            else:
                start = mid + 1
        return end

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 0 
        end = n
        prevMid = 0
        while(start <= end):
            mid = (start + end)/2
            if(isBadVersion(mid)):
                return self.check(prevMid, mid)
            else:
                start = mid+1
            prevMid = mid
        return None
a = Solution()
print(a.firstBadVersion(7))