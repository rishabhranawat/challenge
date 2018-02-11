class Solution(object):
	def LCS(self, s1, s2):
		if(s1 == s2): return s1
		else:
			matrix =[[False for x in len(s)] for y in len(s)]
			for i in range(0, len(matrix), 1):
				for j in range(0, len(matrix), 1):
					if(S[])






			return subs

	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		s1 = s
		s2 = s[::-1]
		print(s1, s2)
		return self.LCS(s1, s2)

a = Solution()
print(a.longestPalindrome("abcdasdfghjkldcba"))

