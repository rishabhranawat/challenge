# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if(root == None):
			return 0
		return max(self.getHeight(root.left) + self.getHeight(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

	def getHeight(self, root):
		if(root == None):
			return 0
		return 1 + max(self.getHeight(root.left), self.getHeight(root.right))