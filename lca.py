# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getPath(self, path, root, p):
        if(root == None): 
            return path
        if(root == p): 
            path.append(p)
            return path
        path.append(root)
        if(root.val < p.val):
            return self.getPath(path, root.right, p)
        else:
            return self.getPath(path, root.left, p)
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1 = (self.getPath([], root, p))
        path2 = (self.getPath([], root, q))

        counter1 = len(path1)-1
        counter2 = len(path2)-1
        while(counter1 >= 0):
            if(path1[counter1] in path2): return path1[counter1]
            counter -= 1
        return None


val = Solution()

# a = TreeNode(6)
# b = TreeNode(2)
# c = TreeNode(8)
# d = TreeNode(0)
# e = TreeNode(4)
# f = TreeNode(7)
# g = TreeNode(9)

# c.left = f
# c.right = g

# b.left = d
# b.right = e

# a.left = b
# a.right = c

# print(val.lowestCommonAncestor(a, b, e).val)

a = TreeNode(2)
b = TreeNode(1)
a.left = b

print(val.lowestCommonAncestor(a, a, b).val)
