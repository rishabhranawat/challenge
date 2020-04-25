from collections import deque

class Node:
    def __init__(self, val, children, color):
        self.val = val
        self.children = children
        self.color = color

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        nodes = []
        for i in range(0, len(graph), 1):
            nodes.append(Node(i, graph[i], None))
        
        nodes[0].color = "red"
        q = deque([nodes[0]])
        visited = set()
        while(len(q) and len(visited) != len(graph)):
            current = q.pop()
            visited.add(current)
            
            for child in current.children:
                if(nodes[child] not in visited):
                    q.append(nodes[child])
                if(current.color == nodes[child].color):
                    return False
                nodes[child].color = "red" if current.color == "blue" else "blue"
            
            if(len(q) == 0):
                for each in nodes:
                    if(each not in visited and each.color == None):
                        each.color = "red"
                        q.append(each)
                        break

        return True

a = Solution()
print(a.isBipartite([[4],[],[4],[4],[0,2,3]]))
print(a.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
print(a.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
print(a.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))
print(a.isBipartite([[1],[0],[4],[4],[2,3]]))