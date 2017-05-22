# Problem Source: LeetCode
# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest 
# path from the root node down to the farthest leaf node.

# Definition for a binary tree node.

### ### ###

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if(root == None):
        return 0
    if(root.left == None and root.right == None):
        return 1
    else:
        return 1+max(maxDepth(root.left), maxDepth(root.right))
