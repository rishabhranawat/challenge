def permute(counter, level, result, s):
	if(level == len(s)): 
		print(result)
		return
	for i in range(0, len(s), 1):
		if(counter[i] == 0):
			continue
		result[level] = s[i]
		counter[i] -= 1
		permute(counter, level+1, result, s)
		counter[i] += 1

permute([1, 1, 1], 0, [None, None, None], "ABC")
