class Solution(object):
	def calculate(self, s):
		s = s.replace(" ", "")
		numbers = []
		expressions = []

		exp = ["*", "/", "+", "-"]
		counter = 0 
		while(counter < len(s)):
			val = s[counter]
			if(val in exp):
				expressions.append(val)
			else:
				num = ""
				while(counter < len(s) and s[counter] not in exp):

					num += s[counter]
					counter += 1
				counter -= 1
				numbers.append(num)
			counter += 1

		i = 0
		while(i < len(expressions)):
			e = expressions[i]
			if(e == "*" or e == "/"):
				prev = int(numbers[i])
				next = int(numbers[i+1])

				v = prev*next if e == "*" else prev/next
				numbers[i] = v
				numbers.pop(i+1)
				expressions.pop(i)
				i -= 1

			i += 1
		
		i = 0
		while(len(expressions) > 0):
			e = expressions[i]
			if(e == "+" or e == "-"):
				prev = int(numbers[i])
				next = int(numbers[i+1])

				v = prev+next if e == "+" else prev-next
				numbers[i] = v
				numbers.pop(i+1)
				expressions.pop(i)
				i -= 1
			i += 1
		return int(numbers[0])

a = Solution()
exp1 = "2*2*2+3"
print(a.calculate(exp1))