class TreeNode:

	def getDepthLists(self, root):
		lists = []

	def createLists(self, node, lists, level):
		if(node == None): return None

		if(level == len(lists)):
			l = []
			lists.append(l)
		else:
			l = lists[level]

		l.append(node)
		self.createLists(node.left, lists, level+1)
		self.createLists(node.right, lists, level+1)
		
