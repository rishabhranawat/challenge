class Solution(object):
	def judgeCircle(self, moves):
		"""
		:type moves: str
		:rtype: bool
		"""
		x = 0
		y = 0
		for move in moves:
			if(move == "U"):
				y += 1
			elif(move == "D"):
				y -= 1
			elif(move == "L"):
				x -= 1
			else:
				x += 1
		return (x == 0) and (y == 0)

a = Solution()
print(a.judgeCircle("UD"))
print(a.judgeCircle("LL"))
print(a.judgeCircle("LLLRRR"))
print(a.judgeCircle("RRLLDDLRLRLU"))

# UD
# x = 0 
# y = 1 - 1

# LL
# x = -1 - 1
# y = 0

# LLL
# x = -1 - 1- 1
# y = 0

