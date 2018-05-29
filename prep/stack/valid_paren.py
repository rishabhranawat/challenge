class Valid:
	def valid(self, s):
		stack = []
		d = {"]":"[", "}":"{", ")":"("}
		for c in s:
			if(c in d.values()):
				stack.append(c)
			elif(c in d.keys()):
				if(stack == [] or d[c] != stack.pop()):
					return False
			else:
				return False
		return stack == []

class Temperature:
	def temp(self, temp):
		res = [0]*len(temp)

		stack = [0]
		for i in range(1, len(temp), 1):
			while(len(stack) and temp[i] > temp[stack[len(stack)-1]]):
				top = stack.pop()
				res[top] = i-top
			stack.append(i)

		while(stack):
			top = stack.pop()
			res[top] = -1
		return res
a = Temperature()
print(a.temp([73, 74, 75, 71, 70, 76, 72]))