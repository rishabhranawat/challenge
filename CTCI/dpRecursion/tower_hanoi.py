class TowerHanoi(object):

	def moveDisks(self, n, origin, destination, buffer):
		if(n <= 0): return 

		self.moveDisks(n-1, origin, buffer, destination)
		self.moveTop(origin, destination)
		self.moveDisks(n-1, origin, destination, buffer)