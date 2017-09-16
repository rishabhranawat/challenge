class Solution(object):
	def __init__(self):
		self.nums = {
		"0":0,
		"1":1,
		"2":2,
		"3":3,
		"4":4,
		"5":5,
		"6":6,
		"7":7,
		"8":8,
		"9":9
		}

	def getNumFromString(self, num):
		ret = 0
		s = 10**(len(num)-1)
		for each in num:
			ret += self.nums[each]*s
			s /= 10
		return ret


	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		su = self.getNumFromString(num1)+self.getNumFromString(num2)
		return str(su)
a = Solution()
print(a.addStrings("123", "1232"))