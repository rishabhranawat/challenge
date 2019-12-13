# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):

	def buildTree(self, preorder, inorder):
		"""
		:type preorder: List[int]
		:type inorder: List[int]
		:rtype: TreeNode
		"""
		if(len(preorder) == 0 or len(preorder) != len(inorder)):
			return None
		
		rootNode = TreeNode(preorder[0])

		stack = deque()
		stack.append(rootNode)

		j = 0
		for i in range(1, len(preorder), 1):
			head = TreeNode(preorder[i])

			parent = stack[-1]
			if(parent.val != inorder[j]):
				parent.left = head
			else:
				while(len(stack) > 0 and stack[-1].val == inorder[j]):
					parent = stack.pop()
					j += 1
				parent.right = head
			stack.append(head)
		return rootNode
