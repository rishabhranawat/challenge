import collections
class Solution(object):

	def findOrderBFS(self, numCourses, prerequisites):
		dic = {i: set() for i in xrange(numCourses)}
		neigh = collections.defaultdict(set)
		for i, j in prerequisites:
			dic[i].add(j)
			neigh[j].add(i)

		# queue stores the courses which have no prerequisites
		queue = collections.deque([i for i in dic if not dic[i]])

		count, res = 0, []
		while queue:
			node = queue.popleft()
			res.append(node)
			count += 1
			for i in neigh[node]:
				dic[i].remove(node)

				# if there are no more prereqs to be visited
				if not dic[i]:
					queue.append(i)
		return res if count == numCourses else []

		
	# DFS
	def findOrderDFS(self, numCourses, prerequisites):
		dic = collections.defaultdict(set)
		neigh = collections.defaultdict(set)
		for i, j in prerequisites:
			dic[i].add(j)
			neigh[j].add(i)
		stack = [i for i in xrange(numCourses) if not dic[i]]
		res = []
		while stack:
			node = stack.pop()
			res.append(node)
			for i in neigh[node]:
				dic[i].remove(node)
				if not dic[i]:
					stack.append(i)
			dic.pop(node)
		return res if not dic else []

a = Solution()
# print(a.findOrder(2, [[0, 1]]))
print(a.findOrderBFS(4, [[1,0],[2,0],[3,1],[3,2]]))
# print(a.findOrder(2, [[1, 0], [0, 1]]))
# print(a.findOrder(3, [[1,0],[1,2],[0,1]]))




