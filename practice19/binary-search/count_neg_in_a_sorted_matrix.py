class Solution(object):
	def countNegatives(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		negCount = 0
		for i in range(0, len(grid), 1):
			row = grid[i]
			for j in range(0, len(row), 1):
				if(row[j] < 0):
					height = len(grid) - i
					if(height == 0):
						negCount += 1
					else:
						negCount += height

					
		return negCount

a = Solution()
print(a.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(a.countNegatives([[1,-1],[-1,-1]]))
print(a.countNegatives([[-1]]))
print(a.countNegatives([[0]]))
print(a.countNegatives([[1,0, -1],[0,-1,-1]]))
print(a.countNegatives([[5,1,0],[-5,-5,-5]]))

