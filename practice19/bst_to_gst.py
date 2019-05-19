# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def preOrder(self, node, traversal):
        if(node == None ):
            return traversal
        self.preOrder(node.left, traversal)
        traversal.append(node)
        self.preOrder(node.right, traversal)
        
    
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        traversal = []
        self.preOrder(root, traversal)
        
        sums = []
        for each in traversal:
            sums.append(each.val)
        
        for i in range(len(sums)-2, -1,-1):
            sums[i] = sums[i]+sums[i+1]
        
        for i in range(0, len(traversal), 1):
            traversal[i].val = sums[i]
        return root