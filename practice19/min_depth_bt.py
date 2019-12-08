from leet_code_tree_builder import TreeBuilder
from tree_node import TreeNode

class Solution(object):
	def minHeight(self, node):
		if(node == None):
			return 0
		if(node.right == None and node.left != None):
			return 1 + self.minHeight(node.left)
		elif(node.left == None and node.right != None):
			return 1 + self.minHeight(node.right)

		return 1 + min(self.minHeight(node.right), self.minHeight(node.left))

	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		return self.minHeight(root)

solver = Solution()
treeBuilder = TreeBuilder()

root1 = treeBuilder.constructTree([3,9,20,None,None,15,7])
root2 = treeBuilder.constructTree([3, 12])

print(solver.minDepth(root1))
print(solver.minDepth(root2))