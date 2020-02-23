import copy
from leet_code_tree_builder import TreeBuilder
from tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
   
    def __init__(self):
        self.ans = None
    
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    
        def findNode(node):
            if not node:
                return False
            
            left = findNode(node.left)
            right = findNode(node.right)
            
            mid = node == p or node == q
            
            if mid + left + right >= 2:
                self.ans = node
            
            return mid or left or right
        
        findNode(root)
        return self.ans

    
solver = Solution()
treeBuilder = TreeBuilder()

root1 = treeBuilder.constructTree([3,5,1,6,2,0,8,None,None,7,4])

print(solver.lowestCommonAncestor(root1, root1.left, root1.left.right.right).val)