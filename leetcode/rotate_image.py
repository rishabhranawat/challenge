class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		newMatrix = []

		for col in range(0, len(matrix), 1):
			col1 = []
			for row in range(0, len(matrix), 1):
				col1.append(matrix[row][col])
			col1.reverse()
			newMatrix.append(col1)

		for row in range(0, len(newMatrix), 1):
			for col in range(0, len(matrix), 1):
				matrix[row][col] = newMatrix[row][col]

a = Solution()
matrix = [["a", "b"],["c", "d"]]
print(a.rotate(matrix))
print(matrix)