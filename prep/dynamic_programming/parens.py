class Solution:
	def parens(self, num):
		result = []
		s = [""]*(num*2)
		self.getParens(result, num, num, s, 0)
		return result
	def getParens(self, result, leftRemaining, rightRemaining, s, count):
		if(leftRemaining < 0 or rightRemaining < leftRemaining): return
		if(leftRemaining == 0 and rightRemaining == 0):
			n = s
			n = "".join(n)
			result.append("".join(n))
		else:
			if(leftRemaining > 0):
				s[count] = "("
				self.getParens(result, leftRemaining-1, rightRemaining, s, count+1)
			if(rightRemaining > leftRemaining):
				s[count] = ")"
				self.getParens(result, leftRemaining, rightRemaining-1, s, count+1)

a = Solution()
print(a.parens(2))
