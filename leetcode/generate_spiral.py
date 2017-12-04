class Solution(object):
	def generateMatrix(self, n):
		if(n == 0): return []
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		matrix = []
		for i in range(0, n, 1):
			new = []
			for j in range(0, n, 1):
				new.append(0)
			matrix.append(new)

		top = 0
		bottom = len(matrix)
		left = 0
		right = len(matrix[0])

		s = []
		counter = 1
		while(top < bottom and left < right):

			# right pass
			for i in range(left, right, 1):
				s.append(matrix[top][i])
				matrix[top][i] = counter
				counter += 1
			top += 1

			# down pass
			for j in range(top, bottom, 1):
				s.append(matrix[j][right-1])
				matrix[j][right-1] = counter
				counter += 1
			right -= 1


			# left pass
			if(top < bottom):
				for k in range(right-1, left-1, -1):
					s.append(matrix[bottom-1][k])
					matrix[bottom-1][k] = counter
					counter += 1
				bottom -= 1

			# up pass
			if(left < right):
				for l in range(bottom-1, top-1, -1):
					s.append(matrix[l][left])
					matrix[l][left] = counter
					counter += 1
				left += 1
		return matrix
