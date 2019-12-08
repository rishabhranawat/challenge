from tree_node import TreeNode

class TreeBuilder(object):

	def constructTree(self, arr):
		nodes = []
		for val in arr:
			if(val != None):
				nodes.append(TreeNode(val))
			else:
				nodes.append(None)

		n = len(nodes)
		for i in range(0, n, 1):
			if(nodes[i] == None):
				continue
			left = 2*(i+1)-1
			right = 2*(i+1)

			if(left >= n):
				continue
			nodes[i].left = nodes[left]

			if(right >= n):
				continue
			nodes[i].right = nodes[right]
		
		if(n > 0):
			return nodes[0]
		return None