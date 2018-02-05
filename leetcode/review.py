def bfs(graph, start):
	visited, queue = set(), [start]
	while(queue):
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex]-visited)
	return visited

def dfs(graph, start):
	visited, stack = set(), [start]
	while(stack):
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex]-visited)
	return visited


def DFS(graph):

	visited = set()
	stack = ['A']

	while(stack):
		visiting_node = stack.pop()
		if(visiting_node not in visited):
			children = graph[visiting_node]
			if(len(children) > 0):
				for each in children:
					if(each not in visited and each not in stack):
						stack.append(each)
						children.remove(each)
						break
				graph[visiting_node] = children
			else:
				visited.add(visiting_node)


graph = {'A': set(['B', 'C']),
		 'B': set(['A', 'D', 'E']),
		 'C': set(['A', 'F']),
		 'D': set(['B']),
		 'E': set(['B', 'F']),
		 'F': set(['C', 'E'])}

print(DFS(graph))