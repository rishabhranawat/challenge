# Problem Source: LeetCode
# Invert a binary tree.

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if(root == None):
        return root
    elif(root.left == None and root.right == None):
        return
    else:
        temp = root.left
        root.left = root.right
        root.right = temp
        invertTree(root.left)
        invertTree(root.right)
        return root

def inOrder(root):
    if(root !=None):
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

t1 = TreeNode(5)
t1l = TreeNode(1)
t1r = TreeNode(6)

t1.left = t1l
t1.right = t1r

inOrder(t1)
invertTree(t1)
inOrder(t1)

