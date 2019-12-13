from leet_code_tree_builder import TreeBuilder
from tree_node import TreeNode


class Solution(object):
    
    def getPath(self, node, p, path):
        if(node == None):
            return path
        
        path.append(node)
        if(node.val == p.val):
            return path
        if(node.val < p.val):
            self.getPath(node.right, p, path)
        else:
            self.getPath(node.left, p, path)
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathp = []
        self.getPath(root, p, pathp)
        
        pathq = []
        self.getPath(root, q, pathq)
        
        for j in range(len(pathp)-1, -1, -1):
            if(pathp[j] in pathq):
                return pathp[j]
            
    
solver = Solution()
treeBuilder = TreeBuilder()

root1 = treeBuilder.constructTree([6,2,8,0,4,7,9,None,None,3,5])
root2 = treeBuilder.constructTree([3, 12])
root3 = treeBuilder.constructTree([1,1,2,2])

print(solver.lowestCommonAncestor(root1, root1.left, root1.right).val)
print(solver.lowestCommonAncestor(root1, root1.left.right.left, root1.left).val)
print(solver.lowestCommonAncestor(root1, root1.left, root1.right).val)