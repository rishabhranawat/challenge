class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        skylineTopBottom = []
        skylineLeftRight = []
        
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(0, rows, 1):
            eachRow = grid[i]
            skylineLeftRight.append(max(eachRow))
        
        for j in range(0, cols, 1):
            maxInCol = grid[0][j]
            for i in range(0, rows, 1):
                if(grid[i][j] > maxInCol):
                    maxInCol = grid[i][j]
            skylineTopBottom.append(maxInCol)
                    
        
        additional = 0
        for i in range(0, rows, 1):
            for j in range(0, cols, 1):
                maxPossibleLR = skylineLeftRight[i]
                maxPossibleTD = skylineTopBottom[j]
                if(maxPossibleLR > maxPossibleTD):
                    diff = maxPossibleTD - grid[i][j]
                else:
                    diff = maxPossibleLR - grid[i][j]
                additional += diff
        return additional