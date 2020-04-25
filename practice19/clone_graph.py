"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if(node == None):
            return None
        nodes = {}
        
        q = deque([node])
        
        while(len(q)):
            current = q.pop()
            nodes[current.val]  = current
            
            for each in current.neighbors:
                if(each.val not in nodes):
                    q.append(each)    
        
        
        newNodes = {}
        
        
        for k, v in nodes.items():
            newNode = Node(v.val, v.neighbors)
            newNodes[newNode.val] = newNode
        
        for k, v in newNodes.items():
            newNode = v
            neighs = []
            for each in v.neighbors:
                neighs.append(newNodes[each.val])
            newNode.neighbors = neighs
        return newNodes[node.val]
        
        