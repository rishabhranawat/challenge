class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = max(A)
        ind = A.index(m)
        if(ind -1 >= 0 and ind + 1 < len(A)):
            left = ind - 1
            right = ind + 1
            
            while(left > 1):
                if(A[left] <= A[left - 1]):
                    return None
                left -= 1
            while(right < len(A) - 1):
                if(A[right] <= A[right+1]):
                    return None
                right += 1
            return ind
        return None
a = Solution()
print(a.peakIndexInMountainArray([0,2,1,0]))
print(a.peakIndexInMountainArray([0,3,2,4,0]))
