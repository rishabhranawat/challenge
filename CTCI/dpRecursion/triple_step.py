class TripleStep(object):

	def trip_recursion(self, n):
		if(n < 0): return 0
		elif(n == 0): return 1
		return self.trip_recursion(n-1)\
		+self.trip_recursion(n-2)\
		+self.trip_recursion(n-3)

	def trip_memo(self, n):
		memo = {0: 1}
		return self.trip_memo_helper(n, memo)

	def trip_memo_helper(self, n, memo):
		if(n < 0): return 0
		if(n in memo):
			return memo[n]
		memo[n] = self.trip_memo_helper(n-1, memo)\
		+self.trip_memo_helper(n-2, memo)\
		+self.trip_memo_helper(n-3, memo)
		return memo[n]

a = TripleStep()
print(a.trip_memo(10))
print(a.trip_recursion(10))

