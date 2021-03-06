class MinStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.data = []
		self.size = 0
		

	def push(self, x):
		"""
		:type x: int
		:rtype: None
		"""
		self.data.append(x)
		self.size += 1
		

	def pop(self):
		"""
		:rtype: None
		"""
		self.size -= 1
		return self.data.pop(self.size)

	def top(self):
		"""
		:rtype: int
		"""
		print(self.size, self.data)
		return self.data[self.size]

	def getMin(self):
		"""
		:rtype: int
		"""
		return min(self.data)
		


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()