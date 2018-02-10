class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(0, len(grid), 1):
            for j in range(0, len(grid[i]), 1):
                current = 0
                val = grid[i][j]
                if(val == 1):
                    
                    if(i-1 == -1 or (i-1>= 0 and grid[i-1][j] == 0)):
                        current += 1
                    if((i+1) == len(grid) or (i+1 < len(grid) and grid[i+1][j] == 0)):
                        current +=1

                    if(j-1 == -1 or (j-1 >= 0 and grid[i][j-1] == 0)):
                        current += 1
                    if(j+1 == len(grid[i]) or (j+1 < len(grid[i]) and grid[i][j+1] == 0)):
                        current += 1

                perimeter += current
        return perimeter
                    
                    
a = Solution()
print(a.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))
print(a.islandPerimeter([[1]]))