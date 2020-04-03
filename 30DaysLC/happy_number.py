class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		num = str(n)
		visited = set()
		
		while(num not in visited):
			visited.add(num)
			if(num == "1"):
				return True
			num = self.calculateSum(num)
			
		return num == "1"
			
			
	def calculateSum(self, num):
		v = 0
		for each in num:
			v += int(each)**2
		return str(v)

a = Solution()
print(a.isHappy("19"))
print(a.isHappy("1"))
print(a.isHappy("0"))
print(a.isHappy("87"))
print(a.isHappy("89"))
print(a.isHappy("100"))