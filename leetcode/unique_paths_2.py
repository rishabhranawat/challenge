class Solution(object):
    def uniquePathsWithObstacles(self, g):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = len(g)
        n = len(g[0])

        maze = [[0]*n]*m
        for i in range(0, m, 1):
            if(g[i][0] != 1): maze[i][0] = 1
        
        for j in range(0, n, 1):
            if(g[0][j] !=1): maze[0][j] = 1
        
        for i in range(1, m, 1):
            for j in range(1, n, 1):
                if(not g[i-1][j] and not g[i][j]): 
                    maze[i][j] = maze[i-1][j]
                else:
                    if(g[i-1][j]): maze[i-1][j] = 0
                    if(g[i][j]): maze[i][j] = 0

                if(g[i][j-1] != 1 and g[i][j] != 1):
                     maze[i][j] += maze[i][j-1]
                else:
                    if(g[i][j-1]): maze[i][j-1] = 0
                    if(g[i][j]): maze[i][j] = 0
        print(maze)
        return maze[m-1][n-1]

a = Solution()
print(a.uniquePathsWithObstacles([[0,0, 0],[0,1,0],[0,0, 0]]))