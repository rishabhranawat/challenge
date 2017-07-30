# Problem Source: LeetCode
# Given a binary tree, find the leftmost value in the last row of the tree.

# Example 1:
# Input:

#     2
#    / \
#   1   3

# Output:
# 1
# Example 2: 
# Input:

#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7

# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.

### ### ###
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findBottomLeftValue(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    rows = [[root]]
    for row in rows:
        temp_each = []
        if(len(row)>0):
            for node in row:
                if(node.left): temp_each.append(node.left)
                if(node.right): temp_each.append(node.right)
            rows.append(temp_each)
    rows = rows[:len(rows)-1]
    return (rows[len(rows)-1][0].val) 

n1 = TreeNode(2)
n1l = TreeNode(1)
n1r = TreeNode(3)

n1.left = n1l
n1.right = n1r

print(findBottomLeftValue(n1))