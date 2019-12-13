class Solution(object):

	def path(self, node, prev):
		if(node == None):
			return 0
		if(node.val != prev):
			return 0
		
		return 1 + max(self.path(node.left, node.val), self.path(node.right, node.val))
	
	def longestUnivaluePath(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		return self.path(root, root.val)