def get_edit_distance(s1, s2):
	matrix = []
	for i in range(0, len(s1)+1, 1):
		matrix.append([0]*(len(s2)+1))

	for i in range(0, len(matrix), 1):
		matrix[i][0] = i

	for j in range(0, len(matrix), 1):
		matrix[0][j] = j

	for i in range(1, len(s1)+1, 1):
		for j in range(1, len(s2)+1, 1):
			match = matrix[i-1][j-1]
			ins = matrix[i][j-1]
			dele = matrix[i-1][j]

			if(s1[i-1] != s2[j-1]):
				ins += 1
				dele += 1
				match += 1
				matrix[i][j] = min(match, ins, dele)
			else:
				matrix[i][j] = matrix[i-1][j-1]

	return matrix[len(s1)][len(s2)]

print(get_edit_distance("", ""))
print(get_edit_distance("greek", "greep"))


