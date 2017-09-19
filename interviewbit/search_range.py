class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        start = 0
        end = len(A)-1
        
        a = [0, 0]
        while(start < end):
            mid = (start+end)/2
            val = A[mid]
            if(val == B):
                if(a[0] == None): a[0] = mid
                starting_point = mid
                v = val
                while(v == B and starting_point >= 0):
                    starting_point -= 1
                    if(starting_point >= 0): v = A[starting_point]
                    
                ending_point = mid
                v = val
                while(v == B and ending_point < len(A)):
                    ending_point += 1
                    if(ending_point < len(A)): v = A[ending_point]
                    
                a[0] = starting_point+1
                a[1] = ending_point-1
                return a
            elif(val < B):
                start = mid
            else:
                end = mid
        return a

a = Solution()
print(a.searchRange([1, 1], 1))