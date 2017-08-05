# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getH(self, head):
        if(head == None): return 0
        else:
            return 1 + max(self.getH(head.right), self.getH(head.left))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None): return True
        l = self.getH(root.left)
        r = self.getH(root.right)
        if(abs(l-r) > 1): return False
        else: return self.isBalanced(root.left) and self.isBalanced(root.right)
        
