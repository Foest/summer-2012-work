import DLL_Node

class Linked_List:
	def __init__(self):
		self.sentinal = DLL_Node.DLL_Node(None)
		self.size = 0

	def insert(self,k):
		newNode = DLL_Node.DLL_Node(k)
		if self.sentinal.nxt==None:
			self.sentinal.nxt = newNode
			self.sentinal.prev = newNode
			newNode.nxt = self.sentinal
			newNode.prev = self.sentinal
			self.size = self.size + 1
		else:
			newNode.prev = self.sentinal.prev
			self.sentinal.prev.nxt = newNode
			newNode.nxt = self.sentinal
			self.sentinal.prev = newNode
			self.size = self.size + 1
			
	def delete(self, k):
		if self.size == 0:
			return None
		currentNode = self.sentinal.nxt
		while(currentNode.key != k):
			currentNode = currentNode.nxt
			if currentNode.key == None:
				return None
		currentNode.prev.nxt = currentNode.nxt
		self.size = self.size - 1
		return currentNode

	def print_list(self):
		if self.size == 0:
			print "List is empty"
		else:
			node = self.sentinal.nxt
			while (node.key != None):
				node.print_node()
				node = node.nxt
	
	def exist_loop(self):
		if self.size == 0:
			return False
		else:
			newNode = self.sentinal.nxt
			prevNode = newNode.prev
			if newNode.prev != prevNode:
				return True
			while newNode.nxt != self.sentinal:
				newNode = newNode.nxt
				prevNode = prevNode.nxt
				if newNode.prev != prevNode:
					return True
			return False


	def length(self):
		return self.size

	def head(self):
		return sentinal.nxt

	def tail(self):
		return sentinal.prev


