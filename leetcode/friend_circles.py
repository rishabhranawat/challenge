def dfs(graph, neighbours, visited):
	for each in neighbours:
		if(each not in visited):
			visited.add(each)
			dfs(graph, graph[each], visited)


def get_connected_components(graph):
	visited = set()
	connected_components = 0

	for node, neighbours in graph.items():
		if(node not in visited):
			visited.add(node)
			dfs(graph, neighbours, visited)
			connected_components += 1
	return connected_components


def findCircleNum(M):
	graph = {}
	for node in range(0, len(M), 1):
		neighbours = []
		for neigh in range(0, len(M), 1):
			if(node != neigh):
				if(M[node][neigh] == 1):
					neighbours.append(neigh)
		graph[node] = neighbours
	return get_connected_components(graph)


print(findCircleNum([[1,1,0],
 [1,1,1],
 [0,1,1]]))

# ip = [[1,1,0],
#  [1,1,1],
#  [0,1,1]]

# print(findCircleNum(ip))
