class RecursiveMultiply(object):

	def recursive_multiply(self, a, b):
		if(a >= b):
			smaller = a
			bigger = b
		else:
			smaller = b
			bigger = a
		print(self.multiply_helper(smaller, bigger))
		print(self.multiply_memo(smaller, bigger, {}))
		print(self.multiply_odd_smart(smaller, bigger))


	def multiply_helper(self, smaller, bigger):
		if(smaller == 0): return 0
		if(smaller == 1): return bigger

		s = smaller/2
		first_half = self.multiply_helper(s, bigger)
		second_half = first_half

		if(smaller % 2 == 1):
			second_half = self.multiply_helper(smaller - s, bigger)
		return first_half + second_half

	def multiply_memo(self, smaller, bigger, memo):
		if(smaller == 0): return 0
		if(smaller == 1): return bigger
		if(smaller in memo): return memo[smaller]

		s = smaller/2
		first_half = self.multiply_memo(s, bigger, memo)
		second_half = first_half

		if(smaller % 2 == 1):
			second_half = self.multiply_memo(smaller-s, bigger, memo)
			memo[smaller-s] = second_half

		memo[smaller] = first_half+second_half
		return memo[smaller]

	def multiply_odd_smart(self, smaller, bigger):
		if(smaller == 0): return 0
		if(smaller == 1): return bigger
		
		s = smaller/2
		first_half = self.multiply_odd_smart(s, bigger)
		second_half = first_half

		if(smaller % 2 ==0): 
			return first_half + second_half
		else: 
			return first_half + second_half + bigger 


a = RecursiveMultiply()
(a.recursive_multiply(5, 8))
(a.recursive_multiply(10, 8))