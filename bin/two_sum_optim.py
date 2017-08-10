def twoSum(arr, target):
	s = []
	for each in arr:
		s.append(target-each)

	for each in s:
		if(each in arr): return [each, target-each]
	return None

arr = [5, 1, 2, 3, 4]
print(twoSum(arr, ))