def merge(start, end, mid, arr):
	n1 = mid - start + 1
	n2 = end - mid

	left = [0]*n1
	right = [0]*n2

	for i in range(0, n1,1):
		left[i] = arr[i+start]

	for j in range(0, n2, 1):
		right[j] = arr[j + mid + 1]

	i = 0
	j = 0
	k = start
	while(i < n1 and j < n2):
		if(left[i] <= right[j]):
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1

	while(i < n1):
		arr[k] = left[i]
		i += 1
		k += 1

	while(j < n2):
		arr[k] = right[j]
		j += 1
		k += 1

def mergeSort(start, end, arr):
	if(start < end):
		mid = (start + end-1)/2
		mergeSort(start, mid, arr)
		mergeSort(mid+1, end, arr)
		merge(start, end, mid, arr)
	return arr

arr = [1, 9, 7, 6, 0]
mergeSort(0, len(arr)-1,arr)
