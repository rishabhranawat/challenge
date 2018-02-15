'''
Max Heap implementation
using an array
'''
class Heap:
	def __init__(self):
		self.heap = []

	def parent(self, index):
		return (index+1)/2-1

	def right_child(self, index):
		if(index != None):
			r = (2*index)+2
			return r if r < len(self.heap) else None
		else:
			return None

	def left_child(self, index):
		if(index != None):
			l = (2*index)+1
			return l if l < len(self.heap) else None
		else:
			return None

	'''
	Inserting a new element into a heap.
	Complexity: O(log n)
	'''
	def push(self, val):
		self.heap.append(val)
		new_index = len(self.heap)-1
		parent = self.parent(new_index)
		while(parent >= 0):
			if(self.heap[parent] < self.heap[new_index]):
				temp = self.heap[parent]
				self.heap[parent] = self.heap[new_index]
				self.heap[new_index] = temp
				new_index = parent
				parent = self.parent(parent)
			else:
				break
		return True

	'''
	Extract Minimum.
	Complexity: O(log n)
	'''
	def extract_maximum(self):
		to_remove = self.heap[0]
		last_val = self.heap.pop()

		self.heap[0] = last_val

		current_index = 0
		right_child = self.right_child(0)
		left_child = self.left_child(0)

		while((right_child and self.heap[current_index] < self.heap[right_child])
			or (left_child and self.heap[current_index] < self.heap[left_child])):

			if((not left_child) or (self.heap[current_index] < self.heap[right_child] 
				and self.heap[right_child] > self.heap[left_child])):
				temp = self.heap[current_index]
				self.heap[current_index] = self.heap[right_child]
				self.heap[right_child] = temp

				current_index = right_child
				right_child = self.right_child(current_index)
				left_child = self.left_child(current_index)

			else:
				temp = self.heap[current_index]
				self.heap[current_index] = self.heap[left_child]
				self.heap[left_child] = temp

				current_index = left_child
				right_child = self.right_child(current_index)
				left_child = self.left_child(current_index)
		return to_remove


a = Heap()
a.push(1)
a.push(0)
a.push(13)
a.push(15)
print(a.heap)
print(a.extract_maximum())
print(a.heap)
print(a.extract_maximum())
print(a.extract_maximum())





