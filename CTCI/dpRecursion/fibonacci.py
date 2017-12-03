class Fibonacci(object):

	def fib_recursion(self, n):
		if(n == 0 or n == 1): return 1
		return self.fib_recursion(n-1)+self.fib_recursion(n-2)

	def fib_memo(self, n):
		memo = {0:1, 1:1}
		for i in range(2, n, 1):
			memo[i] = memo[i-1]+memo[i-2]
		return memo[n-1]+memo[n-2]

	def fib_vars(self, n):
		a = 1
		b = 1

		for i in range(2, n, 1):
			c = a + b
			temp = b
			b = c
			a = temp
		return a + b


a = Fibonacci()
print(a.fib_vars(10))