import sys
class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""

		a = []
		rows = len(grid)
		cols = len(grid[0])
		for i in range(0, rows+1, 1):
			a.append([0]*(cols+1))

		for i in range(0, len(a), 1):
			a[i][0] = None

		for j in range(0, len(a[0]), 1):
			a[0][j] = None
		
		for i in range(1, rows+1, 1):
			for j in range(1, cols+1, 1):
				if(a[i-1][j] == None and a[i][j-1] == None):
					a[i][j] = grid[i-1][j-1]
				elif(a[i-1][j] == None):
					a[i][j] = grid[i-1][j-1]+a[i][j-1]
				elif(a[i][j-1] == None):
					a[i][j] = grid[i-1][j-1]+a[i-1][j]
				else:
					a[i][j] = grid[i-1][j-1] + min(a[i][j-1], a[i-1][j])
		return a[rows][cols]

a = Solution()
print(a.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))