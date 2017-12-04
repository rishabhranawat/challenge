class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if(matrix == None or len(matrix) == 0): return []
		top = 0
		bottom = len(matrix)
		left = 0
		right = len(matrix[0])

		s = []
		while(top < bottom and left < right):

			# right pass
			for i in range(left, right, 1):
				s.append(matrix[top][i])
			top += 1

			# down pass
			for j in range(top, bottom, 1):
				s.append(matrix[j][right-1])
			right -= 1


			# left pass
			if(top < bottom):
				for k in range(right-1, left-1, -1):
					s.append(matrix[bottom-1][k])
				bottom -= 1

			# up pass
			if(left < right):
				for l in range(bottom-1, top-1, -1):
					s.append(matrix[l][left])
				left += 1
		return s





a = Solution()
# print(a.spiralOrder([
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]))

# print(a.spiralOrder([[2,3]]))

print(a.spiralOrder([[7],[9],[6]]))

print(a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))