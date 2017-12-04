class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        maze = [[0]*n]*m
        for i in range(0, m, 1):
            maze[i][0] = 1
        
        for j in range(0, n, 1):
            maze[0][j] = 1
        
        for i in range(1, m, 1):
            for j in range(1, n, 1):
                maze[i][j] = maze[i-1][j] + maze[i][j-1]
        return maze[m-1][n-1]

	def robot_grid_memo(self, maze):
		if(maze == None || len(maze) == 0): return None
		memo = {}
		path = []
		if(self.robot_path_memo(maze, len(maze)-1, 
			len(maze[0]-1, path, memo))):
			return path

	def robot_path_memo(self, maze, row, col, path, memo):
		if(row < 0 or row >= len(maze) or col < 0 or col >= len(col)
			or not maze[row][col]):
			return None

		p = Point(row, col)
		if(p in memo): return memo[p]

		orig = (row == 0 and col == 0)

		success = False
		if(orig or self.robot_path(maze, row-1, col, path) \
			or self.robot_path(maze, row, col-1), path):
			path.append(p)
			success = True

		memo[p] = success
		return success