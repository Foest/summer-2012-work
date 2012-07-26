class DLL_Node:
	def __init__(self,k):
		self.key = k
		self.nxt = None
		self.prev = None
	def print_node(self):
		print self.key
	def set_next(self,node):
		self.nxt = node
	def set_previous(self, node):
		self.prev = node
	def set_key(self,k):
		self.key = k
	def get_next(self):
		return self.nxt
	def get_previous(self):
		return self.prev
	def get_key(self):
		return self.key
