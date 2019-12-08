# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def sumOfLeft(self, node, isLeft):
        if(node == None):
            return 0
        elif(isLeft and node.left == None and node.right == None):
            return node.val
        else:
            return self.sumOfLeft(node.left, True) + self.sumOfLeft(node.right, False)
            
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        
        if(root.left == None and root.right == None):
            return 0
        
        return self.sumOfLeft(root, False)