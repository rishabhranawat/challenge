class Solution(object):
    def bfs(self,node, graph, queue, visited):
        for each in graph[node]:
            if(each not in visited and each not in queue):
                queue.append(each)
        visited.add(node)

    def get_connected_components(self,graph):
        visited = set()
        connected_components = 0

        for node, neighbours in graph.items():

            if(node not in visited):
                queue = [node]
                while(len(queue) != 0):
                    node = queue.pop(0)
                    self.bfs(node, graph, queue, visited)
                connected_components += 1
        return connected_components

    def numIslands(self,grid):
        graph = {}
        for i in range(0, len(grid), 1):
            for j in range(0, len(grid[i]), 1):
                if(grid[i][j] == '0'): continue
                node = str(i)+"_"+str(j)
                neighbours = [node]
                if(i-1 >= 0 and grid[i-1][j] == '1'):
                    neighbours.append(str(i-1)+"_"+str(j))
                if(j-1 >= 0 and grid[i][j-1] == '1'):
                    neighbours.append(str(i)+"_"+str(j-1))
                if(j+1 < len(grid[i]) and grid[i][j+1] == '1'):
                    neighbours.append(str(i)+"_"+str(j+1))
                if(i+1 < len(grid) and grid[i+1][j] == '1'):
                    neighbours.append(str(i+1)+"_"+str(j))
                graph[node] = neighbours
        return self.get_connected_components(graph)
        