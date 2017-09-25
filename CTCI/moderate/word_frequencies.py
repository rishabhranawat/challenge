class Solution:
	def __init__(self, book):
		self.book = book
		self.frequencies = {}

	def initBook(self):
		for each in book:
			if(each in self.frequencies):
				self.frequencies[each] += 1
			else:
				self.frequencies[each] = 1

	def getFrequency(self, word):
		if(word in self.frequencies):
			return self.frequencies[word]
		else:
			return 0
book = ["word", "rish", "book", "word", "rish", "rish"]
a = Solution(book)
a.initBook()
print(a.getFrequency("word"))
print(a.getFrequency("rish"))
print(a.getFrequency("book"))