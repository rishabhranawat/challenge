class Solution(object):
	def findRepeatedDnaSequences(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		dups = set()
		tracker = set()
		if(len(s) < 10): return list(dups)
		for i in range(0, len(s)-9, 1):
			st = str(s[i:i+10])
			if(st in tracker):
				dups.add(st)
			else:
				tracker.add(st)
		return list(dups)
a = Solution()
# print(a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(a.findRepeatedDnaSequences("AAAAAAAAAAA"))




            
            
            