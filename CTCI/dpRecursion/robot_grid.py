class Point:
	def __init__(self, r, c):
		self.r = r
		self.c = c

class RobotGrid(object):

	def robot_grid(self, maze):
		if(maze == None || len(maze) == 0): return None
		path = []
		if(self.robot_path(maze, len(maze)-1, len(maze[0])-1, path)):
			return path

	def robot_path(self, maze, row, col, path):
		if(row < 0 or row >= len(maze) or col < 0 or col >= len(col)
			or not maze[row][col]):
			return False

		orig = (row == 0 and col ==0)
		if(orig or self.robot_path(maze, row-1, col, path) \
			or self.robot_path(maze, row, col-1), path):
			path.append(Point(row, col))
			return True
		
		return False


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








