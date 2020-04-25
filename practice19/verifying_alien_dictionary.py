class Solution(object):
	def isAlienSorted(self, words, order):
		"""
		:type words: List[str]
		:type order: str
		:rtype: bool
		"""
		letterToPos = {}
		for i in range(0, len(order), 1):
			letterToPos[order[i]] = i
		
		for i in range(0, len(words), 1):
			for j in range(i+1, len(words), 1):
				if(not self.isWordSorted(words[i], words[j], letterToPos)):
					return False
		return True
		
	
	def isWordSorted(self, word1, word2, letterToPos):
		start = 0
		while(start < len(word1) and start < len(word2)):
			l1Pos = letterToPos[word1[start]]
			l2Pos = letterToPos[word2[start]]
			
			if(l1Pos > l2Pos):
				return False
			elif(l1Pos < l2Pos):
				return True
			start += 1
		
		if(len(word2) < len(word1)):
			return False
		
		return True
		
		
		