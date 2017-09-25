class Graph:

	def __init__(self, graph):
		self.graph = graph
		self.row = len(graph)
		self.col = len(graph[0])

	def DFS(self):
		


graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
