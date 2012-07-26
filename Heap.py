class Heap:
	def __init__(self):
		self.size = 0
		self.heap = []
		self.heap.append(None)
	def get_size(self):
		return self.size
	
	def insert(self, key):
		self.size += 1
		self.heap.append(key) 
		self.bubble_up(self.size)
	
	def bubble_up(self,loc):
		temp = 0
		prnt = self.parent(loc)
		

		if loc == 1:
			return
		if self.heap[prnt] < self.heap[loc]:
			temp = self.heap[loc]
			self.heap[loc] = self.heap[prnt]
			self.heap[prnt] = temp
			self.bubble_up(prnt)
		return
	
	def extract_max(self):
		if self.size == 0:
			return None
		
		maxNode = self.heap[1]

		if self.size == 1:
			self.heap.pop()
			self.size -= 1
			return maxNode

		self.heap[1] = self.heap.pop()

		self.size -= 1
		self.bubble_down(1)
		return maxNode

	def bubble_down(self, loc):
		temp = 0
		if loc * 2 <= self.size:
			if loc * 2 + 1 <= self.size:
				if (self.heap[loc] < self.heap[loc * 2]) or (self.heap[loc] < self.heap[loc * 2 + 1]):
					if self.heap[loc * 2] < self.heap[loc * 2 + 1]:
						temp = self.heap[loc]
						self.heap[loc] = self.heap[loc * 2 + 1]
						self.heap[loc * 2 + 1] = temp
						self.bubble_down(loc * 2 + 1)
					else:
						temp = self.heap[loc]
						self.heap[loc] = self.heap[loc * 2]
						self.heap[loc * 2] = temp
						self.bubble_down(loc * 2)
			else:
				if self.heap[loc] < self.heap[loc * 2]:
					temp = self.heap[loc]
					self.heap[loc] = self.heap[loc * 2]
					self.heap[loc * 2] = temp
					self.bubble_down(loc * 2)



		


	def parent(self, n):
		return n / 2

	def left_child(self, n):
		return n * 2

	def right_child(self, n):
		return n * 2 + 1

