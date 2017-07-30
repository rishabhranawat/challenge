class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if(numRows == 0): return []
        memo = []
        rows = numRows
        cols = numRows+1
        for i in range(0, rows, 1):
            x = []
            for j in range(0, cols, 1):
                x.append(0)
            memo.append(x)

        memo[0][0] = 1
        retMatrix = []
        if(numRows == 1): 
            retMatrix.append(memo[0][:1])
            return retMatrix
        memo[1][0] = 1
        for i in range(1, rows, 1):
            for j in range(0, cols, 1):
                memo[i][j] = memo[i-1][j]+memo[i-1][j-1]
        
        
        for i in range(0, numRows, 1):
            retMatrix.append(memo[i][:i+1])
        return retMatrix
a = Solution()
print(a.generate(0))