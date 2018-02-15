class TrieNode:
	def __init__(self, c):
		self.children = {}
		self.terminates = False
		self.val = c

class Trie:
	def __init__(self):
		self.root = TrieNode("")
	
	def add_word(self, parent, word):
		if(word == None or len(word) == 0):
			return True
		else:
			c = word[0]
			child = None if c not in parent.children else parent.children[c]

			if(child == None):
				child = TrieNode(word[0])
				parent.children[word[0]] = child

			remaining = word[1:]
			if(len(remaining) > 1):
				self.add_word(child, remaining)
			else:
				child.terminates = True

	def check_exists(self, word, exact):
		if(len(word) == 0 or word == None): return True
		else:
			child = None if word[0] not in self.root.children else self.root.children[word[0]]
			remaining = word[1:]
			terminated = False
			while(child and len(remaining) > 0):
				if(child.terminates): terminated = True 
				child = None if remaining[0] not in child.children else child.children[remaining[0]]
				remaining = remaining[1:]

			if(terminated and len(remaining) > 0):
				return not exact
			else:
				return exact

t = Trie()
t.add_word(t.root, "rishabh")
print(t.check_exists("rishabhranawat", True))







