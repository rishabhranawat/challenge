# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = []
    def getpreOrder(self, node):
        if(node == None): return
        else:
            self.getpreOrder(node.left)
            self.l.append(node.val)
            self.getpreOrder(node.right)
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.getpreOrder(root)
        print(self.l)
        return self.l[k-1]