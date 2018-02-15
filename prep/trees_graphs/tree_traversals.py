class TreeNode:
	def __init__(self, n):
		self.left = None
		self.right = None
		self.val = n


def inOrderTraversal(self, node):
	if(node != None):
		inOrderTraversal(node.left)
		visit(node)
		inOrderTraversal(node.right)

def preOrderTraversal(self, node):
	if(node != None):
		visit(node)
		preOrderTraversal(node.left)
		preOrderTraversal(node.right)

def postOrderTraversal(self, node):
	if(node != None):
		postOrderTraversal(node.left)
		postOrderTraversal(node.right)
		visit(node)
