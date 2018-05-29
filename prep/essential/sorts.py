class MergeSort:

	def sort(self, arr):
		self.ms()

	def ms(self,arr, helper, low, high):
		middle = (low+high)/2
		self.ms(arr, helper, low, middle)
		self.ms(arr, helper, middle+1, high)
		self.merge(arr, helper, low, middle, high)

	def merge(self, arr, helper, low, middle, high):
		for i in range(low, high+1, 1):
			helper[i] = arr[i]

		l = low
		r = middle+1
		current = low

		while(l <= middle and r <= high):
			if(helper[l] <= helper[r]):
				arr[current] = helper[l]
				l += 1
			else:
				arr[current] = helper[r]
				r += 1
			current += 1

		remaining = middle - l
		for i in range(0, remaining+1, 1):
			array[current + i] = helper[l]

class BinarySeach:
	def search(self, arr, val):
		sorted(arr)
		start = 0
		end = len(arr)-1
		while(start < end):
			mid = (start+end)/2
			if(arr[mid] < val):
				start = mid+1
			elif(arr[mid] > val):
				end = mid-1
			else:
				return mid
		return -1

	def recSearch(self, arr, val):
		return self.rec(arr, val, len(arr)-1, 0)

	def rec(self, arr, val, high, low):
		if(high > low): return -1
		mid = (high + low)/2
		if(arr[mid] > val):
			self.rec(arr, val, mid-1, low)
		elif(arr[mid] < val):
			self.rec(arr, val, high, mid+1)
		else:
			return mid
