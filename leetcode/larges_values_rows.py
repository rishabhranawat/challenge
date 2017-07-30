# Problem Source: LeetCode
# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 

# Output: [1, 3, 9]

### ### ###

import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def largestValues(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if(root == None): return []
    rows = [[root]]
    max_vals = [root.val]
    for row in rows:
        temp_each = []
        max_val_each = -sys.maxsize
        if(len(row)>0):
            for node in row:
                if(node.left): 
                    temp_each.append(node.left)
                    if(node.left.val > max_val_each):
                        max_val_each = node.left.val
                if(node.right): 
                    temp_each.append(node.right)
                    if(node.right.val > max_val_each):
                        max_val_each = node.right.val   
            rows.append(temp_each)
            max_vals.append(max_val_each)
    return max_vals[:len(max_vals)-1]
