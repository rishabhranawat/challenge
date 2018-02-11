class Solution(object):
    def getReverse(self, x):
        new = ""
        for each in x:
            if(each == "0"):
                new += "01"
            elif(each == "1"):
                new += "10"
        return new
    def getRows(self, N, rows, target):
        if(N == target): return rows
        if(N == 0):
            rows[1+N] = "0"
        else:
            rows[1+N] = self.getReverse(rows[N])
        return self.getRows(N+1, rows, target)
            
    
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        rows = self.getRows(0, {}, N)
        return rows[N][K-1]
a = Solution()
print(a.kthGrammar(4, 5))
print(a.kthGrammar(1, 1))
print(a.kthGrammar(2, 1))
print(a.kthGrammar(2, 2))
print(a.kthGrammar(4, 5))