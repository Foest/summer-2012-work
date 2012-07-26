import Heap

def main():
	test1()
	test2()

def test1():
	newHeap = Heap.Heap()
	print newHeap.get_size()
	for i in range(0,10):
		newHeap.insert(i)
	print newHeap.heap

def test2():
	newHeap = Heap.Heap()
	extracted = []
	for i in range(0,10):
		newHeap.insert(i)
	
	print newHeap.heap
	for j in range(0,15):
		extracted.append(newHeap.extract_max())
		print newHeap.heap
	
	print extracted
