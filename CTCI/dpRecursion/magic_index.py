class MagicIndex(object):

	def magic_brute(self, arr):
		for i in range(0, len(arr), 1):
			if(arr[i] == i):
				return i

	def magic_bin(self, arr):
		start = 0
		end = len(arr)-1
		return self.magic_bin_dups(arr, 0, end)


	def magic_binary(self, arr, start, end):
		if(start > end): return -1
		mid = (start+end)/2

		if(arr[mid] == mid): 
			return mid

		elif(arr[mid] < mid):
			return self.magic_binary(arr, mid+1, end)

		else:
			return self.magic_binary(arr, start, mid-1)


	def magic_bin_dups(self, arr, start, end):
		if(start > end): return -1
		mid = (start + end)/2

		if(arr[mid] == mid): return mid

		left = min(arr[mid], mid-1)
		l = self.magic_bin_dups(arr, start, left)
		if(l >= 0): return l

		right = max(arr[mid], mid+1)
		r = self.magic_bin_dups(arr, right, end)
		if(r >= 0): return r
		
a = MagicIndex()
print(a.magic_bin([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))
print(a.magic_bin([-10,-5,2,2,2,3,4,8,9,12,13]))


