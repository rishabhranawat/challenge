class Solution(object):

	'''
	Use a Hash table to keep track of the count.
	Time and space complexity O(n)
	'''
	def singleNumberHash(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count = {}
		for each in nums:
			if(each not in count):
				count[each] = 0
			count[each] += 1
		
		for k, v in count.items():
			if(v == 1):
				return k
		return None

	'''
	XOR bitwise operator

	0 xor a = a
	a xor a = 0
	a xor b xor a = (a xor a) xor b = 0 xor b
	'''
	def singleNumberBitWiseXOR(self, nums):
		v = 0
		for each in nums:
			v ^= each
		return v

		