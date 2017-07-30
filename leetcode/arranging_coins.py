class Solution(object):
    def getSteps(self, n):
        s = [0]*(n+1)
        s[1]= 1
        counter = 2
        while(counter < n+1):
            s[counter] = counter+s[counter-1]
            counter += 1
        return s

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = self.getSteps(n)
        start = 0
        end = len(s)-1
        while(start <= end):
            mid = (start + end)/2
            val = s[mid]
            print(s)
            if(val == n): return mid
            elif(n == s[mid-1]): return mid-1
            elif(n == s[mid+1]): return mid+1
            elif(n > s[mid-1] and n < s[mid+1]): return mid-1
            else:
                if(val < n):
                    start = mid+1
                else:
                    end = mid-1
        return None


a = Solution()
print(a.arrangeCoins(5))