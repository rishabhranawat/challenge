class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        zeroedRows = set()
        zeroedCols = set()
        

        for row in range(0, rows, 1):
            for col in range(0, cols, 1):
                val = matrix[row][col]
                if(val == 0):
                    if(row not in zeroedRows):
                        currRow = matrix[row]
                        rowCounter = 0
                        while(rowCounter<cols):
                            if(rowCounter <= col or currRow[rowCounter] ==0):
                                currRow[rowCounter] = 0
                            else:
                                currRow[rowCounter] = -1
                            rowCounter += 1
                        zeroedRows.add(row)
                    if(col not in zeroedCols):
                        colCounter = 0
                        while(colCounter < rows):
                            matrix[colCounter][col] = 0
                            colCounter += 1
                        zeroedCols.add(col)
        print(matrix)
a = Solution()
a.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])