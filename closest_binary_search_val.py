# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.vals = []
    
    def inOrder(self, root):
        if(root != None):
            self.inOrder(root.left)
            self.vals.append(root.val)
            self.inOrder(root.right)
            
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.inOrder(root)
        start = 0
        next = 1
        
        if(len(self.vals) == 1): return self.vals[0]
        while(next < len(self.vals)):
            val1 = self.vals[start]
            val2 = self.vals[next]
            
            if(val1 == target or val2 == target): return int(target)
            if(val1 < target and val2 > target):
                if(abs(val1 - target) > abs(val2 - target)):
                    return val2
                else:
                    return val1
            start += 1
            next += 1
        if(target < self.vals[0]): return self.vals[0]
        else: return self.vals[-1]
        