import Linked_List

def main():
	return None
	
def test1():

	newList = Linked_List.Linked_List()
	for i in range(10):
		newList.insert(i)
	print "length:"
	print newList.length()
	newList.print_list()
	print "-after delete-"
	newList.delete(5)
	newList.print_list()
	newList.delete(10)
	print "-after 2nd delete(shouldn't work)-"
	print "length:" 
	print newList.length()
	newList.print_list()

def test2():
	newList = Linked_List.Linked_List()
	newList.delete(5)
	newList.print_list()

def test3():

	newList = Linked_List.Linked_List()
	for i in range(10):
		newList.insert(i)
	newList.sentinal.nxt.nxt.nxt.nxt.prev = newList.sentinal.nxt.nxt
	print newList.exist_loop()
	newList.print_list()
