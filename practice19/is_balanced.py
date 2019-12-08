# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def getHeight(self, node):
		if(node == None):
			return 1
		return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

	def isValidHeight(self, node):
		if(node == None):
			return True

		rightHeight = self.getHeight(node.right)
		leftHeight = self.getHeight(node.left)

		if(abs(rightHeight - leftHeight) > 1):
			return False

		return self.isValidHeight(node.left) and self.isValidHeight(node.right)

	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		return self.isValidHeight(root)


a = Solution()
root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)

n2.left = n3
n2.right = n4
root.left = n1
root.right = n2
print(a.isBalanced(root))

