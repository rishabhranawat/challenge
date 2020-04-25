class Solution(object):
	
	def validPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		start = 0
		end = len(s)-1

		exempt = 0
		while(start < end):
			lval = s[start]
			rval = s[end]
			
			# regular case
			if(lval != rval): 
				return self.isPali(s[start+1:end+1]) or self.isPali(s[start:end])

			start += 1
			end -= 1
		return True
	
	
	def isPali(self, s):
		start = 0
		end = len(s) - 1
		while(start < end):
			if(s[start] != s[end]):
				return False
			start += 1
			end -= 1
		return True
a = Solution()
print(a.validPalindrome("abca"))
print(a.validPalindrome("aba"))
print(a.validPalindrome("abcba"))
print(a.validPalindrome("pocp"))
print(a.validPalindrome("pbc"))
print(a.validPalindrome("dabba"))
print(a.validPalindrome("abc"))
print(a.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))