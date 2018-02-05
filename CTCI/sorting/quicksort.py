class QuickSort:

	def quicksort(self, arr):
		self.quicksort_helper(arr, 0, len(arr)-1)
		print(arr)
	def quicksort_helper(self, arr, low, high):
		if(low < high):
			pi = self.partition(arr, low, high)

			self.quicksort_helper(arr, low, pi-1)
			self.quicksort_helper(arr, pi+1, high)

	def partition(self, arr, low, high):
		pivot = arr[high]

		partition_index = low - 1

		for j in range(0, high-, 1):
			if(arr[partition_index] >= arr[j]):
				partition_index += 1
				temp = arr[partition_index]
				arr[partition_index] = arr[j]
				arr[j] = temps
		arr[partition_index+1] = pivot
		arr[high] = temp
		return partition_index+1

a = QuickSort()
a.quicksort([1, 31, 2, 23, 21])