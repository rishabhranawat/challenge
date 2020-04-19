from collections import deque

class Solution(object):
	def backspaceCompare(self, S, T):
		"""
		:type S: str
		:type T: str
		:rtype: bool
		"""
		firstS = self.getCleanString(S)
		secondT = self.getCleanString(T)

		return firstS == secondT



	def getCleanString(self, S):
		first = deque([])
		for i in range(0, len(S), 1):
			val = S[i]
			if(val == "#"):
				if(len(first) > 0):
					first.pop()
			else:
				first.append(val)
		return "".join(list(first))

a = Solution()
print(a.backspaceCompare("ab#c", "ad#c"))
print(a.backspaceCompare("ab##", "c#d#"))
print(a.backspaceCompare("a##c", "#a#c"))
print(a.backspaceCompare("a#c", "b"))