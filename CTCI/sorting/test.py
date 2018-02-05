class Test:

	def mergesort(self, arr):
		helper = [0]*len(arr)
		self.mergesort_helper(arr, helper, 0, len(arr)-1)

	def mergesort_helper(self, arr, helper, start, end):
		if(start < end):
			mid = (start+end)/2
			self.mergesort_helper(arr, helper, start, mid)
			self.mergesort_helper(arr, helper, mid+1, end)
			self.merge(arr, helper, start, mid, end)

	def merge(self, arr, helper, start, mid, end):
		for i in range(start, end, 1):
			helper[i] = arr[i]

		helperLeft = start
		helerRight = mid + 1
		current = start

		while(helperLeft <= helperRight and helperRight <= end):
			if(helper[helperLeft] <= helper[helperRight]):
				arr[current] = helper[helperLeft]
				helperLeft += 1
			else:
				arr[current] = helper[helperRight]
				helperRight += 1
			current += 1

		rem = mid - helperLeft
		for i in range(0, rem+1, 1):
			arr[current + i] = helper[helperLeft + i]
