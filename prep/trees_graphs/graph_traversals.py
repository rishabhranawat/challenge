class GraphNode:
	def __init__(self, n):
		self.val = n
		self.children = []


def dfs(node, visited):
	if(node in visited): return
	else:
		print(node.val)
		for each in node.children:
			if(each not in visited):
				dfs(each, visited)

def bfs(node):
	queue = [root]
	visited = set()
	while(queue):
		visiting = queue.pop(0)
		if(visiting in visited): continue
		else:
			print(visiting.val)
			for each in visiting.children:
				if(each not in visited and each not in queue):
					queue.append(each)

'''
Recursive algorithm.
O(V+E)
'''
def dfs(node, visited):
	if(node in visited): return
	else:
		print(node.val)
		visited.add(node)
		for each in node.children:
			if(each not in visited):
				dfs(each, visited)

'''
Not recursive.
O(V+E)
Use a Queue
'''
def bfs(root):
	queue = [root]

	visited = set()
	while(queue):
		node = queue.pop(0)
		if(node in visited): continue
		else:
			print(node.val)
			visited.add(node)
			for each in node.children:
				if(each not in visited and each not in queue):
					queue.append(each)

node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)
node5 = GraphNode(5)
node0 = GraphNode(0)

node0.children = [node1, node4, node5]
node1.children = [node4, node3]
node2.children = [node1]
node3.children = [node2, node4]
node4.children = []
node5.children = []

bfs(node0)
dfs(node0, set())







