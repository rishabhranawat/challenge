from leet_code_tree_builder import TreeBuilder
from tree_node import TreeNode

class Solution(object):

	def bfs(self, node, visited, data):
		if(node == None):
			return

		if(node.val not in data):
			data[node.val] = 0
		
		if(node not in visited):
			data[node.val] += 1
			visited.add(node)

		self.bfs(node.left, visited, data)
		self.bfs(node.right, visited, data)

	def findMode(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		visited = set()
		data = {}
		self.bfs(root, visited, data)

		maxNodes = []
		maxVal = 0

		for k, v in data.items():
			if(v > maxVal):
				maxNodes = [k]
				maxVal = v
			elif(v == maxVal):
				maxNodes.append(k)
				maxVal = v

		return maxNodes

solver = Solution()
treeBuilder = TreeBuilder()

root1 = treeBuilder.constructTree([3,9,20,None,None,15,7])
root2 = treeBuilder.constructTree([3, 12])
root3 = treeBuilder.constructTree([1,1,2,2])

print(solver.findMode(root1))
print(solver.findMode(root2))
print(solver.findMode(root3))