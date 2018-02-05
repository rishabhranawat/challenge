class Successor:

	def inOrderSucc(self, n):
		if(n == None): return None

		if(n.right != None):
			return self.leftMostChild(n.right)
		else:
			TreeNode q = n
			TreeNode parent = q.parent

			while(parent != None and parent.left != q):
				q = parent
				parent = parent.parent
			return parent

	def leftMostChild(self, n):
		if(n == None): return None
		else:
			while(n.left !=None):
				n = n.left
			return n