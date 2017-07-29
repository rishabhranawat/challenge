# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def printMe(self, s):
		for each in s:
			print(each.val)
		print(" ")
		print()
	def getPath(self, root, p):
		path = []
		s = []
		s.append(root)
		visited = set()
		while(len(s) > 0):
			self.printMe(s)
			parent = s.pop()
			path.append(parent)
			if(parent == None):
				return path
			if(parent == p):
				return path
			else:
				if(parent.left != None): 
					s.append(parent.left)
				if(parent.right != None): 
					s.append(parent.right)
		ret = []
		for each in path:
			if(each.left not in visited or each.right not in visited):
				ret.append(each)
		return ret


	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		path1 = (self.getPath(root, p))

		# path2 = (self.getPath(root, q))
		for each in path1:
			print(each.val)

val = Solution()
a = TreeNode(6)
b = TreeNode(2)
c = TreeNode(8)
d = TreeNode(0)
e = TreeNode(4)
f = TreeNode(7)
g = TreeNode(9)

c.left = f
c.right = g

b.left = d
b.right = e

a.left = b
a.right = c

val.lowestCommonAncestor(a, e, e)
