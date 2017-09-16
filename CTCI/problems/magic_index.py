def getMagicIndex(A):
	start = 0
	end = len(A)-1

	while(start < end):
		mid = (start+end)/2
		if(A[mid] < mid):
			start = mid
		elif(A[mid] == mid): 
			return mid
		else: 
			end = mid -1 
	return -1

A = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(getMagicIndex(A))