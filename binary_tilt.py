# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None): 
            return 0
        elif(root.left == None and root.right == None): 
            return 0
        elif(root.left == None and root.right != None):
            return abs(root.right.val) + self.findTilt(root.right)
        elif(root.left != None and root.right == None):
            return abs(root.left.val) + self.findTilt(root.left)
        else:
            return abs(root.left.val - root.right.val) \
            + self.findTilt(root.left) + self.findTilt(root.right)